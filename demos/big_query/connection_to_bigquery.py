from google.cloud import bigquery
import os 

# To do: add following packages to requirements files
#pip install --upgrade google-cloud
#pip install --upgrade google-cloud-bigquery
#pip install --upgrade google-cloud-storage

crendentials_path = r'D:/data engineering/InferencePhaseML/demos/big_query/pythonbq.privateKey.json' 
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = crendentials_path

client = bigquery.Client()
table_id = 'ml-inference-phase-automation.MLInferencePhaseAutomation.DemoConnectionBigQuery'

rows_to_insert = [
    {u'Id': 3, u'Message': 'yee'},
    {u'Id': 4, u'Message': 'uwu'}
] 

errors = client.insert_rows_json(table_id, rows_to_insert)
if errors == []:
    print('New rows have been added.')
else:
    print(f'Encountered errors while insert rows: {errors}')
