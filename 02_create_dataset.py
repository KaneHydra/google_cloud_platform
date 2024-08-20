# -*- coding=utf-8 -*-
import os
from rich import print
from google.cloud import bigquery

# 設置 Google Cloud 認證
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./service_account_key.json"

# 初始化 BigQuery 客戶端
client = bigquery.Client()
print("connection done")

# 定義資料集參數
dataset_id = "ai_dataset_25_python"  # 替換為想要建立的資料集名稱
project_id = "ai-project-25-0819"  # 替換為 Google Cloud 專案 ID
dataset_ref = client.dataset(dataset_id)

# 設定資料集的描述和其他選項
dataset = bigquery.Dataset(dataset_ref)
dataset.description = "This is a new dataset created from Python."
dataset.location = "US"  # 設定資料集的地區位置

# 建立資料集
dataset = client.create_dataset(dataset, timeout=30)  # 可設定超時時間
print(f"dataset: {dataset.dataset_id} ,created")
