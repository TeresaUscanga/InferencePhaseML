import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator



def greet():
    return 'Greeted'
def respond():
    return 'Greet Responded Again'

default_args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2018, 9, 24, 10, 00, 00),
    'concurrency': 1,
    'retries': 0,
    'email_on_failure': False
}

with DAG('inference_workflow_dag',
         default_args=default_args,
         schedule_interval=None,
         max_active_runs=1
         ) as dag:

    execute_query_save = BigQueryInsertJobOperator(
            task_id="execute_query_save",
            configuration={
                "query": {
                    "query": f'select "10" as Id, "holo" as Message',
                    "useLegacySql": False,
                    "destinationTable": {
                        'projectId': "ml-inference-phase-automation",
                        'datasetId': "ml-inference-phase-automation:MLInferencePhaseAutomation",
                        'tableId': "ml-inference-phase-automation:MLInferencePhaseAutomation.DemoConnectionBigQuery",
                    },
                }
            },
        )

