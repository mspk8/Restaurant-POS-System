import sqlite3
connection=sqlite3.connect("KababHouseutills.db")
cursor=connection.cursor()

categories=[
    (1,"Signature"),
    (2,"BBQ"),
    (3,"breakfast"),
    (4,"Desserts")
]

coupon_codes={
    ("KHI20",20),
    ("KABABZ",10),
    ("KHIONTOP",50)
}



menu_make=[(1, 's1', 'Chicken Tawa', 30.0), (1, 's2', 'Butter Chicken', 32.0), (1, 's3', 'Achari Handi', 28.0), (1, 's4', 'Peshawari Karhai', 36.0), (2, 'q1', 'Seekh Kabab', 30.0), (2, 'q2', 'Reshmi Kabab', 32.0), (2, 'q3', 'Kabab Fry', 24.0), (2, 'q4', 'Bihari Kabab', 45.0), (3, 'b1', 'Halwa Puri Set', 10.0), (3, 'b2', 'Chana', 6.0), 
(3, 'b3', 'Haleem', 15.0), (3, 'b4', 'Aloo paratha', 4.0), (4, 'd1', 'Kheer', 8.5), (4, 'd2', 'Gulab Jamun (3pcs)', 9.0), (4, 'd3', 'Gajar Ka Halwa', 15.0), (4, 'd4', 'Ras Malai', 10.0)]


# cursor.executemany("INSERT INTO menu_DB(cat_code,code,name,price) VALUES (?,?,?,?)",
#                    menu_make)


# cursor.executemany("INSERT INTO coupon_codes_DB(code,discount) VALUES(?,?)",
#                    coupon_codes)
# cursor.executemany("INSERT INTO MENU_CATEGORIES_DB(cat_code,cat_name) VALUES(?,?)",
#                categories)



connection.commit() 

all_menu=cursor.execute("SELECT* FROM menu_db WHERE cat_code=2")
print(all_menu.fetchall())

