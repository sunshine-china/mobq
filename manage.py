import  os

if os.path.exists('.env'):
    print('Importing enviroment from .env...')
    for line in open('.env'):
        var =line.strip().split('=')
        if len(var)==2:
            os.environ[var[0]]=var[1]

from app import  create_app,db


from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand

app=create_app(os.getenv('FLASK_CONFIG') or 'default')
manager=Manager(app)
migrate=Migrate(app,db)


manager.add_command('db',MigrateCommand)


if __name__=='__main__':
    manager.run()