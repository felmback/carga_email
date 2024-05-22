from google.cloud import bigquery
import db_dtypes
import os 




def dados():
    credentials = os.environ.get('key_prd')
    client = bigquery.Client.from_service_account_json(credentials)
    query = """
    SELECT 
    UF,
    LOCALIDADE,
    count(1) as VOLUME
    FROM `fibrasil-datalake-prd.gold_zone.tb_viabilidade_cto` 
    GROUP BY UF, LOCALIDADE
    limit 10

    """
    query_job = client.query(query)    
    df = query_job.to_dataframe()
    return df


df = dados()

print(df)
