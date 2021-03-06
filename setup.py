#!/usr/bin/env python
# *****************************************************************************
# © Copyright IBM Corp. 2021.  All Rights Reserved.
#
# This program and the accompanying materials
# are made available under the terms of the Apache V2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
#
# *****************************************************************************
# Vibration condition prediction IoTFunction packager
#
# Author: Philippe Gregoire - IBM in France
# *****************************************************************************

from setuptools import setup, find_packages

setup(
    name='goodvibrations',
    version='0.1.0',
    packages=find_packages(),
    package_data={
        'goodvibrations': ['VibConditionPrediction_P3_skl_v0.20.3.pickle'],
    },
    install_requires=[
        #'dill==0.3.0',
        #'ibm-cos-sdk==2.1.3',
        #'numpy==1.17.3',
        #'pandas>=0.24.0',
        'scikit-learn==0.20.3',
        #'scipy>=1.1.0',
        #'requests==2.18.4',
        #'urllib3==1.22',
        #'ibm_db==3.0.1',
        #'ibm_db_sa==0.3.3',
        #'lxml==4.3.4',
        #'nose>=1.3.7',
        #'psycopg2-binary==2.8.4',
        #'pyod==0.7.5',
        #'scikit-image==0.16.2',
        #'sqlalchemy==1.3.10',
        #'tabulate==0.8.5',
        'autoai_libs==1.12.6'
    ],
    #extras_require = {
    #    'kafka':  ['confluent-kafka==0.11.5']
    #}
)
