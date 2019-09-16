import os, shutil, cv2
from natsort import natsorted


aaa="./3"


# 访问指定文件夹(假设视频都放在这里面)
for root, dirs, files in os.walk(aaa):
    # 按文件名排序
    files = natsorted(files)
    # 遍历所有文件
    for file in files:
        # 如果后缀名为 .mp4
        if os.path.splitext(file)[1] == '.mp4':
            # 拼接成路径写入
            shotname, extension = os.path.splitext(file)
            #print(shotname, extension, file)
            finishcode1 = "ffmpeg -i "+aaa+ "/"+file+" -metadata:s:v rotate=\"0\" -codec copy -y "+aaa+ "/"+shotname+"_"+".mp4"
            os.system(finishcode1)
            os.remove(aaa + "/" + file) 
            os.rename(os.path.join(aaa,shotname+"_"+".mp4"),os.path.join(aaa,shotname+".mp4"))
            cap = cv2.VideoCapture(aaa+ "/"+file)
            w = cap.get(3)
            h = cap.get(4)
            print(w, h)
            cap.release()
            if(w<=h):
                finishcode = "ffmpeg -i "+aaa+ "/"+file+" -metadata:s:v rotate=\"90\" -codec copy -y "+aaa+ "/"+shotname+"_"+".mp4"
                #print(finishcode)
                os.system(finishcode)
                os.remove(aaa + "/" + file)
