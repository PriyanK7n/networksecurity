from NetworkSecurityProject.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig
from NetworkSecurityProject.components.data_ingestion import DataIngestion
from NetworkSecurityProject.components.data_validation import DataValidation
from NetworkSecurityProject.components.data_transformation import DataTransformation
from NetworkSecurityProject.components.model_trainer import ModelTrainer


import sys
# from NetworkSecurityProject.entity.artifact_entity import DataIngestionArtifact
from NetworkSecurityProject.exception.exception import NetworkSecurityException
from NetworkSecurityProject.logging.logger import logging

if __name__ == "__main__":

    try:

        '''Data Ingestion Process Starting'''
        trainingPipelineConfig = TrainingPipelineConfig()

        dataIngestionConfig= DataIngestionConfig(trainingPipelineConfig)
        data_ingestion_obj = DataIngestion(dataIngestionConfig)
        
        logging.info("Initating Data Ingestion Process")
        dataingestionartifact = data_ingestion_obj.initiate_data_ingestion()
        logging.info("Data Ingestion Process Completed")
        print(dataingestionartifact)
        '''Data Ingestion Process Finished'''
        


        '''Data Validation Process Started'''
        data_validation_config=DataValidationConfig(trainingPipelineConfig)
        data_validation=DataValidation(dataingestionartifact, data_validation_config)
        
        logging.info("Initating Data Validation Process")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data Validation Process Completed")
        print(data_validation_artifact)
        '''Data Validation Process Finished'''



        '''Data Transformation Process Started'''
        data_transformation_config = DataTransformationConfig(trainingPipelineConfig)
        logging.info("Initating Data Transformation Process")

        data_transformation = DataTransformation(data_validation_artifact, data_transformation_config)
        
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("Data Transformation Process Completed")
        '''Data Transformation Process Finished'''



        '''Model Training Process Started'''

        # data_transformation_config = DataTransformationConfig(trainingPipelineConfig)
        logging.info("Initating Model Training Process")
        print("Model Trainer uses data_transformation_artifact and ModelTrainerConfig as Input")
        model_trainer_config = ModelTrainerConfig(trainingPipelineConfig)
        model_trainer = ModelTrainer(model_trainer_config = model_trainer_config, data_transformation_artifact = data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiate_model_trainer()
        logging.info("Model Trainer Artifact Created hence Model Training Process Completed")
        
        '''Model Training Process Finished'''

    except Exception as e:
        raise NetworkSecurityException(e, sys)


