import sys
from Xray.components.data_ingestion import DataIngestion
from Xray.entity.artifact_entity import DataIngestionArtifact 
from Xray.entity.config_entity import DataIngestionConfig
from Xray.exception import XrayException
from Xray.logger import logging

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    



      
    def start_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Entered the start_data_ingestion method of TrainPipeline class")
        try:

            logging.info("Getting the data from s3 bucket")

            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config,
            )

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            logging.info("Got the train_set and test_set from s3")

            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )

            return data_ingestion_artifact

        except Exception as e:
            raise XrayException(e, sys)
        
    def run_pipeline(self) -> None:
        logging.info("Entered the run_pipeline method of TrainPipeline class")

        try:
            data_ingestion_artifact: DataIngestionArtifact = self.start_data_ingestion()
            

            logging.info("Exited the run_pipeline method of TrainPipeline class")

        except Exception as e:
            raise XrayException(e, sys)

           
# if __name__ == "__main__":
#     train_pipeline=TrainingPipeline()

#     train_pipeline.start_data_ingestion()