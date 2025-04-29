# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in the Netflix CSV as a DataFrame
df = pd.read_csv("netflix_data.csv")

# Arrange data in columns
df['date_added'] = pd.to_datetime(df['date_added'])
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')
df['duration'] = df['duration'].astype(float)

deceny = df[df['release_year'] >= 1990]
deceny =  deceny[deceny['release_year'] < 2000]
plt.hist(deceny['duration'])
duration = 110

deceny = deceny[deceny['genre'] == 'Action']
short_movie_count = 0
for index, movie in deceny.iterrows():
    if movie['duration'] < 90:
        short_movie_count = short_movie_count + 1
print(short_movie_count)

# Number of genres and type
unique_genres = df['genre'].dropna().unique()
unique_types = df['type'].dropna().unique()
print(f"Total shows : {len(df)}")
print(f"Genres represented ({len(unique_genres)}): {list(unique_genres)}")
print(f"Types represented ({len(unique_types)}): {list(unique_types)}")
print(f"Today, the full duration on platform {sum(df['duration'])} min, it represents {sum(df['duration']) / 60} hours or {sum(df['duration']) / (60 * 24)} days")

# Duration per year
duration_per_year = df.groupby('release_year')['duration'].sum()
plt.figure(figsize=(15, 5))
plt.plot(duration_per_year.index, duration_per_year.values, marker='o')
plt.xlabel("Release date")
plt.ylabel("Total duration (minutes)")
plt.yscale('log')
plt.yticks([100, 500, 1000, 5000, 10000, 50000, 75000], ['100', '500', '1000', '5000', '10000', '50000', '75000'])
plt.xticks([1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2015, 2020, 2025], ['1940', '1950', '1960', '1970', '1980', '1990', '2000', '2010', '2015', '2020', '2025'])
plt.title("Total duration added on the platform per year")
plt.grid()
plt.show()

movies_per_year = df[df['type'] == 'Movie'].groupby('release_year').size().cumsum()  # Sum of films per year
tv_shows_per_year = df[df['type'] == 'TV Show'].groupby('release_year').size().cumsum()  # Sum of TV series per year

combined = pd.DataFrame({'Movies': movies_per_year, 'TV Shows': tv_shows_per_year}).fillna(0)

plt.figure(figsize=(15, 5))
combined.plot(kind='bar', stacked=True, color=['blue', 'red'], edgecolor='black')

plt.xlabel("Release date")
plt.xticks(rotation=45)
plt.ylabel("Number of movies")
plt.title("Movies available per year")
plt.show()

# Films per year : details

movies_per_year = df[df['type'] == 'Movie'].groupby('release_year').size()
tv_shows_per_year = df[df['type'] == 'TV Show'].groupby('release_year').size()
combined = pd.DataFrame({'Movies': movies_per_year, 'TV Shows': tv_shows_per_year}).fillna(0)
plt.figure(figsize=(15, 5))
combined.plot(kind='bar', stacked=True, color=['blue', 'red'], edgecolor='black')
# plt.hist(df[df['type'] == 'Movie']['release_year'].dropna(), bins=30, edgecolor='black', alpha=0.7, label='Movies', color='blue')
# plt.hist(df[df['type'] == 'TV Show']['release_year'].dropna(), bins=11, edgecolor='black', alpha=0.7, label='TV Shows', color='red')

plt.xlabel("Release date")
plt.ylabel("Number of movies")
plt.title("New movies available per year : detailed evolution")
plt.show()

# Genre per year                                                                                        
df_genres = df.explode('genre')
movies_genres = df_genres[df_genres['type'] == 'Movie'].groupby(['release_year', 'genre']).size().unstack(fill_value=0)
tvshows_genres = df_genres[df_genres['type'] == 'TV Show'].groupby(['release_year', 'genre']).size().unstack(fill_value=0)

movies_genres.plot(kind='bar', stacked=True, figsize=(15, 10))
plt.xlabel("Release date")
plt.ylabel("Number of movies")
plt.title("Genre of films added per year")
plt.legend(title="Genres")

tvshows_genres.plot(kind='bar', stacked=True, figsize=(15, 5))
plt.xlabel("Release date")
plt.ylabel("Number of TV series")
plt.title("Genres of TV series added per year")
plt.legend(title="Genres")
plt.show()

def group_year_films(year):
    if year <= 1961:
        return '<1960'
    elif year < 2000:
        return ((year // 20) * 20 ) + 20
    elif year < 2010:
        return ((year // 10) * 10 ) + 10
    elif year <= 2015:
        return ((year // 5) * 5) + 5
    else:
        return ((year // 2) * 2) + 2


def group_year_tv(year):
    if year < 1990:
        return (year // 10) * 10 
    elif year <= 2015:
        return (year // 5) * 5
    else:
        return (year // 2) * 2

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None) 
pd.set_option('display.max_rows', None) 
    
df_movies = df_genres[df_genres['type'] == 'Movie']
print(f"Total number of movies : {len(df_movies)}")
print(f"Average duration of movies : {sum(df_movies['duration']) / len(df_movies)} minutes")
df_movies['year_group'] = df_movies['release_year'].dropna().apply(group_year_films)

df_tv = df_genres[df_genres['type'] == 'TV Show']
print(f"Total number of TV series : {len(df_tv)}\n")
print(f"Average duration of TV series : {sum(df_tv['duration']) / len(df_tv)} minutes")
df_tv['year_group'] = df_tv['release_year'].dropna().apply(group_year_tv)

movies_genres = df_movies.groupby(['year_group', 'genre']).size().unstack(fill_value=0).T
tvshows_genres = df_tv.groupby(['year_group', 'genre']).size().unstack(fill_value=0).T
tvshows_genres['Total'] = tvshows_genres.sum(axis=1)
tvshows_genres.loc['All genres'] = tvshows_genres.sum()

movies_genres = movies_genres.reindex(columns=['<1960'] + [col for col in movies_genres.columns if col != '<1960'] )
movies_genres['Total'] = movies_genres.sum(axis=1)
movies_genres.loc['All genres'] = movies_genres.sum()

print("Genre of films added per year:")
display(movies_genres)

print("\nGenre of TV series added per year:")
display(tvshows_genres)

# Countries
country_counts = df['country'].value_counts().reset_index()
country_counts.columns = ['Country', 'Number of shows']
print(country_counts.head(10))

# Difference between creation year and adding year
netflix_creation_year = 1997
df = df[df['release_year'] >= netflix_creation_year]

# 5 first directors et 10 first actors, TODO : by type and genre
def top_entities(column, top_n=5):
    exploded = df.explode(column)
    return exploded[column].value_counts().head(top_n)

top_directors = top_entities('director', 5)
top_actors = top_entities('cast', 10)
print("Top 5 Directors:")
print(top_directors)
print("\nTop 10 Actors:")
print(top_actors)