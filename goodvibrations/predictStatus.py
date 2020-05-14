import inspect
import logging
import datetime as dt
import math
from sqlalchemy.sql.sqltypes import TIMESTAMP,VARCHAR
import numpy as np
import pandas as pd

from iotfunctions.base import BaseTransformer
from iotfunctions import ui

logger = logging.getLogger(__name__)

# Specify the URL to your package here.
# This URL must be accessible via pip install.
# Example assumes the repository is private.
# Replace XXXXXX with your personal access token.

token= '2c25e35482cff0323dc9c5b0051b7413918b9fdd'
PACKAGE_URL = f"https://{token}@github.com/philippe-gregoire/iotfgoodvibs@starter_package"

class PredictStatus_ICare(BaseTransformer):

    def __init__(self, input_items, predStatus, output_items):
        self.input_items = input_items
        self.output_items = output_items
        self.predStatus = f"{predStatus}"
        super().__init__()

    def execute(self, df):
        print("Enter Execute")
        df = df.copy()
        print("Apply factor")
        for i,input_item in enumerate(self.input_items):
            df[self.output_items[i]] = self.predStatus
        return df

    @classmethod
    def build_ui(cls):
        #define arguments that behave as function inputs
        inputs = []
        inputs.append(ui.UIMultiItem(
                name = 'input_items',
                datatype=float,
                description = "Data items adjust",
                output_item = 'output_items',
                is_output_datatype_derived = True)
                      )
        inputs.append(ui.UISingle(
                name = 'predStatus',
                datatype=string)
                      )
        outputs = []
        return (inputs,outputs)
