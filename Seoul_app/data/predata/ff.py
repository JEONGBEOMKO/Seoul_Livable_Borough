from json import encoder
import pandas as pd
import json
data = pd.read_csv("초등학교.csv")
a = json.dumps(data)
