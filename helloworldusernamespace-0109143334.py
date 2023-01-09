from airflow.operators.python import PythonOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "helloworldusernamespace-0109143334",
}

dag = DAG(
    "helloworldusernamespace-0109143334",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.10.1 pipeline editor using `untitled1.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: {"catalog_type": "airflow-package-catalog", "component_ref": {"airflow_package": "apache_airflow-2.4.1-py3-none-any.whl", "file": "airflow/operators/python.py"}}
op_36a7e6f7_da33_4afe_b1b6_bc3303967185 = PythonOperator(
    task_id="HelloWorld",
    python_callable="helloworld.py",
    op_args="",
    op_kwargs="",
    templates_dict="",
    templates_exts="",
    show_return_value_in_logs=True,
    mounted_volumes=[],
    dag=dag,
)
