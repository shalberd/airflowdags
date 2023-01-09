from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "cephh-0109155354",
}

dag = DAG(
    "cephh-0109155354",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.10.1 pipeline editor using `untitled1.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: helloworld.py
op_5817981e_131b_42de_908b_9ddb22bbc68b = KubernetesPodOperator(
    name="HelloWorld",
    namespace="airflow",
    image="continuumio/anaconda3:2021.11",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.10.1/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.10.1/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.10.1/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.10.1/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.10.1/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.10.1/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'cephh' --cos-endpoint http://ceph-nano-0 --cos-bucket elyrapipelineartifacts --cos-directory 'cephh-0109155354' --cos-dependencies-archive 'helloworld-5817981e-131b-42de-908b-9ddb22bbc68b.tar.gz' --file 'helloworld.py' "
    ],
    task_id="HelloWorld",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "1AIN4Z053K405LWWTLR9",
        "AWS_SECRET_ACCESS_KEY": "gZq2pATNJjPayMjmC0vafbfurPsq2xhi7tptdJT9",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "cephh-{{ ts_nodash }}",
    },
    in_cluster=True,
    config_file="None",
    dag=dag,
)
