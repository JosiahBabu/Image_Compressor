import os
import PIL
import datetime
from PIL import Image
import platform
import testgui
path="C:/Users/adon.augustin/Documents/New folder/image_compressor/Image_Compressor/input"
output_path="C:/Users/adon.augustin/Documents/New folder/image_compressor/Image_Compressor/output"     #"test_protein/saved_files"
notopenfileslog=[]
sizebeforefilelog=[]
sizeafterfilelog=[]
openfileslog=[]
resizedimension=[]

#len = 0

def getUser():
    uname=platform.node()
    print(uname)
    return uname
def CheckLogFile(user):
    try:
        f = open("log.txt", "a")
        now = datetime.datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        f.write("Log is recorded on "+date_time+" "+"Script run by:"+user+"\n")
        f.close()
    except:
        Print("Could not find the log file!")

def CreateLogFile(size):
    f = open("log.txt", "a")
    f.write("Converted File Name |"+" "+"Original Size(Mb) |"+"  "+" Converted Size(Kb) |"+"  "+"Converted Dimension|\n-----------------------------------------------------------------------------------------------------------------------------------------------------\n")
    for i in range(size):
        f.write(str(openfileslog[i])+" "+" "+str(sizebeforefilelog[i])+" "+str(sizeafterfilelog[i])+" "+resizedimension[i]+"\n")
    f.close()

def SizetoMb(size_of_file):
    sizeinmb=size_of_file/(1024*1024)
    return sizeinmb

def SizetoKb(size_of_file):
    sizeinkb=size_of_file/(1024)
    return sizeinkb

def ResizeFiles():
    try:
        for filename in os.listdir(path):
            #if(len==1):
                #break

            print(filename)

            if filename.endswith(".jpg") or filename.endswith(".png"):
                print(os.path.join(path, filename))
                filepath=os.path.join(path, filename)
                notopenfileslog.append(filepath)
                print("size",os.path.getsize(filepath))
                sizeinmb=SizetoMb(os.path.getsize(filepath))
                print("size in mb",sizeinmb)
                if(sizeinmb>6):
                    image = Image.open(os.path.join(path, filename))
                    openfileslog.append(filepath)
                    rot_img = image.rotate(270,expand=True)
                    r,c=rot_img.size
                    print("width:",r,"height",c)
                    rr=int(r/3)
                    cc=int(c/3)
                    resized_image = rot_img.resize((rr,cc))
                    resized_image.save(output_path+'/'+filename, 'JPEG', quality=70)
                    print("resized_width:",rr,"resized_height",cc)
                    resizedimension.append(str(rr)+"X"+str(cc))
                    sizebeforefilelog.append(sizeinmb)
                    sizeafterfilelog.append(SizetoKb(os.path.getsize(output_path+'/'+filename)))
                    #len+=1
                    print("A file found in ",filepath)


                    continue
            else:
                continue

    except:
               print("Exception thrown. path does not exist.")
               input('press any key?\n')

def main():
    user=getUser()
    CheckLogFile(user)
    ResizeFiles()
    CreateLogFile(len(openfileslog))

if __name__=="__main__":
    main()
