import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

SECRET_KEY = "q1=an5ti-z#au*s3t_=##(^e#ihoo4c=ic4pg-7zt)m9x=c8_r"