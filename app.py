import json
import requests
import sys
import hashlib

#Function to calculate the hash using SHA-1 algorithm
def hash_file(filename):

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

#get the name of the file on the command line
textname= sys.argv[1]

# variables:
# url : Holds the host url where the api is found
# header, header2 : saved the parameters for how we would comunicate to the api endpoint 
# files: contain the file we are trying to find and upload. the file is open in a binary format to read it.
url="https://api.metadefender.com/v4/file"
header= { 'apikey': 'APIKEY','callbackurl':'https://webhook.site/d76ffaf8-5dc5-4348-b000-c63e73a847bc', 'Content-Type':'application/octet-stream',
'user-agent':'opswat metadefender cloud' }
header2={ 'apikey': 'APIKEY',}
files = {'file': (textname, open(textname, 'rb'))}

#calculate the hash value from the selected file and saved it to a local variable 
hash_code= hash_file(textname)

#first reponse to check if the hash valued is found in the api database
reponse_hash= requests.get( ( "https://api.metadefender.com/v4/hash/"+hash_code ), headers=header2 )

containe_2=reponse_hash.json()

#if the hash value does not produced the file then we would start 
# to insert the file through a post request
if(reponse_hash.status_code==400 or containe_2["scan_results"]["scan_all_result_a"]=="Not Scanned"):

    #A post request with the file which we are trying to save
    scan_file=requests.post("https://api.metadefender.com/v4/file", headers=header, files=files, )

    #saved the post result in json format on the variable container and 
    # then sabed the data_id to variable "data_id"
    container=scan_file.json()
    data_id=container['data_id']

    #start by calling the get request from datat_id 
    reponse_id= requests.get( ("https://api.metadefender.com/v4/file/"+data_id), headers=header2 )
    container_3=reponse_id.json()

    #Loop through the get post until the scanned hits 100 percent 
    while(container_3["scan_results"]["progress_percentage"] != 100):

        reponse_id= requests.get( ("https://api.metadefender.com/v4/file/"+data_id), headers=header2 )
        container_3=reponse_id.json()

    #print found result in json format
    print(json.dumps(reponse_id.json(), indent= 1, separators =(". ", " = ")))

else:
    #saved the data in json format the print it to the terminal
    example= json.dumps(reponse_hash.json(), indent= 1, separators =(". ", " = "))
    print(example)

