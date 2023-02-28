from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'lester',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

def get_sklearn():
    import sklearn
    print(f"Scikit-learn version: {sklearn.__version__}")
    

def get_matplotlib():
    import matplotlib
    print(f"Matplotlib version: {matplotlib.__version__}")

with DAG(
    dag_id='dag_with_dependencies_v2',
    default_args=default_args,
    start_date=datetime(2023, 2, 1),
    schedule_interval='0 0 * * *'
) as dag:
    get_sklearn = PythonOperator(
        task_id='get_sklearn',
        python_callable=get_sklearn
    )
    
    get_matplotlib = PythonOperator(
        task_id='get_matplotlib',
        python_callable=get_matplotlib
    )

    get_sklearn >> get_matplotlib
