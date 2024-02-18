from datetime import datetime 
from typing import List
import torch 


TIMESTAMP: datetime=datetime.now().strftime("%m_%d_%Y_%H_%M_%S") 

# Data ingestion related constant

ARTIFACT_DIR: str = 'artifacts'


AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
REGION_NAME = "us-east-1"


BUCKET_NAME: str = "lungxray1"

S3_DATA_FOLDER: str="data" 

CLASS_LABEL_1: str='NORMAL'

CLASS_LABEL_2: str = "PNEUMONIA" 

# Data transformation related constant 

BRIGHTNESS: int = 0.10

CONTRAST: int = 0.1

SATURATION: int = 0.10

HUE: int = 0.1

RESIZE: int = 224

CENTERCROP: int = 224

RANDOMROTATION: int = 10

NORMALIZE_LIST_1: List[int] = [0.485, 0.456, 0.406]

NORMALIZE_LIST_2: List[int] = [0.229, 0.224, 0.225]

TRAIN_TRANSFORMS_KEY: str = "xray_train_transforms"

TRAIN_TRANSFORMS_FILE: str = "train_transforms.pkl"

TEST_TRANSFORMS_FILE: str = "test_transforms.pkl"

BATCH_SIZE: int = 2

SHUFFLE: bool = False

PIN_MEMORY: bool = True

