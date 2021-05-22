import json
import os
import requests
from requests import RequestException


def clean_jenkins_queue():

    # Get the contents of the queue
    queue_url = "https://ci.floop.org.uk/queue/api/json?pretty=true"
    r = requests.get(queue_url)
    if r.status_code != 200:
        raise RequestException(f'Couldn\'t get queue from url {queue_url}, status code {r.status_code}')
    task_queue = r.json()

    print(f'Jenkins build queue has {len(task_queue["items"])} items in it')

    # Authentication
    JENKINS_USER = os.getenv("JENKINS_USER", None)
    JENKINS_API_TOKEN = os.getenv("JENKINS_API_TOKEN", None)

    if not JENKINS_API_TOKEN or not JENKINS_API_TOKEN:
        raise ValueError(f'''
        You need to export two environment variables to use this script.

        1.) JENKINS_USER. You supplied {JENKINS_USER}
        2.) JENKINS_API TOKEM. You supplied {JENKINS_API_TOKEN}

        You can get both by clicking your user name in the top right hand corner
        after logging into our jenkins server (click vredentials to set an api token).

        Export them on teh command line via "export JENKINS_USER=<your username" etc
        or add them to ~/.bashrc or ~/.zshrc and restarrt yor terminal.
        ''')

    headers = {
            'Authorization': f'{JENKINS_USER}:{JENKINS_API_TOKEN}'
    }

    # Clear the queue
    for item in task_queue["items"]:
        cancel_queue_item_url = f'https://ci.floop.org.uk/queue/cancelItem?id={item["id"]}'
        print(cancel_queue_item_url)
        r = requests.post(cancel_queue_item_url, auth=(JENKINS_USER,JENKINS_API_TOKEN))
        if r.status_code != 204:
            print(f'Unable to cancel task: {json.dumps(item["task"])}')


if __name__ == "__main__":
    clean_jenkins_queue()