from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPeipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.datascience.logging import logger

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_validation = DataValidationTrainingPeipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    model_trainer = ModelTrainerPipeline()
    model_trainer.initiate_model_training()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e 