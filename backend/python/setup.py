import setuptools
import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import docker_webui

DIR_PATH=os.path.dirname(os.path.realpath(__file__))

requirements = []
with open(DIR_PATH + "/requirements.txt", "r") as req_file:
    requirements = req_file.readlines()
test_requirements = []
with open(DIR_PATH + "/test-requirements.txt", "r") as test_req_file:
    test_requirements = test_req_file.readlines()

setuptools.setup(
    name="docker_webui",
    version=docker_webui.__version__,
    author="Daniel Borlay",
    author_email="borlay.daniel@gmail.com",
    description="Web based user interface for Docker containers",
    url="https://github.com/dborlay/docker-web-ui",
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': ['dockerwebui=docker_webui.cmd:main']
    },
    package_data={
        'docker_webui': ['web.yml']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Environment :: Console",
        "Operating System :: Unix"
    ],
    install_requires=requirements,
    extras_require={
        'test': test_requirements
    },
)
