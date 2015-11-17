__author__ = 'Gerhard'

import requests
import json


def create_user(username):
    email = "christopher.ott@gmx.net"
    post_data = '{"attributes": [{"label": "email","value": "'+ email +'"},{"label": "user name","value": "'+ username +'"}]}'
    response = requests.post('https://sentinel.apimanagement.hana.ondemand.com:443/api/watchlist_service/rest/users',
                         data=post_data,
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


######## params ########
#ids:    list of Strings
def create_watchlist(user_id, stock_ids):
    post_data = '{"type": "compose","watchlist_name": "reference compose","preferences": ' \
                '{' \
                    '"exchange_id": "1",' \
                    '"transaction_cost": 0.25,' \
                    '"selection_metric": "returns",' \
                    '"strategy_type": "single",' \
                    '"backtesting_duration_in_months": 6,' \
                    '"is_managed": false, ' \
                    '"stocks": ' + str(stock_ids) + \
                    '}' \
                '}'
    response = requests.post('https://sentinel.apimanagement.hana.ondemand.com:443/api/watchlist_service/rest/users/'+ user_id +'/watchlists',
                             data=post_data,
                             allow_redirects=True,
                             headers={'api_key': 'Jds7JaVbE3alY4cVeEwWu2MRhLxWXKsG'})
    response_json = json.loads(response.text)
    print response_json
    watchlist_id = 5 #TODO: response_json["some_label"]
    return watchlist_id


def main():
    #a = create_user("a", "b")
    #b = create_user("c", "b")
    #c = create_user("ar", "b")
    #print a
    #print b
    #print c
    user_id = create_user("bla")
    print user_id
    create_watchlist(user_id, ["12", "13"])

if __name__ == "__main__":
    main()