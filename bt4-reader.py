#!/usr/bin/env python2
import pygatt.backends
import binascii
import sys
import serial

def printIndication(handle, value):
    print value
    #val_str = binascii.unhexlify(''.join(value))
    #print val_str
    #print ' '.join(map(bin,bytearray(val_str)))
    val_fix = []
    for i in range(len(value)):
         val_fix.append(int(value[i], 16)&0x7F)
    val_str_fix = ''.join(map(chr,val_fix))
    sys.stdout.write(val_str_fix)
    sys.stdout.flush()
    #ser.write(val_str_fix)
         

#ser = serial.Serial("/dev/pts/2")
#print(ser.name) 


adapter = pygatt.backends.GATTToolBackend("hci0", open('/tmp/gatt.log', 'w'))
adapter.start(False)
#print(adapter)
while True:  
    try:
        device = adapter.connect('20:91:48:4C:4C:54')
        break
    except pygatt.exceptions.NotConnectedError:
        print('Waiting...')
        

#print(device.char_read("00002a00-0000-1000-8000-00805f9b34fb"))
#print(device.discover_characteristics())
device.subscribe('0000ffe1-0000-1000-8000-00805f9b34fb', printIndication, True)

while False:
    adapter._receive()

while True:
    inp = raw_input()
    device.char_write_handle(0x12, bytearray(inp))
