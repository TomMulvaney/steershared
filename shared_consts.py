# API
ACCESS_TOKEN = 'access_token'
BLACKLIST_TOKENS = 'blacklist_tokens'
CONSUMER = 'consumer'
CONTENT_TYPE = 'content_type'
DECODED_TOKEN = 'decoded_token'
DEV = 'dev'
JWT_SECRET = 'JWT_SECRET'
JWT_ALGO = 'JWT_ALGO'
PASS = 'password'
REFRESH_TOKEN = 'refresh_token'
RETAILER = 'retailer'
TOKEN_HEADER_KEY = 'Token'
TOKEN_TYPE = 'token_type'
TOWN = 'town'
USER_TYPE = 'user_type'
DATA = 'data'

# Third Parties
FACEBOOK = 'Facebook'
GOOGLE_PLUS = 'Google+'
PINTEREST = 'Pinterest'
TWITTER = 'Twitter'
TWITTER_KEY = 'TWITTER_KEY'
TWITTER_SECRET = 'TWITTER_SECRET'

# Machine Learning
CATEGORY_TYPES = 'category_types'

# Database
DB_ACCESS_MODULE = 'DB_ACCESS_MODULE'
DB_ID = 'DB_ID'
DOCUMENTDB_HOST = 'DOCUMENTDB_HOST'
DOCUMENTDB_MASTER_KEY = 'DOCUMENTDB_MASTER_KEY'
MONGO_DB = 'MONGO_DB'

# Error Handling
UNKNOWN_ID = 'unknown_id'

# Collections
BEACONS = 'beacons'
BEACON_INTERACTIONS = 'consumer_beacon_interactions'
CALENDAR_EVENTS = 'consumer_calendar_events'
CATEGORIES = 'categories'
CONSUMERS = 'consumers'
IAB_CATEGORIES = 'iab_categories'
INTERACTIONS = 'interactions'
LAST_UPDATE_IDS = 'last_update_ids'
OFFERS = 'offers'
OFFER_INTERACTIONS = 'consumer_offer_interactions'
PRODUCTS = 'products'
PRODUCT_INTERACTIONS = 'consumer_product_interactions'
RATINGS = 'ratings'
RECOMMENDATIONS = 'recommendations'
RETAILERS = 'retailers'
RETAILER_INTERACTIONS = 'consumer_retailer_interactions'
RETAILER_USERS = 'retailer_users'
THIRD_PARTY_INTERACTIONS = 'consumer_third_party_interactions'
TOWN_USERS = 'town_users'

COLLECTIONS = [BEACONS, BLACKLIST_TOKENS, CALENDAR_EVENTS, BEACON_INTERACTIONS, OFFER_INTERACTIONS,
               PRODUCT_INTERACTIONS, RETAILER_INTERACTIONS, THIRD_PARTY_INTERACTIONS, CONSUMERS, IAB_CATEGORIES,
               PRODUCTS, OFFERS, RATINGS, RETAILER_USERS, RETAILERS, TOWN_USERS]

# Attributes
ADDRESS = 'address'
BEACON_ID = 'beacon_id'
BEACON_TYPE = 'beacon_type'
CATEGORY_CODE = 'category_code'
CATEGORY_ID = 'category_id'
COMMENT = 'comment'
CONSUMER_ID = 'consumer_id'
DESCRIPTION = 'description'
DOB = 'date_of_birth'
DURATION = 'duration'
EMAIL = 'email'
FIRSTNAME = 'firstname'
GENDER = 'gender'
HASHED_PASS = 'hashed_password'
IAB_CATEGORY_ID = 'iab_category_id'
IAB_CATEGORY_NAME = 'iab_category_name'
ID = 'id'
IMAGE_FILENAMES = 'image_filenames'
IMAGE_URL = 'image_url'
INTERACTION_TYPE = 'interaction_type'
IS_ACTIVE = 'is_active'
IS_ADMIN = 'is_admin'
IS_FILE_UPLOAD = 'is_file_upload'
IS_PREDICTION = 'is_prediction'
ITEM_ID = 'item_id'
ITEM_NAME = 'item_name'
ITEM_TYPE = 'item_type'
KMEANS_CATEGORY_ID = 'kmeans_category_id'
LAT = 'latitude'
LOGO_IMAGE_FILENAME = 'logo_image_filename'
LOGO_IMAGE_URL = 'logo_image_url'
LONG = 'longitude'
MAJOR = 'major'
MINOR = 'minor'
NAME = 'name'
OCCURRED_AT = 'occurred_at'
OCCURS_AT = 'occurs_at'
OFFER_ID = 'offer_id'
PARENT_CATEGORY_CODE = 'parent_category_code'
PARENT_ID = 'parent_id'
PARENT_NAME = 'parent_name'
PHONE = 'phone'
POSTCODE = 'postcode'
PRICE = 'price'
PRIMARY_THIRD_PARTY_NAME = 'primary_third_party_name'
PRODUCT_ID = 'product_id'
PRODUCT_IDS = 'product_ids'
QR_URL = 'qr_url'
QUANTITY = 'quantity'
QUANTITY_PER_CONSUMER = 'quantity_per_consumer'
QUANTITY_TOTAL = 'quantity_total'
RATING = 'rating'
RAW = 'raw'
RETAILER_ID = 'retailer_id'
RETAILER_NAME = 'retailer_name'
RETAILER_TYPE = 'retailer_type'
SALT = 'salt'
SECRET_TOKEN = 'secret_token'
SENTIMENT = 'sentiment'
STARTS_AT = 'starts_at'
STOPS_AT = 'stops_at'
SUBCATEGORY_ID = 'subcategory_id'
SURNAME = 'surname'
SURVEY_IMAGE_URL = 'survey_image_url'
TERMS_AND_CONDITIONS = 'terms_and_conditions'
THIRD_PARTY_USER_ID = 'third_party_user_id'
THIRD_PARTY_NAME = 'third_party_name'
THIRD_PARTY_TOKENS = 'third_party_tokens'
TYPE = 'type'
USERNAME = 'username'
VALUE = 'value'
WEBSITE = 'website'

# Attribute Values
PURCHASE = 'purchase'
IMPRESSION = 'impression'

LEGAL_ATTRS = {BEACONS: [BEACON_TYPE, ID, IS_ACTIVE, MAJOR, MINOR, RETAILER_ID],
               BLACKLIST_TOKENS: [],
               CALENDAR_EVENTS: [CONSUMER_ID, IAB_CATEGORY_ID, ID, LAT, LONG, NAME, OCCURS_AT, THIRD_PARTY_NAME],
               BEACON_INTERACTIONS: [BEACON_ID, CONSUMER_ID, DURATION, MAJOR, MINOR, OCCURRED_AT, RETAILER_ID],
               OFFER_INTERACTIONS: [COMMENT, CONSUMER_ID, ID, INTERACTION_TYPE, OCCURRED_AT, OFFER_ID, RETAILER_ID,
                                    SENTIMENT],
               PRODUCT_INTERACTIONS: [COMMENT, CONSUMER_ID, ID, INTERACTION_TYPE, OCCURRED_AT, PRODUCT_ID, RETAILER_ID,
                                      SENTIMENT],
               RETAILER_INTERACTIONS: [COMMENT, CONSUMER_ID, ID, INTERACTION_TYPE, OCCURRED_AT, RETAILER_ID, SENTIMENT],
               THIRD_PARTY_INTERACTIONS: [CONSUMER_ID, IAB_CATEGORY_ID, ID, INTERACTION_TYPE, RAW, SENTIMENT,
                                          THIRD_PARTY_NAME],
               CONSUMERS: [ADDRESS, DOB, EMAIL, FIRSTNAME, GENDER, HASHED_PASS, ID, PHONE, POSTCODE,
                           PRIMARY_THIRD_PARTY_NAME, SALT, THIRD_PARTY_TOKENS, USERNAME],
               IAB_CATEGORIES: [CATEGORY_CODE, ID, PARENT_CATEGORY_CODE, PARENT_ID, PARENT_NAME, NAME],
               PRODUCTS: [KMEANS_CATEGORY_ID, DESCRIPTION, IAB_CATEGORY_ID, IAB_CATEGORY_NAME, ID, IMAGE_FILENAMES,
                          IMAGE_URL, IS_FILE_UPLOAD, NAME, PRICE, QUANTITY, RETAILER_ID, SURVEY_IMAGE_URL,
                          STOPS_AT],
               OFFERS: [KMEANS_CATEGORY_ID, DESCRIPTION, IAB_CATEGORY_ID, ID, IMAGE_FILENAMES, IMAGE_URL, NAME,
                        PRODUCT_IDS, QUANTITY_PER_CONSUMER, QUANTITY_TOTAL, RETAILER_ID, SURVEY_IMAGE_URL, STARTS_AT,
                        STOPS_AT, TERMS_AND_CONDITIONS],
               RATINGS: [CONSUMER_ID, ID, IS_PREDICTION, IMAGE_FILENAMES, ITEM_ID, ITEM_TYPE, NAME, PRICE, RETAILER_ID,
                         RETAILER_NAME, SENTIMENT, STARTS_AT, STOPS_AT, QUANTITY],
               RETAILER_USERS: [EMAIL, FIRSTNAME, HASHED_PASS, ID, IS_ADMIN, PHONE, RETAILER_ID, SALT, SURNAME,
                                USERNAME],
               RETAILERS: [ADDRESS, IAB_CATEGORY_ID, ID, DESCRIPTION, EMAIL, IMAGE_FILENAMES, LAT, LOGO_IMAGE_FILENAME,
                           LOGO_IMAGE_URL, LONG, NAME, PHONE, POSTCODE, RETAILER_TYPE, SURVEY_IMAGE_URL, WEBSITE],
               TOWN_USERS: [EMAIL, FIRSTNAME, HASHED_PASS, ID, PHONE, SALT, SURNAME, USERNAME]}

MANDATORY_ATTRS = {BEACONS: [BEACON_TYPE, IS_ACTIVE, MAJOR, MINOR, RETAILER_ID],
                   BLACKLIST_TOKENS: [],
                   CALENDAR_EVENTS: [IAB_CATEGORY_ID, NAME, OCCURS_AT],
                   BEACON_INTERACTIONS: [BEACON_ID, CONSUMER_ID, DURATION, MAJOR, MINOR, OCCURRED_AT, RETAILER_ID],
                   OFFER_INTERACTIONS: [INTERACTION_TYPE, OCCURRED_AT, OFFER_ID, RETAILER_ID, SENTIMENT],
                   PRODUCT_INTERACTIONS: [INTERACTION_TYPE, OCCURRED_AT, PRODUCT_ID, RETAILER_ID,
                                          SENTIMENT],
                   RETAILER_INTERACTIONS: [INTERACTION_TYPE, OCCURRED_AT, RETAILER_ID, SENTIMENT],
                   THIRD_PARTY_INTERACTIONS: [CONSUMER_ID, IAB_CATEGORY_ID, SENTIMENT, THIRD_PARTY_NAME],
                   CONSUMERS: [],
                   IAB_CATEGORIES: [CATEGORY_CODE, NAME],
                   PRODUCTS: [IS_FILE_UPLOAD, NAME, PRICE, RETAILER_ID],
                   OFFERS: [NAME, PRODUCT_IDS, RETAILER_ID],
                   RATINGS: [CONSUMER_ID, IS_PREDICTION, ITEM_ID, ITEM_TYPE, NAME, PRICE, RETAILER_ID, RETAILER_NAME,
                             SENTIMENT],
                   RETAILER_USERS: [IS_ADMIN, RETAILER_ID, USERNAME],
                   RETAILERS: [LAT, LONG, NAME],
                   TOWN_USERS: [USERNAME]}

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
ACCOUNT_KEY = 'AccountKey:'
CONTENT_TYPE = 'Content-Type'
AUTHORIZATION = 'Authorization'
SENT_SCORE = 'Score'
KEY_PHRASES = 'KeyPhrases'

# Modes
MODE_HEADER_KEY = 'Mode'
DEBUG = 'debug'
EVAL = 'eval'
RELEASE = 'release'
TEST = 'test'
DEFAULT_MODE = 'DEFAULT_MODE'

# AzureBlobConnector and AzureTableConnector
AZURE_ACCOUNT_NAME = 'AZURE_ACCOUNT_NAME'
AZURE_ACCOUNT_KEY = 'AZURE_ACCOUNT_KEY'
CONTAINER = 'container'

# Default column name when converting pd.Series to pd.DataFrame
SERIES_COLUMN = 'VALUES'