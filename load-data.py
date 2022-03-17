# Databricks notebook source
url = "https://raw.githubusercontent.com/froliol/Databricks-DW-Demo/main/data/sales_reps.csv?token=GHSAT0AAAAAABSTU7MQYJ5THYZKTCLTIVNOYRTRMDQ"
from pyspark import SparkFiles
spark.sparkContext.addFile(url)

# COMMAND ----------

# MAGIC %sh
# MAGIC ls data

# COMMAND ----------

# MAGIC %sh
# MAGIC wget -P /tmp https://github.com/froliol/Databricks-DW-Demo/blob/main/data/sales_reps.csv.gz

# COMMAND ----------

# MAGIC %fs ls /tmp

# COMMAND ----------

# MAGIC %fs ls file:/tmp

# COMMAND ----------

#%fs cp file:/tmp/sales_rep.csv.gz dbfs:/tmp/sales_rep.csv.gz
dbutils.fs.ls("file:/tmp/sales_reps.csv.gz")

# COMMAND ----------

df = spark.read.csv("file:/tmp/sales_rep.csv.gz")

# COMMAND ----------

#dbutils.fs.mv("file:/tmp/sales_rep.csv.gz","dbfs:/tmp/sales_rep.csv.gz")
dbutils.fs.mv("dbfs:/tmp/sales_rep.csv.gz", "file:/tmp/sales_rep.csv.gz")

# COMMAND ----------

# MAGIC %fs ls file:/tmp/

# COMMAND ----------

# MAGIC %fs cp file:/tmp/sales_reps.csv.gz /tmp/sales_reps.csv.gz

# COMMAND ----------

dbutils.fs.ls("/tmp")

# COMMAND ----------


