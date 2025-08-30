ALLOWED_HOSTS = ["*"]
DEBUG = True

DATABASES = {
    "default" : {
        "ENGINE" : "django.db.backends.postgresql",
        "NAME" : "vc.ru",
        "USER" : "postgres",
        "PASSWORD" : "mukhibillo",
        "HOST" : "localhost",
        "PORT" : "5432",
        "ATOMIC_REQUEST" : True,
    }
}

HOST = "http://localhost:8000"




