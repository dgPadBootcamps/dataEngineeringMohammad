from influencer_collection.constants import WEIGHT


def get_influencers(data):
    influencer = {}
    for item in data:
        if item["User"]["is_Verified"]:
            # if the user is verified fill the list with user name and the engagements total
            key = item["User"]["UserName"]
            weight = item["favorite_count"] + item["retweet_count"] + item["reply_count"]
            influencer_data = influencer.get(key, {"tweets": [], WEIGHT: weight})

            influencer_data["tweets"].append({"text": item["Text"]})
            influencer_data[WEIGHT] = influencer_data[WEIGHT] + weight

            influencer[key] = influencer_data

    top_influencer = list(influencer.items())
    for i in range(0, len(top_influencer) - 1):
        for j in range(i + 1, len(top_influencer)):
            if top_influencer[i][1][WEIGHT] < top_influencer[j][1][WEIGHT]:
                maximum = top_influencer[i]
                top_influencer[i] = top_influencer[j]
                top_influencer[j] = maximum
    influencer = top_influencer[:10]

    return influencer
