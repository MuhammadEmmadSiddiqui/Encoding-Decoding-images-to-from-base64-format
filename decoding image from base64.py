import base64
# opening output.bin and read as binary
#NOTE FILE NAME WHICH YOU CONVERT i named here as output.bin 
file=open("output.bin","rb")
byte=file.read() #what we read in file we are fethching in byte object
file.close() #closing what we read because alresady store in byte object
# opening image file and named it and use it to (write binary as wb) 

#NOTE WHATEVER IMAGE FILE NAME YOU WANT TO DO I NAMED HERE AS RASPBERRYPI.PNG
fh=open('raspberrypi.png','wb')
fh.write(base64.b64decode(byte))   # decoding byte object in image file.png
fh.close()  # closing it
