from flask_session import sessions
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import create_app, db
from flask_session import Session
# flask_script
app = create_app('develop')
manager = Manager(app)
# 数据库迁移
Migrate(app, db)
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    #sessions['name'] = 'lucy'
    return "index"
if __name__ == '__main__':
    manager.run()