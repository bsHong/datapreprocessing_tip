import pandas as pd

df = pd.read_csv("data.csv")

# df["date"] -> int64 
# 20170101

df["date"] = df["data"].astype("str")

# date type 변경
df["date"] = pd.to_datetime(df["date"])

# date type 변경2
## 이게 성능이 더 좋음
df['locdate']=df['date'].apply(lambda _ : datetime.strptime(_,'%Y%m%d'))

