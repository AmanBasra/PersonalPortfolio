import os

import sys, site
from django.core.wsgi import get_wsgi_application

# Add the app’s directory to the PYTHONPATH

sys.path.append("/home/abasra/PersonalPortfolio/Portfolio")
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
application = get_wsgi_application()