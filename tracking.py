from flask import Flask
from flask.ext.pymongo import PyMongo

SECRET_KEY = 'flask-session-insecure-secret-key'
WTF_CSRF_SECRET_KEY = 'this-is-not-random-but-it-should-be'

MONGO_URI = 'mongodb://'
MONGO_HOST = '10.55.55.5'
MONGO_PORT = 27017
MONGO_AUTO_START_REQUEST = False
MONGO_DBNAME = 'students'
MONGO_USERNAME = None
MONGO_PASSWORD = None
MONGO_REPLICA_SET = None


app = Flask(__name__)

# connect to MongoDB with the defaults
mongo1 = PyMongo(app)

class School:
    def __init__(self, name, num, addr, s_type):
        self.num = num
        self.name = name
        self.addr = addr
        self.s_type = s_type
    def describe(self):
        print "%s is a %s located at %s." % (self.name, self.s_type, self.address)
    def request(self,arg):
        request[arg] # I'm not sure if that's what you want, I copied it from the dict you had there
    def save():
    	# implement the saving to MongoDB here


# Instead of creating a dict for each school you simply instantiate the class:
# MIT=School(1,'Cambridge','university')
# Harvard=School(2,'Cambridge','university')
# >>> MIT.address
# 'Cambridge'
# >>> Harvard.s_type
# 'university'

# >>> MIT.describe()
# MIT is a university located at Cambridge.

@app.route('/')
def home_page():
    students = mongo.db.users.find({'firstname': 'John'})
    return render_template('index.html',
        online_users=students)

@app.route('/students/<firstname>')
def user_profile(firstname):
    user = mongo.db.students.find_one_or_404({'_id': firstname})
    return render_template('student.html', student=student)

# Valid object ID strings are converted into ObjectId objects
@app.route('/<ObjectId:student_id>')
def show_student(student_id):
    task = mongo.db.students.find_one_or_404(student_id)
    return render_template('student.html', student=student)



if __name__ == "__main__":
    app.debug = True
    db.create_all()
    app.run()


