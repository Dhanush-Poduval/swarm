from setuptools import find_packages, setup
import os 
from glob import glob 
package_name = 'lidar_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'launch'),glob('launch/*')),
        (os.path.join('share',package_name,'model'),glob('model/*')),
        (os.path.join('share',package_name,'parameters'),glob('parameters/*')),
        (os.path.join('share',package_name,'world'),glob('world/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dhanush',
    maintainer_email='dhanushpoduval@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
