import pandas as pd

xls = pd.ExcelFile('imdb.xlsx')#this is entire workbook

df = xls.parse('imdb')#these are seperate sheets

df_directors = xls.parse('directors')

df_countries = xls.parse('countries')

#1)merge all data into one data frame
df=pd.merge(left=df,right=df_directors,how='inner',left_on='director_id',right_on='id')
df=pd.merge(left=df,right=df_countries,how='inner',left_on='country_id',right_on='id')

#drop certain columns and check size
df=df.drop(['id_x','id_y'],axis=1)
#print(df.shape)

#2)clean the data remove the last unknown char from title
df["movie_title"]=df['movie_title'].str.replace('Ê',"")
test=df['movie_title']

#3)get the directors with the most movies
most_dir=df['director_name'].value_counts()
#print(most_dir)
most_dir=most_dir[:1]
#print(most_dir)

#4)check for empty columns
empty=df.isna().sum()
#print(empty)

#5)save nolans all movies in a variable
nolan=df['director_name'].str.contains('Nolan')
nolan_data=df[nolan][['movie_title','imdb_score']]
#print(nolan_data)

#6)what is the avergae rating of nolans movies
nolan_mean=df[nolan]['imdb_score'].mean()
#print(nolan_mean)

#7)select the non-usa movies made after 1960 by Hayao Miyazaki.
c_id=df['country_id']!=1
t_id=df['title_year']>1960
d_id=df['director_name'].str.contains('Miyazaki')
miyazaki=df[c_id & t_id & d_id]
#print(miyazaki)

#8)describe the basic statistics
desc=df.describe()
#print(desc)

#9)which was the year that produced the most movies ?
max_prod=df['title_year'].value_counts()
print(max_prod.head(1))