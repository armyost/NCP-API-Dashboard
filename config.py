## Prod Config 입력

db = {			
    'user'     : 'root',
    'password' : 'root',
    'host'     : 'localhost',
    'port'     : 3306,
    'database' : 'test_db'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
ACCESS_KEY = '엑세스키 입력'
SECRET_KEY = '시크릿키 입력'


## Dev Config 입력

test_db = {			
    'user'     : 'root',
    'password' : 'root',
    'host'     : 'localhost',
    'port'     : 3306,
    'database' : 'test_db',
}

dev_config = {		
    'DB_URL' : f"mysql+mysqlconnector://{test_db['user']}:{test_db['password']}@{test_db['host']}:{test_db['port']}/{test_db['database']}?charset=utf8",
    'ACCESS_KEY' : '엑세스키 입력',
    'SECRET_KEY' : '시크릿키 입력'
}