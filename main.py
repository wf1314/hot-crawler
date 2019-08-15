from flask_script import Manager
from hot_crawler import create_app

app = create_app()
# configure your app

manager = Manager(app)

if __name__ == "__main__":
    manager.run()

