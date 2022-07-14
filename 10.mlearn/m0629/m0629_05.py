import urllib.request as req
import gzip, os, os.path
import struct

# def to_csv(name,maxdata):
img_f = open("./mnist/train-images-idx3-ubyte","rb")
lbl_f = open("./mnist/train-labels-idx1-ubyte","rb")
csv_f = open("./mnist/train.csv","w",encoding="utf-8")
# img_f = open("./mnist/t10k-images-idx3-ubyte","rb")
# lbl_f = open("./mnist/t10k-labels-idx1-ubyte","rb")
# csv_f = open("./mnist/test.csv","w",encoding="utf-8")

# 헤더 정보 읽기 - 정수로 4byte씩 2개를 읽어요
mag,lbl_count=struct.unpack(">II",lbl_f.read(8))
mag,img_count=struct.unpack(">II",img_f.read(8))
rows,cols=struct.unpack(">II",img_f.read(8))
pixels= rows*cols

res=[]
for idx in range(lbl_count):
    if idx > 5000: break
    label= struct.unpack("B",lbl_f.read(1))[0]    
    bdata = img_f.read(pixels)
    sdata = list(map(lambda a:str(a),bdata))
    csv_f.write(str(label)+',')
    csv_f.write(",".join(sdata)+"\r\n")
    
    
csv_f.close()
lbl_f.close()
img_f.close()

print("csv파일 생성 완료")
img_f = open("./mnist/t10k-images-idx3-ubyte","rb")
lbl_f = open("./mnist/t10k-labels-idx1-ubyte","rb")
csv_f = open("./mnist/test.csv","w",encoding="utf-8")

# 헤더 정보 읽기 - 정수로 4byte씩 2개를 읽어요
mag,lbl_count=struct.unpack(">II",lbl_f.read(8))
mag,img_count=struct.unpack(">II",img_f.read(8))
rows,cols=struct.unpack(">II",img_f.read(8))
pixels= rows*cols

res=[]
for idx in range(lbl_count):
    if idx > 5000: break
    label= struct.unpack("B",lbl_f.read(1))[0]    
    bdata = img_f.read(pixels)
    sdata = list(map(lambda a:str(a),bdata))
    csv_f.write(str(label)+',')
    csv_f.write(",".join(sdata)+"\r\n")
    
    
csv_f.close()
lbl_f.close()
img_f.close()

print("csv파일 생성 완료")
