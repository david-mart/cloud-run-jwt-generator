from urllib.parse import urlparse
import urllib
import argparse
import pyperclip

import google.auth.transport.requests
import google.oauth2.id_token
import os
parser = argparse.ArgumentParser()

parser.add_argument("--url", help="Cloud Run Service URL")
parser.add_argument("--credentials", help="Service account file path")

args = parser.parse_args()
# Service account key path
credential_path = args.credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


def make_authorized_get_request():
    """
    make_authorized_get_request makes a GET request to the specified HTTP endpoint
    by authenticating with the ID token obtained from the google-auth client library
    using the specified audience value.
    """

    # Cloud Run uses your service's hostname as the `audience` value
    audience = args.url.replace(urlparse(args.url).path, "")
    # For Cloud Run, `endpoint` is the URL (hostname + path) receiving the request
    endpoint = args.url

    req = urllib.request.Request(endpoint)

    auth_req = google.auth.transport.requests.Request()
    id_token = google.oauth2.id_token.fetch_id_token(auth_req, audience)
    req.add_header("Authorization", f"Bearer {id_token}")
    os.system('clear')
    pyperclip.copy(f"Bearer {id_token}")
    print(f"Bearer {id_token} \n\n Copied to clipboard")
    


make_authorized_get_request()
