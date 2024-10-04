from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'


def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirement= []
    with open("requirement.txt","r") as file_obj:
        requirement = file_obj.readlines()
        requirement=[req.replace("\n","") for req in requirement]

        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)
    return requirement
setup(
    name='mlproject',
    version='1.0.0',
    author='Soumyak',
    author_email='soumyakgolder2000@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirement.txt")
)