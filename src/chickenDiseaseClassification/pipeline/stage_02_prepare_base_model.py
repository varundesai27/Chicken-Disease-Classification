from chickenDiseaseClassification.config.configuration import ConfigurationManager
from chickenDiseaseClassification.components.prepare_base_model import PrepareBaseModel
from chickenDiseaseClassification import logger

STAGE_NAME = "Preapre Base Model Stage"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            prepare_base_model = PrepareBaseModel(config.get_prepare_base_mode())
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
        except Exception as e:
            logger.error(f"Error in DataIngestion: {e}")
            raise e

if __name__ == '__main__':
    try:
        logger.info(f"----- stage: {STAGE_NAME} -----")
        data_ingestion = PrepareBaseModelTrainingPipeline()
        data_ingestion.main()
        logger.info(f"----- end of stage: {STAGE_NAME} -----")
    except Exception as e:
        logger.error(f"Error in {STAGE_NAME}: {e}")
        raise e