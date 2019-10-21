# Project 1 Generative Text

Will Stock, wstock@ucsd.edu

## Abstract

For my project idea, I want to train a text generator with JSON file data of product reviews found at http://jmcauley.ucsd.edu/data/amazon/. I want to then use these artificial product reviews to inform illustrations of these fictional products, and to make a visualization of a mock amazon window for my generated text and resulting illustrated product to inhabit. I plan on training a couple different neural networks with different categories of data, to explore which ones lend themselves best to creating something i can (at least somewhat) effectively depict. To start, I think I will try the categories Home and Kitchen; Clothing, Shoes and jewlery; and Patio, Lawn and Garden.

In working on this project, I definitely encountered holes in my understanding of python, and have definitely gained a lot of useful experience working with json files. Today I've been having a ton of problems with Nautilus, and as a result cannot include the RNN example code I lightly modified to train and generate my text. I will include that here as soon as I can get back on the server. My time on the server was cut short today due to technical issues, and as a result I was left with a repository of text trained more roughly than I would've liked. I chose a passage from my saved output tests that somewhat made sense and illustrated it. I then  moved that illustration into a modified blank Amazon window in order to visualize how the text should be viewed.

## Model/Data

Briefly describe the files that are included with your repository:
Included in my repository are:
the dataset I drew from: Home_and_Kitchen_5.json
The code I made to pull review data out of this json file (json2txt.py)
The condensed text from 5000 reviews from this dataset (RNN_Script_HK.txt)
And the RNN example code I used to generate a RNN in order to 

## Code


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


RNN example code: (AS SOON AS POSSIBLE)

## Results

- Documentation of your generative text in an effective form. A file with your generated text (.pdf, .doc, .txt). 

## Technical Notes

Any implementation details or notes we need to repeat your work. 
- Does this code require other pip packages, software, etc?
- Does it run on some other (non-datahub) platform? (CoLab, etc.)

## Reference

https://stackoverflow.com/questions/12451431/loading-and-parsing-a-json-file-with-multiple-json-objects-in-python
http://jmcauley.ucsd.edu/data/amazon/
