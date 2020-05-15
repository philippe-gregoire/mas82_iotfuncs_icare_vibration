import datetime as dt
import json
import pandas as pd
import numpy as np
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, func
from iotfunctions.base import BaseTransformer
from iotfunctions.metadata import EntityType
from iotfunctions.db import Database
from iotfunctions import ui

with open('credentials_as.json', encoding='utf-8') as F:
  credentials = json.loads(F.read())
db_schema = None
db = Database(credentials=credentials)

from goodvibrations.predictStatus import PredictStatus_ICare
fn = PredictStatus_ICare(
    input_items = ['speed', 'speed_recalculated', 'peak-to-peak', 'peak_plus',
       'peak_minus', 'order1', 'crest_factor', 'HF', 'globalG', 'globalV',
       'global_sousSynch', 'non_synchroneG', 'synchroneG', 'non_synchroneV',
       'synchroneV'],
    predStatus = 'Green',
    output_items = ['predStaus']
              )
df = fn.execute_local_test(db=db, db_schema=db_schema, generate_days=1,to_csv=True)
print(df)
