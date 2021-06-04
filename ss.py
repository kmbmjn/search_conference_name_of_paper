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
    venue_result = r["results"][0]["venue"]["text"]

    return title_result, venue_result

search_title_list = [
"Dronet: Learning to fly by driving",
"Attention, learn to solve routing problems!",
"Tell me where to look: Guided attention inference network",
"Deep k-nearest neighbors: Towards confident, interpretable and robust deep learning",
"Adversarial audio synthesis",
"Albumentations: fast and flexible image augmentations",
"Singan: Learning a generative model from a single natural image",
"Basnet: Boundary-aware salient object detection",
"Manifold mixup: Better representations by interpolating hidden states",
]

# replace xa0
search_title_list = [search_title.replace(u'\xa0', u' ') for search_title in search_title_list]
# replace .
search_title_list = [search_title.replace('.', '') for search_title in search_title_list]
# replace !
search_title_list = [search_title.replace('!', '') for search_title in search_title_list]

title_result_list = []
venue_result_list = []
for search_title in search_title_list:
    title_result, venue_result = search_by_title(search_title)

    # replace .
    title_result = title_result.replace('.', '')
    # replace !
    title_result = title_result.replace('!', '')
    if search_title.lower() != title_result.lower():
        print(search_title.lower())
        print(title_result.lower())

    title_result_list.append(title_result)
    venue_result_list.append(venue_result)

print(search_title_list)
print(title_result_list)
for venue in venue_result_list:
    print(venue)


# To Do
# 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition -> CVPR
# 2019 IEEE/CVF International Conference on Computer Vision (ICCV) -> ICCV
# 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) -> CVPR
# NIPS 2018
