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

# 定義 SQL 查詢以使用模型進行預測，只取五筆非 NULL 的資料
query = f"""
SELECT *
FROM ML.PREDICT(
    MODEL `{project_id}.{dataset_id}.imported_tf_model`,
    (
        SELECT title AS input
        FROM `bigquery-public-data.hacker_news.full`
        WHERE title IS NOT NULL
        LIMIT 5 -- 限制結果為五筆資料
    )
)
"""

# 執行 SQL 查詢以進行預測
query_job = client.query(query)
results = query_job.result()  # 等待查詢完成

# 印出預測結果
for row in results:
    print(row)
