#!/usr/bin/env python

###
# Make sure to install requests before running:
# > pip install requests
# Documentation for the requests library can be found here: http://docs.python-requests.org/en/master/
try: 
    import requests
    from datetime import datetime
    # import jsbeautifier
    import json
    from tabulate import tabulate
    from num2words import num2words
    import math
except ModuleNotFoundError as e:
    print("-Error- Failed to import prerequisite {}. Please install prior to running this script.".format(e.name))
    exit(1)

#globals:
URL = "http://data.sfgov.org/resource/bbb8-hzi6.json?"
APP_TOKEN = "6aY2UA87Pevkb7F5WhWUdO9hW"
START = True

PARAMS = {
    "$$app_token": APP_TOKEN,
    "$limit": 10,
    "$offset": 0
}#'$offset' is accessed frequently for navigating and tracking pages

#uses specified json file to determine what information to request
def pull_params(params = "docs/params.json"):
    sort = []
    with open(params) as json_file:
        data = json.load(json_file)
    
    #determines how the data sould be arranged
    for key, value in data["SORT"].items():
        sort = (key, value)

    #filters out all fields designated as false in the JSON
    data_list = [key for key, value in data["Data"].items() if value]
    data_list.insert(0, data_list.pop(data_list.index(sort[0])))
    
    #renames any fields specified in the JSON
    for key, value in data["RENAME"].items():
        if key in data_list:
            data_list[data_list.index(key)] += " AS " + value
    return data_list, sort


#determines the fields and order that will be displayed 
def pick_data():
    data_list, sort = pull_params()
    order = "$order= " + " ".join(sort)
    columns = "$select=" + ",".join(data_list)
    query = "&".join([order, columns])
    return query


#filters out food truck that are closed during out query
def time_window(visit_time):

    #filter out anywhere not open today
    today = "dayofweekstr=" + visit_time.strftime("%A")

    #filter out anywhere not currently open
    current_time = visit_time.strftime("%H:%M")
    time_range = "$where=start24 < \'" + current_time + "\' AND end24 > \'" + current_time + "\'"

    return "&".join([time_range, today])


#combines the URL with the pick_data and time_window filters 
def query_filter(url):
    filters = [pick_data(), time_window(datetime.now())]

    return url + "&".join(filters)

#UNUSED
#Store requested data in a JSON file
# def create_JSON(data, file = "truck_query.json"):
#     options = jsbeautifier.default_options()
#     options.indent_size = 2
#     z = jsbeautifier.beautify(json.dumps(data), options)
#     z.replace("\\n", " ")
#     with open(file, "w") as f:
#             f.write(z)


#prompts user to transition to an alternative page of data
def next_page(trucks):
    #offers navigation to previous pages once passed the 1st page
    if PARAMS["$offset"] >= PARAMS["$limit"]:
        print("\nType \'Start\' to navigate to the 1st page\n")
        
        print("\nType \'Prev\' for the " + num2words(PARAMS["$offset"]//10, to='ordinal_num') + " page\n")
    else:
        print("San Francisco Food Trucks open at this time:\n")

    #offers navigation to subsequent pages up until the final page
    if len(trucks) >= PARAMS["$limit"]:
        print("\nType \'Next\' for the " + num2words(PARAMS["$offset"]//10 + 2, to='ordinal_num') + " page\n")
        
        print("\nType \'Last\' to navigate to the final page\n")
    else:
        print("\nEnd of list. No more Food Trucks open at this time.\n")

    #always offer an Exit option
    print("\nType \'Exit\' to conclude search\n")
    
    resp = input(">>")
    return process_input(resp, trucks)

#determines the appropriate response for each user input
def process_input(resp, trucks):
    if resp.lower() == "next" and len(trucks) >= PARAMS["$limit"]:
        PARAMS["$offset"] += 10
    
    elif resp.lower() == "start":
        PARAMS["$offset"] = 0
    
    elif resp.lower() == "prev" and PARAMS["$offset"] >= PARAMS["$limit"]:
        PARAMS["$offset"] -= 10
    
    elif resp.lower() == "last":
        while len(trucks) >= PARAMS["$limit"]:
            process_input("next", trucks)
            trucks = make_request().json()
    
    elif resp.lower() == "exit":
        return True
    
    else:
        print("\nINVALID COMMAND. Please try again")
        next_page(trucks)
    return False

#formats and prints the food truck data
def format_data(trucks):
    i = PARAMS["$offset"] + 1
    n = PARAMS["$offset"] + len(trucks) + 1
    if(i < n):
        print(tabulate(trucks, headers='keys', showindex=range(i, n), tablefmt='fancy_grid'))
    else:
        print("Not enough trucks are open to put any on this page!")
        print("Please use the navigation tools to find what you're looking for!")

#applies filter methods to the url, makes a request, and returns the response
def make_request():
    global URL, START
    if START:
        START = False
        URL = query_filter(URL)
    return requests.get(URL, PARAMS)
    

#drives the program and 
def display_query():
    data = make_request()
    if not data.ok:
        print('HTTP', data.status_code)
        print("Error retrieving data")
    else:
        stop = False
        while not stop:
            trucks = data.json()
            format_data(trucks)
            stop = next_page(trucks)
            data = make_request()

#Run program:
display_query()
#Print URL used:
print("URL used:", URL)