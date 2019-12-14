import psutil
import platform

f=open('info.txt','w')
#OS
f.write(platform.system() + '\n')
#memory
f.write(str(psutil.virtual_memory().total) + '\n')
#user
a=psutil.users()
f.write(str(a[0].name) + '\n')
f.close()

