# Databricks notebook source
# MAGIC %sh
# MAGIC wget -P /tmp https://github.com/froliol/Databricks-DW-Demo/blob/main/data/products.csv.bz2

# COMMAND ----------

# MAGIC %fs cp file:/tmp/products.csv.bz2 /tmp/products.csv.bz2

# COMMAND ----------

# MAGIC %fs ls file:/tmp/

# COMMAND ----------

# MAGIC %fs ls /tmp/
