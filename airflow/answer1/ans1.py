from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def print_hello():
    print("Hello World, This is Airflow")

with DAG(
        'hello_airflow_demo',
        schedule_interval=None,
        start_date=datetime(2024, 12, 4),
        catchup=False,
) as dag:


    hello_task = PythonOperator(
        task_id='print_hello_airflow_task',
        python_callable = print_hello,
    )


    hello_task