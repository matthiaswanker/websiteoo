__author__ = 'Gerhard'

import requests
import json
import random

######## params ########
#username:        unique
######## return ########
#ID of the new user
########################
def create_user(username):
    email = username +"@"+ username + ".de"
    post_data = '{"attributes": [{"label": "email","value": "'+ email +'"},{"label": "user name","value": "'+ username +'"}]}'
    response = requests.post('https://sentinel.apimanagement.hana.ondemand.com:443/api/watchlist_service/rest/users',
                         data=post_data,
                         allow_redirects=True,
                         headers={'api_key': 'Jds7JaVbE3alY4cVeEwWu2MRhLxWXKsG'})
    assert response.status_code < 300, response.text
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
######## return ########
#ID of the new watchlist
########################
def create_watchlist(user_id, stock_ids):
    stock_ids_formatted = [str(x) for x in stock_ids]
    post_data = '{"type": "compose","watchlist_name": '+ user_id +',"preferences": ' \
                '{' \
                    '"exchange_id": "1",' \
                    '"transaction_cost": 0.25,' \
                    '"selection_metric": "returns",' \
                    '"strategy_type": "all",' \
                    '"backtesting_duration_in_months": 2,' \
                    '"is_managed": true, ' \
                    '"time_slice": "month", ' \
                    '"time_slices_per_period": 3, ' \
                    '"historical_periods": 3, ' \
                    '"lower_bound": 0.0, ' \
                    '"upper_bound": 1.0, ' \
                    '"stocks": ' + str(stock_ids_formatted) + \
                    '}' \
                '}'
    response = requests.post('https://sentinel.apimanagement.hana.ondemand.com:443/api/watchlist_service/rest/users/'+ user_id +'/watchlists',
                             data=post_data,
                             allow_redirects=True,
                             headers={'api_key': 'Jds7JaVbE3alY4cVeEwWu2MRhLxWXKsG'})
    assert response.status_code < 300, str(stock_ids[0])
    response_json = json.loads(response.text)
    watchlist_url = response_json["data"]["location"]
    index = watchlist_url.find("rest/watchlists")+16
    watchlist_id=watchlist_url[index:]
    return watchlist_id


def optimize_watchlist(watchlist_id):
    response = requests.get('https://sentinel.apimanagement.hana.ondemand.com:443/api/po_service/rest/historical?watchlist='+ watchlist_id +'&end_date=today&context=true',
                             allow_redirects=True,
                             headers={'api_key': 'Jds7JaVbE3alY4cVeEwWu2MRhLxWXKsG'})
    assert response.status_code < 300
    response_json = json.loads(response.text)
    allocations = [(x["stock_id"],x["daily_details"][-1]["allocation"]) for x in response_json["data"]["items"][0]["performance_details"]]
    #return: all weights and last month's earnings (to be used as estimated earnings for the future)
    return (allocations, response_json["data"]["items"][0]["last_earnings"])

def main():
    random.seed()
    user_id = create_user(str(random.randint(0, 1000)))
    watchlist_id = create_watchlist(user_id, ["3", "5", "1", "37", "2", "38", "27", "28"])
    print watchlist_id
    optimize_watchlist(watchlist_id)


if __name__ == "__main__":
    main()