import subprocess

def adb_connect(host, port):
    """
    Kết nối với thiết bị Android qua ADB.
    """
    try:
        result = subprocess.run(f"adb connect {}:{}".format(host, port))
    except Exception as e:
        print(f"Cannot connect to device: {str(e)}")
        return None
    
adb_connect("192.168.1.99", "5555")