import requests
import re

def search_by_title(search_title_in_list):
    ## search_title_in_list = "Representation learning with contrastive predictive coding"

    data = {
        "queryString": search_title_in_list,
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

    search_title_out = r["results"][0]["title"]["text"]
    venue_result = r["results"][0]["venue"]["text"]

    return search_title_out, venue_result

# define search title
search_title_in_list = [
"CullNet: Calibrated and Pose Aware Confidence Scores for Object Pose Estimation, PDF"
]

# replace xa0 in search title
search_title_in_list = [search_title_in.replace(u'\xa0', u' ') for search_title_in in search_title_in_list]
# replace . in search title
search_title_in_list = [search_title_in.replace('.', '') for search_title_in in search_title_in_list]
# replace ! in search title
search_title_in_list = [search_title_in.replace('!', '') for search_title_in in search_title_in_list]
# replace ’ in search title
search_title_in_list = [search_title_in.replace('’', "'") for search_title_in in search_title_in_list]

# start search
search_title_out_list = []
venue_result_list = []
for search_title_in in search_title_in_list:
    # get search
    search_title_out, venue_result = search_by_title(search_title_in)

    # test correspondence
    # replace .
    search_title_out = search_title_out.replace('.', '')
    # replace !
    search_title_out = search_title_out.replace('!', '')
    # replace ’
    search_title_out = search_title_out.replace("’", "'")

    if search_title_in.lower().replace(" ","") != search_title_out.lower().replace(" ",""):
        print(search_title_in.lower().replace(" ",""))
        print(search_title_out.lower().replace(" ",""))

    # venue edit
    if "Computer Vision and Pattern Recognition Workshop" in venue_result:
        venue_result = "CVPRW"
    elif "Computer Vision and Pattern Recognition" in venue_result:
        venue_result = "CVPR"
    elif "International Conference on Computer Vision Workshop" in venue_result:
        venue_result = "ICCVW"
    elif "International Conference on Computer Vision" in venue_result:
        venue_result = "ICCV"
    elif venue_result.lower() == "arxiv":
        venue_result = "arXiv"
    # ICLR 2016 to ICLR
    elif re.search(r'\d+$', venue_result) is not None:
        venue_result = venue_result[:-5]
    # 2017 IEEE Symposium on Security and Privacy (SP)
    elif re.search(r'^\d', venue_result) is not None:
        venue_result = venue_result[5:]

    search_title_out_list.append(search_title_out)
    venue_result_list.append(venue_result)

print("[Search Title in List]:")
print(search_title_in_list)
print("")
print("[Search Title out List]:")
print(search_title_out_list)
print("")
print("[Result]:")
for venue in venue_result_list:
    print(venue)
