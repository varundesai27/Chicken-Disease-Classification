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