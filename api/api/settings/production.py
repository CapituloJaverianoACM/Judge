from .common import *
import ipaddress


ALLOWED_HOSTS = list()
CORS_ORIGIN_WHITELIST = list()

# TODO - change this
CORS_ORIGIN_ALLOW_ALL = True

if os.environ.get("ALLOW_HOST", None) is not None:
    for host in os.environ.get("ALLOW_HOST", "").split(", "):
        ALLOWED_HOSTS += [
            '%s' % ip for ip in ipaddress.ip_network(host).hosts()
        ]

if os.environ.get("ALLOW_NAMES", None) is not None:
    ALLOWED_HOSTS += [
        "{0}".format(host_name)
        for host_name in os.environ.get("ALLOW_NAMES", "").split(", ")
    ]

    CORS_ORIGIN_WHITELIST = [
        "{0}".format(host_name)
        for host_name in os.environ.get("ALLOW_NAMES", "").split(", ")
    ]

DEBUG = False

ROOT_URLCONF = '%s.%s.urls' % (SITE_NAME, SITE_NAME)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS
