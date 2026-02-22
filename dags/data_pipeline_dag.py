from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "dheeraj",
    "start_date": datetime(2024, 1, 1),
}

with DAG(
    dag_id="local_data_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
) as dag:

    clean_task = BashOperator(
        task_id="clean_data",
        bash_command="python3 scripts/clean.py"
    )

    metrics_task = BashOperator(
        task_id="run_metrics",
        bash_command="python3 scripts/metrics.py"
    )

    clean_task >> metrics_task

