from chickenDiseaseClassification import logger

from chickenDiseaseClassification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from chickenDiseaseClassification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from chickenDiseaseClassification.pipeline.stage_03_training import ModelTrainingPipeline
from chickenDiseaseClassification.pipeline.stage_04_evaluation import EvaluationPipeline
STAGE_NAME = "Data Inngestion Stage"
try:
    logger.info(f"----- stage: {STAGE_NAME} -----")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"----- end of stage: {STAGE_NAME} -----")
except Exception as e:
    logger.error(f"Error in {STAGE_NAME}: {e}")
    raise e

STAGE_NAME = "Prepare Base Model Stage"
try:
    logger.info(f"----- stage: {STAGE_NAME} -----")
    data_ingestion = PrepareBaseModelTrainingPipeline()
    data_ingestion.main()
    logger.info(f"----- end of stage: {STAGE_NAME} -----")
except Exception as e:
    logger.error(f"Error in {STAGE_NAME}: {e}")
    raise e

STAGE_NAME = "Model Training Stage"
try:
    logger.info(f"----- stage: {STAGE_NAME} -----")
    data_ingestion = ModelTrainingPipeline()
    data_ingestion.main()
    logger.info(f"----- end of stage: {STAGE_NAME} -----")
except Exception as e:
    logger.error(f"Error in {STAGE_NAME}: {e}")
    raise e

STAGE_NAME = "Evaluation Stage"

try:
    logger.info(f"----- stage: {STAGE_NAME} -----")
    data_ingestion = EvaluationPipeline()
    data_ingestion.main()
    logger.info(f"----- end of stage: {STAGE_NAME} -----")
except Exception as e:
    logger.error(f"Error in {STAGE_NAME}: {e}")
    raise e