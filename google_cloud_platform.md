---
id: google_cloud_platform
aliases: []
tags: []
---

# google cloud platform

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

上課內容參考:[使用远程模型和 ML.GENERATE_TEXT 函数生成文本](https://cloud.google.com/bigquery/docs/generate-text-tutorial?hl=zh-cn)

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

![圖](https://i.imgur.com/XM2i0tC.png)

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

![圖](https://i.imgur.com/f249D6w.png)

建完之後複製模型ID `ai_dataset_25_0719_us.llm_model`

## query model via prompt

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

![圖](https://i.imgur.com/rSc081u.png)

### query more prompt

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

![圖](https://i.imgur.com/EVKis78.png)

### flatten json output

記得先把查詢欄位移除, `flatten_json_output` 會自己產生欄位

```sql
SELECT *
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
        100 AS max_output_tokens,
        TRUE AS flatten_json_output
    )
);
```

![圖](https://i.imgur.com/Q3WKiqd.png)

### emotion analysis

```sql
SELECT
  ml_generate_text_result['predictions'][0]['content'] AS generated_text,
  ml_generate_text_result['predictions'][0]['safetyAttributes']
    AS safety_attributes,
  * EXCEPT (ml_generate_text_result)
FROM ML.GENERATE_TEXT(
  MODEL `ai_dataset_25_0719_us.llm_model`,
  (
      SELECT
      CONCAT(
          'perform sentiment analysis on the following text, return one the following categories: positive, negative: ',
          review
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

![圖](https://i.imgur.com/1PBC8zj.png)

## 語義分析

### 建立 CLOUD_AI_NATURAL_LANGUAGE_V1 model

```sql
CREATE OR REPLACE MODEL `ai-project-25-0719.ai_dataset_25_0719_us.my_nlp_model`
REMOTE WITH CONNECTION `projects/ai-project-25-0719/locations/us/connections/ai-vertexai-25-0719`
OPTIONS (REMOTE_SERVICE_TYPE='CLOUD_AI_NATURAL_LANGUAGE_v1');
```

![圖](https://i.imgur.com/E9YgmXU.png)

### 建立 table 一次丟很多prompt 進去

在 `ai_dataset_25_0719_us` 上面右鍵建立資料表

資料表 `my_nlp_table`

資料表類型 原生資料表

Schema有兩個
`comment`, STRING, NULLABLE
`text_content`, STRING, NULLABLE

然後建立資料表

![圖](https://i.imgur.com/eO3Wzzr.png)

![圖](https://i.imgur.com/ydsBIF2.png)

### 插入 input 內容

```sql
INSERT INTO `ai-project-25-0719.ai_dataset_25_0719_us.my_nlp_table` (text_content)
VALUES
  ('你什麼時候產生了我使用鏡花水月的錯覺'),
  ('為什麼要演奏春日影！'),
  ('珍惜生命，我用Python。');
```

![圖](https://i.imgur.com/P3lc37S.png)

### 使用資料表內容 input 到模型裡面 進行語義分析

```sql
SELECT *
FROM ML.UNDERSTAND_TEXT(
    MODEL `ai-project-25-0719.ai_dataset_25_0719_us.my_nlp_model`,
    TABLE `ai-project-25-0719.ai_dataset_25_0719_us.my_nlp_table`,
    STRUCT(
        'analyze_sentiment' AS nlu_option
    )
);
```

![圖](https://i.imgur.com/ZDpEs0q.png)

```json
[
    {
        "ml_understand_text_result": "{\"document_sentiment\":{\"magnitude\":0.1,\"score\":0.1},\"language\":\"zh\",\"sentences\":[{\"sentiment\":{\"magnitude\":0.1,\"score\":0.1},\"text\":{\"begin_offset\":-1,\"content\":\"珍惜生命，我用Python。\"}}]}",
        "ml_understand_text_status": "",
        "comment": null,
        "text_content": "珍惜生命，我用Python。"
    },
    {
        "ml_understand_text_result": "{\"document_sentiment\":{\"magnitude\":0.5,\"score\":-0.5},\"language\":\"zh-Hant\",\"sentences\":[{\"sentiment\":{\"magnitude\":0.5,\"score\":-0.5},\"text\":{\"begin_offset\":-1,\"content\":\"你什麼時候產生了我使用鏡花水月的錯覺\"}}]}",
        "ml_understand_text_status": "",
        "comment": null,
        "text_content": "你什麼時候產生了我使用鏡花水月的錯覺"
    },
    {
        "ml_understand_text_result": "{\"document_sentiment\":{\"magnitude\":0.5,\"score\":-0.5},\"language\":\"zh-Hant\",\"sentences\":[{\"sentiment\":{\"magnitude\":0.5,\"score\":-0.5},\"text\":{\"begin_offset\":-1,\"content\":\"為什麼要演奏春日影！\"}}]}",
        "ml_understand_text_status": "",
        "comment": null,
        "text_content": "為什麼要演奏春日影！"
    }
]
```

### 進行語法分析

```sql
SELECT *
FROM ML.UNDERSTAND_TEXT(
    MODEL `ai-project-25-0719.ai_dataset_25_0719_us.my_nlp_model`,
    TABLE `ai-project-25-0719.ai_dataset_25_0719_us.my_nlp_table`,
    STRUCT(
        'analyze_syntax' AS nlu_option
    )
);
```

![圖](https://i.imgur.com/pgul9wB.png)

```json
[
    {
        "ml_understand_text_result": "{\"language\":\"zh\",\"sentences\":[{\"text\":{\"begin_offset\":-1,\"content\":\"珍惜生命，我用Python。\"}}],\"tokens\":[{\"dependency_edge\":{\"head_token_index\":4,\"label\":59},\"lemma\":\"珍惜\",\"part_of_speech\":{\"proper\":2,\"tag\":11},\"text\":{\"begin_offset\":-1,\"content\":\"珍惜\"}},{\"dependency_edge\":{\"label\":18},\"lemma\":\"生命\",\"part_of_speech\":{\"proper\":2,\"tag\":6},\"text\":{\"begin_offset\":-1,\"content\":\"生命\"}},{\"dependency_edge\":{\"head_token_index\":4,\"label\":32},\"lemma\":\"，\",\"part_of_speech\":{\"proper\":2,\"tag\":10},\"text\":{\"begin_offset\":-1,\"content\":\"，\"}},{\"dependency_edge\":{\"head_token_index\":4,\"label\":28},\"lemma\":\"我\",\"part_of_speech\":{\"person\":1,\"proper\":2,\"tag\":8},\"text\":{\"begin_offset\":-1,\"content\":\"我\"}},{\"dependency_edge\":{\"head_token_index\":4,\"label\":54},\"lemma\":\"用\",\"part_of_speech\":{\"proper\":2,\"tag\":11},\"text\":{\"begin_offset\":-1,\"content\":\"用\"}},{\"dependency_edge\":{\"head_token_index\":4,\"label\":18},\"lemma\":\"Python\",\"part_of_speech\":{\"proper\":1,\"tag\":12},\"text\":{\"begin_offset\":-1,\"content\":\"Python\"}},{\"dependency_edge\":{\"head_token_index\":4,\"label\":32},\"lemma\":\"。\",\"part_of_speech\":{\"proper\":2,\"tag\":10},\"text\":{\"begin_offset\":-1,\"content\":\"。\"}}]}",
        "ml_understand_text_status": "",
        "comment": null,
        "text_content": "珍惜生命，我用Python。"
    },
    {
        "ml_understand_text_result": "{\"language\":\"zh-Hant\",\"sentences\":[{\"text\":{\"begin_offset\":-1,\"content\":\"你什麼時候產生了我使用鏡花水月的錯覺\"}}],\"tokens\":[{\"dependency_edge\":{\"head_token_index\":3,\"label\":28},\"lemma\":\"你\",\"part_of_speech\":{\"person\":2,\"proper\":2,\"tag\":8},\"text\":{\"begin_offset\":-1,\"content\":\"你\"}},{\"dependency_edge\":{\"head_token_index\":2,\"label\":16},\"lemma\":\"什麼\",\"part_of_speech\":{\"proper\":2,\"tag\":8},\"text\":{\"begin_offset\":-1,\"content\":\"什麼\"}},{\"dependency_edge\":{\"head_token_index\":3,\"label\":57},\"lemma\":\"時候\",\"part_of_speech\":{\"proper\":2,\"tag\":6},\"text\":{\"begin_offset\":-1,\"content\":\"時候\"}},{\"dependency_edge\":{\"head_token_index\":3,\"label\":54},\"lemma\":\"產生\",\"part_of_speech\":{\"proper\":2,\"tag\":11},\"text\":{\"begin_offset\":-1,\"content\":\"產生\"}},{\"dependency_edge\":{\"head_token_index\":3,\"label\":77},\"lemma\":\"了\",\"part_of_speech\":{\"aspect\":1,\"proper\":2,\"tag\":9},\"text\":{\"begin_offset\":-1,\"content\":\"了\"}},{\"dependency_edge\":{\"head_token_index\":6,\"label\":28},\"lemma\":\"我\",\"part_of_speech\":{\"person\":1,\"proper\":2,\"tag\":8},\"text\":{\"begin_offset\":-1,\"content\":\"我\"}},{\"dependency_edge\":{\"head_token_index\":3,\"label\":11},\"lemma\":\"使用\",\"part_of_speech\":{\"proper\":2,\"tag\":11},\"text\":{\"begin_offset\":-1,\"content\":\"使用\"}},{\"dependency_edge\":{\"head_token_index\":9,\"label\":37},\"lemma\":\"鏡花水月\",\"part_of_speech\":{\"proper\":2,\"tag\":6},\"text\":{\"begin_offset\":-1,\"content\":\"鏡花水月\"}},{\"dependency_edge\":{\"head_token_index\":7,\"label\":46},\"lemma\":\"的\",\"part_of_speech\":{\"case\":5,\"proper\":2,\"tag\":9},\"text\":{\"begin_offset\":-1,\"content\":\"的\"}},{\"dependency_edge\":{\"head_token_index\":6,\"label\":18},\"lemma\":\"錯覺\",\"part_of_speech\":{\"proper\":2,\"tag\":6},\"text\":{\"begin_offset\":-1,\"content\":\"錯覺\"}}]}",
        "ml_understand_text_status": "",
        "comment": null,
        "text_content": "你什麼時候產生了我使用鏡花水月的錯覺"
    },
    {
        "ml_understand_text_result": "{\"language\":\"zh-Hant\",\"sentences\":[{\"text\":{\"begin_offset\":-1,\"content\":\"為什麼要演奏春日影！\"}}],\"tokens\":[{\"dependency_edge\":{\"head_token_index\":3,\"label\":43},\"lemma\":\"為\",\"part_of_speech\":{\"proper\":2,\"tag\":11},\"text\":{\"begin_offset\":-1,\"content\":\"為\"}},{\"dependency_edge\":{\"label\":36},\"lemma\":\"什麼\",\"part_of_speech\":{\"proper\":2,\"tag\":8},\"text\":{\"begin_offset\":-1,\"content\":\"什麼\"}},{\"dependency_edge\":{\"head_token_index\":3,\"label\":8},\"lemma\":\"要\",\"part_of_speech\":{\"proper\":2,\"tag\":11},\"text\":{\"begin_offset\":-1,\"content\":\"要\"}},{\"dependency_edge\":{\"head_token_index\":3,\"label\":54},\"lemma\":\"演奏\",\"part_of_speech\":{\"proper\":2,\"tag\":6},\"text\":{\"begin_offset\":-1,\"content\":\"演奏\"}},{\"dependency_edge\":{\"head_token_index\":5,\"label\":56},\"lemma\":\"春日\",\"part_of_speech\":{\"proper\":2,\"tag\":6},\"text\":{\"begin_offset\":-1,\"content\":\"春日\"}},{\"dependency_edge\":{\"head_token_index\":3,\"label\":18},\"lemma\":\"影\",\"part_of_speech\":{\"proper\":2,\"tag\":13},\"text\":{\"begin_offset\":-1,\"content\":\"影\"}},{\"dependency_edge\":{\"head_token_index\":3,\"label\":32},\"lemma\":\"！\",\"part_of_speech\":{\"proper\":2,\"tag\":10},\"text\":{\"begin_offset\":-1,\"content\":\"！\"}}]}",
        "ml_understand_text_status": "",
        "comment": null,
        "text_content": "為什麼要演奏春日影！"
    }
]
```

## 人口普查分類器

### 檢查數據

```sql
SELECT
    age,
    workclass,
    marital_status,
    education_num,
    occupation,
    hours_per_week,
    income_bracket,
    functional_weight
FROM `bigquery-public-data.ml_datasets.census_adult_income`
LIMIT 100;
```

![圖](https://i.imgur.com/mqAQ4kF.png)

### 準備樣本數據, 建立 VIEW

```sql
CREATE OR REPLACE VIEW
`ai_dataset_25_0719_us.input_data` AS
SELECT
    age,
    workclass,
    marital_status,
    education_num,
    occupation,
    hours_per_week,
    income_bracket,
    CASE
        WHEN MOD(functional_weight, 10) < 8 THEN 'training'
        WHEN MOD(functional_weight, 10) = 8 THEN 'evaluation'
        WHEN MOD(functional_weight, 10) = 9 THEN 'prediction'
    END AS dataframe
FROM `bigquery-public-data.ml_datasets.census_adult_income`;
```

![圖](https://i.imgur.com/S9WORIC.png)

#### 查詢 VIEW

```sql
SELECT * FROM `ai_dataset_25_0719_us.input_data`;
```

![圖](https://i.imgur.com/YQdGuxE.png)

### 建立分類模型

```sql
CREATE OR REPLACE MODEL
`ai_dataset_25_0719_us.census_model`
OPTIONS(
    model_type='LOGISTIC_REG',
    auto_class_weights=TRUE,
    data_split_method='NO_SPLIT',
    input_label_cols=['income_bracket'],
    max_iterations=15
) AS
SELECT * EXCEPT(dataframe)
FROM `ai_dataset_25_0719_us.input_data`
WHERE dataframe = 'training';
```

![圖](https://i.imgur.com/zbyRCBg.png)
