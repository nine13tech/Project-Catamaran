class APIConfig(object):

    def __init__(self):
        pass


VERSION = "2.0.14.1"
# prod, or dev
CURRENT_ENV = 'prod'

LOCAL_DJANGO_DEBUG = True
DEVEL_DJANGO_DEBUG = True
PROD_DJANGO_DEBUG = False

MANIFEST_DB = '<path to manifest db>'
BANNER_DB = '<path to banner db>'
BUNGIE_URL = 'https://www.bungie.net'
BASE_DIR = '<path to base dir>'

# These need to be set for prod/devel sites. Write your own landscape determinator for your software that sets these
# values to BUNGIE_KEY, BUNGIE_SECRET, BUNGIE_API_KEY before calling the API.

# PROD
BUNGIE_KEY_PROD = "<bungie key id number>"
BUNGIE_SECRET_PROD = "<bungie secret>"
BUNGIE_API_KEY_PROD = "<bungie api key>"
BUNGIE_ORIGIN_PROD = '<your origin key>'

# DEVEL
BUNGIE_KEY_DEVEL = "<bungie key id number>"
BUNGIE_SECRET_DEVEL = "<bungie secret>"
BUNGIE_API_KEY_DEVEL = "<bungie api key>"
BUNGIE_ORIGIN_DEVEL = '<your origin key>'
