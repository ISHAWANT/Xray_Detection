import os
import sys
from typing import Tuple

import joblib
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
from torchvision.datasets import ImageFolder

from xray.entity.artifacts_entity import (
    DataIngestionArtifact,
    DataTransformationArtifact,
)
from xray.entity.config_entity import DataTransformationConfig
from xray.exception import XRayException
from xray.logger import logging


class DataTransformation:
    def __init__(
        self,
        data_transformation_config: DataTransformationConfig,
        data_ingestion_artifact: DataIngestionArtifact,
    ):
        self.data_transformation_config = data_transformation_config

        self.data_ingestion_artifact = data_ingestion_artifact

    def transforming_training_data(self) -> transforms.Compose:
        try:
            logging.info(
                "Entered the transforming_training_data method of Data transformation class"
            )

            train_transform: transforms.Compose = transforms.Compose(
                [
                    transforms.Resize(self.data_transformation_config.RESIZE),
                    transforms.CenterCrop(self.data_transformation_config.CENTERCROP),
                    transforms.ColorJitter(
                        **self.data_transformation_config.color_jitter_transforms
                    ),
                    transforms.RandomHorizontalFlip(),
                    transforms.RandomRotation(
                        self.data_transformation_config.RANDOMROTATION
                    ),
                    transforms.ToTensor(),
                    transforms.Normalize(
                        **self.data_transformation_config.normalize_transforms
                    ),
                ]
            )

            logging.info(
                "Exited the transforming_training_data method of Data transformation class"
            )

            return train_transform

        except Exception as e:
            raise XRayException(e, sys)

    def transforming_testing_data(self) -> transforms.Compose:
        logging.info(
            "Entered the transforming_testing_data method of Data transformation class"
        )

        try:
            test_transform: transforms.Compose = transforms.Compose(
                [
                    transforms.Resize(self.data_transformation_config.RESIZE),
                    transforms.CenterCrop(self.data_transformation_config.CENTERCROP),
                    transforms.ToTensor(),
                    transforms.Normalize(
                        **self.data_transformation_config.normalize_transforms
                    ),
                ]
            )

            logging.info(
                "Exited the transforming_testing_data method of Data transformation class"
            )

            return test_transform

        except Exception as e:
            raise XRayException(e, sys)

    def data_loader(self,train_transform:transforms.Compose,test_transform:transforms.Compose)-> Tuple[DataLoader,DataLoader]:
        try:
            logging.info('Entered the data loader method of data transformation class')
            train_data: Dataset = ImageFolder(
                os.path.join(self,data_ingestion_artifact.train_file_path),
                transform=train_transform
            )
            test_data: Dataset = ImageFolder(
                os.path.join(self.data_ingestion_artifact.test_file_path),
                transform=test_transform
            )

            logging.info('Created train data and test data paths') 

            train_loader: DataLoader = DataLoader(
                train_data, **self.data_transformation_config.data_loader_params
            )
            test_loader: DataLoader = DataLoader(
                test_data, **self.data_transformation_config.data_loader_params
            )

            logging.info("Exited the data loader method of data transformation class")
            return train_loader,test_loader 


        except Exception as e:
            raise XrayException(e,sys)

    def initiate_data_transformation(self)->DataTransformationArtifact: 
        try:
            logging.info("Entered the initiate data_transforamtion method of data transfomation class")

            train_transform: transform.Compose = self.transforming_testing_data()
            test_transform: transform.Compose = self.transforming_testing_data() 
            
            os.makedirs(self.data_transformation_config.artifact_dir,exit_ok=True) 

            joblib.dump(
                train_transform,self.data_transformation_config.test_transforms_file
            )
            joblib.dump(
                test_transform,sefl.data_transformation_config.test_transforms_file
            )

            



