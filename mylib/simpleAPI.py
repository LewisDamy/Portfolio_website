import requests

api_url = "https://jsonplaceholder.typicode.com/todos"

#################### GET Method ####################
# response = requests.get(api_url)
#
# # print(response.json())
# # print(response.status_code)
# # print(response.headers['Content-Type'])


#################### POST Method ####################
# todo = {
#     "userId" : 1,
#     "title": "Buy milk",
#     "completed" : False
# }
# response = requests.post(api_url, json=todo)
# print(response.json())
# print(response.status_code)

# ########    IMDB CODE    ########
# import imdb
# ia = imdb.IMDb()
# code = "1"
# movie = ia.get_movie(code)
# print(movie["title"])
# @app.get("/movie/{item_id}")
# def search_movie(item_id: int):
#     movie = ia.get_movie(item_id)
#     return {"movie_id": item_id, "movie": movie["title"]}


