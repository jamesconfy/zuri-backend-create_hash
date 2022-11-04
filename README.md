# How Code Works

This work is created using [Python](https://www.python.org) and librabries (csv, json, hashlib and an external local obj module that cotains the json schema)

## How to run the code on your system

1. Clown the repository using `git clone`
2. After clowning open the directory where you have each files and do a `python3 hash.py` NB: You need to already have python installed on your system (preferably python:3.10 and upwards).
3. You will be promoted to enter the name of the CSV file you want to create the hash for. NB: The CSV file have to be in the same directory, so copy the CSV file to the cloned directory.
4. After inputting the file name, the filename.output.csv will be created for you and also a filename.json that contains the nft attributes.

Once the code is ran, you are prompt to input the name of your CSV file (note: this file have to be in the same folder as the code, there is also no need to add the extenstion).

With this inputted value, your output file name is generated and the computation starts.

## Procedures

The input file is first opened in read mode and the row_count (i.e the length of data) is computted and stored in the row_count variable (This is meant to be added to the json file later)

Afterwards, both the input file and output files are opened in both read and write mode as the process goes hand in hand. The data in both files are opened in a dictionary pattern using the DictReader and DictWriter from the CSV librabry. Each header from the input file is added to the ouput file and "Hashed" is added to it also (for the json file).

We loop over the values in the input file and the needed data like (Series Number, UUID, Description, Filename etc.) is gotten and used to create the object (not the same as a json schema) [can be found (here](./schema.json)). The created object is first converted to a json object using the dumps method from the JSON librabry.

This JSON object is then hashed using the sha256 from the HASHLIB librabry and the hashed value is added to the data gotten from the input file. This data is then written to the writer (output) file.
