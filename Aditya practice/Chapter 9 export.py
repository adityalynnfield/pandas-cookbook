import pandas as pd
import sqlite3

con = sqlite3.connect("../data/weather_2012.sqlite")
df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con)
df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con, index_col='id')

weather_df = pd.read_csv('../data/weather_2012.csv')
con = sqlite3.connect("../data/test_db.sqlite")
con.execute("DROP TABLE IF EXISTS weather_2012")
weather_df.to_sql("weather_2012", con)
con = sqlite3.connect("../data/test_db.sqlite")
df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con)

con = sqlite3.connect("../data/test_db.sqlite")
df = pd.read_sql("SELECT * from weather_2012 ORDER BY Weather LIMIT 3", con)

df