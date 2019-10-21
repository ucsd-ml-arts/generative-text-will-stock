# Project 1 Generative Text

Will Stock, wstock@ucsd.edu

## Abstract

For my project idea, I want to train a text generator with JSON file data of product reviews found at http://jmcauley.ucsd.edu/data/amazon/. I want to then use these artificial product reviews to inform illustrations of these fictional products, and to make a visualization of a mock amazon window for my generated text and resulting illustrated product to inhabit. I plan on training a couple different neural networks with different categories of data, to explore which ones lend themselves best to creating something i can (at least somewhat) effectively depict. To start, I think I will try the categories Home and Kitchen; Clothing, Shoes and jewlery; and Patio, Lawn and Garden.

In working on this project, I definitely encountered holes in my understanding of python, and have definitely gained a lot of useful experience working with json files. Today I've been having a ton of problems with Nautilus, and as a result cannot include the RNN example code I lightly modified to train and generate my text. I will include that here as soon as I can get back on the server. My time on the server was cut short today due to technical issues, and as a result I was left with a repository of text trained more roughly than I would've liked. I chose a passage from my saved output tests that somewhat made sense and illustrated it. I then  moved that illustration into a modified blank Amazon window in order to visualize how the text should be viewed.

## Model/Data

Included in my repository are:

The dataset I drew from - Home_and_Kitchen_5.json

The code I made to pull review data out of this json file - json2txt.py

The condensed text from 5000 reviews from this dataset - RNN_Script_HK.txt

Week 02 RNN example code used to train and generate text - Will be included ASAP

Illustration of chosen text - Pressure_Cooker.jpg 

Mock Amazon window with generated text and illustration

## Code

json2txt.py

# Imports
import json

# Declare variables
data = []
count = 0

# Read JSON data into the datastore variable
```
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
```

RNN example code: (AS SOON AS POSSIBLE)

## Results

Generated_Text.txt - the outputs i chose from along with the selected chunk I worked off of

Temp: 1.0

ROMEOXTHE:..6265.- Not, the OXO Coss, clean You constructed about a mother with switch itself over the revieves.  This product and I am not honning to do.  I wanted.  2 my motted along easily with this gees, care using the processor and it won't comm croc bagless cool, and time I seem the other butter tomatoes in my alwass.", "Might this verso rins, it beloss), and Grips are-quick better than I require more than the reviewer. My humbing for giving the Buset it to re potatoes in.  Ithis thing is made with this plastic cons It has secure to eat it sent the bottom had been vacuum, I cansty ligr under excell bread part. Cleans strong it and eand than you have an also helps keep it. It's rerained the for resistasted for your out how cocon 20'm non-vacuum 5 stars easily and use it rugs, and it works fine, evenly nef the pots.  This can be untelved you to sevet. It has reveet hasing to prep by me how long, or hold not a sifting because if it really required 2/months The amazing. It got the sirely

Temp: 0.5

IT is a great model when much more items that when you take ice cream makers in the market in the food product.  Minist a couple of the store and peelers to be of the freezer in the first tool for some of the market and easy to use.  The sharp enough to this one and this is a great quality and this little fun the timer that can take for easy and this is a good product.  I have to replace my old one.  I had to say that it is a the bowl is stainless steel bowl to make sure the best set of the cooker with the holes to make sure if it doesn\'t the bag for meat and installer and it is easy to clean.  The handle is no some of the core out of the small, which is a lot of the blade is the meat of the sides and for the sharp to the floor and the best of the freezer and a bad of the most mark is the blades are the mix in the core, and it is still gets the bowl for my hand back in the rating on the dishwasher and cheese and seem to make your mos

ROMEONDBAZELY............70dBA...........60dBAA.......60dBA..................60ddBA...............15dBABLA.............60dBABABLY.............................................75W.........................7.99606..............................................................6000..................................67WBALY...............................................................69800......70dBAW..........................................................10000070700000..................70dBA...................67070dBA.........70ddBABA)....................676dBA.........00dBA3.............................66dBA2..........................................600dBA................................70600dBA.................770dBA..............50dBA................$1717000..................................................70dBA........6.606......................9170.6.66822.6.600000000dBA....6.660................$70000010d............6.60dBA....................638dBA......56dBA.......69.00dBA................

This products and I was think it is probably through the first one that I like the in the first time to the scoop that is the way the first time I like the tool to a few more than the recipes and the blade is that it is perfect for my pressure cooker for my counter.  I have this to all of the bowl with a little with this product to have to small and the 1ureking stainless steel plastic scraper is a little time.  I have a spoon back potatoes that would have to cook so much so I like the potatoes with this scraper to move the job done in the pain to instruction is thick and the cooker in Chinang the cover is still to be a little noise to soon easily and deners.  I was not even for your hand. The only acrass to stick to replace the instructions in the sink with the fact that the best since I have to pull out a lot of potatoes and it is a bit from the short on the sides of the top and the pressure cooker with the fact that are cooked out a little handle to scrub the handle is that this is a gr

This is my greens and the construction works well.  I find it is always only a great little mixing.  I can start to piece in the freezer for the can opener I think it is a bit of all the core was that it works well.  This is a good product and I like the batteries and was a bit more than making the cord to prep are all the time it works well made.  It's much be a potato mashing new too much as the are need on a few while it would be sure that is nice and was this with this one was a bit of such as the fact it would be a little on the fan into the small size and it was sure it comes and the back in the dishwasher stuff that is not sure it was the best of a handle is worth the motor handle and the rubber handle is line of an ice cream maker in a pressure cooker with this basic holes and easy to clean.  On the batteries, and its good quality and sturdy and it still works great for my been most of the base with this for its from the motor and was a little size for the problem so it works well

Chosen Chunk:

Not sure it was the best of a handle is worth the motor handle and the rubber handle is line of an ice cream maker in a pressure cooker with this basic holes and easy to clean.  On the batteries, and its good quality and sturdy and it still works great


## Technical Notes

None for this project

## Reference

https://stackoverflow.com/questions/12451431/loading-and-parsing-a-json-file-with-multiple-json-objects-in-python
http://jmcauley.ucsd.edu/data/amazon/
