from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'AutoRobo_pkg'

launch_dir = os.path.join(os.path.dirname(__file__), 'launch')
launch_files = glob(os.path.join(launch_dir, '*.launch.py')) 


setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', launch_files)
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='willykpark',
    maintainer_email='willykpark@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['image_subscriber = AutoRobo_pkg.image_subscriber:main',
        ],
    },
    
)
