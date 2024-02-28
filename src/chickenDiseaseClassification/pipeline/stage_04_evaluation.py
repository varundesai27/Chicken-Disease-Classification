from chickenDiseaseClassification.config.configuration import ConfigurationManager
from chickenDiseaseClassification.components.evaluation import Evaluation
from chickenDiseaseClassification import logger

STAGE_NAME = "Evaluation Stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            evaluation = Evaluation(config.get_validation_config())
            evaluation.evaluation()
            evaluation.save_score()
        except Exception as e:
            raise e

if __name__ == '__main__':
    try:
        logger.info(f"----- stage: {STAGE_NAME} -----")
        data_ingestion = EvaluationPipeline()
        data_ingestion.main()
        logger.info(f"----- end of stage: {STAGE_NAME} -----")
    except Exception as e:
        logger.error(f"Error in {STAGE_NAME}: {e}")
        raise e