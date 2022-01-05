import json
  
register_details = [
    {
        "search_for": "topman",
        "email": "landonorris4@gmail.com",
        "min_price": "abc"
    },
    {
        "search_for": "nike",
        "email": "a.mcpie4@gmail.com",
        "min_price": "70"
    }
]

# Iterating through the json
# list
for i in range(len(register_details)):
    print('Name: ' + register_details[i]['search_for'])
    print('Email: ' + register_details[i]['email'])
    print('Min. Price: ' + register_details[i]['min_price'] + '\n')