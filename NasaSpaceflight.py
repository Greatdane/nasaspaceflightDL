import subprocess
import os

# https://forum.nasaspaceflight.com/index.php?topic=51332
# wget -e robots=off -r -k -np --accept-regex 'action=dlattach' --content-disposition -U Mozilla -w 3 'https://forum.nasaspaceflight.com/index.php?topic=51332'
# wget -U Mozilla -w 3 -O index.html 'https://forum.nasaspaceflight.com/index.php?topic=51332'

# Variables
topic = "51332"
pages = 156
page_start = 1
# ---------

URL = "https://forum.nasaspaceflight.com/index.php?topic="
complete_URL = URL + topic
print(complete_URL)

# args = ['wget', '-e', 'robots=off', '-r', '-k', '-np','--accept-regex', 'action=dlattach', '--content-disposition', '-U', 'Mozilla', '-w', '3' , complete_URL]

for page in range(page_start-1, pages):
    print("Downloading page " + str(page+1))
    # make dir
    dir = str(page+1).zfill(len(str(pages)))
    os.mkdir(dir)
    os.chdir(dir)
    counter = page * 20 
    # images
    args = ['wget', '-e', 'robots=off', '-r', '-k', '-np','--accept-regex', 'action=dlattach', '--content-disposition', '-U', 'Mozilla', '-w', '2' , complete_URL+"."+str(counter)]
    print(complete_URL+"."+str(counter))
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print("Images Downloaded")
    # html page
    args2 = ['wget', '-U', 'Mozilla', '-w', '2' , '-O', 'index.html', complete_URL+"."+str(counter)]
    process2 = subprocess.Popen(args2, stdout=subprocess.PIPE)
    stdout, stderr = process2.communicate()
    print("HTML downloaded")
    os.chdir('..')


# process = subprocess.Popen(args, stdout=subprocess.PIPE)
# stdout, stderr = process.communicate()
