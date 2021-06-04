import requests

def search_by_title(search_title):
## search_title = "Representation learning with contrastive predictive coding"

    data = {
        "queryString": search_title,
        "page": 1,
        "pageSize": 1,
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

    # import pprint
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(r)
    # print(r.keys())
    # print(r["results"][0])

    title_result = r["results"][0]["title"]["text"]
    # print(title_result)

    venue_result = r["results"][0]["venue"]["text"]
    # print(venue_result)

    return title_result, venue_result

search_title_list = [
"Representation learning with contrastive predictive coding",
"Attention u-net: Learning where to look for the pancreas",
]
title_result_list = []
venue_result_list = []
for search_title in search_title_list:
    title_result, venue_result = search_by_title(search_title)
    title_result_list.append(title_result)
    venue_result_list.append(venue_result)

print(search_title_list)
print(title_result_list)
for venue in venue_result_list:
    print(venue)
