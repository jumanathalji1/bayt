import os
from random import randint

CHROME_DRIVER_LOCATION = os.environ.get("CHROME_DRIVER_LOCATION")
# Generate random email to avoid duplication
EMAIL = 'test_email_' + (''.join(["{}".format(randint(0, 9)) for num in range(0, 3)])) + '@test.net'
PASSWORD = os.environ.get("PASSWORD", "testPASSword01")

