### commit


이름초성_작업내용_순서


### 브랜치


이름초성


### 호칭
OO님


### 기능

#### 박선후


config.py 
- MySQL 연결을 위한 설정파일 


connect.py
- MySQL DB 연결하는 기능


fetchall.py
- DB에서 모든 데이터를 읽어오는 기능




#### 장민준


insertData.py
- 데이터를 추가하는 기능
- url에 다음과 같은 형식으로 입력
    - '/insert/<title>/<isbn>' 


updateData.py
- 데이터를 업데이트하는 기능
- url에 다음과 같은 형식으로 입력
    - '/update/<int:id>/<title>'


deleteData.py 
- 데이터를 삭제하는 기능
- url에 다음과 같은 형식으로 입력
    - '/delete/<int:id>'



#### 임현욱


app.py


templates/list.html     //html 파일        

