# Databricks notebook source
# MAGIC %sh
# MAGIC wget -P /tmp https://github.com/froliol/Databricks-DW-Demo/blob/main/data/products.csv.bz2

# COMMAND ----------

# MAGIC %sh
# MAGIC bzip2 -dkf /tmp/products.csv.bz2

# COMMAND ----------

# MAGIC %fs cp file:/tmp/products.csv /tmp/products.csv

# COMMAND ----------

# MAGIC %fs ls file:/tmp/

# COMMAND ----------

# MAGIC %fs ls /tmp/

# COMMAND ----------

# df = spark.read.load("dbfs:/tmp/products.csv.bz2", format="csv")
df = spark.read.option("sep", ",").csv("/tmp/products.csv")

# COMMAND ----------

df.show()
