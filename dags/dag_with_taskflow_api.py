from datetime import datetime, timedelta
from airflow.decorators import dag, task

default_args = {
    'owner': 'lester',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


@dag(dag_id='dag_with_taskflow_api_v2',
     default_args=default_args,
     start_date=datetime(2023, 2, 25, 2),
     schedule_interval='@daily')
def hello_world_etl():

    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name': 'Lester',
            'last_name': 'Ilao'
        }

    @task()
    def get_age():
        return 22

    @task()
    def greet(first_name, last_name, age):
        print(F'Hello World! My name is {first_name} {last_name} and age I am {age} years old.')

    # name = get_name()
    name_dict = get_name()
    age = get_age()

    greet(first_name=name_dict['first_name'], last_name=name_dict['last_name'], age=age)


greet_dag = hello_world_etl()
