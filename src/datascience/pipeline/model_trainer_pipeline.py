from src.datascience.entity.config_entity import ModelTrainerConfig
from src.datascience.components.model_trainer import ModelTrainer
from src.datascience.config.configuration import ConfigurationManager
from src.datascience.logging import logger 

STAGE_NAME = "Model Trainer Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.train()


if __name__=="__main__":
    try:
        logger.info(f">>>>> {STAGE_NAME} started <<<<<")
        obj = ModelTrainerPipeline()
        obj.initiate_model_training()
        logger.info(f">>>>> {STAGE_NAME} completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise e 

        



