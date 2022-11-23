import pandas as pd
import PandasConvertList as PCL

df = pd.read_excel('DATA_BASE.xlsx')

read = PCL.change_in_list(df)

print(read)