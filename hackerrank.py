a = """
a,b,c
hello,,world
,why,
"""

import pandas as pd
import numpy as np

data = []
row = []
string_build = []
for idx, i in enumerate(a):
    if (idx == 0) and (i == '\n'):
        continue # skip new line at the beginning
    elif (idx == 0) and (i != '\n'): # some string we need to parse
        pass
    else:
        pass

    if (i != ',') and (i != '\n'): 
        string_build.append(i)

    elif ((i == ',') or (i == '\n')) and (string_build != []):
        row.append("".join(string_build))
        string_build = []
    
    elif ((i == ',') or (i == '\n')) and (string_build == []):
        row.append(np.nan)
        # string_build = []
    else:
        pass

    if i == '\n':
        print(row)
        data.append(row)
        row = []
    else:
        pass
    
print(data)
df = pd.DataFrame(data)
print(df)