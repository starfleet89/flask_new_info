import logging

import redis

class Config(object):
    #工程信息配置
    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
    DEBUG = True
    # 导入数据库配置
    # 设置数据库连接
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1:3306/information'
    # 动态追踪设置
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 显示原始sql
    SQLALCHEMY_ECHO = True

    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    #flask_session配置信息
    SESSION_TYPE = "redis" #指定session保存到redis中
    SESSION_USE_SIGNER = True #让cookie中的sessionid 被加密处理
    #使用redis实例
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 86400 #session有效期/秒
    #日志级别
    LEVEL = logging.DEBUG
# 开发环境
class DevelopConfig(Config):
    pass
# 生产环境
class ProductConfig(Config):
    DEBUG = False
    LEVEL = logging.ERROR

# 测试环境
class TestingConfig(Config):
    TESTING = True
# 通过统一的字典进行配置类的访问
config_dict = {
    "develop":DevelopConfig,
    "product":ProductConfig,
    "testing":TestingConfig,
}