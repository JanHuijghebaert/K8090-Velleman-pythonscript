#----------------------------------------------------------------------
# Author : Jan Huijghebaert
# Description : Opens serial terminal to K8090 from Velleman
#----------------------------------------------------------------------

# Imports
import sys
import time
import serial
import K8090_commands

# Get serial COM port
print("Connect to ", str(sys.argv[1]))

# Connect to K8090
ser = serial.Serial(port=str(sys.argv[1]), baudrate=19200, timeout=None, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

# Example program
for relay_num in range(1,9):
	ser.write(K8090_commands.relay_toggle(relay_num))
	time.sleep(0.5)
	ser.write(K8090_commands.relay_toggle(relay_num))
	time.sleep(0.5)

# Close serial connection with K8090
ser.close()