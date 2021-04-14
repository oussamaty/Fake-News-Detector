from flask import Flask, json, request
from detector.main import get_score
api = Flask(__name__)

@api.route('/score', methods=['GET'])
def score():
      print('Connected')
      score = get_score(json.loads(request.args.get('request'))['tweet'])
      return json.dumps({'score':score})
if __name__ == '__main__':
    api.run()