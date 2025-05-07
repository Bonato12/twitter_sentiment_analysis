import requests
import pandas as pd
from preprocessing_dataset import preprocessing_dataset_response


bearer_token = 'AAAAAAAAAAAAAAAAAAAAAFY9owEAAAAA5N1wgcpARBFdenlLE0V%2F8NDr6aQ%3D7pzRccH530wX3HRrfESY3VOVFR1oPapfB3mlSJVldWAqyHusVS'

def create_headers(bearer_token):
    return {
        "Authorization": f"Bearer {bearer_token}",
    }

def get_tweet_by_id(headers, tweet_ids):
    url = "https://api.twitter.com/2/tweets"
    params = {
        "ids": ",".join(tweet_ids),  # Lista de IDs separados por coma
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

# Ejemplo de IDs de tweets para buscar
tweet_ids = ["1877489261898838098","1877437940395106661","1877522314452926655","1877523839967535119,1877404176298230164,1877411360897737055","1877426476338835904","1877352477546172486","1877464749333520387","1877180543739011563","1877047045648732577","1877468421194924185","1877426511667470640","1877558976247730625","1877558622961463554","1876855047306305783","1877558376076378365","1877558264377856050","1877554724712402972","1877556014783820237","1877560977442382045","1877560843337949286","1877560718511210596","1877560277132038221","1877559676692292003","1877558369864613984","1877556107494785191","1877555146009239660","1877554705942880475","1877551812011765996","1876009043409719659","1875744502176215343","1876118331197133211","1847348893404553472","1847381873309454414","1847349513729773570","1876626448695337216","1874247421682913450","1875357567893090694","1673693414561292297","1877366046652268941","1844521560821858451","1845591241783959745","1847792878707159355","1870452489478410584","1874988855482552397","1832193532607475816","1877053031381946774","1876037422636749133","1851676201552912445","1825268456410775720","1874821196279103818","1875663501345038746","1876998620748108193","1809986047574417521","1874214730220642741","1780424498497396795","1765761742490001842","1808545556261679337","1840108829872402632","1838024999543697442","1876758578737930527","1876797468572319796","1876754715347767630","1877730479392117129","1877680858384957940","1877691968098033976","1852198654947242050","1877650978553352208","1865179407045840972","1876724909348466916","1837992391707443625","1875004594436350034", "1876191593604251999","1877015748440182804","1877824111306584239" ,"1876490405149368489","1877729032776642718","1875064972251996397","1875636748451246299","1876693557341261864","1877384242637812182","1877023390822785048","1877538744993001910","1877345323854553325","1841513279023091831","1874511172919243127","1877057794987217326","1713887517160657191","1877728334752170027","1874289448969789834","1848129440003260864","1873700394645533001","1869688398111531476","1868163461018214777"] # Sustituir con IDs reales

def get_tweets(tweet_ids):
    headers = create_headers(bearer_token)
    tweets = get_tweet_by_id(headers, tweet_ids)
    if 'data' in tweets:
        for tweet in tweets['data']:
            print(f"Tweet ID: {tweet['id']} - Texto: {tweet['text']}")
    else:
        print("No se encontraron tweets o hubo un error:", tweets)


def get_tweet_by_id(headers, tweet_id):
    url = f"https://api.twitter.com/2/tweets/{tweet_id}"
    response = requests.get(url, headers=headers)
    return response.json()

def get_responses_to_tweet(headers, tweet_id):
    url = "https://api.twitter.com/2/tweets/search/recent"
    params = {
        "query": f"conversation_id:{tweet_id}",  
        "tweet.fields": "author_id,conversation_id,in_reply_to_user_id",  
        "max_results": 100 
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def get_responses(tweet_id):
    headers = create_headers(bearer_token)
    tweet_data = get_tweet_by_id(headers, tweet_id)
    if 'data' in tweet_data:
        tweet_text = tweet_data['data']['text']
        print(f"Tweet original: {tweet_text}")

    responses = get_responses_to_tweet(headers, tweet_id)
    if 'data' in responses:
        print("\nRespuestas al tweet:")
        ids = []
        texts = []
        for response in responses['data']:
            tweet_id = response['id']
            tweet_text = response['text']
            print(f"Respuesta ID: {tweet_id} - Texto: {tweet_text}")
            ids.append(tweet_id)
            texts.append(tweet_text)
        df = pd.DataFrame({'ID': ids, 'Tweet': texts})
        df.to_csv('response_milei2.csv', index=False, encoding='utf-8')
    else:
        print("No se encontraron respuestas o hubo un error:", responses)


#get_responses(1908875600585957484)
#https://x.com/therealbuni/status/1911213828953559248


#get_responses(1911213828953559248)


#https://x.com/Trumperizar/status/1910873110888272050

get_responses(1910873110888272050)
