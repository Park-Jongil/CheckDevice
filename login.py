import urllib.request
from http.client import HTTPSConnection
from base64 import b64encode
import requests

#출처: https://hack4profit.tistory.com/27 [hack4profit]
def CookieTest() :
    url = "http://192.168.0.101/basic/basic.php"
    login_form = {"id":"admin", "pw":"admin"}
    login_req = urllib.urlencode(login_form)
    request = urllib2.Request(url, login_req)
    response = urllib2.urlopen(request)
    cookie = response.headers.get('Set-Cookie')

    request = urllib2.Request("http://192.168.0.101/system/time.php?app=get")
    request.add_header('cookie', cookie)
    response = urllib2.urlopen(request)
    print( response.read() )

def main():
    with requests.Session() as s:
        response = s.get('http://192.168.0.101/basic/basic.php', auth=('admin', 'admin'))
        cookie = response.headers.get('Set-Cookie')
        print(response.status_code)
        response = s.get( 'http://192.168.0.101/system/time.php?app=get' )
        print( response.text ) 

        request = request("http://192.168.0.101/system/time.php?app=get")
        request.add_header('cookie', cookie)
        response = request.urlopen(request)
        print( response.read() )


if __name__ == '__main__':
    main()

# 200 <div lang=EN-US style='font-size:24.0pt;font-family:Times New Roman;'>
# <b>401 Unauthorized</b></div></br><div lang=EN-US style='font-size:12.0pt;font-family:Times New Roman;'>
# You must enter a valid login ID and password to access this resource.</div>


