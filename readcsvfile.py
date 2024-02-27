import pandas as pd

df = pd.read_csv('netflix_titles.csv')

# print(df.head())

# 나라가 한국인 행 찾기.
한국 = df[df['country']=='South Korea']

# print(한국)

# 'duration' 열에서 'min' 값을 추출하여 새로운 'duration_min' 열을 만듭니다.
df['duration_min'] = df['duration'].str.extract('(\d+)', expand=False).astype(float)

# 'duration_min' 열을 기준으로 최댓값을 가지는 행을 찾습니다.
max_duration_row = df[df['duration_min'] == df['duration_min'].max()]

# 결과를 출력합니다.
print("가장 긴 min 값의 행:")
print(max_duration_row)