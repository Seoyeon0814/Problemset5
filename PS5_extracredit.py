# Grad student extra credit
from sqlalchemy import create_engine, MetaData, Table, select, func, and_
import pandas as pd
import matplotlib.pyplot as plt

# Configure Database Connection (데이터베이스 연결 설정)
db_path = "/blue/bsc4452/seoyeon0814/problem_set5/world.sqlite"  # 경로 수정
engine = create_engine(f'sqlite:///{db_path}')
connection = engine.connect()
metadata = MetaData()

# Load Table (테이블 로드)
country = Table('country', metadata, autoload_with=engine)
city = Table('city', metadata, autoload_with=engine)

# Write an SQLAlchemy query to extract the total population of cities and country data (SQLAlchemy 쿼리 작성: 도시 인구 합계와 국가 데이터 추출)
query = (
    select([
        country.c.Name,
        country.c.LifeExpectancy,
        country.c.Population,
        func.sum(city.c.Population).label('CityPopulation')
    ])
    .select_from(country.join(city, country.c.Code == city.c.CountryCode))
    .group_by(country.c.Code)
    .having(and_(country.c.Population != None, country.c.LifeExpectancy != None))
)

# Retrieve Data (데이터 가져오기)
result = connection.execute(query).fetchall()

# Create a Pandas DataFrame (Pandas DataFrame 생성)
df = pd.DataFrame(result, columns=["CountryName", "LifeExpectancy", "CountryPopulation", "CityPopulation"])

# Calculate the city population ratio (CityPopulation / CountryPopulation) (도시 인구 비율 계산 (CityPopulation / CountryPopulation))
df['UrbanRatio'] = df['CityPopulation'] / df['CountryPopulation']

# Close Connection (연결 닫기)
connection.close()

# Data Visualization (데이터 시각화)
plt.figure(figsize=(10, 6))
plt.scatter(df['UrbanRatio'], df['LifeExpectancy'], alpha=0.7, edgecolor='k')
plt.title("Life Expectancy vs Urban Population Ratio", fontsize=16)
plt.xlabel("Urban Population Ratio (CityPopulation / CountryPopulation)", fontsize=14)
plt.ylabel("Life Expectancy", fontsize=14)
plt.grid(True)
plt.show()
