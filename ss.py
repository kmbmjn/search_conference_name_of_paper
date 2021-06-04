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

# define search title
search_title_list = [
"Provable defenses against adversarial examples via the convex outer adversarial polytope",
"On detecting adversarial perturbations",
"A closer look at memorization in deep networks",
"Certified defenses against adversarial examples",
"Decision-based adversarial attacks: Reliable attacks against black-box machine learning models",
"Adversarial examples are not bugs, they are features",
"Theoretically principled trade-off between robustness and accuracy",
"Detecting adversarial samples from artifacts",
"Mitigating adversarial effects through randomization",
"Adversarial training methods for semi-supervised text classification",
"Pixeldefend: Leveraging generative models to understand and defend against adversarial examples",
"Distributional smoothing with virtual adversarial training",
"Adversarial attacks on neural network policies",
"Adversarially robust generalization requires more data",
"Feature denoising for improving adversarial robustness",
]

# replace xa0 in search title
search_title_list = [search_title.replace(u'\xa0', u' ') for search_title in search_title_list]
# replace . in search title
search_title_list = [search_title.replace('.', '') for search_title in search_title_list]
# replace ! in search title
search_title_list = [search_title.replace('!', '') for search_title in search_title_list]

# start search
title_result_list = []
venue_result_list = []
for search_title in search_title_list:
    # get search
    title_result, venue_result = search_by_title(search_title)

    # test correspondence
    # replace .
    title_result = title_result.replace('.', '')
    # replace !
    title_result = title_result.replace('!', '')
    if search_title.lower().replace(" ","") != title_result.lower().replace(" ",""):
        print(search_title.lower().replace(" ",""))
        print(title_result.lower().replace(" ",""))

    # venue edit
    if "Computer Vision and Pattern Recognition" in venue_result:
        venue_result = "CVPR"
    elif "International Conference on Computer Vision" in venue_result:
        venue_result = "ICCV"

    title_result_list.append(title_result)
    venue_result_list.append(venue_result)

print(search_title_list)
print(title_result_list)
print("")
for venue in venue_result_list:
    print(venue)


# To Do
# NIPS 2018
# ICLR 2016
