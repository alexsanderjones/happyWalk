# Is Walkability related to Happiness?

For this mini-project, I wanted to take a look and see if there is a relationship between a city's walkability and general happiness of its residents. Kim Dovey and Elek Pafka define walkability as a combination of "density, mix, and access", but in general terms it's the accessibility of sufficient amenities by foot.  
For this project, I used two main packages: pandas and statsmodels. Pandas is used for general dataframe manipulation, and statsmodels was used to perform a significance test on the Least-Squares model produced. To produce a dataframe for a city's general happiness, I used BeautifulSoup and scraped an article from the website https://wallethub.com/edu/happiest-places-to-live/32619. The dataframe containing a city's walkability score is derived from the EPA.  
Some things to note: in the github I do not have the walkability index table because it is simply TOO large to import into github. As such, the link to the "walkability.csv" file in my code can be found below:
https://edg.epa.gov/EPADataCommons/public/OA/EPA_SmartLocationDatabase_V3_Jan_2021_Final.csv

## Limitations  
The walkability table entries are separated by CBSAs, which are defined as "core-based statistical area". This is fine in GEOID and linking with other government data, but doesn't fit well with the data I had. Unfortunately, in the process of trying to merge these two dataframes together, I had to leave out some entries (e.g. Fort Worth got lumped in Dallas, etc.).
Walkability and Happiness are both very subjective measures, so I have reservations in calling this a very scientific process.


Other than that, I hope you enjoy this analysis!