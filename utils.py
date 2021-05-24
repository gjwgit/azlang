import os
from mlhub.pkg import get_private


# ----------------------------------------------------------------------
# Request subscription key and endpoint from user.
# ----------------------------------------------------------------------

def request_priv_info():
    PRIVATE_FILE = "private.json"

    path = os.path.join(os.getcwd(), PRIVATE_FILE)

    values = get_private(path, "azlang", "Azure LUIS")

    subscription_key, endpoint, location, id = values

    return subscription_key, endpoint, location, id
