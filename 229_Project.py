#import dataset
import pandas as pd
pd.options.mode.chained_assignment = None
import numpy as np
from ast import literal_eval
filename = '/Users/LilyLiu/Documents/Stanford/Class/CS229/Project/the-movies-dataset/movies_metadata.csv'
raw_data = open(filename, 'rt')
movie = pd.read_csv(raw_data, delimiter=',')
movie["id"] = list(movie["id"])
movie = pd.DataFrame(movie)



#import user data
filename = '/Users/LilyLiu/Documents/Stanford/Class/CS229/Project/the-movies-dataset/ratings.csv'
raw_data = open(filename, 'rt')
user = pd.read_csv(raw_data, delimiter=',')
user = pd.DataFrame(user)
print(movie.shape)


# print(movie["spoken_languages"].head()[0:3])
# print("user:", user.shape)

#to dictionary
# def to_dict(lst):
#     for ind, item in enumerate(lst):
#         if (pd.notna(item)) and len(item[1:-1]) > 0:
#             # print(lang)
#             lst[ind] = literal_eval(item[1:-1])
#     return list

##convert columns to dictionaries
# movie["genres"] = to_dict(movie["genres"])
# movie["spoken_languages"] = to_dict(movie["spoken_languages"])
# # movie["belongs_to_collection"] = to_dict(movie["belongs_to_collection"])
# movie["production_companies"] = to_dict(movie["production_companies"])
# movie["production_countries"] = to_dict(movie["production_countries"])

##save files to pickle
# movie.to_pickle('/Users/LilyLiu/Documents/Stanford/Class/CS229/Project/the-movies-dataset/test.pkl')
# import pickle
# with open('/Users/LilyLiu/Documents/Stanford/Class/CS229/Project/the-movies-dataset/test.pkl', 'wb') as handle:
#     pickle.dump(movie, handle, protocol=pickle.HIGHEST_PROTOCOL)


# print(movie["spoken_languages"][0])
# print(movie["spoken_languages"][1], type(movie["spoken_languages"][1][0]))

user8 = user[user["userId"]==8]
user8_movieid = list(user8["movieId"])
user8_movie = []
for i in movie["id"]:
    if i in user8_movieid:
        print("i=", i)
        # print("list=", list(movie["id"]) == i)
        user8_movie.append(movie[movie["id"] == i])
print("user8 movie=", user8_movie)
