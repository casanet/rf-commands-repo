from dotenv import load_dotenv
import os
import sys
load_dotenv()

app_name = 'rf-commands-repo'
local_server_key_header = 'local-key'
rf_repository_key_header = 'rf-repository-api-key'

REMOTE_SERVER_URL = os.getenv("REMOTE_SERVER_URL")
if not REMOTE_SERVER_URL:
    msg = 'REMOTE_SERVER_URL not exists... exiting'
    print(msg)
    sys.exit(msg)

RF_REPOSITORY_API_KEY = os.getenv("RF_REPOSITORY_API_KEY")
if not RF_REPOSITORY_API_KEY:
    msg = 'RF_REPOSITORY_API_KEY not exists... exiting'
    print(msg)
    sys.exit(msg)
