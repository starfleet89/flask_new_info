from flask import Flask, session
import redis
from flask_script import Manager
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_migrate import Migrate,MigrateCommand
app = Flask(__name__)

class Config(object):
    #工程信息配置
    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
    DEBUG = True
    # 导入数据库配置
    # 设置数据库连接
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/information'
    # 动态追踪设置
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # 显示原始sql
    app.config['SQLALCHEMY_ECHO'] = True

    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    #flask_session配置信息
    SESSION_TYPE = "redis" #指定session保存到redis中
    SESSION_USE_SIGNER = True #让cookie中的sessionid 被加密处理
    #使用redis实例
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 86400 #session有效期/秒


app.config.from_object(Config)
# 初始化数据库
db = SQLAlchemy(app)
# 初始化redis 对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启csrf保护，只做服务器验证功能，
CSRFProtect(app)
# 设置session保存指定位置
Session(app)

manager = Manager(app)
Migrate(app,db)
manager.add_command('db',MigrateCommand)

@app.route('/')
def index():
    session['name'] = 'lucy'
    return 'index'

if __name__ == '__main__':
    app.run()
