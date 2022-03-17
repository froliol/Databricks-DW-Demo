# Databricks notebook source
# MAGIC %sh
# MAGIC wget -P /tmp https://github.com/froliol/Databricks-DW-Demo/blob/main/data/products.csv.zip

# COMMAND ----------

# MAGIC %fs ls file:/tmp

# COMMAND ----------

# MAGIC %fs cp file:/tmp/sales_reps.csv.gz /tmp/sales_reps.csv.gz

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


