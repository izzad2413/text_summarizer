import os
import box.exceptions 
import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations # ensure that the input of params match the hint
def read_yaml(path_to_yaml: Path) -> ConfigBox: # Using ConfigBox for easy dictionary data manipulation 
    """
    Read a YAML file and convert it into a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the YAML file to be read.
    
    Raises:
        Value Error: if yaml is empty
        e: empty file
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
        
@ensure_annotations # ensure that the input of params match the hint
def create_directories(path_to_directories: list, verbose=True):
    """
    Create list of directories
    
    Args:
        path_to_directories (list): List of directories to be created.
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Default to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory: {path} created successfully")

            
@ensure_annotations # ensure that the input of params match the hint
def get_size(path: Path) -> str:
    """
    Get size in KB
    
    Args:
        path (Path): path of the file
        
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
    