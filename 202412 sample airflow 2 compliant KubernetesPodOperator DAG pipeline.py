from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from kubernetes.client import models as k8s
from airflow.providers.cncf.kubernetes.secret import Secret
from airflow import DAG
import pendulum

args = {
    "project_id": "202412-Sven-Pipeline-Sample-1211104854",
}

dag = DAG(
    dag_id="202412-Sven-Pipeline-Sample-1211104854",
    default_args=args,
    schedule="@once",
    start_date=pendulum.today("UTC").add(days=-1),
    description="""
Created with Elyra 3.16.0.dev0 pipeline editor using `hello-generic-world-2.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: load_data.ipynb

op_84d9f7e8_295e_4337_a8d3_e5cd7a97226a = KubernetesPodOperator(
    name="load_weather_data",
    namespace="tst-airflow",
    image="mycontainerrepo.com/analytics/workbench-images@sha256:7d428ae5fb8c497e4217501bc93243c6918691736ef32a8e90c54da80a51f742",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/bin/utils/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/bin/utils/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///opt/app-root/bin/utils/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/bin/utils/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name '202412 Sven Pipeline Sample' --cos-endpoint https://s3-for-elyra.internals.mycompany.com --cos-bucket ix-jupyter-apps-dev --cos-directory 'project/helloworldsven/202412 Sven Pipeline Sample-1211104854' --cos-dependencies-archive 'load_data-84d9f7e8-295e-4337-a8d3-e5cd7a97226a.tar.gz' --file 'load_data.ipynb' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' "
    ],
    task_id="load_weather_data",
    env_vars={
        "SSL_CERT_FILE": "/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem",
        "REQUESTS_CA_BUNDLE": "/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem",
        "PIP_CERT": "/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem",
        "NO_PROXY": ".cluster.local,.ocp4test.mycompany.com,.mycompany.com,.svc,.internals.mycompany.com,10.0.0.0/16,10.0.0.0/8,10.128.0.0/14,127.0.0.1,172.30.0.0/16,api-int.ocp4test.mycompany.com,localhost,ocp4test.mycompany.com,mycompany.com,registry.ixcloud.ch,mycompany.com,internals.mycompany.com",
        "HTTP_PROXY": "http://server-proxy.internals.mycompany.com:8080",
        "HTTPS_PROXY": "http://server-proxy.internals.mycompany.com:8080",
        "DATASET_URL": "https://repo.internals.mycompany.com/artifactory/ix_datascience_intern/noaa-weather-data-jfk-airport.tar.gz",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "202412 Sven Pipeline Sample-{{ ts_nodash }}",
    },
    container_resources=k8s.V1ResourceRequirements(
        requests={
            "cpu": "1",
            "memory": "1G",
        },
        limits={
            "cpu": "1.5",
            "memory": "2G",
        },
    ),
    volumes=[
        k8s.V1Volume(
            name="pvc-in-airflow-namespace",
            persistent_volume_claim=k8s.V1PersistentVolumeClaimVolumeSource(
                claim_name="pvc-in-airflow-namespace",
            ),
        ),
        k8s.V1Volume(
            name="trusted-ca",
            config_map=k8s.V1ConfigMapVolumeSource(
                name="trusted-ca",
                optional=False,
                items=[k8s.V1KeyToPath(key="ca-bundle.crt", path="tls-ca-bundle.pem")],
            ),
        ),
    ],
    volume_mounts=[
        k8s.V1VolumeMount(
            name="pvc-in-airflow-namespace",
            mount_path="/opt/app-root/src",
            sub_path="None",
            read_only=False,
        ),
        k8s.V1VolumeMount(
            name="trusted-ca",
            mount_path="/etc/pki/ca-trust/extracted/pem",
            read_only=True,
        ),
    ],
    secrets=[
        Secret(
            "env", "AWS_ACCESS_KEY_ID", "elyra-cos-s3-secret-openshift-airflow", "AWS_ACCESS_KEY_ID"
        ),
        Secret(
            "env",
            "AWS_SECRET_ACCESS_KEY",
            "elyra-cos-s3-secret-openshift-airflow",
            "AWS_SECRET_ACCESS_KEY",
        ),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file=None,
    dag=dag,
)

op_84d9f7e8_295e_4337_a8d3_e5cd7a97226a.image_pull_policy = "IfNotPresent"


# Operator source: Part 1 - Data Cleaning.ipynb

op_c154af0d_ebb0_4dcd_8629_e5dc224c17db = KubernetesPodOperator(
    name="part1_data_cleaning",
    namespace="tst-airflow",
    image="mycontainerrepo.com/analytics/workbench-images@sha256:7d428ae5fb8c497e4217501bc93243c6918691736ef32a8e90c54da80a51f742",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/bin/utils/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/bin/utils/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///opt/app-root/bin/utils/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/bin/utils/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name '202412 Sven Pipeline Sample' --cos-endpoint https://s3-for-elyra.internals.mycompany.com --cos-bucket ix-jupyter-apps-dev --cos-directory 'project/helloworldsven/202412 Sven Pipeline Sample-1211104854' --cos-dependencies-archive 'Part 1 - Data Cleaning-c154af0d-ebb0-4dcd-8629-e5dc224c17db.tar.gz' --file 'Part 1 - Data Cleaning.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv' "
    ],
    task_id="part1_data_cleaning",
    env_vars={
        "SSL_CERT_FILE": "/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem",
        "REQUESTS_CA_BUNDLE": "/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem",
        "PIP_CERT": "/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem",
        "NO_PROXY": ".cluster.local,.ocp4test.mycompany.com,.mycompany.com,.svc,.internals.mycompany.com,10.0.0.0/16,10.0.0.0/8,10.128.0.0/14,127.0.0.1,172.30.0.0/16,api-int.ocp4test.mycompany.com,localhost,ocp4test.mycompany.com,mycompany.com,registry.ixcloud.ch,mycompany.com,internals.mycompany.com",
        "HTTP_PROXY": "http://server-proxy.internals.mycompany.com:8080",
        "HTTPS_PROXY": "http://server-proxy.internals.mycompany.com:8080",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "202412 Sven Pipeline Sample-{{ ts_nodash }}",
    },
    container_resources=k8s.V1ResourceRequirements(
        requests={
            "cpu": "1",
            "memory": "1G",
        },
        limits={},
    ),
    volumes=[
        k8s.V1Volume(
            name="pvc-in-airflow-namespace",
            persistent_volume_claim=k8s.V1PersistentVolumeClaimVolumeSource(
                claim_name="pvc-in-airflow-namespace",
            ),
        ),
        k8s.V1Volume(
            name="trusted-ca",
            config_map=k8s.V1ConfigMapVolumeSource(
                name="trusted-ca",
                optional=False,
                items=[k8s.V1KeyToPath(key="ca-bundle.crt", path="tls-ca-bundle.pem")],
            ),
        ),
    ],
    volume_mounts=[
        k8s.V1VolumeMount(
            name="pvc-in-airflow-namespace",
            mount_path="/opt/app-root/src",
            sub_path="None",
            read_only=False,
        ),
        k8s.V1VolumeMount(
            name="trusted-ca",
            mount_path="/etc/pki/ca-trust/extracted/pem",
            read_only=True,
        ),
    ],
    secrets=[
        Secret(
            "env", "AWS_ACCESS_KEY_ID", "elyra-cos-s3-secret-openshift-airflow", "AWS_ACCESS_KEY_ID"
        ),
        Secret(
            "env",
            "AWS_SECRET_ACCESS_KEY",
            "elyra-cos-s3-secret-openshift-airflow",
            "AWS_SECRET_ACCESS_KEY",
        ),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file=None,
    dag=dag,
)

op_c154af0d_ebb0_4dcd_8629_e5dc224c17db.image_pull_policy = "IfNotPresent"

op_c154af0d_ebb0_4dcd_8629_e5dc224c17db << op_84d9f7e8_295e_4337_a8d3_e5cd7a97226a


# Operator source: Part 2 - Data Analysis.ipynb

op_f7981b2b_8a22_4d1a_a0ec_57baeb710528 = KubernetesPodOperator(
    name="part2_data_analysis",
    namespace="tst-airflow",
    image="mycontainerrepo.com/analytics/workbench-images@sha256:7d428ae5fb8c497e4217501bc93243c6918691736ef32a8e90c54da80a51f742",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/bin/utils/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/bin/utils/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///opt/app-root/bin/utils/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/bin/utils/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name '202412 Sven Pipeline Sample' --cos-endpoint https://s3-for-elyra.internals.mycompany.com --cos-bucket ix-jupyter-apps-dev --cos-directory 'project/helloworldsven/202412 Sven Pipeline Sample-1211104854' --cos-dependencies-archive 'Part 2 - Data Analysis-f7981b2b-8a22-4d1a-a0ec-57baeb710528.tar.gz' --file 'Part 2 - Data Analysis.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv;data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv' "
    ],
    task_id="part2_data_analysis",
    env_vars={
        "SSL_CERT_FILE": "/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem",
        "REQUESTS_CA_BUNDLE": "/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem",
        "PIP_CERT": "/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem",
        "NO_PROXY": ".cluster.local,.ocp4test.mycompany.com,.mycompany.com,.svc,.internals.mycompany.com,10.0.0.0/16,10.0.0.0/8,10.128.0.0/14,127.0.0.1,172.30.0.0/16,api-int.ocp4test.mycompany.com,localhost,ocp4test.mycompany.com,mycompany.com,registry.ixcloud.ch,mycompany.com,internals.mycompany.com",
        "HTTP_PROXY": "http://server-proxy.internals.mycompany.com:8080",
        "HTTPS_PROXY": "http://server-proxy.internals.mycompany.com:8080",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "202412 Sven Pipeline Sample-{{ ts_nodash }}",
    },
    container_resources=k8s.V1ResourceRequirements(
        requests={
            "cpu": "1",
            "memory": "6G",
        },
        limits={},
    ),
    volumes=[
        k8s.V1Volume(
            name="pvc-in-airflow-namespace",
            persistent_volume_claim=k8s.V1PersistentVolumeClaimVolumeSource(
                claim_name="pvc-in-airflow-namespace",
            ),
        ),
        k8s.V1Volume(
            name="trusted-ca",
            config_map=k8s.V1ConfigMapVolumeSource(
                name="trusted-ca",
                optional=False,
                items=[k8s.V1KeyToPath(key="ca-bundle.crt", path="tls-ca-bundle.pem")],
            ),
        ),
    ],
    volume_mounts=[
        k8s.V1VolumeMount(
            name="pvc-in-airflow-namespace",
            mount_path="/opt/app-root/src",
            sub_path="None",
            read_only=False,
        ),
        k8s.V1VolumeMount(
            name="trusted-ca",
            mount_path="/etc/pki/ca-trust/extracted/pem",
            read_only=True,
        ),
    ],
    secrets=[
        Secret(
            "env", "AWS_ACCESS_KEY_ID", "elyra-cos-s3-secret-openshift-airflow", "AWS_ACCESS_KEY_ID"
        ),
        Secret(
            "env",
            "AWS_SECRET_ACCESS_KEY",
            "elyra-cos-s3-secret-openshift-airflow",
            "AWS_SECRET_ACCESS_KEY",
        ),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file=None,
    dag=dag,
)

op_f7981b2b_8a22_4d1a_a0ec_57baeb710528.image_pull_policy = "IfNotPresent"

op_f7981b2b_8a22_4d1a_a0ec_57baeb710528 << op_c154af0d_ebb0_4dcd_8629_e5dc224c17db


# Operator source: Part 3 - Time Series Forecasting.ipynb

op_29e9335a_7f52_40d7_9eb0_e7c671d67dfc = KubernetesPodOperator(
    name="part3_time_series_forecasting",
    namespace="tst-airflow",
    image="mycontainerrepo.com/analytics/workbench-images@sha256:7d428ae5fb8c497e4217501bc93243c6918691736ef32a8e90c54da80a51f742",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/bin/utils/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/bin/utils/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///opt/app-root/bin/utils/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/bin/utils/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name '202412 Sven Pipeline Sample' --cos-endpoint https://s3-for-elyra.internals.mycompany.com --cos-bucket ix-jupyter-apps-dev --cos-directory 'project/helloworldsven/202412 Sven Pipeline Sample-1211104854' --cos-dependencies-archive 'Part 3 - Time Series Forecasting-29e9335a-7f52-40d7-9eb0-e7c671d67dfc.tar.gz' --file 'Part 3 - Time Series Forecasting.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv;data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv' "
    ],
    task_id="part3_time_series_forecasting",
    env_vars={
        "SSL_CERT_FILE": "/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem",
        "REQUESTS_CA_BUNDLE": "/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem",
        "PIP_CERT": "/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem",
        "NO_PROXY": ".cluster.local,.ocp4test.mycompany.com,.mycompany.com,.svc,.internals.mycompany.com,10.0.0.0/16,10.0.0.0/8,10.128.0.0/14,127.0.0.1,172.30.0.0/16,api-int.ocp4test.mycompany.com,localhost,ocp4test.mycompany.com,mycompany.com,registry.ixcloud.ch,mycompany.com,internals.mycompany.com",
        "HTTP_PROXY": "http://server-proxy.internals.mycompany.com:8080",
        "HTTPS_PROXY": "http://server-proxy.internals.mycompany.com:8080",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "202412 Sven Pipeline Sample-{{ ts_nodash }}",
    },
    container_resources=k8s.V1ResourceRequirements(
        requests={
            "cpu": "1",
            "memory": "1.5G",
        },
        limits={},
    ),
    volumes=[
        k8s.V1Volume(
            name="pvc-in-airflow-namespace",
            persistent_volume_claim=k8s.V1PersistentVolumeClaimVolumeSource(
                claim_name="pvc-in-airflow-namespace",
            ),
        ),
        k8s.V1Volume(
            name="trusted-ca",
            config_map=k8s.V1ConfigMapVolumeSource(
                name="trusted-ca",
                optional=False,
                items=[k8s.V1KeyToPath(key="ca-bundle.crt", path="tls-ca-bundle.pem")],
            ),
        ),
    ],
    volume_mounts=[
        k8s.V1VolumeMount(
            name="pvc-in-airflow-namespace",
            mount_path="/opt/app-root/src",
            sub_path="None",
            read_only=False,
        ),
        k8s.V1VolumeMount(
            name="trusted-ca",
            mount_path="/etc/pki/ca-trust/extracted/pem",
            read_only=True,
        ),
    ],
    secrets=[
        Secret(
            "env", "AWS_ACCESS_KEY_ID", "elyra-cos-s3-secret-openshift-airflow", "AWS_ACCESS_KEY_ID"
        ),
        Secret(
            "env",
            "AWS_SECRET_ACCESS_KEY",
            "elyra-cos-s3-secret-openshift-airflow",
            "AWS_SECRET_ACCESS_KEY",
        ),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file=None,
    dag=dag,
)

op_29e9335a_7f52_40d7_9eb0_e7c671d67dfc.image_pull_policy = "IfNotPresent"

op_29e9335a_7f52_40d7_9eb0_e7c671d67dfc << op_c154af0d_ebb0_4dcd_8629_e5dc224c17db
