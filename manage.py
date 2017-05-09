import app
import sys

if __name__ == "__main__":
    if sys.argv[1] == 'initdb':
        from initdb import initdb
        initdb()
    else:
        app.run()
