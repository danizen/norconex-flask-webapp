#!/usr/bin/env python
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))


from flask_script import Manager, Server
from norconex import app


manager = Manager(app)

manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host='127.0.0.1')
)


if __name__ == '__main__':
    manager.run()

