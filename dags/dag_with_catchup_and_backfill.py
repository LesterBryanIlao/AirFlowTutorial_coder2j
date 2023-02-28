from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.decorators import dag, task

default_args = {
    'owner': 'lester',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


@dag(dag_id='dag_with_catchup_and_backfill_v2',
     default_args=default_args,
     start_date=datetime(2023, 2, 27, 2),
     schedule_interval='@daily',
     catchup=False)
def dag_with_catchup_and_backfill():

    task1 = BashOperator(
        task_id='task1',
        bash_command='echo This is a simple bash command!'
    )
    
    task1


new_dag = dag_with_catchup_and_backfill()


# with DAG(
#     dag_id='dag_with_catchup_and_backfill_v0',
#     default_args=default_args,
#     start_date=datetime(2023, 2, 27, 2),
#     schedule_interval='@daily',
#     catchup=True
# ) as dag:
#     task1 = BashOperator(
#         task_id='task1',
#         bash_command='echo This is a simple bash command!'
#     )

#     task1
