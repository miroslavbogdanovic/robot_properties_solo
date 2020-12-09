Robot Properties Solo
---------------------

### What it is

URDF and ROS integration of the Solo BLMC robot

### Get Started

Assuming you have already installed Pinocchio:

Install bullet_utils
```
git clone git@github.com:huaijiangzhu/bullet_utils.git
cd bullet_utils
pip3 install .
```

Install robot_properties_solo
```
git clone git@github.com:huaijiangzhu/robot_properties_solo.git
cd robot_properties_solo
pip3 install .
```

Load Solo12 in PyBullet
```
import pybullet as p
from bullet_utils.env import BulletEnvWithGround
from robot_properties_solo.solo12wrapper import Solo12Robot

env = BulletEnvWithGround(p.GUI)
robot = env.add_robot(Solo12Robot)
```

### Authors

- Felix Grimmiger
- Maximilien Naveau
- Avadesh Meduri
- Julian Viereck
- Huaijiang Zhu

### Copyrights

Copyright(c) 2018-2021 Max Planck Gesellschaft, New York University

### License

BSD 3-Clause License


