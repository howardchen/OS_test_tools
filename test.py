from getIp import getIp
from isNetLinked import isNetLinked
from Is64Windows import Is64Windows
from fileMove import FileMove

print(getIp())
print(isNetLinked())
print(Is64Windows())
file_handle = FileMove()
print(file_handle.fileCopy)
print(file_handle.uploadResult)