from influencer_collection.constants import WEIGHT
from influencer_collection.helpers import get_topTopics


def get_topics(influencer):
    influencer_topics = {}
    final_model = []
    for item in influencer:
        key = item[0]
        weight = item[1][WEIGHT]
        top_topics = get_topTopics(item)
        topics = influencer_topics.get(key, {WEIGHT: weight, "topics": top_topics})
        influencer_topics[key] = topics

    for i in influencer_topics:
        children = []
        top = tuple(influencer_topics[i]["topics"])
        for j in top:
            children.append({"name": j[0], "value": j[1]})
        final_model.append({"name": i, "value": influencer_topics[i][WEIGHT],
                            "children": children})
    return final_model
