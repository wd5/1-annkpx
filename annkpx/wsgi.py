import os
from os.path import dirname
import sys

ROOT = dirname(dirname(dirname(os.path.abspath(__file__))))
PROJECT_ROOT = ROOT + "/annkpx/"
sys.path.append(PROJECT_ROOT)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "annkpx.settings")
activate_this = PROJECT_ROOT + "/env/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
