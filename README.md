# K8090 Velleman Pythonscript
This script can be used to control the K8090 8-channel relay card from Velleman over the serial USB port.

### Requirements
1) Make sure python is installed
2) You need the pyserial package, in Command Prompt:

```
> pip install pyserial
```

### Instructions
1) Connect the board to the PC
2) Open the Device manager to find the serial port name (e.g. COM8)
3) Open the Command Prompt and navigate to the pythonscript
4) Enter next command:

```
> python K8090_terminal.py COM8
```
