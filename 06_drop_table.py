# -*- coding=utf-8 -*-
import os
from rich import print
from google.cloud import bigquery

# 設置 Google Cloud 認證
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./service_account_key.json"

# 初始化 BigQuery 客戶端
client = bigquery.Client()
print("connection done")

# 定義資料集和資料表名稱
dataset_id = "ai_dataset_25"
table_id = "age_table"

# 定義資料表參數
table_ref = client.dataset(dataset_id).table(table_id)

# 刪除資料表
client.delete_table(table_ref)
print(f"table: {table_id} ,deleted")
