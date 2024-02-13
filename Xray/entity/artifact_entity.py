from dataclasses import dataclass
from torch.utils.data.dataloader import DataLoader
# from Xray.logger import logger
# from Xray.exception import XrayException
# from Xray.constant.training_pipeline import * 

@dataclass
class DataIngestionArtifact:
    train_file_path: str
    test_file_path: str 

@dataclass
class DataTransformationArtifact:
    transformed_train_object: DataLoader

    transformed_test_object: DataLoader

    train_transform_file_path: str

    test_transform_file_path: str