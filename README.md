## Cloud Run endpoint demo auth token generator 

Given you already have a Cloud Run instance with Authenticated Access running, follow the steps below:

1. Create service account with per-service permissions ([Service Identity](https://cloud.google.com/run/docs/securing/service-identity#per-service-identity), [Authenticating Developers](https://cloud.google.com/run/docs/authenticating/developers))
2. Download API key JSON ([Create and manage keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys))
3. Create python environment and install dependencies
```
python -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```
4. Run the token generator script
```
python run.py --url=[FULL_API_ENDPOINT] --credentials=[CREDENTIALS_JSON_FILE_PATH]

```
where FULL_API_ENDPOINT is the full path, including the endpoint (without the query params), i.e. `https://my-service-jfkie.a.run.app/my-service-endpoint`, and CREDENTIALS_JSON_FILE_PATH is a full path to the file downloaded in step 2 (i.e. `/Users/jon.do/Downloads/my-credentials.json`).


Read more info in [Official Docs](https://cloud.google.com/run/docs/authenticating/service-to-service).