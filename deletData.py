from mysql.connector import Error
from connect import connect

def delete_customer(id):
    """고객 데이터를 삭제하는 함수"""
    query = "DELETE FROM users WHERE id = %s"
    data = (id)
    
    try:
        conn = connect()  # 데이터베이스에 연결
        if conn is None:
            print("데이터베이스 연결에 실패했습니다.")
            return
        
        cursor = conn.cursor()
        
        # 데이터 삭제
        cursor.execute(query, data)
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"{cursor.rowcount}개의 행이 삭제되었습니다.")
        else:
            print("삭제할 데이터가 없습니다.")
    
    except Error as error:
        print(f"데이터 삭제 중 오류가 발생했습니다: {error}")
    
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            print("데이터베이스 연결이 종료되었습니다.")
