import os
from box.exceptions import BoxValueError
import yaml
from chickenDiseaseClassification import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path)->ConfigBox:
    """
    Read yaml file and return a ConfigBox object.

    Parameters
    ----------
    path_to_yaml : Path
        Path to the yaml file.

    Returns
    -------
    ConfigBox
        ConfigBox object.
    """
    try:
        with open(path_to_yaml, "r") as f:
            config = yaml.safe_load(f)
            logger.info(f"yaml file: {path_to_yaml} is loaded successfully")
            return ConfigBox(config)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        logger.error(f"yaml file: {path_to_yaml} is not loaded successfully")
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create directories.

    Parameters
    ----------
    path_to_directories : list
        List of directories to be created.
    verbose : bool, optional
        Whether to print the information. The default is True.

    Returns
    -------
    None.
    """
    for directory in path_to_directories:
        os.makedirs(directory, exist_ok=True)
        if verbose:
            logger.info(f"Creating directory: {directory}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save json file.

    Parameters
    ----------
    path : Path
        Path to the json file.
    data : dict
        Data to be saved.

    Returns
    -------
    None.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file: {path} is saved successfully")


@ensure_annotations
def load_jasons(path: Path)->ConfigBox:
    """
    Load json file and return a ConfigBox object.

    Parameters
    ----------
    path : Path
        Path to the json file.

    Returns
    -------
    ConfigBox
        ConfigBox object.
    """
    with open(path) as f:
        data = json.load(f)
    logger.info(f"json file: {path} is loaded successfully")
    return ConfigBox(data)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save binary file.

    Parameters
    ----------
    data : Any
        Data to be saved.
    path : Path
        Path to the binary file.

    Returns
    -------
    None.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file: {path} is saved successfully")

@ensure_annotations
def load_bin(path: Path)->Any:
    """
    Load binary file and return the data.

    Parameters
    ----------
    path : Path
        Path to the binary file.

    Returns
    -------
    Any
        Data.
    """
    data = joblib.load(path)
    logger.info(f"binary file: {path} is loaded successfully")
    return data

@ensure_annotations
def get_size(path: Path)->str:
    """
    Get the size of a file.

    Parameters
    ----------
    path : Path
        Path to the file.
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"

@ensure_annotations
def decodeImage(imgstring,filename):
    """
    Decode base64 image.

    Parameters
    ----------
    imgstring : str
        Base64 image.
    filename : str
        Name of the file.

    Returns
    -------
    None."""
    imgdata = base64.b64decode(imgstring)
    with open(filename, "wb") as f:
        f.write(imgdata)
        f.close()

@ensure_annotations
def encodeImageIntoBase64(croppedImagePath):
    """
    Encode image into base64.

    Parameters
    ----------
    croppedImagePath : str
        Path to the image.
    """
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())

