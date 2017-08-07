import serial
import binascii
import struct
import time

OP_CODE = {"PRIV_SEND": "A"}


#AA5E28D6A97A2479A65527F7290311A3624D4CC0FA1578598EE3C2613BF99522
#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
#2222222222222222222222222222222222222222222222222222222222222222
#5555555555555555555555555555555555555555555555555555555555555555
#f14a18f85ea864a33d679207e7d4a122d86785e696e24b912d792f85711833c4
#1837BC2C546D46C705204CF9F857B90B1DBFFD2A7988451670119945BA39A10B

C = 0
i = 0
j = 0
b = str(0)
d = 0
tt = 0
p = serial.Serial('COM4',500000,timeout=2)
ff = 0
w = 0
cc = hex(204)
ww = struct.pack(b'B',int(cc,16))
zbit = struct.pack(b'B',int(tt))
zflag = 0

while tt == 0:
 if d == 0: 
  yo = input('Press A: Public Key Generation \nPress B: Sign Message Hash \n')
  if yo == 'a':
   C = 160
   d = 1
  if yo == 'b':
   C = 176
   d = 1
  if yo == 'c':
   p.write(ww)
   ff = p.read(1000)
   print(ff)
 #if d == 1:
 #  xx = struct.pack(b'B',int(C))
 #  p.write(xx)
 #  b = str(0)
 #  i = 0

 if d == 1:
     text = input("To FPGA: ")
     assert len(text) == 64, 'Must be 256 bit hex value'
     taco = int(text,16)
     data = hex(taco)
     print(data)
     i = 2
     j = 0
     while i < 66:
        tmp = int(data[i],16) + C
        send = struct.pack(b'B',tmp)
        #print(send)
        p.write(send)
        i = i + 1
     while j <= 64:
        ff = binascii.hexlify(p.read(1))
        qq = str(ff)
        ww = qq[2:4]
        b = b + ww
        j = j + 1
     print(b[3:])
     b = str(0)
     d = 0
#    zflag = 0

exit()


