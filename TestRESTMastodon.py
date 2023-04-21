import requests
from mastodon import Mastodon, MastodonNotFoundError, MastodonRatelimitError, StreamListener
import csv, os, time, json

def delete_mastodon_status(status_id, access_token):
    url = "https://mastodon.social/@jionghao/api/v1/statuses/{}".format(status_id)
    headers = {
        "Authorization": "Bearer {}".format(access_token),
    }

    response = requests.delete(url, headers=headers)

    if response.status_code == 200:
        print("Status deleted successfully!")
        print(response.json())
    elif response.status_code == 404:
        print("Status not found. It may have been already deleted or the status ID is incorrect.")
    else:
        print("Error deleting status. HTTP status code: {}".format(response.status_code))
        print(response.text)
# Stream federated timeline for a given hashtag (text search on streaming data is not supported)
def stream_federated_timeline_given_hashtag(access_token):
    URL = "https://theblower.au/api/v1/timelines/tag/{}".format("poverty")
    headers = {
        "Authorization": "Bearer {}".format(access_token),
    }

    response = requests.get(URL, headers=headers)

    if response.status_code == 200:
        print("Get the local timeline successfully!")
        for data in response.json():
            print(data)
    elif response.status_code == 404:
        print("Failed to get local timeline")
    else:
        print("Error get local timeline. HTTP status code: {}".format(response.status_code))
        print(response.text)
# Full-text search can be performed on accounts, statuses (posts), or hashtags(please  note it requires a different endpoint v2)
def full_text_search(access_token):
    URL = "https://theblower.au/api/v2/search?q={}".format("income")
    headers = {
        "Authorization": "Bearer {}".format(access_token),
    }
    
    response = requests.get(URL, headers=headers)

    if response.status_code == 200:
        print("Get the request text successfully!")
        print(response.json())
    elif response.status_code == 404:
        print("Failed to get the request text")
    else:
        print("Error get the request text. HTTP status code: {}".format(response.status_code))
        print(response.text)
        
def streaming_Mastodon_timeline():
    pass
if __name__ == "__main__":
    access_token = "MVXpwFYU7so-i0x6kyltoq-Y7jZW8bm2Nv8yOIklQrc"  
    status_id = "110197044539110917"


    stream_federated_timeline_given_hashtag(access_token)
    #full_text_search(access_token)