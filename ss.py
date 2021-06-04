import requests
import pprint
pp = pprint.PrettyPrinter(indent=4)

data = {
    ## "queryString": "machine learning",
    "queryString": "Darts: Differentiable architecture search",
    "page": 1,
    "pageSize": 10,
    "sort": "relevance",
    "authors": [],
    "coAuthors": [],
    "venues": [],
    "yearFilter": None,
    "requireViewablePdf": False,
    "publicationTypes": [],
    "externalContentTypes": []
}
r = requests.post(
    'https://www.semanticscholar.org/api/1/search', json=data).json()

pp.pprint(r)
