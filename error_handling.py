# This will overwrite the first output
file = open('youtube.txt', 'w') #'w' will create file if not present

try:
    file.write('Hello File Try')
finally:
    file.close()
    
#another process
with open('youtube.txt', 'w') as file:
    file.write('Hello File with')
    
#for keeping both output
file = open('youtube_new.txt', 'w') #'w' will create file if not present

try:
    file.write('Hello File Try')
finally:
    file.close()
    
#another process
with open('youtube_new.txt', 'a') as file:
    file.write('\nHello File with')