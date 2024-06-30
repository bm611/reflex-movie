import os
import asyncio
import requests
import json
from typing import List, Dict

API_KEY = os.environ["API_KEY"]


def get_popular():
    data = {}
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en-US&page=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        print("API ERROR")
    return data["results"]


def get_movie_details(movie_id: str):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    data = {}
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        print("API ERROR")
    return data


def get_search_results(query: str) -> List[Dict[str, str]]:
    data = {}
    url = f"https://api.themoviedb.org/3/search/movie?query={query}&api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        print("API ERROR")
    return data["results"]
