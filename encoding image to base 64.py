#importing base64 to convert png image to base64 format
#base 64 is in built librarary in python
import base64
#opening image in (rerad binary by rb) and calling it imagefile 
#NOTE GIVE IMAGE FILE PATH
with open("image path","rb") as imagefile:
    byteform=base64.b64encode(imagefile.read())   #encoding it to byteform     
f=open('output.bin','wb')  #opening a new binary file where we will store our image byteform we converted earlier
f.write(byteform) #writing byteform in file name output.bin
f.close()     #clsing it
