import os
import asyncio
import requests
import json

API_KEY = os.environ["API_KEY"]

# url = "https://api.themoviedb.org/3/movie/550?api_key="


def get_popular():

    url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en-US&page=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        print("API ERROR")
    return data["results"]


# res = get_popular()
# print(res["results"][0]["original_title"])
# for movie in res["results"]:
#     print(movie["original_title"])
