import json

from google_cloud.download_objects import download_blob


def read_data():
    # file_path = ["C:/Users/MOHD/Documents/dgPad/dgPad2/data_saving/tweets_lebanon_2021-11-25.json",
    #              "C:/Users/MOHD/Documents/dgPad/dgPad2/data_saving/tweets_lebanon_2021-11-24.json",
    #              "C:/Users/MOHD/Documents/dgPad/dgPad2/data_saving/tweets_lebanon_2021-11-23.json",
    #              "C:/Users/MOHD/Documents/dgPad/dgPad2/data_saving/tweets_lebanon_2021-11-22.json",
    #              "C:/Users/MOHD/Documents/dgPad/dgPad2/data_saving/tweets_lebanon_2021-11-21.json",
    #              "C:/Users/MOHD/Documents/dgPad/dgPad2/data_saving/tweets_lebanon_2021-11-20.json",
    #              "C:/Users/MOHD/Documents/dgPad/dgPad2/data_saving/tweets_lebanon_2021-11-19.json",
    #              ]
    # data = []
    # for i in range(0, len(file_path)):
    #     with open(file_path[i], 'r', encoding="utf8") as full_data:  # get the data from the json file
    #         data = data + json.loads(full_data.read())
    data = download_blob("dgpad-mhmd-test", "tweets-data/tweets_lebanon_2021-11-17.json")
    return json.loads(data)
