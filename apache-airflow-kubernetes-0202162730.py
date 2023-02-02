from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.contrib.kubernetes.volume_mount import VolumeMount
from airflow.contrib.kubernetes.volume import Volume
from airflow.kubernetes.secret import Secret
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "apache-airflow-kubernetes-0202162730",
}

dag = DAG(
    "apache-airflow-kubernetes-0202162730",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
A generic pipeline tutorial
    """,
    is_paused_upon_creation=False,
)


# Operator source: load_data.ipynb

op_bb889c69_b23a_484e_8fb3_e69309f38a98 = KubernetesPodOperator(
    name="Load_weather_data",
    namespace="default",
    image="quay.io/opendatahub-contrib/workbench-images@sha256:16cab66461f294ab79e8947d469646826c9afdf3cdb56d8d1bc30ab7763f8555",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.1/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.1/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.1/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.1/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.1/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.1/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'apache-airflow-kubernetes' --cos-endpoint http://minio-service.opendatahub.svc.cluster.local:9000 --cos-bucket elyraairflowartifacts --cos-directory 'apache-airflow-kubernetes-0202162730' --cos-dependencies-archive 'load_data-bb889c69-b23a-484e-8fb3-e69309f38a98.tar.gz' --file 'load_data.ipynb' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' "
    ],
    task_id="Load_weather_data",
    env_vars={
        "DATASET_URL": "https://dax-cdn.cdn.appdomain.cloud/dax-noaa-weather-data-jfk-airport/1.1.4/noaa-weather-data-jfk-airport.tar.gz",
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "apache-airflow-kubernetes-{{ ts_nodash }}",
    },
    volumes=[
        Volume(
            name="data-elyra",
            configs={"persistentVolumeClaim": {"claimName": "data-elyra"}},
        ),
    ],
    volume_mounts=[
        VolumeMount(
            name="data-elyra",
            mount_path="/opt/app-root/src",
            sub_path="None",
            read_only=False,
        ),
    ],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_bb889c69_b23a_484e_8fb3_e69309f38a98.image_pull_policy = "IfNotPresent"

op_bb889c69_b23a_484e_8fb3_e69309f38a98.doc = """
        Download the data
    """


# Operator source: Part 1 - Data Cleaning.ipynb

op_8c96e288_4461_4d7e_8e0d_353c1fdb0c8c = KubernetesPodOperator(
    name="Part_1___Data_Cleaning",
    namespace="default",
    image="quay.io/opendatahub-contrib/workbench-images@sha256:16cab66461f294ab79e8947d469646826c9afdf3cdb56d8d1bc30ab7763f8555",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.1/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.1/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.1/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.1/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.1/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.1/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'apache-airflow-kubernetes' --cos-endpoint http://minio-service.opendatahub.svc.cluster.local:9000 --cos-bucket elyraairflowartifacts --cos-directory 'apache-airflow-kubernetes-0202162730' --cos-dependencies-archive 'Part 1 - Data Cleaning-8c96e288-4461-4d7e-8e0d-353c1fdb0c8c.tar.gz' --file 'Part 1 - Data Cleaning.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv' "
    ],
    task_id="Part_1___Data_Cleaning",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "apache-airflow-kubernetes-{{ ts_nodash }}",
    },
    volumes=[
        Volume(
            name="data-elyra",
            configs={"persistentVolumeClaim": {"claimName": "data-elyra"}},
        ),
    ],
    volume_mounts=[
        VolumeMount(
            name="data-elyra",
            mount_path="/opt/app-root/src",
            sub_path="None",
            read_only=False,
        ),
    ],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_8c96e288_4461_4d7e_8e0d_353c1fdb0c8c.image_pull_policy = "IfNotPresent"

op_8c96e288_4461_4d7e_8e0d_353c1fdb0c8c.doc = """
        Clean the data
    """

op_8c96e288_4461_4d7e_8e0d_353c1fdb0c8c << op_bb889c69_b23a_484e_8fb3_e69309f38a98


# Operator source: Part 2 - Data Analysis.ipynb

op_dcf486ef_2d73_4306_a3ca_af720a1f8eb3 = KubernetesPodOperator(
    name="Part_2___Data_Analysis",
    namespace="default",
    image="quay.io/opendatahub-contrib/workbench-images@sha256:16cab66461f294ab79e8947d469646826c9afdf3cdb56d8d1bc30ab7763f8555",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.1/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.1/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.1/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.1/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.1/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.1/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'apache-airflow-kubernetes' --cos-endpoint http://minio-service.opendatahub.svc.cluster.local:9000 --cos-bucket elyraairflowartifacts --cos-directory 'apache-airflow-kubernetes-0202162730' --cos-dependencies-archive 'Part 2 - Data Analysis-dcf486ef-2d73-4306-a3ca-af720a1f8eb3.tar.gz' --file 'Part 2 - Data Analysis.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv;data/noaa-weather-data-jfk-airport/jfk_weather.csv' "
    ],
    task_id="Part_2___Data_Analysis",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "apache-airflow-kubernetes-{{ ts_nodash }}",
    },
    volumes=[
        Volume(
            name="data-elyra",
            configs={"persistentVolumeClaim": {"claimName": "data-elyra"}},
        ),
    ],
    volume_mounts=[
        VolumeMount(
            name="data-elyra",
            mount_path="/opt/app-root/src",
            sub_path="None",
            read_only=False,
        ),
    ],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_dcf486ef_2d73_4306_a3ca_af720a1f8eb3.image_pull_policy = "IfNotPresent"

op_dcf486ef_2d73_4306_a3ca_af720a1f8eb3.doc = """
        Analyze the data
    """

op_dcf486ef_2d73_4306_a3ca_af720a1f8eb3 << op_8c96e288_4461_4d7e_8e0d_353c1fdb0c8c


# Operator source: Part 3 - Time Series Forecasting.ipynb

op_1e4b1763_337e_4f84_ae9c_a6cc79a1b7eb = KubernetesPodOperator(
    name="Part_3___Time_Series_Forecasting",
    namespace="default",
    image="quay.io/opendatahub-contrib/workbench-images@sha256:16cab66461f294ab79e8947d469646826c9afdf3cdb56d8d1bc30ab7763f8555",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.1/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.1/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.1/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.1/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.1/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.1/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'apache-airflow-kubernetes' --cos-endpoint http://minio-service.opendatahub.svc.cluster.local:9000 --cos-bucket elyraairflowartifacts --cos-directory 'apache-airflow-kubernetes-0202162730' --cos-dependencies-archive 'Part 3 - Time Series Forecasting-1e4b1763-337e-4f84-ae9c-a6cc79a1b7eb.tar.gz' --file 'Part 3 - Time Series Forecasting.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv;data/noaa-weather-data-jfk-airport/jfk_weather.csv' "
    ],
    task_id="Part_3___Time_Series_Forecasting",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "apache-airflow-kubernetes-{{ ts_nodash }}",
    },
    volumes=[
        Volume(
            name="data-elyra",
            configs={"persistentVolumeClaim": {"claimName": "data-elyra"}},
        ),
    ],
    volume_mounts=[
        VolumeMount(
            name="data-elyra",
            mount_path="/opt/app-root/src",
            sub_path="None",
            read_only=False,
        ),
    ],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_1e4b1763_337e_4f84_ae9c_a6cc79a1b7eb.image_pull_policy = "IfNotPresent"

op_1e4b1763_337e_4f84_ae9c_a6cc79a1b7eb.doc = """
        Explore approaches to predicting future temperatures
    """

op_1e4b1763_337e_4f84_ae9c_a6cc79a1b7eb << op_8c96e288_4461_4d7e_8e0d_353c1fdb0c8c
