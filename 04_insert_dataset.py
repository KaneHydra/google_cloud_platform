# -*- coding=utf-8 -*-
import os
from rich import print
from google.cloud import bigquery

# 設置 Google Cloud 認證
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./service_account_key.json"

# 初始化 BigQuery 客戶端
client = bigquery.Client()
print("connection done")

# 定義資料集和表資料表名稱
project_id = "ai-project-25-0819"  # 替換為 Google Cloud 專案 ID
# dataset_id = "ai-project-25-0819.ai_dataset_25"
dataset_id = "ai_dataset_25"
# dataset_id = "ai_dataset_25_python"
table_id = "age_table"

# 定義資料
rows_to_insert = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 35}]

# 插入資料
errors = client.insert_rows_json(f"{dataset_id}.{table_id}", rows_to_insert)

if errors == []:
    print("data insert successfully")
else:
    print(f"error: {errors}")
