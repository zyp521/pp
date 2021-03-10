import pandas as pd

index = pd.date_range('2020/3/8', periods=9, freq='T')
out = pd.DataFrame(range(9), index=index)

print(out)
print(out.resample('3T').sum())

