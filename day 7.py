properties = {
    "data": {
        "profiles":[
            {
                "name" : "Bikki",
                "rank" : 1,
                "contact":["9857029085","9860729085"],
            },
            {
                "name":"Saurabh",
                "rank": 2,
                "contact":["9846199","9854519"],
            },
        ]
    },
    "total_count": 2,
}

profiles = properties.get("data").get("profiles")
for profile in profiles:
    print("**********************")
    print(f"Name :{profile.get('name')}")
    print(f"Rank : {profile.get('rank')}")
    for idx, contact in enumerate(profile.get("contact"),1):
        print(f"Comtact {idx}: {contact}")
