import pandas as pd

cites = {"ahvaz":32,
         "tehran":18,
         "shiraz":22,
         "kerman":30}

temp = [32, 18, 22, 30]

print("\nSeries Cites:")
ds = pd.Series(cites)
print(ds)

print("\nSeries temp:")
ds = pd.Series(temp, index=["ahvaz", "tehran", "shiraz", "kerman"])
print(ds)