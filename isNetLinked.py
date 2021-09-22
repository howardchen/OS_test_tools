# judge network is connect or not
import requests
import sys
def isNetLinked():
    try:
        requests.get('https://www.google.com.tw/')
        requests.get('https://www.yahoo.com.tw/')
        requests.get('https://edition.cnn.com/')
        return True
    except:
        return False
        sys.exit(1)
