# Opswat Coding Assessment Assignment

## Set-Up

This project was design with python 3.8.5 version. You must have atleast python 3.0 in order to run this project. Furthermore you must import several functions tool such as: json, requests, sys, hashlib.

## Importing Tools

To import the necessary tools go to your command line and write:

```bash
pip install json
pip install requests
pip install sys
pip install hashlib
```

In order for the program to work you must install these libraries

## How the start the program

To start the program you must be at the main directory, where the program is located at. Then you open your command line at that directory and type.

```bash
python app.py sample.txt
```
You always need to include a file alonside the program in order for it work 

## Main Purpose

The main object for this project is to generate a simple program to scan a file against metadefender.opswat.com API's. In order to test it the program would lookup first the hash function of a file and then using the value with a "get" function. Second, if it could not locate a file with its hash number then it would need to scan the file, which the user is trying to upload, with a "post" function. Furthermore, after the the program call the post function it would then scanned metadefender.com api with the file "data_id" multiple times until the file is then uploaded.


## Functions

### hash_file( string<filename>)

Function calculate the hash value of the file by using SHA-1 algorithm

### request.get(https://api.metadefender.com/v4/file/:dataId)

Function that call the get function by finding a file with a "data_id". This would scanned the file that is uploaded and checked wether or not is has completely scanned 

### request.post(https://api.metadefender.com/v4/file)

Function that call the post function that will upload a file to the MetaDefender Cloud. Futhermore, it will intiated a scan for all cloud engine that MetaDefender Cloud has.

### request.get(https://api.metadefender.com/v4/file/:hash)

Function that call a get function from a file hash value. For this hash value is calculated from SHA-1 algorithm.
