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

