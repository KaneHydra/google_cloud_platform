---
id: 20240719_google_cloud_platform
aliases: []
tags: []
---

# 20240719 google cloud platform

[![hackmd-github-sync-badge](https://hackmd.io/-WctByEWQh2OJE99Thhggw/badge)](https://hackmd.io/-WctByEWQh2OJE99Thhggw)

戴佳樺 Oscar 老師

hgfd12000@gmail.com

[上課教材Hacker.md](https://hackmd.io/@4HupY3slSPWy7VByk-0aXA/r1TUvEvuC)

課堂可能還會補充其他資料

## 免費抵用額度

AWS 不是所有的產品都能使用抵免額度

Azure 沒有抵免額度

GoogleCloud 所有的產品都可以用抵免額度

## Google GCP

DeepMind 其實是 Google 的子公司

TensorFlow 也是 Google 研發的

Google

-   BI
    -   數據分析
    -   視覺化
-   機器學習

-   BigQuery

### SQL vs NoSQL vs NewSQL

-   SQL
    -   OLTP
    -   OLAP
-   NoSQL
    -   Document-based databases
    -   Key-value stores
    -   Column-oriented databases
    -   Graph-based databases
-   New SQL

[What is NewSQL?](https://phoenixnap.com/kb/newsql)

[SQL vs NoSQL vs NewSQL: An In-depth Literature Review](https://blog.reachsumit.com/posts/2022/06/sql-nosql-newsql/)

## 應用

-   SQL
    -   SQL (CloudSQL)
        -   通用型
        -   資料一致性
        -   Web框架
-   NewSQL (Google Spanner)
    -   SQL管理+大規模擴展性
    -   遊戲公司
    -   物流公司
    -   智慧工廠
    -   社交軟體
-   資料倉儲 (BigQuery)
    -   資料交換
    -   分析同一平臺處理
    -   ML AI 視覺化 數據分析

## BigQuery

BI 就是 business intelligence 商業應用分析

-   BigQuery ML 數據分析 BI
    -   無伺服器架構 (Serverless？)
        -   容量 PayAsYouGo
        -   硬體 不用設定
    -   支持SQL
        -   SQL方言
            -   Google SQL
    -   即時查詢
        -   批次查詢
    -   導入導出
        -   雲端環境
            -   AWS S3
            -   GCP GCS
        -   本地上傳
            -   傳統的 Online Database 不行？
    -   機器學習
        -   VertexAI
            -   模型建立(在資料庫裡面)
                -   把資料直接送入模型裡面，就可以進行預測評估
                -   輸出
                    -   txt
                    -   json
    -   視覺化 Visualization
        -   Looker Studio
            -   免費
            -   各類圖表

## 架構

-   組織公司 (GCP)
    -   專案 project
        -   同一個專案下面可以建立跨區域資源
        -   服務 & API
            -   資源
        -   啟用 API
            -   BigQuery
                -   建立自己的 DataSet 資料集
                    -   模型
                        -   TrainingModel訓練模型
                        -   Vertex AI
                            -   服務帳號
                            -   LLM模型
                    -   DataTable
                    -   DataView
                    -   設定 區域&可用區
-   無組織 (AWS)
    -   跨區域服務無法互相存取

## 步驟

-   GCP 帳號建立
-   綁定付款帳號
-   建立專案
    -   ID `ai-project-25-0719`
-   啟用 API
    -   BigQuery
    -   BigQuery Connection
    -   Vertex AI API
    -   Cloud Natural Language API
-   位置格式
    -   專案ID.資料及ID.模型名稱or資料表名稱
-   建立資料集
    -   ID `ai_dataset_25_0719_us`
        -   多地區
        -   地區 US(多個美國地區)
    -   ID `ai_dataset_25_0719_eu`
        -   多地區
        -   地區 EU(多個歐盟地區)
-   新增公開資料集
    -   新增 往下拉
    -   公開資料集
    -   USA Names
    -   查看資料集
    -   左邊下面找到 usa names 展開
    -   點 `usa_1910_2013`
    -   右邊點 DETAILS
    -   複製 Table ID `bigquery-public-data.usa_names.usa_1910_2013`
-   查詢資料
    -   方法1 在左邊的 `usa_1910_2013` 上面點 Query
    -   方法2 上面tab點+, 可以自己下 SQL Query, table 就寫 `bigquery-public-data.usa_names.usa_1910_2013`

```sql
SELECT
name,
SUM(number) AS total
FROM `bigquery-public-data.usa_names.usa_1910_2013`
GROUP BY name
ORDER BY total DESC
LIMIT 100;
```

![](https://i.imgur.com/XM2i0tC.png)

-   儲存查詢結果

    -   儲存結果, 但是會佔用空間
    -   儲存檢視表 `top100name`

## 建立Vertex模型

新增
連線至外部資料來源
選擇VertexAI遠端模型、遠端函式和BigLake(Cloud資源)
連線ID `ai-vertexai-25-0719`
多地區 US(多個美國地區)

複製 Services Account ID, 等等建立服務帳號會用到

## 建立服務帳號

-   開啟 IAM
-   授予存取權
    -   新增主體, 貼剛剛的 Service Account ID
        -   指派角色 Vertex AI 使用者
        -   新增其他角色 BigQuery Connection User
        -   新增其他角色 服務使用情形消費者
    -   儲存

## 建立LLM模型

-   回到 BigQuery
-   建立SQL查詢

```sql
CREATE OR REPLACE MODEL `ai_dataset_25_0719_us.llm_model`
REMOTE WITH CONNECTION `projects/ai-project-25-0719/locations/us/connections/ai-vertexai-25-0719`
OPTIONS (ENDPOINT='text-bison');
```

MODEL 前面是 dataset 名稱,
打字他自己會跳出來

後面接`.llm_model`

![](https://i.imgur.com/f249D6w.png)

建完之後複製模型ID `ai_dataset_25_0719_us.llm_model`

## 查詢模型

```sql
SELECT
ml_generate_text_result['predictions'][0]['content'] AS generated_text,
ml_generate_text_result['predictions'][0]['safetyAttributes'] AS safety_attributes,
* EXCEPT (ml_generate_text_result)
FROM ML.GENERATE_TEXT(
    MODEL `ai_dataset_25_0719_us.llm_model`,
    (
        SELECT
        CONCAT(
            'Extract the key words from the text bellow: ',review
        ) AS prompt,
        *
        FROM `bigquery-public-data.imdb.reviews`
        LIMIT 5
    ),
    -- 控制隨機性
    STRUCT(
        0.2 AS temperature,
        100 AS max_output_tokens
    )
);
```

![](https://i.imgur.com/rSc081u.png)

下其他 prompt 查詢

```sql
SELECT
ml_generate_text_result['predictions'][0]['content'] AS generated_text,
ml_generate_text_result['predictions'][0]['safetyAttributes'] AS safety_attributes,
* EXCEPT (ml_generate_text_result)
FROM ML.GENERATE_TEXT(
    MODEL `ai_dataset_25_0719_us.llm_model`,
    (
        SELECT
        CONCAT(
            'perform sentiment analysis on the following text, return one the following categories: positive, negative: ',review
        ) AS prompt,
        *
        FROM `bigquery-public-data.imdb.reviews`
        LIMIT 5
    ),
    STRUCT(
        0.2 AS temperature,
        100 AS max_output_tokens
    )
);
```

![](https://i.imgur.com/EVKis78.png)
