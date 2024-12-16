from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime


def fetch_and_print_variable():
    var_value = Variable.get("greeting")
    print(f"Value of 'greeting' is: {var_value}")


dag_params = {
    "dag_id": "read_airflow_variable_demo",
    "schedule_interval": None,
    "start_date": datetime(2024, 12, 3),
    "catchup": False,
}

with DAG(**dag_params) as dag:
    task = PythonOperator(
        task_id="print_variable_task",
        python_callable=fetch_and_print_variable,
    )

task
