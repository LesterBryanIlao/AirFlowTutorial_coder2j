from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'lester',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


def greet(name, age):
    print(f'Hello World! My name is {name} and age I am {age} years old.')


with DAG(
    dag_id='dag_with_python_operator_v1',
    default_args=default_args,
    description='Sample DAG with PythonOperator',
    start_date=datetime(2023, 2, 25, 2),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={'name': 'Tome', 'age': 22}
    )
