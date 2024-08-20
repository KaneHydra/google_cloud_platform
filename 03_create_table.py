# -*- coding=utf-8 -*-
import os
from rich import print
from google.cloud import bigquery

# 設置 Google Cloud 認證
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./service_account_key.json"

# 初始化 BigQuery 客戶端
client = bigquery.Client()
print("connection done")

# 定義資料集和資料表
# dataset_id = "ai_dataset_25_python"
dataset_id = "ai_dataset_25"
table_id = "age_table"
schema = [
    bigquery.SchemaField("name", "STRING"),
    bigquery.SchemaField("age", "INTEGER"),
]

# 定義表格參數
table_ref = client.dataset(dataset_id).table(table_id)
table = bigquery.Table(table_ref, schema=schema)

# 建立資料表
table = client.create_table(table)
print(f"table: {table.table_id} ,created")
