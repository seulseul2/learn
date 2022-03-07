__static files__

INSTALLED_APPS 맨 마지막에 보면 staticfiles라는 기본적인 앱이 들어가 있습니다.

또, 마지막에 보면 STATIC_URL = '/static/' 이라고 써있는 걸 확인할 수 있다.



templates 경로가 app/templates/__(여기부터 계산)__인 것처럼, static은 app/static/__(여기부터 계산)__

STATICFILES_DIRS = [BASE_DIR/'static',] 기본적으로 작성되어있지 않기 때문에 추가해주어야 함.

