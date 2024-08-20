# -*- coding=utf-8 -*-
import os
from rich import print
from google.cloud import bigquery

# 設置 Google Cloud 認證
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./service_account_key.json"

# 初始化 BigQuery 客戶端
client = bigquery.Client()
print("connection done")

# 定義資料集名稱
dataset_id = "ai_dataset_25"

# 定義資料集參數
dataset_ref = client.dataset(dataset_id)

# 刪除資料集
client.delete_dataset(dataset_ref, delete_contents=True)
print(f"dataset: {dataset_id} ,deleted")
