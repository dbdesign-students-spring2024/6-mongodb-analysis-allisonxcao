# AirBnB MongoDB Analysis

## Part 1: Data
The data selected is Air BnB listings from Albany. New York. 

| id     | listing_url                            | name                                              | description                                       |
|--------|----------------------------------------|---------------------------------------------------|---------------------------------------------------|
| 1489424| https://www.airbnb.com/rooms/1489424   | Welcoming, easygoing, comfy bed, entire level     | Queen size bed, extra comfy mattress, ...         |
| 2992450| https://www.airbnb.com/rooms/2992450   | Luxury 2 bedroom apartment                        | The apartment is located in a quiet neighborho... |
| 3820211| https://www.airbnb.com/rooms/3820211   | Restored Precinct in Center Sq. w/Parking         | Cozy, cool little 1BR Apt in the heart Albany'... |
| 5651579| https://www.airbnb.com/rooms/5651579   | Large studio apt by Capital Center & ESP@         | Spacious studio with hardwood floors, fully eq... |
| 6623339| https://www.airbnb.com/rooms/6623339   | Center Sq. Loft in Converted Precinct w/ Parking  | Large renovated 1 bedroom apartment in convert... |
| 7563949| https://www.airbnb.com/rooms/7563949   | Rest or work in peace | Garden | Wifi | Kitchen   | This sunlit, street-facing one bedroom is a pe... |

I chose to scrub the data by deleting any columns that had blanks and also really long rows that are not as necessary for quanitative data analysis such as descriptions or host about. 

## Part 2: Data Analysis
1. show exactly two documents from the listings collection in any order.
'''
db.listings.find().limit(2)
'''
Outputs:
'''
    [
  {
    "name": "Welcoming, easygoing, comfy bed, entire level",
    "price": "$50.00",
    "neighbourhood": "Albany, New York, United States",
    "host_id": 5294164,
    "host_name": "Efrat",
    "host_is_superhost": "f",
    "beds": 1,
    "review_scores_rating": 4.75
  },
  {
    "name": "Luxury 2 bedroom apartment",
    "price": "$70.00",
    "neighbourhood": null,
    "host_id": 4621559,
    "host_name": "Kenneth",
    "host_is_superhost": "f",
    "beds": 2,
    "review_scores_rating": 3.56
  }
]
'''

2. show exactly 10 documents in any order, but "prettyprint" in easier to read format, using the pretty() function.
'''
db.listings.find().limit(10).pretty()
'''
Output:
'''

  {
    "_id": 1,
    "name": "Welcoming, easygoing, comfy bed, entire level",
    "price": "$50.00",
    "neighbourhood": "Albany, New York, United States",
    "host_id": 5294164,
    "host_name": "Efrat",
    "host_is_superhost": "f",
    "beds": 1,
    "review_scores_rating": 4.75
  },
  {
    "_id": 2,
    "name": "Luxury 2 bedroom apartment",
    "price": "$70.00",
    "neighbourhood": null,
    "host_id": 4621559,
    "host_name": "Kenneth",
    "host_is_superhost": "f",
    "beds": 2,
    "review_scores_rating": 3.56
  },
  {
    "_id": 3,
    "name": "Restored Precinct in Center Sq. w/Parking",
    "price": "$125.00",
    "neighbourhood": "Albany, New York, United States",
    "host_id": 19648678,
    "host_name": "Terra",
    "host_is_superhost": "f",
    "beds": 4,
    "review_scores_rating": 4.74
  }
'''
3. choose two hosts (by reffering to their host_id values) who are superhosts (available in the host_is_superhost field), and show all of the listings offered by both of the two hosts

'''
db.listings.find({host_id: {$in: [host_id1, host_id2]}, host_is_superhost: 't'}, {name: 1, price: 1, neighbourhood: 1, host_name: 1, host_is_superhost: 1})
'''
Output:
'''
    [
  {"name": "Charming 1BR State Capitol, downtwn", "price": "$85.00", "neighbourhood": "Albany, New York, United States", "host_name": "Robert", "host_is_superhost": "t"},
  {"/Fire Place Bungalow\\ 1917 SUNY Eagle 6Beds 2Bath": "$243.00", "neighbourhood": "Albany, New York, United States", "host_name": "Peter", "host_is_superhost": "t"},
  {"/Miller Colonial\\ 1946 SUNY Eagle Hill 5Bed 2Bath": "$333.00", "neighbourhood": "Albany, New York, United States", "host_name": "Peter", "host_is_superhost": "t"}
]
'''

4. Find all the unique host_name values

'''
db.listings.distinct('host_name')
'''
Output:
'''
{
  "_id": null,
  "unique_host_names": [
    "Efrat",
    "Kenneth",
    "Terra",
 ]
}
'''

5. find all of the places that have more than 2 beds in a neighborhood of your choice (referred to as either the neighborhood or neighbourhood_group_cleansed fields in the data file), ordered by review_scores_rating descending
'''
db.listings.find({neighbourhood: 'NeighborhoodName', beds: {$gt: 2}, review_scores_rating: {$ne: null}}).sort({review_scores_rating: -1})
'''
Output:
'''
[
  {"name": "Smoking allowed on front porch! Massage recliner!", "beds": 4, "review_scores_rating": 5.0, "price": "$150.00"},
  {"name": "Albany 3 Bedroom Apt. Sleeps 6", "beds": 4, "review_scores_rating": 5.0, "price": "$110.00"},
  {"name": "Comfy private room in a Residential House, Albany", "beds": 3, "review_scores_rating": 5.0, "price": "$45.00"}
]
'''

6. show the number of listings per host
'''
db.listings.aggregate([{$group: {_id: '$host_id', count: {$sum: 1}}}])
'''
Output:
'''
[
  {"host_name": "Aaron", "count": 1},
  {"host_name": "Abba", "count": 6},
  {"host_name": "Adam", "count": 2}
]
'''

7. Find top 3 hosts with highest average review score
''' 
db.listings.aggregate([{$group: {_id: "$host_name", averageRating: {$avg: "$review_scores_rating"}}}, {$match: {averageRating: {$gte: 4}}}, {$sort: {averageRating: -1}}, {$limit: 3}])
'''

Output:
'''
[
  {
    "host_name": "Ahmad",
    "averageRating": 5.0
  },
  {
    "host_name": "Amar",
    "averageRating": 5.0
  },
  {
    "host_name": "Andrew",
    "averageRating": 5.0
  }
]
'''
I selected a new field to find because neighborhood was split between Albany and N/A. 





