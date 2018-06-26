# -*- coding: utf-8 -*-

from api import api as application
import os

port = int(os.environ.get("PORT", 5000))
application.run(host='0.0.0.0', port=port)
