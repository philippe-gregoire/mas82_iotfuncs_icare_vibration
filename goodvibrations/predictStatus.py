# *****************************************************************************
# © Copyright IBM Corp. 2021.  All Rights Reserved.
#
# This program and the accompanying materials
# are made available under the terms of the Apache V2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
#
# *****************************************************************************
# Vibration condition prediction IoTFunction for MAS Monitor
#
# Uses a pipeline that has been generated using AutoAI and pickled
#
# This function applies the unpickled pipeline to incoming dataframe
#
# Author: Philippe Gregoire - IBM in France
# *****************************************************************************

import logging

from iotfunctions.base import BaseTransformer
from iotfunctions import ui

logger = logging.getLogger(__name__)

# Specify the URL to your package here.
# This URL must be accessible via pip install.

PACKAGE_URL = f"git+https://github.com/philippe-gregoire/mas82_iotfuncs_icare_vibration@mas82_starter"

class PredictCondition(BaseTransformer):
    ''' Predict an equipment condition by applying an AutoAI-generated model

        Here we will apply the packaged VibConditionPrediction_P3 pickled model
        to the 'deviceid', 'Order1_fftV', 'Order1_fftG', 'Order2_fftV', 'Order2_fftG', 'Order3_fftV', 'Order3_fftG'
        columns from the I-Care sensor

    '''
    def __init__(self, condition):
        super().__init__()
        self.condition = condition
        self.columns=['deviceid', 'Order1_fftV', 'Order1_fftG', 'Order2_fftV', 'Order2_fftG', 'Order3_fftV', 'Order3_fftG']

        logger.info(f"Init of function for condition ={self.condition} and columns={self.columns}")

        import os,io,pickle
        import goodvibrations
        #import autoai_libs

        import sklearn
        logger.info(f"Using sklearn version {sklearn.__version__}")

        pipeline_file='VibConditionPrediction_P3.pickle'
        logger.info(f"Loading pipeline from file {pipeline_file}")

        with io.open(os.path.join(os.path.dirname(goodvibrations.__file__),pipeline_file),'rb') as f:
            self.pipeline=pickle.loads(f.read())
        logger.info(f"Loaded pipeline from {pipeline_file}")
        logger.info(self.pipeline)

    def execute(self, df):
        logger.info(f"Enter Execute with {len(df)} rows")
        logger.info(df.describe(include='all'))

        # Filter out rows where we have NaNs
        import math
        df=df[df[self.columns[1:]].apply(lambda row: all([not math.isnan(c) for c in row]),axis=1)].copy()
        logger.info(f"Retaining {len(df)} non-NaN rows to predict on")

        df[self.condition]=self.pipeline.predict(df.reset_index()[self.columns].to_numpy())

        logger.info(f"predicted values statistics:")
        logger.info(df[self.condition].value_counts())

        return df

    @classmethod
    def build_ui(cls):
        # We don't need specific input, and output the predicted condition
        return ([],[ui.UIFunctionOutSingle(name='condition', datatype=str, description='Predicted condition')])
