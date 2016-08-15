#This script uses SQL and Python to compute the ratio of how much 
#land area countries claim as their territory versus how much water 
#area they claim


import sqlite3



conn = sqlite3.connect("factbook.db")

cursor = conn.cursor()



total_area_land = cursor.execute("select sum(area_land) from facts where area_land != '';").fetchone()[0]

total_area_water = cursor.execute("select sum(area_water) from facts where area_water != '';").fetchone()[0]



land_water_ratio = total_area_land/total_area_water

print(land_water_ratio)
