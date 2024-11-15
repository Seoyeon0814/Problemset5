# QUESTION 1
import sqlite3

# 데이터베이스 경로 설정
db_path = "/blue/bsc4452/seoyeon0814/problem_set5/world.sqlite"  

# SQLite 데이터베이스 연결
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# SQL 쿼리 작성: 독립 연도가 가장 최근인 국가 찾기
sql_query = """
SELECT Name, IndepYear
FROM country
WHERE IndepYear IS NOT NULL
ORDER BY IndepYear DESC
LIMIT 1;
"""

# SQL 실행
cursor.execute(sql_query)
result = cursor.fetchone()

# 결과 출력
if result:
    print(f"The country with the most recent independence is {result[0]}, in {result[1]}.")
else:
    print("No country found with independence year.")

# 연결 닫기
connection.close()