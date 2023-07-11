import json

from influencer_collection.influencer import get_influencers
from influencer_collection.dataRead import read_data
from influencer_collection.topics import get_topics


def save_influencerTopics():
    data = read_data()
    influencers = get_influencers(data)
    influencers_topic = get_topics(influencers)
    json_file = open("influencers_topics.json", "w", encoding='utf-8')
    tags = json.dumps(influencers_topic, indent=4, default=str, ensure_ascii=False)
    json_file.write(tags)


save_influencerTopics()
