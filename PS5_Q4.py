# QUESTION 4
from sqlalchemy import create_engine, MetaData, Table, select
import pandas as pd
import matplotlib.pyplot as plt

# 데이터베이스 연결 설정
db_path = "/blue/bsc4452/seoyeon0814/problem_set5/world.sqlite"  # 경로 수정
engine = create_engine(f'sqlite:///{db_path}')
connection = engine.connect()
metadata = MetaData()

# 테이블 로드
country = Table('country', metadata, autoload_with=engine)

# SQLAlchemy 쿼리 작성: LifeExpectancy와 Population 추출
query = select([country.c.LifeExpectancy, country.c.Population]).where(country.c.LifeExpectancy != None)

# 데이터 가져오기
result = connection.execute(query).fetchall()

# Pandas DataFrame 생성
df = pd.DataFrame(result, columns=["LifeExpectancy", "Population"])

# 연결 닫기
connection.close()

# 데이터 필터링: Population과 LifeExpectancy가 유효한 값만 사용
df = df.dropna()

# Matplotlib로 시각화
plt.figure(figsize=(10, 6))
plt.scatter(df['Population'], df['LifeExpectancy'], alpha=0.7, edgecolor='k')
plt.title("Life Expectancy vs Population", fontsize=16)
plt.xlabel("Population", fontsize=14)
plt.ylabel("Life Expectancy", fontsize=14)
plt.grid(True)
plt.show()