# SF_FoodTrucks
Display list of all food trucks currently open in the Bay Area!

## Quick Overview:
This project was run on Python 3.8.5.
### Required Libraries:

#### requests:
```
$ pip install requests
```
#### tabulate:
```
$ pip install tabulate
```
#### num2words:
```
$ pip install num2words
```

## Input:

### Run:
-Navigate to the redfinWS folder
-run program with:
```
$ python foodTruck.py
```

### Console:
The console will prompt the user for input to help navigate from page to page.
```
Type 'Start' to navigate to the 1st page

Type 'Prev' for the ___ page

Type 'Next' for the ___ page

Type 'Last' to navigate to the final page

Type 'Exit' to conclude search
```

## Output:
Alphabetical list of all food trucks open in San Francisco at the time of running the program.
Each page of data will hold a minimum of 10 food trucks and their respective addresses.
### Food Truck Tables:

```
San Francisco Food Trucks open at this time:

╒════╤═════════════════════════════════════════════════════════════════════════╤═════════════════╕
│    │ NAME                                                                    │ ADDRESS         │
╞════╪═════════════════════════════════════════════════════════════════════════╪═════════════════╡
│  1 │ Bay Area Dots, LLC                                                      │ 567 BAY ST      │
├────┼─────────────────────────────────────────────────────────────────────────┼─────────────────┤
│  2 │ Bay Area Dots, LLC                                                      │ 900 BEACH ST    │
├────┼─────────────────────────────────────────────────────────────────────────┼─────────────────┤
│  3 │ Cochinita                                                               │ 490 BRANNAN ST  │
├────┼─────────────────────────────────────────────────────────────────────────┼─────────────────┤
│  4 │ El Tonayense #60                                                        │ 2355 FOLSOM ST  │
├────┼─────────────────────────────────────────────────────────────────────────┼─────────────────┤
│  5 │ Julie's Hot Dogs                                                        │ 2386 MISSION ST │
├────┼─────────────────────────────────────────────────────────────────────────┼─────────────────┤
│  6 │ Leo's Hot Dogs                                                          │ 2301 MISSION ST │
├────┼─────────────────────────────────────────────────────────────────────────┼─────────────────┤
│  7 │ San Francisco Carts & Concessions, Inc. DBA Stanley's Steamers Hot Dogs │ 345 STOCKTON ST │
├────┼─────────────────────────────────────────────────────────────────────────┼─────────────────┤
│  8 │ San Francisco Carts & Concessions, Inc. DBA Stanley's Steamers Hot Dogs │ 100 GEARY ST    │
├────┼─────────────────────────────────────────────────────────────────────────┼─────────────────┤
│  9 │ San Francisco Carts & Concessions, Inc. DBA Stanley's Steamers Hot Dogs │ 251 GEARY ST    │
├────┼─────────────────────────────────────────────────────────────────────────┼─────────────────┤
│ 10 │ San Francisco Carts & Concessions, Inc. DBA Stanley's Steamers Hot Dogs │ 233 GEARY ST    │
╘════╧═════════════════════════════════════════════════════════════════════════╧═════════════════╛

Type 'Next' for the 2nd page


Type 'Last' to navigate to the final page


Type 'Exit' to conclude search

>>
```



## Tests:
Work Sample requested that testing be left out of project.

## Tips and tricks:
You can change the information that will be displayed on the Food Truck tables by assigning `true` to any `DATA` field in params.json

```json
    "Data": {
        "dayorder": false,
        "dayofweekstr": false,
        "starttime": false,
        "endtime": false,
        "permit": false,
        "location": true,
        "locationdesc": false,
        "optionaltext": false,
        "locationid": false,
        "start24": false,
        "end24": false,
        "cnn": false,
        "addr_date_create": false,
        "addr_date_modified": false,
        "block": false,
        "lot": false,
        "coldtruck": false,
        "applicant": true,
        "x": false,
        "y": false,
        "latitude": false,
        "longitude": false,
        "location_2": false
    }
```# SF_FoodTrucks
