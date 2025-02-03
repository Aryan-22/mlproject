from setuptools import find_packages,setup
from typing import List
HYPHEN__E_DOT = '-e .'
def get_requirements(file_path)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        reqs = file_obj.readlines()
        requirements = [req.replace("\n","") for req in reqs]

        if HYPHEN__E_DOT in requirements:
            requirements.remove(HYPHEN__E_DOT)
    return requirements
setup(
    name = "mlproject",
    version = "0.0.1",
    author = "Aryan",
    author_email="aryancoder03@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")

)