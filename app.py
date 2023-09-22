import sys
from src.MLproject.logger import logging
from src.MLproject.exception   import CustomException
if __name__=="__main__":
    logging.info("the execution has started")
try:
    a=10
except Exception as e:
    logging.info("Custom Exceptiom")
    raise CustomException(e,sys)
from src.MLproject import utils
df=utils.read_sql_data()
print(df)