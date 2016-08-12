DB_ACCESS_MODULE = 'DB_ACCESS_MODULE'
DB_ID = 'DB_ID'
DOCUMENTDB_HOST = 'DOCUMENTDB_HOST'
DOCUMENTDB_MASTER_KEY = 'DOCUMENTDB_MASTER_KEY'
MONGO_DB = 'MONGO_DB'


# General
UNKNOWN_ID = 'unknown_id'
COLLECTION = 'collection'
CONSUMER = 'consumer'
RETAILER = 'retailer'
TOWN = 'town'
USER = 'user'
USER_TYPE = 'user_type'
TOKEN_TYPE = 'token_type'

DECODED_TOKEN = 'decoded_token'
REFRESH_TOKEN = 'refresh_token'
ACCESS_TOKEN = 'access_token'
PASS = 'password'
BLACKLIST_TOKENS = 'blacklist_tokens'


TOKEN_HEADER_KEY = 'Token'
JWT_SECRET = 'JWT_SECRET'
JWT_ALGO = 'JWT_ALGO'

CONTENT_TYPE = 'content_type'


# Collections
RECOMMENDATIONS = 'recommendations'
CONSUMERS = 'consumers'
INTERACTIONS = 'interactions'
RETAILERS = 'retailers'
RETAILER_USERS = 'retailer_users'
TOWN_USERS = 'town_users'
CATEGORIES = 'categories'
BEACONS = 'beacons'
TOKENS = 'third_party_tokens'
LAST_UPDATES = 'last_third_party_updates'
PRODUCT_INTERACTIONS = 'consumer_product_interactions'
OFFER_INTERACTIONS = 'consumer_offer_interactions'
RETAILER_INTERACTIONS = 'consumer_retailer_interactions'
BEACON_INTERACTIONS = 'consumer_beacon_interactions'
THIRD_PARTY_INTERACTIONS = 'consumer_third_party_interactions'
CALENDAR_EVENTS = 'consumer_calendar_events'
PRODUCTS = 'products'
OFFERS = 'offers'
RATINGS = 'ratings'


COLLECTIONS = [RECOMMENDATIONS, CONSUMERS, RETAILERS, RETAILER_USERS, TOWN_USERS, CATEGORIES, BEACONS, TOKENS,
               LAST_UPDATES, PRODUCT_INTERACTIONS, OFFER_INTERACTIONS, RETAILER_INTERACTIONS, BEACON_INTERACTIONS,
               THIRD_PARTY_INTERACTIONS, CALENDAR_EVENTS, PRODUCTS, OFFERS, BLACKLIST_TOKENS, RATINGS]


# Attributes
ID = 'id'
NAME = 'name'
USERNAME = 'username'
FIRST_NAME = 'first_name'
SURNAME = 'surname'
GENDER = 'gender'
DOB = 'date_of_birth'
IDENTITY_TYPE = 'identity_type'
IDENTITY_KEY = 'identity_key'
HASHED_PASS = 'hashed_password'
SALT = 'salt'
DESCRIPTION = 'description'
POSTCODE = 'postcode'
ADDRESS = 'address'
LONG = 'longitude'
LAT = 'latitude'
EMAIL = 'email'
PHONE = 'phone'
WEBSITE = 'website'
IMAGE_URL = 'image_url'
TYPE = 'type'

CONSUMER_ID = 'consumer_id'
ITEM_ID = 'item_id'
CATEGORY_ID = 'category_id'
SUBCATEGORY_ID = 'subcategory_id'
RETAILER_ID = 'retailer_id'

QUANTITY = 'quantity'
PRICE = 'price'
QR_URL = 'qr_url'
RATING = 'rating'

STARTS_AT = 'starts_at'
STOPS_AT = 'stops_at'
OCCURRED_AT = 'occurred_at'

IS_FILE_UPLOAD = 'is_file_upload'

QUANTITY_TOTAL = 'quantity_total'
QUANTITY_PER_CONSUMER = 'quantity_per_consumer'
TERMS_AND_CONDITIONS = 'terms_and_conditions'

IMAGE_FILENAMES = 'image_filenames'

VALUE = 'value'
COMMENT = 'comment'

RETAILER_NAME = 'retailer_name'

INTERACTION_TYPE = 'interaction_type'
ITEM_TYPE = 'item_type'

PRODUCT_ID = 'product_id'
OFFER_ID = 'offer_id'

IS_ADMIN = 'is_admin'

IS_PREDICTION = 'is_prediction'

SENTIMENT = 'sentiment'

MANDATORY_ATTRS = {RETAILERS: [NAME],
                   PRODUCTS: [NAME, PRICE, RETAILER_ID]}
LEGAL_ATTRS = {RETAILERS: [ID, CATEGORY_ID, SUBCATEGORY_ID, NAME, DESCRIPTION, POSTCODE, ADDRESS, LONG, LAT, EMAIL,
                           PHONE, WEBSITE, IMAGE_URL],
               CONSUMERS: [ID, USERNAME, FIRST_NAME, SURNAME, GENDER, DOB, IDENTITY_TYPE, IDENTITY_KEY, HASHED_PASS,
                           POSTCODE, ADDRESS, EMAIL, PHONE],
               RECOMMENDATIONS: [ID, CONSUMER_ID, ITEM_ID, TYPE, NAME, RETAILER_ID, CATEGORY_ID, SUBCATEGORY_ID,
                                 STARTS_AT, STOPS_AT, QUANTITY, PRICE, QR_URL, RATING, DESCRIPTION, IMAGE_FILENAMES],
               PRODUCTS: [ID, RETAILER_ID, CATEGORY_ID, SUBCATEGORY_ID, NAME, DESCRIPTION, PRICE, QUANTITY, STOPS_AT,
                          IMAGE_URL, IS_FILE_UPLOAD, IMAGE_FILENAMES],
               OFFERS: [ID, RETAILER_ID, CATEGORY_ID, SUBCATEGORY_ID, NAME, DESCRIPTION, STARTS_AT, STOPS_AT,
                        QUANTITY_TOTAL, QUANTITY_PER_CONSUMER, TERMS_AND_CONDITIONS, IMAGE_URL, IMAGE_FILENAMES],
               PRODUCT_INTERACTIONS: [ID, INTERACTION_TYPE, VALUE, OCCURRED_AT, COMMENT, CONSUMER_ID, RETAILER_ID,
                                      PRODUCT_ID],
               OFFER_INTERACTIONS: [ID, INTERACTION_TYPE, VALUE, OCCURRED_AT, COMMENT, CONSUMER_ID, RETAILER_ID,
                                    OFFER_ID]}


# Errors
MISSING_DOCS = 'Documents not found'
ILLEGAL_ATTRS = 'Illegal Attributes for doc'


# Actions
CREATE = 'create'
READ = 'read'
UPDATE = 'update'
DELETE = 'delete_products'
AUTH = 'auth'
VALIDATE = 'validate'
REGISTER = 'register'


# Text Classifier
TEXT_API_APP_ID = 'TEXT_API_APP_ID'
TEXT_API_KEY = 'TEXT_API_KEY'
TEXT = 'text'
TAXONOMY = 'taxonomy'
IAB_QAG = 'iab-qag'
CATEGORIES = 'categories'
CONFIDENT = 'confident'
SCORE = 'score'


# Sentiment Analysis
SENT_API_KEY = 'SENT_API_KEY'
SENT_BASE_URL = 'https://api.datamarket.azure.com/data.ashx/amla/text-analytics/v1/GetSentiment?'
ACCOUNT_KEY = 'AccountKey:'
CONTENT_TYPE = 'Content-Type'
AUTHORIZATION = 'Authorization'
SENT_SCORE = 'Score'
KEY_PHRASES = 'KeyPhrases'
PHRASES_BASE_URL =  'https://api.datamarket.azure.com/data.ashx/amla/text-analytics/v1/GetKeyPhrases?'


# Modes
MODE_HEADER_KEY = 'Mode'
DEBUG = 'debug'
RELEASE = 'release'
TEST = 'test'
EVAL = 'eval'
