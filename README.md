# flask-setup-practice
Controller - Service - Model기반 flask 프로젝트 연습

### CLI
- `makefile`을 통해 시스템 패키지 설치.
- `manage.py`를 이용해서 쉽게 `flask` 스크립트 관리.


1. 파이썬 환경 설치(파이썬이 있으면 스킵)
```sh
# 우분투 스크립트 기준, 다른 OS 사용 시 makefile의 [system-packages] 수정
> make install
> make tests
```
2. DB 마이그레이션 초기 설정
```sh
# 마이그래이션 스크립트 실행
> python manage.py db init
> python manage.py db migrate --message 'initial db migration'
> python manage.py db upgrade
```
3. 앱 실행
```sh
# 쉬운 실행
> ./00_Run_dev_app_server.sh
# 혹은 밑의 라인 실행
> export FLASK_ENV=development
> python manage.py run
```

### Swagger UI
- 서버 실행 후  `http://127.0.0.1:5000/` 로 API 실행 확인


### 라이브러리
- `Flask-Bcrypt`: 패스워드 해싱
- `Flask-Migrate`: `Alembic` 기반 db 마이그래이션 도구, 버전관리 제공(굿..!)
- `Flask-SQLAlchemy`: Python 기반 ORM `SQLAlchemy`의 `Flask` 버전
- `PyJWT`: JWT 인코딩 / 디코딩 기능 제공 - HS256(HMAC SHA-256) 기반
- `Flask-Script`: `Flask` 명령어 도구
- `Flask-Testing`: `Flask` 기반 테스트 도구, SQLAlchemy랑 통합 테스트할 때 편하다.
- `flask-restx`: `Flask`를 이용해 REST API를 만들 때 도와주는 라이브러리, Blueprints를 통해 애플리케이션 제작이 매우 편해지고 api를 `swagger ui`로 보여주기에 문서화 할 때 굉장한 생산성을 얻는다.

