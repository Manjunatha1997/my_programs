import os

path = '/home/manju/fabrics/'

res = os.walk(path)
temp = []


for obj in res:
    root = obj[0]
    folders = obj[1]
    files = obj[2]
    c= 1
    for folder in folders:
        # print(folder,c)
        c += 1

        detail_file_size = {}
        size = 0
        for f in os.listdir(root+folder):
            # print(root+folder+'/'+f)
            file_size = root+folder+'/'+f
            size = os.path.getsize(file_size)
            size += size

        print(size)
        detail_file_size[folder] = size

    temp.append(detail_file_size)



print(temp)
print(len(temp))