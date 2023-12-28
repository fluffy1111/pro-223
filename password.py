import zipfile
import time

folderpath = input('Path to the file: ')
zipf = zipfile.ZipFile(folderpath)
global result
result = 0
global tried
tried = 0
c=0

counter=0
characters =['0','1','2','3','4','5','6','7','8','9',
                'a','b','c','d','e','f','g','h','i','j','l','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

file_open = open("wordlist.txt","w")

for i in range(len(words)):
    word = words[i]
    password = word.encode('utf8').strip()
    c=c+1
    print('Trying to decode password by: {}'.format(word))
    try:
        with zipfile.ZipFile(folderpath,'r') as zf:
            zf.extractall (pwd=password)
            print("Success! The password is: "+word)
            endtime = time.time()
            result = 1
        break
    except:
        pass

if not zipf:
    print('The zipped file/folder is not password protected! You can successfully open it!')
else:
    starttime = time.time()
    wordListFile = open('wordlist.txt', 'r',errors='ignore')

if(result == 0):
    print("Sorry, password not found. A total of "+str(c)+"+ possible combinations tried in "+str(duration)+" seconds. Passwword is not of 4 characters.")
else:
    duration = endtime - starttime
    print('Congratulations!!! Password found after trying '+str(c)+' combinations in '+str(duration)+' seconds')

for i in characters:
    for j in characters:
        for l in characters:
            guess = str(i) + str(j) + str(k) + str(l)
            file_open.write(guess)
            file_open.write('\n')
            counter+=1
print("wordlist of {} passwords created".format(counter))