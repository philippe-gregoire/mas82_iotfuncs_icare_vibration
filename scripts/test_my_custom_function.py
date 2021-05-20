# *****************************************************************************
# © Copyright IBM Corp. 2021.  All Rights Reserved.
#
# This program and the accompanying materials
# are made available under the terms of the Apache V2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
#
# *****************************************************************************
# Vibration condition prediction IoTFunction for MAS Monitor testere
#
# Author: Philippe Gregoire - IBM in France
# *****************************************************************************

from iotfunctions.db import Database
import os,sys,io,json

def main(argv):
  sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__),'..')))

  credPath=os.path.join(os.path.dirname(__file__),f"credentials_as_{os.environ['USERNAME']}.json")
  print(f"Loading credentials from {credPath}")
  with io.open(credPath, encoding='utf-8') as F:
    credentials = json.loads(F.read())
  db_schema = None
  db = Database(credentials=credentials)

  from goodvibrations.predictStatus import PredictCondition
  print(f"Registering function")
  db.unregister_functions(["PredictCondition"])
  try:
    db.register_functions([PredictCondition])
  except Exception as exc:
    print(exc)

  fn = PredictCondition(condition='predStatus')
  df = fn.execute_local_test(db=db, db_schema=db_schema, generate_days=1,to_csv=True)
  print(df)

if __name__ == "__main__":
    import logging
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    main(sys.argv)
