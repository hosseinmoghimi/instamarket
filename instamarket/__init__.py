import pymysql
from .settings import MYSQL

if MYSQL:
    pymysql.version_info = (2, 0, 1, "final", 0)
    pymysql.install_as_MySQLdb()
