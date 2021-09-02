/************************************************************************
Copyright (c) 2020, Unitree Robotics.Co.Ltd. All rights reserved.
Use of this source code is governed by the MPL-2.0 license, see LICENSE.
************************************************************************/

#include "unitree_legged_sdk/unitree_legged_sdk.h"
#include <iostream>
#include <math.h>
#include <stdint.h>
#include <stdio.h>

using namespace std;
using namespace UNITREE_LEGGED_SDK;

class Custom {
public:
  Custom() : control(LeggedType::A1, LOWLEVEL), udp() {
    control.InitCmdData(cmd);
  }
  void UDPRecv();
  void UDPSend();
  void RobotControl();

  Control control;
  UDP udp;
  LowCmd cmd = {0};
  LowState state = {0};
  float qInit[3] = {0};
  float qDes[3] = {0};
  float sin_mid_q[3] = {0.0, 1.2, -2.5};
  float Kp[3] = {0};
  float Kd[3] = {0};
  double time_consume = 0;
  int rate_count = 0;
  int sin_count = 0;
  int motiontime = 0;
  float dt = 0.002; // 0.001~0.01

  const float pi = 3.1415;

  float motor_destination = 0;
  float read_initial_position = 0;

  float speed = 3.0;
  const int target_leg = FR_2;
  float target_position = -150 * pi / 180;
  float state_angle = 0;
  float state_tau = 0;
};

void Custom::UDPRecv() { udp.Recv(); }

void Custom::UDPSend() { udp.Send(); }

double jointLinearInterpolation(double initPos, double targetPos, double rate) {
  double p;
  rate = std::min(std::max(rate, 0.0), 1.0);
  p = initPos * (1 - rate) + targetPos * rate;
  return p;
}

void Custom::RobotControl() {
  motiontime++;
  udp.GetRecv(state);
  // printf("%d  %f\n", motiontime, state.motorState[FR_2].q);

  // gravity compensation
  cmd.motorCmd[FR_0].tau = -0.65f;
  cmd.motorCmd[FL_0].tau = +0.65f;
  cmd.motorCmd[RR_0].tau = -0.65f;
  cmd.motorCmd[RL_0].tau = +0.65f;

  // if( motiontime >= 100){
  if (motiontime >= 0) {
    // first, get record initial position
    // if( motiontime >= 100 && motiontime < 500){
    if (motiontime >= 0 && motiontime < 10) {
      // qInit[0] = state.motorState[FR_0].q;
      // qInit[1] = state.motorState[FR_1].q;
      // qInit[2] = state.motorState[FR_2].q;
      read_initial_position = state.motorState[target_leg].q;
    }
    // second, move to the origin point of a sine movement with Kp Kd
    // if( motiontime >= 500 && motiontime < 1500){
    if (motiontime >= 10 && motiontime < 400) {
      rate_count++;
      double rate = rate_count / 200.0; // needs count to 200
      Kp[0] = 5.0;
      Kp[1] = 5.0;
      Kp[2] = 5.0;
      Kd[0] = 1.0;
      Kd[1] = 1.0;
      Kd[2] = 1.0;

      // qDes[0] = jointLinearInterpolation(qInit[0], sin_mid_q[0], rate);
      // qDes[1] = jointLinearInterpolation(qInit[1], sin_mid_q[1], rate);
      // qDes[2] = jointLinearInterpolation(qInit[2], sin_mid_q[2], rate);
      motor_destination = jointLinearInterpolation(read_initial_position,
                                                   target_position, rate);
    }
    double sin_joint1, sin_joint2;
    // last, do sine wave
    if (0) {
      sin_count++;
      sin_joint1 = 0.6 * sin(3 * M_PI * sin_count / 1000.0);
      sin_joint2 = -0.6 * sin(1.8 * M_PI * sin_count / 1000.0);
      // qDes[0] = sin_mid_q[0];
      // qDes[1] = sin_mid_q[1];
      qDes[1] = target_position + sin_joint2;
      // qDes[2] = sin_mid_q[2];
    }

    // cmd.motorCmd[FR_0].q = qDes[0];
    // cmd.motorCmd[FR_0].dq = 0;
    // cmd.motorCmd[FR_0].Kp = Kp[0];
    // cmd.motorCmd[FR_0].Kd = Kd[0];
    // cmd.motorCmd[FR_0].tau = -0.65f;

    // cmd.motorCmd[FR_1].q = qDes[1];
    // cmd.motorCmd[FR_1].dq = 0;
    // cmd.motorCmd[FR_1].Kp = Kp[1];
    // cmd.motorCmd[FR_1].Kd = Kd[1];
    // cmd.motorCmd[FR_1].tau = 0.0f;

    cmd.motorCmd[target_leg].q = motor_destination;
    cmd.motorCmd[target_leg].dq = speed;
    cmd.motorCmd[target_leg].Kp = Kp[2];
    cmd.motorCmd[target_leg].Kd = Kd[2];
    cmd.motorCmd[target_leg].tau = 0.0f;

    // while(1)
    {
      state_angle = state.motorState[FL_1].q;
      state_tau = state.motorState[FL_1].tauEst;

      cout << " current angle : " << state_angle * 180 / pi << endl;
      cout << " current tau : " << state_tau << endl;
      usleep(1000);
    }
  }

  if (motiontime > 10) {
    // control.PositionLimit(cmd);
    // control.PowerProtect(cmd, state, 1);
    // control.PositionProtect(cmd, state, 0.087);
  }

  udp.SetSend(cmd);
}

int main(void) {
  std::cout << "Control level is set to LOW-level." << std::endl
            << "WARNING: Make sure the robot is hung up." << std::endl
            << "Press Enter to continue..." << std::endl;
  std::cin.ignore();

  Custom custom;

  LoopFunc loop_control("control_loop", custom.dt,
                        boost::bind(&Custom::RobotControl, &custom));
  LoopFunc loop_udpSend("udp_send", custom.dt, 3,
                        boost::bind(&Custom::UDPSend, &custom));
  LoopFunc loop_udpRecv("udp_recv", custom.dt, 3,
                        boost::bind(&Custom::UDPRecv, &custom));

  loop_udpSend.start();
  loop_udpRecv.start();
  loop_control.start();

  while (1) {
    sleep(10);
  };

  return 0;
}
