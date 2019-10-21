#Resources
# https://stackoverflow.com/questions/12451431/loading-and-parsing-a-json-file-with-multiple-json-objects-in-python

# Imports
import json

# Declare variables
data = []
count = 0

#Read JSON data into the datastore variable
with open('Home_and_Kitchen_5.json') as f:
    for line in f:
        if(count < 5000):
            data.append(json.loads(line)['reviewText'])

            print(json.loads(line)['reviewText'])
            count += 1
        else:
            #write to file
            file = open("RNN_Script_HK.txt", "w")
            strD = str(data)
            file.write(strD)
            file.close()
            break
