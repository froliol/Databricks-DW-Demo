# Databricks notebook source
import urllib 

urllib.request.urlretrieve("https://github.com/froliol/Databricks-DW-Demo/raw/main/data/sales_reps.zip", "/tmp/sales_reps.csv.zip")

# COMMAND ----------

# MAGIC %sh
# MAGIC wget("https://github.com/froliol/Databricks-DW-Demo/blob/main/data/sales_reps.zip")

# COMMAND ----------



# COMMAND ----------

import pandas as pd
df = pd.read_csv("./data/products.csv.zip")
df
