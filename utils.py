import os
from mlhub.pkg import get_private


# ----------------------------------------------------------------------
# Request subscription key and endpoint from user.
# ----------------------------------------------------------------------

def request_priv_info():
    PRIVATE_FILE = "private.json"

    path = os.path.join(os.getcwd(), PRIVATE_FILE)

    subscription_key, endpoint, location, id = get_private(path, "azlang", "Azure LUIS")

    return subscription_key, endpoint, location, id
