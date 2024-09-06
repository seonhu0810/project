from mysql.connector import Error
from connect import connect

def update_customer(name, bookname, id):

    #고객 데이터를 업데이트하는 함수
    query = "UPDATE users SET name = %s, bookname = %s, id = %s"
    data = (name, bookname, id,)
    
    try:
        conn = connect()  # 데이터베이스에 연결
        if conn is None:
            print("데이터베이스 연결에 실패했습니다.")
            return
        
        cursor = conn.cursor()
        
        # 데이터 업데이트
        cursor.execute(query, data)
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"{cursor.rowcount}개의 행이 업데이트되었습니다.")
        else:
            print("업데이트할 데이터가 없습니다.")
    
    except Error as error:
        print(f"데이터 업데이트 중 오류가 발생했습니다: {error}")
    
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            print("데이터베이스 연결이 종료되었습니다.")


