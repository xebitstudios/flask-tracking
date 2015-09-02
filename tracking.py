_cwd = dirname(abspath(__file__))

SECRET_KEY = 'flask-session-insecure-secret-key'
MONGO_URI = 'mongodb://'
MONGO_HOST = '10.55.55.5'
MONGO_PORT = 27017
MONGO_AUTO_START_REQUEST = False
MONGO_DBNAME = 'bills'
MONGO_USERNAME = None
MONGO_PASSWORD = None
MONGO_REPLICA_SET = None
WTF_CSRF_SECRET_KEY = 'this-is-not-random-but-it-should-be'


app = Flask(__name__)
app.config.from_object(__name__)

db = SQLAlchemy(app)

# class Site(db.Model):
#     __tablename__ = 'tracking_site'

#     id = db.Column(db.Integer, primary_key=True)
#     base_url = db.Column(db.String)
#     visits = db.relationship('Visit', backref='tracking_site', lazy='select')

#     def __repr__(self):
#         return '<Site %r>' % (self.base_url)

#     def __str__(self):
        # return self.base_url

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


