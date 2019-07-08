from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
from datetime import datetime
import urllib.request
import requests
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

# Manual Datetime Setting(HiTron)
def Set_DateTime(IpAddr) :   
    res = requests.get('http://' + IpAddr + '/basic/basic.php', auth=('admin', 'admin'))
    if (res.status_code==200) :
        now = datetime.now() 
        url1 = "http://" + IpAddr + "/system/time.php?app=set&tsyncmode=0&tzone=62&dst_enable=0&dt=" + now.strftime('%Y-%m-%d') + "&tm=" + now.strftime('%H:%M:%S')
        res = requests.get(url1,auth=('admin', 'admin') )
        if (res.status_code==200) :
            print( "DateTime Set Success Device = " + IpAddr)
        else :
            print( "DateTime Set Failure Device = " + IpAddr)
    else :
        print( "Not Support Device = " + IpAddr)

# NTP Server Setting (Hitron)
def Ser_NTP_Server(IpAddr,NTP_Server) :   
    res = requests.get('http://' + IpAddr + '/basic/basic.php', auth=('admin', 'admin'))
    if (res.status_code==200) :
        now = datetime.now() 
        url1 = "http://" + IpAddr + "/system/time.php?app=set&tsyncmode=2&tzone=62&dst_enable=0&ntp_server=" + NTP_Server
        res = requests.get(url1,auth=('admin', 'admin') )
        print( res.text )
    else :
        print( "Not Support Device = " + IpAddr)

# Manual Datetime Setting(HiTron)
def Set_DateTime_LG(IpAddr) :   
    res = requests.get('http://' + IpAddr + '/basic/basic.php', auth=('admin', 'admin'))
    if (res.status_code==200) :
        now = datetime.now() 
        datestr = "&year=" + str(now.year) + "&month=" + str(now.month) + "&day=" + str(now.day) 
        timestr = "&hour=" + str(now.hour) + "&minute=" + str(now.minute) + "&second=" + str(now.second) 
        url1 = "http://" + IpAddr + "/httpapi?SetDateTimeConfig&dateTimeMode=DATETIME_MODE_MANUAL" + datestr + timestr
        res = requests.get(url1,auth=('admin', 'admin') )
        if (res.status_code==200) :
            print( "DateTime Set Success Device = " + IpAddr)
        else :
            print( "DateTime Set Failure Device = " + IpAddr)
    else :
        print( "Not Support Device = " + IpAddr)


# NTP Server Setting (LG)
def Ser_NTP_Server_LG(IpAddr,NTP_Server) :   
    res = requests.get('http://' + IpAddr + '/basic/basic.php', auth=('admin', 'admin'))
    if (res.status_code==200) :
        now = datetime.now() 
        url1 = "http://" + IpAddr + "/httpapi?SetDateTimeConfig&dateTimeMode=DATETIME_MODE_AUTO&interval=NTP_INTERVAL_ONE_DAY&serverAddress=" + NTP_Server
        res = requests.get(url1,auth=('admin', 'admin') )
        print( res.text )
    else :
        print( "Not Support Device = " + IpAddr)


def AuthTest():
#    res = requests.get('http://192.168.0.101/basic/basic.php', auth=HTTPBasicAuth('admin', 'admin'))
#    res = requests.get('http://192.168.0.101/basic/basic.php', auth=HTTPDigestAuth('admin', 'admin'))
# OAuth2 Authentication，先安装requests-oauthlib
#    url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
#    auth = OAuth2('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN')
#    requests.get(url, auth=auth)
    res = requests.get('http://192.168.0.101/basic/basic.php', auth=('admin', 'admin'))
    print(res.status_code)
    res = requests.get("http://192.168.0.101/system/time.php?app=get",auth=('admin', 'admin') )
    print( res.text )
    data1 = { 'app':'set' , 'dt':'2019-07-05' }
    res = requests.get("http://192.168.0.101/system/time.php",params=data1,auth=('admin', 'admin') )
    print( res.text )
    res = requests.get("http://192.168.0.101/system/time.php?app=get",auth=('admin', 'admin') )
    print( res.text )

def main() :
    conn = create_connection("CameraStatus.db")
    cur = conn.cursor()
    cur.execute("SELECT seq,assets_name,equip_ip FROM tbl_CameraInfo ")
    rows = cur.fetchall()
    for row in rows :
        print("시간설정중 : " + str(row[1]) + " [" + str(row[2]) + "]" )
#        Set_DateTime( str(row[2]) )    
    conn.close()  

if __name__ == '__main__':
    main()
#    Set_DateTime('192.168.0.101')
#    Ser_NTP_Server('192.168.0.101','192.168.0.1')
#    res = requests.get("http://192.168.0.101/system/time.php?app=get",auth=('admin', 'admin') )
#    print( res.text )



