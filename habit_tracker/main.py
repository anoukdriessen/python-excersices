import requests
from datetime import datetime


GRAPH_TIMEMANAGEMENT = "timemanagement"
GRAPHS = [GRAPH_TIMEMANAGEMENT]

# create a profile
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url= pixela_endpoint, json=user_params)
# print(response.text)

# create a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "timemanagement",
    "name": "4 dingen Vandaag",
    "unit": "dingen",
    "type": "int",
    "color": "sora",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
change_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/timemanagement"
change_graph_values = {
    "name": "Timemanagement Commitments",
    "unit": "Commitment",
}
# response = requests.put(url=change_graph_endpoint, json=change_graph_values, headers=headers)
# print(response.text)

today = datetime.now()
# print(today.strftime("%Y%m%d"))

# add to graph
timemanegement_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_TIMEMANAGEMENT}"
pixel_data = {
    "date": "20220330",
    "quantity": "20",
}
response = requests.post(url=timemanegement_endpoint, json=pixel_data, headers=headers)
print(response.text)