from setuptools import find_packages,setup
from typing import List
#for returning the list of requirements
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements
setup(
    name='Student-mark prediction',
    version='0.0.1',
    author='Hemanth Kumar',
    author_email='hemanth052004@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    )
