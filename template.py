import os 
from pathlib import Path
import logging
import os
from pathlib import Path


logging.basicConfig(level=logging.INFO)

project_name  = "MLproject"

list_of_files = [
                    
                    f"src/{project_name}/__init__.py",
                    f"src/{project_name}/component/data_gitingestion.py",
                    f"src/{project_name}/component/data_transformation.py",
                    f"src/{project_name}/component/model_trainer.py",
                    f"src/{project_name}/component/model_monitoring.py",
                    f"src/{project_name}/piplines/__init__.py",
                    f"src/{project_name}/piplines/training_pipline.py",
                    f"src/{project_name}/piplines/prediction_pipline.py",
                    f"src/{project_name}/exception.py",
                    f"src/{project_name}/logger.py",
                    f"src/{project_name}/utils.py",
                    'app.py',
                    'Dockerfile',
                    'main.py'
]

for filepath in list_of_files:
    fileapth = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file{filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f" {filename} already exist")