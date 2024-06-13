import os
from pathlib import Path # handle filesystem paths and operations
import logging # tracking events

#  logging system to display messages with a level of INFO or higher and formats the log messages to include the timestamp and the message.
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "text_summarizer"

# relative paths of directories and files that need to be created for the project
list_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "notebooks/trials.ipynb",
]


for filepath in list_files:
    filepath = Path(filepath) # filepath converted to a Path object for easier manipulation
    filedir, filename = os.path.split(filepath) # extract folder and file

    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # create the directory and any necessary parent directories, prevents an error if the directory already exists
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # checks if the file does not exist or if it exists but is empty
        with open(filepath,'w') as f: # creates an empty file
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")