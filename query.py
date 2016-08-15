#This program executes a SQLite query to select the 10 countries 
#with the
#least population from the facts table, and then prints 
#the results 


import sqlite3



conn = sqlite3.connect("factbook.db")

query = "select name from facts order by population asc;"

first_ten = conn.cursor().execute(query).fetchmany(10)

print(first_ten)