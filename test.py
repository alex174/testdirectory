from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!  This is an internal app page!</h1>'

@app.route('/facedetector',methods=['GET'])
def facedetector():
    args=request.args
    face_left=args.get("face_left")
    face_top=args.get("face_top")
    face_right=args.get("face_right")
    face_bottom=args.get("face_bottom")
    face_id=args.get("face_id")
    info="New face with ID: " + face_id + " detected at X pos " + face_left + " and Y pos " + face_right
    return info
