from datetime import datetime 
from typing import List
import torch 


TIMESTAMP: datetime=datetime.now().strftime("%m_%d_%Y_%H_%M_%S") 

ARTIFACT_DIR: str = 'artifacts'

AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
REGION_NAME = "us-east-1"

BUCKET_NAME: str = "lungxray1"

S3_DATA_FOLDER: str="data" 

CLASS_LABEL_1: str='NORMAL'

CLASS_LABEL_2: str = "PNEUMONIA" 

