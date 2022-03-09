# nesting dictionary in a disctionary
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

# travel_log = {
    # "France": ["Partis", "Lille", "Dijon"],
    # "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }
# travel_log["Netherlands"] = ["Utrecht", "Steenwijk", "Amsterdam", "Maastricht", "Groningen"] 

# add new log
def add_new_country(country, visits, cities):
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities": cities,
    })

# print all
def showLogs():
    for log in travel_log:
        print(log)  

showLogs()
add_new_country("Netherlands", 10,["Utrecht", "Steenwijk", "Amsterdam", "Maastricht", "Groningen"] )    

showLogs()