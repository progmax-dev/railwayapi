


# importing the requests library
import requests

# api-endpoint
URL = "https://www.confirmtkt.com/pnr-status/8713373377"
#8713373377

#8713395024

# sending get request and saving the response as response object
r = requests.get(url = URL)

# extracting data in json format
data = r.text.split('\"')
ind= data.index('PredictionPercentage')


# extracting latitude, longitude and formatted address
# of the first matching location

# printing the output
print(data[ind+2])
