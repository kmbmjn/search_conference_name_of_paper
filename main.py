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
        "externalContentTypes": [],
    }
    r = requests.post("https://www.semanticscholar.org/api/1/search", json=data).json()

    ## for debugging purpose
    # import pprint
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(r)
    # print(r.keys())
    # print(r["results"][0])

    search_title_out = r["results"][0]["title"]["text"]
    venue_result = r["results"][0]["venue"]["text"]

    return search_title_out, venue_result


# read search title
search_title_in_list = []
f = open("search_title_in_list.txt", "r")
line = f.readline()
search_title_in_list.append(line)
while line:
    line = f.readline()
    search_title_in_list.append(line)
f.close()
search_title_in_list.pop()

# replace \n in search title
search_title_in_list = [search_title_in.replace(u"\n", u"") for search_title_in in search_title_in_list]
# replace xa0 in search title
search_title_in_list = [search_title_in.replace(u"\xa0", u" ") for search_title_in in search_title_in_list]

# replace . in search title
search_title_in_list = [search_title_in.replace(".", "") for search_title_in in search_title_in_list]
# replace ! in search title
search_title_in_list = [search_title_in.replace("!", "") for search_title_in in search_title_in_list]
# replace ? in search title
search_title_in_list = [search_title_in.replace("?", "") for search_title_in in search_title_in_list]
# replace : in search title
search_title_in_list = [search_title_in.replace(":", "") for search_title_in in search_title_in_list]
# replace ’ in search title
search_title_in_list = [search_title_in.replace("’", "'") for search_title_in in search_title_in_list]
# replace - in search title
search_title_in_list = [search_title_in.replace("-", " ") for search_title_in in search_title_in_list]

# start search
search_title_out_list = []
venue_result_list = []
for search_title_in in search_title_in_list:
    # get search
    search_title_out, venue_result = search_by_title(search_title_in)

    # test matching
    # replace .
    search_title_out = search_title_out.replace(".", "")
    # replace !
    search_title_out = search_title_out.replace("!", "")
    # replace ?
    search_title_out = search_title_out.replace("?", "")
    # replace :
    search_title_out = search_title_out.replace(":", "")
    # replace ’
    search_title_out = search_title_out.replace("’", "'")
    # replace -
    search_title_out = search_title_out.replace("-", " ")

    if search_title_in.lower().replace(" ", "") != search_title_out.lower().replace(" ", ""):
        print("Match Error.")
        print(search_title_in.lower().replace(" ", ""))
        print(search_title_out.lower().replace(" ", ""))
        print("")

    # workshop alert
    if "workshop" in venue_result:
        print("workshop alert.")
        print(venue_result)
        print("")
    if "Workshop" in venue_result:
        print("workshop alert.")
        print(venue_result)
        print("")

    # edit venue
    if "Computer Vision and Pattern Recognition Workshop" in venue_result:
        venue_result = "CVPRW"
    elif "CVPR Workshop" in venue_result:
        venue_result = "CVPRW"
    elif "Computer Vision and Pattern Recognition" in venue_result:
        venue_result = "CVPR"
    elif "International Conference on Computer Vision Workshop" in venue_result:
        venue_result = "ICCVW"
    elif "International Conference on Computer Vision" in venue_result:
        venue_result = "ICCV"
    elif venue_result.lower() == "arxiv":
        venue_result = "arXiv"
    elif "Winter Conference on Applications of Computer Vision" in venue_result:
        venue_result = "WACV"
    # ICLR 2016 to ICLR
    elif re.search(r"\d+$", venue_result) is not None:
        venue_result = venue_result[:-5]
    # 2017 IEEE Symposium on Security and Privacy (SP)
    elif re.search(r"^\d", venue_result) is not None:
        venue_result = venue_result[5:]
    elif venue_result == "":
        venue_result = "None"

    search_title_out_list.append(search_title_out)
    venue_result_list.append(venue_result)

print("[Search Title In List]:")
print(search_title_in_list)
print("")
print("[Search Title Out List]:")
print(search_title_out_list)
print("")
print("[Result]:")
for venue in venue_result_list:
    print(venue)
