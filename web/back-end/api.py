import flask
import oauth2 as oauth
import json
import yaml

from ml.classifier.NaiveBayesClassification import NaiveBayesClassification

app = flask.Flask(__name__)
app.config['DEBUG'] = True

nbc = NaiveBayesClassification(data_source='../../ml/RawData/training_data_final.csv')

with open(file='./config.yaml', mode='r') as file:
    data = yaml.load(file)
    consumer_key = data['consumer_key']
    consumer_secret = data['consumer_secret']
    access_token = data['access_token']
    access_secret = data['access_secret']
print('Got file data')

twitter_api = 'https://api.twitter.com/1.1/statuses/user_timeline.json?'
consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
token = oauth.Token(key=access_token, secret=access_secret)
client = oauth.Client(consumer, token)
print('Got client connection')


@app.route('/test', methods=['GET'])
def test():
    print('here')
    return 'Hello, World'


@app.route('/get-tweets/<username>/<count>', methods=['GET'])
def get_tweets(username='DevanshJatin', count=10):
    generated_request = twitter_api + 'screen_name=' + username + '&count=' + str(count)
    response, data = client.request(generated_request)
    tweets = json.loads(data)
    ret_data = {'data': []}

    for tweet in tweets:
        object = {
            "tweet": '',
            "score": -1,
            "id": -1
        }
        object['tweet'] = tweet['text']
        # print(object['tweet'])
        object['score'] = int(nbc.get_prediction([tweet['text']])[0])
        # print(object['score'])
        object['id'] = tweet['id_str']
        object = json.loads(json.dumps(object))

        ret_data['data'].append(object)
    return ret_data


if __name__ == '__main__':
    app.run()

