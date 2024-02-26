from chickenDiseaseClassification.config.configuration import ConfigurationManager
from chickenDiseaseClassification.components.data_ingestion import DataIngestion
from chickenDiseaseClassification import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion = DataIngestion(config.get_data_ingestion_config())
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            logger.error(f"Error in DataIngestion: {e}")
            raise e