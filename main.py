from chickenDiseaseClassification import logger

from chickenDiseaseClassification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Inngestion Stage"
try:
    logger.info(f"----- stage: {STAGE_NAME} -----")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"----- end of stage: {STAGE_NAME} -----")
except Exception as e:
    logger.error(f"Error in {STAGE_NAME}: {e}")
    raise e