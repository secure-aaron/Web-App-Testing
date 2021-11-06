import requests
from bs4 import BeautifulSoup

'''
After looking at the specified url using the wayback machine on specific dates, its safe to assube 20-80 are good threshholds to buy and sell respectively.
'''
FEAR_AND_GREED_URL = "https://money.cnn.com/data/fear-and-greed/" # Devlare final variable for the URL
FEAR_AND_GREED_PHRASE = "Fear &amp; Greed Now: " # data in the html data to look for.
FEAR_THRESHOLD = 20
GREED_THRESHOLD = 80
INSTRUMENT_TO_BUY = "QQQ" # not used yet since I have not imported the robinhood project to this application

r = requests.get(FEAR_AND_GREED_URL) # request the data from the url and assign it to r
html = r.content # Assign the retrieved data to html
soup = BeautifulSoup(html) # throw the retrieved html data to beautifulsoup to parse it



div = soup.find_all(id="needleChart") # Parse the retrieved data for the the div with the id of needleChart and assign it to div

div = str(div[0]) # assign the data to the first element in the array and cast it to a string.

print(div)

position = div.find(FEAR_AND_GREED_PHRASE) # find the position of the specified phrase in the retrieved div

print(position) # return the position, and that is result is 165 in this case



position = position + len(FEAR_AND_GREED_PHRASE) # reassign the position value to itself + the length of the specified string 
                                                 # so that it will be close to the required number

print(position) # print the new position

print(div[position:position+3]) # print the data ni the div with that new position + 3 more places for the required number.

current_fear_and_greed_index = int(div[position:position+3].strip()) # strip any weird spaces in the retrieved value, cast it to an int, and assign it to a variable.


print(current_fear_and_greed_index) # print the value
print(type(current_fear_and_greed_index)) # return the value's data type

others_are_greedy = current_fear_and_greed_index >= GREED_THRESHOLD
orthers_are_fearful = current_fear_and_greed_index <= FEAR_THRESHOLD


if others_are_greedy:
    # sell sell sell!
    pass

if orthers_are_fearful:
    # buy buy buy!
    pass








