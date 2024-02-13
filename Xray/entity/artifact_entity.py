from dataclasses import dataclass
from torch.utils.data.dataloader import DataLoader
# from Xray.logger import logger
# from Xray.exception import XrayException
# from Xray.constant.training_pipeline import * 

@dataclass
class DataIngestionArtifact:
    train_file_path: str
    test_file_path: str 