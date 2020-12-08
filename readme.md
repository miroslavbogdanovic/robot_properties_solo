Robot Properties Solo
---------------------

### What it is

URDF and ROS integration of the Solo BLMC robot

### Get Started

Assuming you have already install Pinocchio:

Install pinocchio_bullet
```
git clone git@github.com:machines-in-motion/pinocchio_bullet.git
cd pinocchio_bullet
pip3 install .
```

Install robot_properties_solo
```
git clone git@github.com:huaijiangzhu/robot_properties_solo.git
cd pinocchio_bullet
pip3 install .
```

Load Solo12 in PyBullet
```
from robot_properties_solo.solo12wrapper import Solo12Robot
robot = Solo12Robot()
```

### Authors

- Felix Grimmiger
- Maximilien Naveau
- Avadesh Meduri
- Julian Viereck

### Copyrights

Copyright(c) 2018-2019 Max Planck Gesellschaft, New York University

### License

BSD 3-Clause License


