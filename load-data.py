# Databricks notebook source
df = spark.read.option("header", True).option("inferSchema", True).csv("file:/Workspace/Repos/louis.frolio@databricks.com/Databricks-DW-Demo/data/products.csv")

# COMMAND ----------

/Workspace/Repos/louis.frolio@databricks.com/Databricks-DW-Demo/data/products.csv
