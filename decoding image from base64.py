import base64
# opening output.bin and read as binary
file=open("output.bin","rb")
byte=file.read() #what we read in file we are fethching in byte object
file.close() #closing what we read because alresady store in byte object
# opening image file and named it and use it to (write binary as wb) 
fh=open('raspberrypi.png','wb')
fh.write(base64.b64decode(byte))   # decoding byte object in image file.png
fh.close()  # closing it
