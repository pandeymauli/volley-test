from flask import Flask, request, jsonify
import os

app = Flask(__name__)
app.config['HEROKU_ON'] = os.environ.get('HEROKU')

# root
@app.route("/")
def index():
    """
    this is a root dir of my server
    :return: str
    """
    return "This is root!!!!"


# GET
@app.route('/users/<user>')
def hello_user(user):
    """
    this serves as a demo purpose
    :param user:
    :return: str
    """
    return "Hello %s!" % user


# POST
@app.route('/api/post_some_data', methods=['POST'])
def get_text_prediction():
    """
    predicts requested text whether it is ham or spam
    :return: json
    """
    print("X")
    #json = request.get_json()
    print(request.data)
    # if len(json['token']) == 0:
    #     return jsonify({'error': 'invalid input'})

    return "H"#jsonify({'you sent this': json['data segment']})


if __name__ == '__main__':
    app.run()
