# QUESTION 3
import sqlite3

# 데이터베이스 경로 설정
db_path = "/blue/bsc4452/seoyeon0814/problem_set5/world.sqlite"  # 경로 수정
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# South Sudan의 두 도시 데이터 추가
try:
    # 기존 데이터 확인
    cursor.execute("SELECT * FROM city WHERE CountryCode = 'SSD';")
    existing_cities = cursor.fetchall()

    if len(existing_cities) > 0:
        print("South Sudan cities already exist in the table:")
        for city in existing_cities:
            print(city)
    else:
        # SQL INSERT 실행
        sql_insert = """
        INSERT INTO city (Name, CountryCode, Population)
        VALUES 
            ('Juba', 'SSD', 525953),
            ('Malakal', 'SSD', 147450);
        """
        cursor.execute(sql_insert)

        # 변경 사항 저장
        connection.commit()
        print("Cities Juba and Malakal have been added to the city table.")

except sqlite3.Error as e:
    print(f"Database error: {e}")

finally:
    # 연결 닫기
    if connection:
        connection.close()