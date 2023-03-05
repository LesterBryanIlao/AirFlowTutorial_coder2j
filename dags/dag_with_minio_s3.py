from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor

default_args = {
    'owner': 'lester',
    'retries': 5,
    'retry_delay': timedelta(minutes=10)
}

with DAG(
    dag_id='dag_with_minio_s3_v1',
    default_args=default_args,
    start_date=datetime(2023, 2, 1),
    schedule_interval='@daily'
) as dag:
    task1 = S3KeySensor(
    task1_id='sensor_minio_s3',
    bucket_name='airflow',
    # aws_connection_id=
    )
    
