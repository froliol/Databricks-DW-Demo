# Databricks notebook source
df = spark.read.option("header", True).option("inferSchema", True).csv("file:/Workspace/Repos/louis.frolio@databricks.com/Databricks-DW-Demo/data/products.csv")

# COMMAND ----------

url = 'https://raw.githubusercontent.com/froliol/Databricks-DW-Demo/2dafd082a3c1d250d9336d9aa7c5da98a92355bc/data/products.csv'
from pyspark import SparkFiles
spark.sparkContext.addFile(url)
df = spark.read.csv(SparkFiles.get("products.csv"), header=True)

# COMMAND ----------

url = "https://github.com/froliol/Databricks-DW-Demo/blob/2dafd082a3c1d250d9336d9aa7c5da98a92355bc/data/?format=csv"
     
from pyspark import SparkFiles
sc.addFile(url)
     
path  = SparkFiles.get('download')
df = spark.read.csv("file://" + path, header=True, inferSchema= True, sep = ";")

# COMMAND ----------

data/products.csv
https://github.com/froliol/Databricks-DW-Demo/blob/2dafd082a3c1d250d9336d9aa7c5da98a92355bc/data/products.csv
https://raw.githubusercontent.com/froliol/Databricks-DW-Demo/2dafd082a3c1d250d9336d9aa7c5da98a92355bc/data/products.csv?token=GHSAT0AAAAAABSTU7MQI5ZXSKUJ23GQ2ZMWYRTPK5A

# COMMAND ----------

url = 'https://raw.githubusercontent.com/jokecamp/FootballData/master/openFootballData/cities.csv'
from pyspark import SparkFiles
spark.sparkContext.addFile(url)
df = spark.read.csv(SparkFiles.get("cities.csv"), header=True)

# COMMAND ----------

import pandas as pd
df = pd.read_csv("./data/products.csv")
df
