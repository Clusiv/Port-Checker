from flask import Flask,request

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def root():
    print(request.data)
    print(request.json)
    if request.method == 'GET':
        return 'OK'
    else:
        return 'ACCEPTED'

app.run()