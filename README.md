
### Зависимости
* [Boost](http://www.boost.org) (version 1.5.4 or higher)
* [CMake](http://www.cmake.org) (version 2.8.3 or higher)
* [LCM](https://lcm-proj.github.io) (version 1.4.0 or higher)

### Сборка
```bash
cd lcm
mkdir build
cd build
cmake ..
make
sudo make install
cd ..
cd lcm-python
sudo python3 setup.py install
cd ..
cd ..
mkdir build
cd build
cmake ../
make
```

### Использование
# Python
```bash
cd scripts
python3 Robot_Python.py
```
# С++
```bash
cd build
sudo example_dance
```


