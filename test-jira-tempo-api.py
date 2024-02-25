import requests
import json
import pandas as pd

'''
getting the data through an api-call
'''

# specifying the endpoint
url = "[your-jira-url]/rest/tempo-timesheets/4/worklogs/search"
# creating an authentication object using registered username and password
authentication = ("", "")
# the header parameter contains the desired format of data
headers = {
    'Content-Type': 'application/json'
}
# formulating the query
query = {
 "from": "2023-01-01",
 "to": "2024-12-31",
 "teamId": [29, 5, 27, 17, 8, 18, 32, 31, 16, 14, 20, 33, 30, 2, 22, 15, 28, 21]
 }
jsonQuery = json.dumps(query)
# creating a request object with the above parameters
response = requests.post(
    url,
    data=jsonQuery,
    auth=authentication,
    headers=headers
)
# print(response.status_code)
# getting all the erfasste zeit entries by using the json load-method
reponseAdjusted = json.dumps(json.loads(response.text),
                           sort_keys=True,
                           indent=4,
                           separators=(",", ": "))
# converting the output to a dictionary object
dictWorkLogs = json.loads(reponseAdjusted)

# converting the dictionary to a dataframe - an object power bi can read
regTime = pd.json_normalize(dictWorkLogs)

