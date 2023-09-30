#!/usr/bin/python
import Unitree_Python_sdk
import time
unitree_robot = Unitree_Python_sdk.Unitree_Robot()
#print(state.footForce) - for debug
motion_time = 0
while True:
    time.sleep(0.002)
    # Uncomment the following line to control the pose of robot
    # The four arguments are: roll, pitch, yaw, bodyHeight.
     
    #state = unitree_robot.robot_pose(0.1, 0.0, 1, 0.0)
    
    # Uncomment the following line to control the movement of robot
    # The arguments are: gait type, forward speed, sideway speed, rotate speed, speed level and body height.
    # Gait type: 0.idle  1.trot  2.trot running  3.climb stair
    # Forward speed: unit: m/s -1.0 ~ 1.0
    # Sideway speed: unit: m/s -1.0 ~ 1.0
    # Rotate speed: unit: rad/s -1.0 ~ 1.0
    # Speed level: 0. default low speed. 1. medium speed 
    # Body height: unit: m, default: 0.28m
    
    #state = unitree_robot.robot_walking(gaitType = 1, forwardSpeed = -0.1, sidewaySpeed = 0.0, rotateSpeed = 0.0, speedLevel = 0, bodyHeight = 0.2)
   
    if motion_time > 0:     
      robot_state = unitree_robot.unitree_robot.getState()
      unitree_robot.robot_control()
      unitree_robot.send_UDP() 
    
    if (motion_time == 0):
       unitree_robot.mode = 0

    #BEGIN
    
    # POINT 0 - Поворот против часовой стрелки
    if (motion_time > 100 and motion_time < 2050): # 1700
      state = unitree_robot.robot_walking(gaitType = 1, forwardSpeed = 0, rotateSpeed = 2, speedLevel = 1)
    if (motion_time >= 2050 and motion_time < 2060): #не добавляем, а потом + 10
      state = unitree_robot.robot_walking(gaitType = 0, forwardSpeed = 0, rotateSpeed = 0, speedLevel = 0)
    if (motion_time == 2060): #this
      state = unitree_robot.mode = 0
    
    # POINT 0 - Поворот по часовой стрелке
    if (motion_time >= 2110 and motion_time < 3170): # половина от полного оборота
      state = unitree_robot.robot_walking(gaitType = 1, forwardSpeed = 0, rotateSpeed = -2, speedLevel = 1)
    if (motion_time >= 3170 and motion_time < 3180): # не изменяем и + 10
      state = unitree_robot.robot_walking(gaitType = 0, forwardSpeed = 0, rotateSpeed = 0, speedLevel = 0)
    if (motion_time == 3180): #this
      state = unitree_robot.mode = 0
    
    # POINT 0 - Идем до POINT 1
    if (motion_time >= 3200 and motion_time < 5000): #1800
      state = unitree_robot.robot_walking(gaitType = 1, forwardSpeed = 0.5, speedLevel = 1) 
    if (motion_time == 5000): #this
      state = unitree_robot.mode = 0  
    
    # POINT 1 - Поворот по часовой стрелке
    if (motion_time >= 5005 and motion_time < 6005): #+5 и 1000
      state = unitree_robot.robot_walking(gaitType = 1, forwardSpeed = 0, rotateSpeed = -2, speedLevel = 1)
    if (motion_time == 6005): #this
      state = unitree_robot.mode = 0  
    
    # POINT 1 - Танцевальный элемент (опускаем переднюю часть туловища и поднимаем переднюю)
    if (motion_time >= 6010 and motion_time < 6110):
      state = unitree_robot.robot_pose(0.8, 0.8, 0.25, -0.1)
    if (motion_time >= 6210 and motion_time < 6410):
      state = unitree_robot.robot_pose(-0.8, 0.8, -0.25, -0.1)
    if (motion_time > 6510 and motion_time < 6710):
      state = unitree_robot.robot_pose(0.8, 0.8, 0.25, -0.1)
    if (motion_time >= 6810 and motion_time < 6910):
      state = unitree_robot.robot_pose(-0.8, 0.8, -0.25, -0.1)
    if (motion_time > 7010 and motion_time < 7110):
      state = unitree_robot.robot_pose(0.8, 0.8, 0.25, -0.1)
    if (motion_time >= 7210 and motion_time < 7410):
      state = unitree_robot.robot_pose(-0.8, 0.8, -0.25, -0.1)
    if (motion_time == 7410): #this
      state = unitree_robot.mode = 0  
    
    # POINT 1 - Поворот против часовой стрелки
    if (motion_time > 7510 and motion_time < 8760): # 1250
      state = unitree_robot.robot_walking(gaitType = 1, forwardSpeed = 0, rotateSpeed = 2, speedLevel = 0)
    if (motion_time >= 8760 and motion_time < 8770): #не добавляем, а потом + 10
      state = unitree_robot.robot_walking(gaitType = 0, forwardSpeed = 0, rotateSpeed = 0, speedLevel = 0)
    if (motion_time == 8770): #this
      state = unitree_robot.mode = 0  

    # POINT 1 - Идем под столом до POINT 2
    if (motion_time >= 8780 and motion_time < 12600):
      state = unitree_robot.robot_walking(gaitType = 1, forwardSpeed = 0.5, speedLevel = 1) 
    if (motion_time == 12600): #this
      state = unitree_robot.mode = 0  

    # POINT 2 - Поворот против часовой стрелки
    if (motion_time > 12600 and motion_time < 13050):
      state = unitree_robot.robot_walking(gaitType = 1, forwardSpeed = 0, rotateSpeed = 2, speedLevel = 1)
    if (motion_time >= 13050 and motion_time < 13060):
      state = unitree_robot.robot_walking(gaitType = 0, forwardSpeed = 0, rotateSpeed = 0, speedLevel = 0)
    if (motion_time == 13060): #this
      state = unitree_robot.mode = 0  

    # POINT 2 - Идем до POINT 3
    if (motion_time >= 13110 and motion_time < 14510):
      state = unitree_robot.robot_walking(gaitType = 1, forwardSpeed = 0.5, speedLevel = 1) 
    if (motion_time == 14510): #this
      state = unitree_robot.mode = 0  

    # POINT 3 - Поворот против часовой стрелки
    if (motion_time > 14540 and motion_time < 15110):
      state = unitree_robot.robot_walking(gaitType = 1, forwardSpeed = 0, rotateSpeed = 2, speedLevel = 1)
    if (motion_time >= 15110 and motion_time < 15120):
      state = unitree_robot.robot_walking(gaitType = 0, forwardSpeed = 0, rotateSpeed = 0, speedLevel = 0)
    if (motion_time == 15120): #this
      state = unitree_robot.mode = 0 
    
    
    # POINT 3 - Ползем под столом до POINT 4
    if (motion_time >= 15130 and motion_time < 18330):
      state = unitree_robot.robot_walking(gaitType = 1, forwardSpeed = 0.5, footRaiseHeight = -0.04, speedLevel = 0, bodyHeight = -0.2)
    if (motion_time == 18330): #this
      state = unitree_robot.mode = 0  
    

    '''
    # POINT 4 - Поворот
    if (motion_time > x and motion_time < x): # 550
      state = unitree_robot.robot_walking(gaitType = 1, forwardSpeed = 0, rotateSpeed = -2, speedLevel = 1)
    if (motion_time >= x and motion_time < x): #не добавляем, а потом + 10
      state = unitree_robot.robot_walking(gaitType = 0, forwardSpeed = 0, rotateSpeed = 0, speedLevel = 0)
    if (motion_time == x): #this
      state = unitree_robot.mode = 0 

    # POINT 4 - Бег
    if (motion_time >= x and motion_time < x): #900
      state = unitree_robot.robot_walking(gaitType = 1, forwardSpeed = 0.5, speedLevel = 1) 
    if (motion_time == x): #this
      state = unitree_robot.mode = 0  
    
    # POINT 5 - Поворот
    if (motion_time > x and motion_time < x): # 550
      state = unitree_robot.robot_walking(gaitType = 1, forwardSpeed = 0, rotateSpeed = 2, speedLevel = 1)
    if (motion_time >= x and motion_time < x): #не добавляем, а потом + 10
      state = unitree_robot.robot_walking(gaitType = 0, forwardSpeed = 0, rotateSpeed = 0, speedLevel = 0)
    if (motion_time == x): #this
      state = unitree_robot.mode = 0

    # POINT 5 - Идем до точки 6
    if (motion_time >= x and motion_time < x): #900
      state = unitree_robot.robot_walking(gaitType = 1, forwardSpeed = 0.5, speedLevel = 1) 
    if (motion_time == x): #this
      state = unitree_robot.mode = 0  

    # POINT 6 - Поворот
    if (motion_time > x and motion_time < x): # 550
      state = unitree_robot.robot_walking(gaitType = 1, forwardSpeed = 0, rotateSpeed = 2, speedLevel = 1)
    if (motion_time >= x and motion_time < x): #не добавляем, а потом + 10
      state = unitree_robot.robot_walking(gaitType = 0, forwardSpeed = 0, rotateSpeed = 0, speedLevel = 0)
    if (motion_time == x): #this
      state = unitree_robot.mode = 0

    # POINT 6 - Танцевальный элемент (приседаем влево/вправо)
    <...>

    # POINT 6 - Идем до точки 7
    if (motion_time >= x and motion_time < x): #900
      state = unitree_robot.robot_walking(gaitType = 1, forwardSpeed = 0.5, speedLevel = 1) 
    if (motion_time == x): #this
      state = unitree_robot.mode = 0  

    # POINT 7 - Восьмерка через точку 0 и останавливаемся в точке 7
    <...>

    # POINT 7 - Поворот в нужное направление перед сальто
    if (motion_time > x and motion_time < x): # 550
      state = unitree_robot.robot_walking(gaitType = 1, forwardSpeed = 0, rotateSpeed = 2, speedLevel = 1)
    if (motion_time >= x and motion_time < x): #не добавляем, а потом + 10
      state = unitree_robot.robot_walking(gaitType = 0, forwardSpeed = 0, rotateSpeed = 0, speedLevel = 0)
    if (motion_time == x): #this
      state = unitree_robot.mode = 0

    # POINT 7 - Сальто
    <...>

    # POINT 7 - Ложимся
    <...>
    '''

    motion_time += 1

    # return state of robot    
    # imu                       //rpy[0], rpy[1], rpy[3]
    # gaitType                  // 0.idle  1.trot  2.trot running  3.climb stair
    # footRaiseHeight           // (unit: m, default: 0.08m), foot up height while walking
    # position                  // (unit: m), from own odometry in inertial frame, usually drift
    # bodyHeight                // (unit: m, default: 0.28m),
    # velocity                  // (unit: m/s), forwardSpeed, sideSpeed, rotateSpeed in body frame
    # yawSpeed                  // (unit: rad/s), rotateSpeed in body frame        
    # footPosition2Body         // foot position relative to body
    # footSpeed2Body            // foot speed relative to body
    # footForce
