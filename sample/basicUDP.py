'''
  basicUDP.py - This is basic UDP example.
  Created by Yasin Kaya (selengalp), September 19, 2018.
'''

from nbiot import nbiot
import time

your_ip = "xx.xx.xx.xx" # change with your ip
your_port = "xxxx" # change with your port

node = nbiot.NBIoT()

node.sendATComm("ATE1","OK\r\n")

node.setScrambleConf(node.SCRAMBLE_ON)
node.setAutoConnectConf(node.AUTO_ON)

node.getIMEI()
time.sleep(0.5)
node.getFirmwareInfo()
time.sleep(0.5)
node.getHardwareInfo()
time.sleep(0.5)

node.setIPAddress(your_ip)
time.sleep(0.5)
node.setPort(your_port)
time.sleep(0.5)

node.connectToOperator()
time.sleep(0.5)

node.closeConnection()
time.sleep(0.5)
node.startUDPService()
time.sleep(0.5)

node.sendDataUDP("Hello World!\r\n")
time.sleep(0.5)
