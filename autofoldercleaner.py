import os

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(files,foldername):
    for file in files:
        os.replace(file,f"{foldername}/{file}")



files=os.listdir()
files.remove('autofoldercleaner.py')


createIfNotExist('Images')
createIfNotExist('Documents')
createIfNotExist('Medias')
createIfNotExist('Compressed_files')
createIfNotExist('Setup_files')
createIfNotExist('Others')

imgExts = ['.jpg','.png','.jpeg','.gif']
images=[file for file in files if os.path.splitext(file)[1].lower() in imgExts]

docExts = ['.txt','.pdf','.pptx','.xlsx','.docx','.json']
docs=[file for file in files if os.path.splitext(file)[1].lower() in docExts]

mediaExts = ['.mp4','.flv','.mp3','.wav']
medias=[file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

compressedFilesExts = ['.zip','.rar']
compressedfiles=[file for file in files if os.path.splitext(file)[1].lower() in compressedFilesExts]

setupExts = ['.exe','.setup']
setupfiles=[file for file in files if os.path.splitext(file)[1].lower() in setupExts]

others=[]
for file in files:
    ext= os.path.splitext(file)[1].lower()
    if (ext not in imgExts) and (ext not in docExts) and (ext not in mediaExts) and (ext not in compressedFilesExts) and (ext not in setupExts) and os.path.isfile(file):
        others.append(file)

move(images,'Images')
move(docs,'Documents')
move(medias,"Medias")
move(compressedfiles,"Compressed_files")
move(setupfiles,"Setup_files")
move(others,"Others")



