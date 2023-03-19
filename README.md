Team Project for SE class in Sp23

Team: 
* Jeremy Huey, Captain
* Chris Tighe
* Ijeoma Ogbogu
* Mengli Yang
# Note: due to some funky merging, the automatic blame might not be fully correct for who has done what code. 

Projects: 
ca01 - Project 1: This is a simple flask/python webapp that takes in a gpt secret key, opens up a localhost webserver for the app. 
The app has 4 different prompts for quickly querying ChatGPT (model="text-davinci-003") on 4 different fun topics of our interest.
You simply type in something related to the prompts and see what chatgpt gets from it. 

To run: 
Download ca01 from here. 
(go to openai and get your own secret key) https://platform.openai.com/account/api-keys
Paste that into the file secret.sh inside of dir ca01 : 
'''
#!/bin/bash
APIKEY="<ENTER YOUR KEY HERE>"
export APIKEY
'''
run 
$ chmod +x secret.sh #allows executing this script.
$ . secret.sh # this edits your env to accept your own secret key. 
$ export -p # check your env vars. 
$ python3 webapp.py
click the link to go to your localhost. http://127.0.0.1:5001/
then choose a person's name for a prompt type
type a prompt!
See the result!

