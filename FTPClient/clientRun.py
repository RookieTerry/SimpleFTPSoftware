import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from bin import ftpclient

if __name__ == "__main__":
    ftpclient.run()
