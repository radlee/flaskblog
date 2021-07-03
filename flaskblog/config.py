import os

class Config:
   SECRET_KEY = '44604b6a227ef4672dee304f643c2159'
   SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
   MAIL_SERVER = 'smtp.googlemail.com'
   MAIL_PORT = 587
   MAIL_USE_TLS = True
   MAIL_USERNAME = 'prof.lolito@gmail.com'
   MAIL_PASSWORD = 'Leander247365'
   SQLALCHEMY_TRACK_MODIFICATIONS = False
   