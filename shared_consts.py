# API
ACCESS_TOKEN = 'access_token'
BLACKLIST_TOKENS = 'blacklist_tokens'
CONSUMER = 'consumer'
CONTENT_TYPE = 'content_type'
DECODED_TOKEN = 'decoded_token'
JWT_SECRET = 'JWT_SECRET'
JWT_ALGO = 'JWT_ALGO'
PASS = 'password'
REFRESH_TOKEN = 'refresh_token'
RETAILER = 'retailer'
TOKEN_HEADER_KEY = 'Token'
TOKEN_TYPE = 'token_type'
TOWN = 'town'
USER_TYPE = 'user_type'

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
LAST_UPDATES = 'last_third_party_updates'
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
TOKENS = 'third_party_tokens'
TOWN_USERS = 'town_users'

COLLECTIONS = [BEACONS, BLACKLIST_TOKENS, CALENDAR_EVENTS, BEACON_INTERACTIONS, OFFER_INTERACTIONS,
               PRODUCT_INTERACTIONS, RETAILER_INTERACTIONS, THIRD_PARTY_INTERACTIONS, CONSUMERS, IAB_CATEGORIES,
               PRODUCTS, OFFERS, RATINGS, RETAILER_USERS, RETAILERS, TOWN_USERS]

# Attributes
ADDRESS = 'address'
BEACON_ID = 'beacon_id'
BEACON_TYPE = 'beacon_type'
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
ID = 'id'
IMAGE_FILENAMES = 'image_filenames'
IMAGE_URL = 'image_url'
INTERACTION_TYPE = 'interaction_type'
IS_ACTIVE = 'is_active'
IS_ADMIN = 'is_admin'
IS_FILE_UPLOAD = 'is_file_upload'
IS_PREDICTION = 'is_prediction'
ITEM_ID = 'item_id'
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
PARENT_ID = 'parent_id'
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
SENTIMENT = 'sentiment'
STARTS_AT = 'starts_at'
STOPS_AT = 'stops_at'
SUBCATEGORY_ID = 'subcategory_id'
SURNAME = 'surname'
SURVEY_IMAGE_URL = 'survey_image_url'
TERMS_AND_CONDITIONS = 'terms_and_conditions'
THIRD_PARTY_NAME = 'third_party_name'
TYPE = 'type'
USERNAME = 'username'
VALUE = 'value'
WEBSITE = 'website'

LEGAL_ATTRS = {BEACONS: [BEACON_TYPE, ID, IS_ACTIVE, MAJOR, MINOR, RETAILER_ID],
               BLACKLIST_TOKENS: [],
               CALENDAR_EVENTS: [CONSUMER_ID, IAB_CATEGORY_ID, ID, LAT, LONG, NAME, OCCURS_AT],
               BEACON_INTERACTIONS: [BEACON_ID, CONSUMER_ID, DURATION, ID, RETAILER_ID, OCCURRED_AT],
               OFFER_INTERACTIONS: [COMMENT, CONSUMER_ID, ID, INTERACTION_TYPE, OCCURRED_AT, OFFER_ID, RETAILER_ID,
                                    SENTIMENT],
               PRODUCT_INTERACTIONS: [COMMENT, CONSUMER_ID, ID, INTERACTION_TYPE, OCCURRED_AT, PRODUCT_ID, RETAILER_ID,
                                      SENTIMENT],
               RETAILER_INTERACTIONS: [COMMENT, CONSUMER_ID, ID, INTERACTION_TYPE, OCCURRED_AT, RETAILER_ID, SENTIMENT],
               THIRD_PARTY_INTERACTIONS: [CONSUMER_ID, IAB_CATEGORY_ID, ID, INTERACTION_TYPE, RAW, SENTIMENT,
                                          THIRD_PARTY_NAME],
               CONSUMERS: [ADDRESS, DOB, EMAIL, FIRSTNAME, GENDER, HASHED_PASS, ID, PHONE, POSTCODE,
                           PRIMARY_THIRD_PARTY_NAME, SALT, TOKENS, USERNAME],
               IAB_CATEGORIES: [ID, PARENT_ID, NAME],
               PRODUCTS: [KMEANS_CATEGORY_ID, DESCRIPTION, IAB_CATEGORY_ID, ID, IMAGE_FILENAMES, IMAGE_URL,
                          IS_FILE_UPLOAD, NAME, PRICE, QUANTITY, RETAILER_ID, SURVEY_IMAGE_URL, STOPS_AT],
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
                   CALENDAR_EVENTS: [CONSUMER_ID, IAB_CATEGORY_ID, NAME, OCCURS_AT],
                   BEACON_INTERACTIONS: [BEACON_ID, CONSUMER_ID, DURATION, RETAILER_ID, OCCURRED_AT],
                   OFFER_INTERACTIONS: [CONSUMER_ID, INTERACTION_TYPE, OCCURRED_AT, OFFER_ID, RETAILER_ID, SENTIMENT],
                   PRODUCT_INTERACTIONS: [CONSUMER_ID, INTERACTION_TYPE, OCCURRED_AT, PRODUCT_ID, RETAILER_ID,
                                          SENTIMENT],
                   RETAILER_INTERACTIONS: [CONSUMER_ID, INTERACTION_TYPE, OCCURRED_AT, RETAILER_ID, SENTIMENT],
                   THIRD_PARTY_INTERACTIONS: [CONSUMER_ID, IAB_CATEGORY_ID, SENTIMENT, THIRD_PARTY_NAME],
                   CONSUMERS: [],
                   IAB_CATEGORIES: [NAME],
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
SENT_BASE_URL = 'https://api.datamarket.azure.com/data.ashx/amla/text-analytics/v1/GetSentiment?'
ACCOUNT_KEY = 'AccountKey:'
CONTENT_TYPE = 'Content-Type'
AUTHORIZATION = 'Authorization'
SENT_SCORE = 'Score'
KEY_PHRASES = 'KeyPhrases'
PHRASES_BASE_URL = 'https://api.datamarket.azure.com/data.ashx/amla/text-analytics/v1/GetKeyPhrases?'

# Modes
MODE_HEADER_KEY = 'Mode'
DEBUG = 'debug'
EVAL = 'eval'
RELEASE = 'release'
TEST = 'test'
