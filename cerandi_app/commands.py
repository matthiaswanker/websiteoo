__author__ = 'Gerhard'

import requests
import json


def create_user():
    response = requests.post('https://sentinel.apimanagement.hana.ondemand.com:443/api/watchlist_service/rest/users',
                         data={"username": "abcd"},
                         allow_redirects=True,
                         headers={'api_key': 'Jds7JaVbE3alY4cVeEwWu2MRhLxWXKsG'})
    assert response.status_code < 300
    user_link = json.loads(response.text)["data"]["location"]
    return user_link[user_link.find("users")+6:]


def delete_user(user_id):
    response = requests.delete('https://sentinel.apimanagement.hana.ondemand.com:443/api/watchlist_service/rest/users/'+user_id,
                               headers={'api_key': 'Jds7JaVbE3alY4cVeEwWu2MRhLxWXKsG'})
    assert response.status_code < 300 or response.status_code == 404, response.text


def get_stock_summary(stock_id):
    #TODO
    response = requests.get('https://sentinel.apimanagement.hana.ondemand.com:443/api/watchlist_service/rest/users',
                            headers={'api_key': 'Jds7JaVbE3alY4cVeEwWu2MRhLxWXKsG'})
    pass


def get_stock_facts(stock_id):
    response = requests.get('https://sentinel.apimanagement.hana.ondemand.com:443/api/text_analytics_service/rest/topics?exchange=1&stock='+stock_id,
                            headers={'api_key': 'Jds7JaVbE3alY4cVeEwWu2MRhLxWXKsG'})
    if (response.status_code >= 300):
        return []
    else:
        stock_topics_full_list = json.loads(response.text)["data"]["items"]
        stock_topics = [x["label"] for x in stock_topics_full_list]
        return stock_topics


def add_watchlist():
    response = requests.post('https://sentinel.apimanagement.hana.ondemand.com:443/api/watchlist_service/rest/users/564A5B8DF5F2C576E1000000AC12017B/watchlists',
                             allow_redirects=True,
                             headers={'api_key': 'Jds7JaVbE3alY4cVeEwWu2MRhLxWXKsG'})
    response_json = json.loads(response.text)
    watchlist_id = 5 #TODO: response_json["some_label"]
    return watchlist_id


def main():
    get_stock_facts("26")

if __name__ == "__main__":
    main()