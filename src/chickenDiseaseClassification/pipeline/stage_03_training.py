from chickenDiseaseClassification.config.configuration import ConfigurationManager
from chickenDiseaseClassification.components.prepare_callbacks import PrepareCallbacks
from chickenDiseaseClassification.components.training import Training
from chickenDiseaseClassification import logger

STAGE_NAME = "Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            prepare_callback_config = config.get_prepare_callbacks_config()
            prepare_callbacks = PrepareCallbacks(config=prepare_callback_config)
            callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

            training_config = config.get_training_config()
            training = Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train(callback_list=callback_list)
        except Exception as e:
            raise e