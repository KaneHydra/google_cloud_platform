# -*- coding=utf-8 -*-
import os
from rich import print
from google.cloud import bigquery

# 設置 Google Cloud 認證
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./service_account_key.json"

# 初始化 BigQuery 客戶端
client = bigquery.Client()
print("connection done")

project_id = "ai-project-25-0819"
dataset_id = "ai_dataset_25"
# 定義 SQL 查詢以創建模型
query = f"""
CREATE OR REPLACE MODEL `{project_id}.{dataset_id}.imported_tf_model`
OPTIONS (
    MODEL_TYPE='TENSORFLOW',
    MODEL_PATH='gs://cloud-training-demos/txtclass/export/exporter/1549825580/*'
)
"""

# 執行 SQL 查詢以創建模型
query_job = client.query(query)
query_job.result()  # 等待查詢完成

print("TensorFlow model import BigQuery ML")
