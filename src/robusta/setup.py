from setuptools import find_packages, setup

package_name = 'robusta'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=[
        'setuptools',
        'rclpy',
        'std_msgs',
        ],
    zip_safe=True,
    maintainer='minseok',
    maintainer_email='minseok5432@gmail.com',
    description='Examples modified from Raj Tagore ROS1 tutorials',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
		    'send_decision  = robusta.send_decision:main',
            'decision_maker = robusta.decision_maker:main',
        ],
    },
)
