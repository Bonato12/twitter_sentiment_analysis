import requests


bearer_token = 'AAAAAAAAAAAAAAAAAAAAAFY9owEAAAAA5N1wgcpARBFdenlLE0V%2F8NDr6aQ%3D7pzRccH530wX3HRrfESY3VOVFR1oPapfB3mlSJVldWAqyHusVS'

def create_headers(bearer_token):
    return {
        "Authorization": f"Bearer {bearer_token}",
    }

def search_tweets(headers, query):
    url = "https://api.twitter.com/2/tweets/search/recent"
    params = {
        "query": query,
        "max_results": 100,  
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()


headers = create_headers(bearer_token)
query = "#Boca"  
tweets = search_tweets(headers, query)

if 'data' in tweets:
    for tweet in tweets['data']:
        print(f"Tweet: {tweet['text']}")
else:
    print("No se encontraron tweets o hubo un error:", tweets)