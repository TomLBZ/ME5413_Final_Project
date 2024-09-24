from setuptools import setup, find_packages

setup(
    name='inorbit_br',
    version='0.0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['setuptools'],
    author='liboz',
    author_email='liboz@todo.todo',
    maintainer='liboz',
    maintainer_email='liboz@todo.todo',
    description='A ROS bridge for InOrbit',
)