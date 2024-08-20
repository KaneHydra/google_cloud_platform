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

# 定義查詢語句
query = f"""
SELECT name, age
FROM `{project_id}.{dataset_id}.age_table`
WHERE age > 30;
"""

# 執行查詢
query_job = client.query(query)

# 獲取結果
results = query_job.result()

# 印出結果
for row in results:
    print(f"name: {row.name}, age: {row.age}")
