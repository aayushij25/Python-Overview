import os
from datetime import datetime
# print(dir(os))

print(os.getcwd())

os.chdir('/Users/aayushijaiswal/Documents/Masters/')
# os.mkdir('Sem2')
# os.makedirs('Sem3/Sub1')
# os.rmdir('Sem2')
# os.removedirs('Sem3/Sub1')
# os.rename('Sem2', 'New Folder')
mod_time = os.stat('Sem1').st_mtime
print(os.getcwd(), "\n", os.listdir(), '\n', datetime.fromtimestamp(mod_time))

