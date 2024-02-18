# from Xray.configuration.aws_connection import S3Client
# ins = S3Client() 

# Data Ingestion 
from Xray.entity.config_entity import DataIngestionConfig
from Xray.entity.artifact_entity import DataIngestionArtifact 

from Xray.components.data_ingestion import DataIngestion 

di_ins = DataIngestion(DataIngestionConfig)
di_art = di_ins.initiate_data_ingestion() 


