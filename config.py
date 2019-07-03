import os

# EDIT
USERNAME = 'email@domain.com'
PASSWORD = 'your_pass'
COURSES = [

'angular-essential-training-2018',
#'node-js-essential-training-3',
#'learning-npm-the-node-package-manager-3',
# 'building-angular-and-node-apps-with-authentication',
# 'building-a-website-with-node-js-and-express-js-2',
# 'learning-mongodb',
# 'express-essential-training',
# 'building-restful-web-apis-with-node-js-and-express',
# 'node-js-securing-restful-apis',
# 'node-js-security',
# 'node-js-testing-and-code-quality',
# 'node-js-deploying-applications'
]

# EDIT IF YOU NEED TO
BASE_DOWNLOAD_PATH = os.path.join(os.path.dirname(__file__), "downloads/become-a-mean-javascript-developer")
USE_PROXY = False
PROXY = "http://127.0.0.1:8888" if USE_PROXY else None

