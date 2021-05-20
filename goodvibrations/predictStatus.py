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

PACKAGE_URL = f"https://github.com/philippe-gregoire/mas82_iotfuncs_icare_vibration@mas82_starter"

import autoai_libs

class PredictStatus_ICare(BaseTransformer):

    def __init__(self, input_items, predStatus, output_items):
        self.input_items = input_items
        self.output_items = output_items
        self.predStatus = str(predStatus)

        import pickle
        import io
        import os
        import goodvibrations

        FILE='VE-1138_All'
        pn='P3'
        #target='Status'

        self.pipes={}
        for p in ('preproc','feateng','predict'):
            with io.open(f"{os.path.join(os.path.dirname(goodvibrations.__file__),FILE)}_P{pn}_{p}.pickle",'rb') as f:
                self.pipes[p]=pickle.loads(f.read())
        print("Loaded models")

        super().__init__()

    def execute(self, df):
        print("Enter Execute")
        #df = df.copy()
        print(f"Apply factor to {len(self.input_items)}")

        preV=self.pipes['preproc'].transform(df.values)
        feV=self.pipes['feateng'].transform(preV)
        predV=self.pipes['predict'].predict(feV)
        print(f"predicted values={predV}")
        for i,input_item in enumerate(self.output_items):
            df[self.output_items[i]] = predV
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
                datatype=str)
                      )
        outputs = []
        return (inputs,outputs)
