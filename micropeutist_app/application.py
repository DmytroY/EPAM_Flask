from .config import app
from .models.model import *


import EPAM_Flask.micropeutist_app.views.web_view

import EPAM_Flask.micropeutist_app.rest.api_view
import EPAM_Flask.micropeutist_app.views.web_view

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
