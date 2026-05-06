import logging

import duckdb
import pendulum
from airflow import DAG
from airflow.models import Variable
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

# Конфигурация DAG
OWNER = "a.bekkaliyev"
DAG_ID = "raw_from_api_to_s3" # Обычно соответствует названию файла

# Используемые таблицы в DAG
LAYER = "raw"
SOURCE = "earthquake"

#S3
ACCESS_KEY = Variable.get("access_key")
SECRET_KEY = Variable.get("sercet_key")

LONG_DESCRIPTION = """
# Описание дага в большом объеме 
"""

SHORT_DESCRIPTION = " Короткое описание дага в малом объеме"

args = {
    "owner": OWNER,
    "start_date": pendulum.datetime(2026, 5, 7),
    "catchup": True,
    "retries": 3,
    "retry_delay": pendulum.duration(hours=1)
    
}


def get_dates(**context) -> tuple[str, str]:
    pass
    

