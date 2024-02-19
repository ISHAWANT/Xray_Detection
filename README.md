#  Xray Lung Classifier

## Problem statement
Pneumonia is an inflammatory lung disease that mostly affects the alveoli, which are tiny air sacs.A productive or dry cough, chest pain, fever, and trouble breathing are common symptoms. There is variability in the condition's severity. Most often, infections with viruses or bacteria cause pneumonia; less frequently, infections with other microorganisms, some drugs, or illnesses like autoimmune diseases do.Risk factors include a history of smoking, a weakened immune system, asthma, diabetes, heart failure, cystic fibrosis, and chronic obstructive pulmonary disease (COPD). A physical examination and the patient's symptoms are frequently used to make the diagnosis. Blood tests, sputum culture, and chest X-rays can all aid in the diagnosis' confirmation.According to how it was obtained, the illness can be categorized, for example, as pneumonia contracted in a hospital, community, or through medical care. Our job is to develop an API that can determine if the provided photos are penumonia or not.

## Solution Proposed
The solution proposed for the above problem is that we have used Computer vision to solve the above problem to classify the data. We have used the Pytorch
framework to solve the above problem also we have have created our custom CNN network with the help of pytorch. Then we have created a API which takes in the images and predicts wheter a person is having Pneumonia or not. Then we have dockerized the application and deployed the model on AWS cloud.


![xray_arch](https://user-images.githubusercontent.com/71321529/216753362-aeb34400-d21d-4b21-b2ce-63b86a47b594.jpg)

## Dataset used
The dataset was shared by Apollo diagnostic center for research purpose. So we hvae created a POC with the given data.

## Tech Stack Used
1. Python 
2. FastAPI 
3. Pytorch
4. Docker
5. AWS
6. Azure

## Infrastructure required
1. AWS S3
2. AWS App Runner
3. Github Actions

## How to run

Step 1. Download the zip file
```
Download the zip file and extract it to a folder.
```
Step 2. Create a conda environment.
```
conda create -p env python=3.8 -y
```
```
conda activate ./env
````
Step 3. Install the requirements 
```
pip install -r requirements.txt
```
Step 4. Export the environment variable
```bash
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

export AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>

```
Step 5. Run the application server
```
python app.py
```
Step 6. Train application
```bash
http://localhost:8001/train
```
Step 7. Prediction application
```bash
http://localhost:8001/predict
```
## Run locally

1. Check if the Dockerfile is available in the project directory

2. Build the Docker image
```
docker build -t xray_classification .
```

3. Run the Docker image
```
docker run -d -p 8001:8001 -e AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID> -e AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY> xray_classifier
```

## Models Used
* Custom CNN architecture

## `xray` is the main package folder which contains 


**Components** : Contains all components of Deep Learning(CV) Project
- data_ingestion
- data_transformation
- model_training
- model_evaluation
- model_pusher


**Custom Logger and Exceptions** are used in the Project for better debugging purposes.

## Conclusion
- The project we have created can also be in real-life by doctors to check whether the person is having Pneumonia or not. It will help doctors to take
better decisions.
