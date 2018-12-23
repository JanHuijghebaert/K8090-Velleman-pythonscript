#----------------------------------------------------------------------
# Author : Jan Huijghebaert
# Description : Generates commands for K8090 from Velleman
#----------------------------------------------------------------------


# Brief : Turn relay on command
# Param : relay_num : Number of relay (1 to 8)
# Return : Generated command m
def relay_on(relay_num):
    m = bytearray()
    m.append(0x04)
    m.append(0x11)
    mask = 1 << (relay_num - 1)
    m.append(mask)
    m.append(0x00)
    m.append(0x00)
    sum = (0x04 + 0x11 + mask)
    chk = ((sum ^ 0xFFF) & 0xFF) + 1
    m.append(chk)
    m.append(0x0F)
    return m


# Brief : Turn relay off command
# Param : relay_num : Number of relay (1 to 8)
# Return : Generated command m
def relay_off(relay_num):
    m = bytearray()
    m.append(0x04)
    m.append(0x12)
    mask = 1 << (relay_num - 1)
    m.append(mask)
    m.append(0x00)
    m.append(0x00)
    sum = (0x04 + 0x12 + mask)
    chk = ((sum ^ 0xFFF) & 0xFF) + 1
    m.append(chk)
    m.append(0x0F)
    return m


# Brief : Toggle relay command
# Param : relay_num : Number of relay (1 to 8)
# Return : Generated command m
def relay_toggle(relay_num):
    m = bytearray()
    m.append(0x04)
    m.append(0x14)
    mask = 1 << (relay_num - 1)
    m.append(mask)
    m.append(0x00)
    m.append(0x00)
    sum = (0x04 + 0x14 + mask)
    chk = ((sum ^ 0xFFF) & 0xFF) + 1
    m.append(chk)
    m.append(0x0F)
    return m