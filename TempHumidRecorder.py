import Adafruit_DHT
import os
import time

sensor = Adafruit_DHT.DHT22
pin = 17

DISCPMFORT_LIMIT_Good = 75
DISCPMFORT_LIMIT_NotGood = 80
DISCPMFORT_LIMIT_Bad = 85
DISCPMFORT_LIMIT_TooBad = 90

#不快指数の計算
def calcDiscomfort(tmp, hmd):
    return 0.81*tmp + 0.01*hmd*(0.99*tmp - 14.3) + 46.3

#CPU温度
def calcCPUTmp():
    cmd = '/opt/vc/bin/vcgencmd measure_temp'
    line = os.popen(cmd).readline().strip()
    return line.split('=')[1].split("'")[0]

while(True):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    print("湿度： {:.1f}%".format(humidity))
    print("温度： {:.1f}degC".format(temperature))
    print("不快指数： {:.1f}".format(calcDiscomfort(temperature, humidity)))
    print("CPU温度：" + calcCPUTmp() + "degC")
    print()
    
    time.sleep(2)