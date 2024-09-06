from _mysql_connector import Error
from connect import connect

#이름 책이름 id

def insert_data(name, bookname, id):
    query = "INSERT INTO users (name, bookname, id) VALUES (%s, %s, %s)" 
    data = (name, bookname, id)

    try:
        # connect 함수로 데이터베이스에 연결
        conn = connect()  # 이때 config 파일을 이용한 연결이 이미 설정된 상태
        cursor = conn.cursor()
        
        # 데이터 삽입
        cursor.execute(query, data)
        conn.commit()
        
        print(f"{cursor.rowcount}개의 행이 삽입되었습니다.")
    except Error as error:
        print("error")
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
