# from Xray.configuration.aws_connection import S3Client

# ins = S3Client()

# from Xray.pipeline.training_pipeline import TrainPipeline 

# if __name__=='__main__':
#     print('Hello') 
#     training_pipeline=TrainPipeline()
#     training_pipeline.run_pipeline()
import sys

from Xray.components.data_ingestion import DataIngestion
from Xray.entity.artifact_entity import DataIngestionArtifact
from Xray.entity.config_entity import DataIngestionConfig

di_ins = DataIngestion(DataIngestionConfig)

di_art = di_ins.initiate_data_ingestion()