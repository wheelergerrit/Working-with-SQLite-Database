#Growth.py is a script to read the facts table into Pandas, and then
#compute the projected population for each country in 2050


import math

import pandas as pd

import sqlite3



conn = sqlite3.connect("factbook.db")

query = "select * from facts;"


facts = pd.read_sql_query(query, conn)

facts = facts.dropna(axis=0)



def final_pop(growth_rate, init_pop):

	years = 35

	return init_pop*(math.e**((growth_rate/100) * years))



facts["population_2050"] = facts.apply(lambda x: final_pop(x["population_growth"], x["population"]), axis=1)

facts = facts.sort_values(by=("population_2050"), axis=0, ascending=False)


top_ten = facts[["name","population_2050"]]

print(top_ten[:10])