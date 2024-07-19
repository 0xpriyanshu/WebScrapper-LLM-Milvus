
# WebScrapper-LLM-Milvus

This crawls upto 5 depths &amp; organizes website knowledge for LLM question answering.



## Objective

This assess the ability to perform extensive web crawling up to a depth of 5 levels (parent link -> sub-link -> sub-link -> sub-link -> sub-link), create a vector database using MILVUS, and develop a question-answering system using an LLM (Language Model).




### STEP1: WEB CRAWLING
This Python script utilizes Scrapy to crawl and extract data from the Nvidia CUDA documentation website.

LINK: https://github.com/0xpriyanshu/WebScrapper-LLM-Milvus/blob/main/nvidia_docs_spider.py

#### Installation
Python (version 3.6 or later recommended)
,Install libraries:

```bash
  pip install scrapy
```
#### Usage


    
1.Save script as`nvidia_docs_crawler.py`.

2.Run

```bash
  scrapy crawl nvidia_docs -o output.json
```
This crawls the website up to 5 levels, extracting page titles and content.

#### Output

The script extracts URL, title, and content and gets stored in json format in file named `output.json`.

### STEP 2,3 & 4: DATA CHUNKING AND VECTOR DATABASE CREATION , RETRIEVAL AND RE-RANKING & QUESTION ANSWERING
This code implements a document retrieval and question answering system using Sentence Transformers and Milvus.

LINK: https://github.com/0xpriyanshu/WebScrapper-LLM-Milvus/blob/main/model.ipynb

#### 1. Environment Setup

Before running the code, ensure you have the following libraries installed:

pandas
sentence-transformers
sklearn
pymilvus
milvus
transformers
You can install them using pip:

```bash
  pip install pandas sentence-transformers sklearn pymilvus transformers
```
#### 2. Data Chunking and Vector Database Creation (Cells 3, 9)
#### 2.1. Data Chunking (Cell 3)
- This step involves splitting the document content into smaller chunks based on semantic similarity.

- The `advanced_chunk_text` function (Cell 3) utilizes Sentence Transformers to encode sentences and perform hierarchical clustering to create chunks.

#### 2.2. Vector Database Creation (Cell 9)
- Milvus is used to create a vector database for storing document embeddings.

- The code defines a collection schema with fields for document ID, embedding, and URL (Cell 8).

- Sentence Transformers are used to generate embeddings for each content chunk (Cell 9).

- Embeddings and corresponding URLs are inserted into the Milvus collection (Cell 9).

#### 3. Retrieval and Re-ranking (Cells 12)

#### 3.1. Retrieval (Cell 12)

- This step retrieves relevant documents from the database based on a user query.

- A BM25 ranking is initially applied using `rank_bm25` (Cell 12).

- Milvus is then used to search for documents with embeddings similar to the query embedding using an HNSW index (Cell 12).

#### 3.2. Re-ranking (Cell 12)
- The retrieved documents from both BM25 and Milvus are merged and re-ranked based on their similarity to the query using Sentence Transformers (Cell 12).

#### 4. Question Answering (Cells 12, 13)

#### 4.1. Context Selection (Cell 12)
- The top K re-ranked documents are used as context for question answering.

#### 4.2. Answering (Cell 13)
- A pre-trained question answering pipeline (`distilbert-base-cased-distilled-squad`) is used to answer questions based on the retrieved contexts (Cell 13).

#### 5. Usage
The code provides a `retrieve_and_answer_questions` function (Cell 13) that takes a query as input and returns a list of answer passages from the retrieved documents.

#### EXAMPLE 

```bash
query = "how to install cuda?"
answers = retrieve_and_answer_questions(query)
print("Answers to '{}' based on retrieved documents:".format(query))
for i, answer in enumerate(answers):
  print("{}. {}".format(i+1, answer))
```

This code demonstrates a basic workflow for building a document retrieval and question answering. For any query reach out to priyanshukumarweb3@gmail.com.


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://0xpriyanshu.github.io/0xpriyanshu/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/priyanshukrs)


