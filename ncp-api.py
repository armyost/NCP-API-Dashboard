from flask		import Flask
from sqlalchemy	import create_engine

from model		import apiDao
from service	import apiService
from view    	import create_endpoints

class Services:
    pass

def create_app(dev_config = None):
	app = Flask(__name__)
	
	if dev_config is None:
		print("Config Called from config.py")
		app.config.from_pyfile("config.py")
	else:
		print("Config Called from dev_config")
		app.config.update(dev_config)

	## 환경설정 적용
	database = create_engine(app.config['DB_URL'], encoding = 'utf-8', max_overflow = 0)
	access_key = app.config['ACCESS_KEY']
	secret_key = app.config['SECRET_KEY']

    ## Persistenace Layer
	api_dao  = apiDao(database)

    ## Business Layer
	services = Services
	services.api_service = apiService(api_dao, access_key, secret_key)

	## Endpoint 생성
	create_endpoints(app, services)
	return app	


if __name__=="__main__":
	## Flask App 실행
	app=create_app()
	app.run(host="0.0.0.0", port="8080")



	

