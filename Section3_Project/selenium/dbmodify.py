import pandas as pd
import numpy as np

df = pd.read_csv("/Users/hamhwijin/Section3_Project/selenium/review_data.csv", names=["name", "tags", "price", "like", "score"])

# tags 컬럼 # 제거
df["tags"] = df['tags'].str.replace("#", "")

# 음료 가격 -> , 제거 후 int로 타입 변환
df["price"] = df["price"].str.replace(",", "").astype(int)

# like 컬럼 결측치 "없음"으로 대체
df["like"] = df["like"].fillna("없음")

# 내가 남긴 후기 점수라고 가정
np.random.seed(42)
df["score"] = np.random.randint(1, 5+1, 40)

#print(df)
print(df["like"].unique())
#df.to_csv('review_modify.csv', index=False)