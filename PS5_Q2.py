# QUESTION 2
import sqlite3

# Database Connection (데이터베이스 연결)
db_path = "/blue/bsc4452/seoyeon0814/problem_set5/world.sqlite"
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Check if South Sudan already exists (South Sudan이 이미 존재하는지 확인)
cursor.execute("SELECT * FROM country WHERE Code = 'SSD';")
if cursor.fetchone():
    print("Country with Code 'SSD' already exists.")
else:
    # Execute SQL (SQL 실행)
    sql_insert = """
    INSERT INTO country (Code, Name, Continent, Region, SurfaceArea, Population, LifeExpectancy, IndepYear)
    VALUES ('SSD', 'South Sudan', 'Africa', 'Eastern Africa', 619745, 11062113, 57.3, 2011);
    """
    cursor.execute(sql_insert)

    # Save Changes (변경 사항 저장)
    connection.commit()

    # Confirmation Message (확인 메시지)
    print("South Sudan has been added to the country table.")

# Close Connection (연결 닫기)
connection.close()
