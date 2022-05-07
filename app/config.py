import os

SQLALCHEMY_DATABASE_URI_TMPL = "postgresql+psycopg2://%(user)s:%(passwd)s@%(host)s:%(port)s/%(name)s"


class Config:
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASS = os.getenv("DB_PASS", "")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "postgres")

    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI_TMPL % {
        'user': DB_USER,
        'passwd': DB_PASS,
        'host': DB_HOST,
        'port': DB_PORT,
        'name': DB_NAME
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
