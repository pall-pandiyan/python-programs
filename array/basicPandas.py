# pandas is another framework used to manupulate array
# here i import pandas using element 'pd'
# 
# in pandas 'Series()' is used to initialise the single dimention array
# and 'DataFrame()' for multi dimention array
# unlike numpy which list contains another list as element,
# pandas follows index for rows and heaader for column identification

import pandas as pd

s1=pd.Series([10,20,30,40])
print(s1)
print(type(s1))

s2=pd.DataFrame({"Name":["Apple","Orenges","Banana"],"Value":[150,210,55]})
print(s2)
print(type(s2))

# 0    10
# 1    20
# 2    30
# 3    40
# dtype: int64
# <class 'pandas.core.series.Series'>
#       Name  Value
# 0    Apple    150
# 1  Orenges    210
# 2   Banana     55
# <class 'pandas.core.frame.DataFrame'>