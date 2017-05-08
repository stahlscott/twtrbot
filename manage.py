import app
import sys


if __name__ == "__main__":
    if sys.argv == 'initdb':
        app.init_db()
    else:
        app.run()
