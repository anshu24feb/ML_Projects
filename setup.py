# Thisi file is responsible for creating packages required for this project and build
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(file_path:str)-> List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [r.replace("\n","")  for r in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements



setup(
    name="ML Projects",
    version="1.0.0",
    author="anshu",
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')

)


