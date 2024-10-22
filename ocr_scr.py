#Install dependencies
#pip install easyocr
#pip install --force-reinstall -v "Pillow==9.5.0" ##Downgrade Pillow to 9.5.0

#Import libraries
import easyocr
import os

folder_path = r"C:\Caminho" #label image folder path

jpgnames = []
result=[]
for file in os.listdir(folder_path):

    file_path = os.path.join(folder_path, file)
    # just for the .jpg
    if file_path.endswith(".jpg"):
        jpgnames.append(file)
i=0
while i < len(jpgnames):
    reader = easyocr.Reader(['en', 'pt', 'es'], cudnn_benchmark=True)
    img_path=[folder_path+"\\"+jpgnames[i]]
    print(img_path)
    result1 = reader.readtext_batched(img_path, n_width=800, n_height=600, detail=0, paragraph=True)
    print(result1)
    result.append(result1[0][0])

    i=i+1
    print(i)
print(result)
f = open("C:\Caminho\labelname.txt", "w")  # .txt save path
for line in result:

    f.write(line + '\n')
f.close()