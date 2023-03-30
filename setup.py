from setuptools import setup,find_packages


def get_requirements(file_path:str)->List[str]:# It takes a file path as input and returns a list of strings representing the requirements.
    requirements=[]
    with open(file_path) as file_obj:#The with statement ensures that the file is properly closed when we're done with it
        for line in file_obj:
            line = line.strip()#This removes any leading or trailing whitespace from the line
            if not line or line.startswith('#'):#If line is emtpy or starts with # means comment skip with continue
                continue
            if line.startswith('-e'):#if line starts with -e again skip with continue
                continue
            requirements.append(line)#append current line 
    return requirements
            
            

setup(
    name='covid_project',
    version='1.0.0.',
    author='VukDjunisijevic',
    author_email='vucina19931906@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')     
)