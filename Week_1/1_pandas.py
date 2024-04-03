import pandas as pd

cites = {"ahvaz":32,
         "tehran":18,
         "shiraz":22,
         "kerman":30}

temp = [32, 18, 22, 30]



print("\nSeries Cites:")
ds1 = pd.Series(cites)
print(ds1)

print("\nSeries temp:")
ds = pd.Series(temp, index=["ahvaz", "tehran", "shiraz", "kerman"])
print(ds)

print(ds.keys)
print(ds.values)


# print(cites.ahvaz) # => Wrongggggggggg
print(ds1.ahvaz)

print(ds.ahvaz)
print(ds[0])

print(ds[["ahvaz", "shiraz"]])
print(ds[:2])
print(ds[[0, 2]])

print(ds[[True, False, True, False]])

m = ds.mean()
print(m)
print(ds > m)

