import os
import urllib.request as request 
import zipfile
from chickenDiseaseClassification import logger
from chickenDiseaseClassification.utils.common import get_size
from chickenDiseaseClassification.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(
        self,
        config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        """
        Download the file from the source URL and save it locally
        """
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url= self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"Downloaded {filename} to {self.config.local_data_file} with following info: \n{headers}")
        else:
            logger.info(f"File {self.config.local_data_file} already exists of size: {get_size(Path(self.config.local_data_file))}")
    
    def extract_zip_file(self):
        """
        Unzip the downloaded file
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,"r") as zip_ref:
            zip_ref.extractall(unzip_path)