import os

def secure_delete(path, passes=1):

    if os.path.exists(path):
        fileSize = os.path.getsize(path)
        with open(path, 'w+') as file:
            for i in range(passes):
                file.write(os.urandom(fileSize))
        os.remove(path)
        print('File deleted: ' + path)
