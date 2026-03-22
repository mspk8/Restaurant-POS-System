menu={
    "Signature": {
        "s1": {
            "Name": "Chicken Tawa",
            "Price": 30.0
        },
        "s2": {
            "Name": "Butter Chicken",
            "Price": 32.0
        },
        "s3": {
            "Name": "Achari Handi",
            "Price": 28.0
        },
        "s4": {
            "Name": "Peshawari Karhai",
            "Price": 36.0
        }
    },
    "BBQ": {
        "q1": {
            "Name": "Seekh Kabab",
            "Price": 30.0
        },
        "q2": {
            "Name": "Reshmi Kabab",
            "Price": 32.0
        },
        "q3": {
            "Name": "Kabab Fry",
            "Price": 24.0
        },
        "q4": {
            "Name": "Bihari Kabab",
            "Price": 45.0
        }
    },
    "breakfast": {
        "b1": {
            "Name": "Halwa Puri Set",
            "Price": 10.0
        },
        "b2": {
            "Name": "Chana",
            "Price": 6.0
        },
        "b3": {
            "Name": "Haleem",
            "Price": 15.0
        },
        "b4": {
            "Name": "Aloo paratha",
            "Price": 4.0
        }
    },
    "desserts": {
        "d1": {
            "Name": "Kheer",
            "Price": 8.5
        },
        "d2": {
            "Name": "Gulab Jamun (3pcs)",
            "Price": 9.0
        },
        "d3": {
            "Name": "Gajar Ka Halwa",
            "Price": 15.0
        },
        "d4": {
            "Name": "Ras Malai",
            "Price": 10.0
        }
    }
}





menu_catrgories={
    1:"Signature",
    2:"BBQ",
    3:"breakfast",
    4:"Desserts"
}

final=[]
index=1
keys=[1,2,3,4]

for category in menu:
        for code in menu[category]:
            name=menu[category][code]["Name"]
            price=menu[category][code]["Price"]
            new=(index,code,name,price)
            final.append(new)
        index+=1
        


print(final)




done=[(1, 's1', 'Chicken Tawa', 30.0), (1, 's2', 'Butter Chicken', 32.0), (1, 's3', 'Achari Handi', 28.0), (1, 's4', 'Peshawari Karhai', 36.0), (1, 'q1', 'Seekh Kabab', 30.0), (1, 'q2', 'Reshmi Kabab', 32.0), (1, 'q3', 'Kabab Fry', 24.0), (1, 'q4', 'Bihari Kabab', 45.0), (1, 'b1', 'Halwa Puri Set', 10.0), (1, 'b2', 'Chana', 6.0), 
(1, 'b3', 'Haleem', 15.0), (1, 'b4', 'Aloo paratha', 4.0), (1, 'd1', 'Kheer', 8.5), (1, 'd2', 'Gulab Jamun (3pcs)', 9.0), (1, 'd3', 'Gajar Ka Halwa', 15.0), (1, 'd4', 'Ras Malai', 10.0)]

