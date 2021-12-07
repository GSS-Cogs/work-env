
# Where the user has specified custom python dependencies via the 
# WORKENV_CUSTOM_REQS environment variable, add them to the
# standard additional_requirments.txt before finishing the sync.

import os
from pathlib import Path
import requests

custom_requirements = os.getenv("WORKENV_CUSTOM_REQS", None)

if custom_requirements:

    if not custom_requirements.endswith('.txt'):
        raise ValueError('Work-env can only be extened via a requirments'
            f' file ending with .txt. You\'ve provided {custom_requirements}')

    is_http_reqs = (custom_requirements.startswith("http://") or 
        custom_requirements.startswith("https://"))

    if is_http_reqs:
        r = requests.get(custom_requirements)
        if not r.ok:
            raise Exception(f'Failed to get custom requirements from url '
                f' {custom_requirements} with status code {r.status_code}')
        req_text = r.text

    else:
        if not os.path.isfile(custom_requirements):
            raise Exception(f'Custom requirements file could not be '
                'found at provided location {custom_requirments}.')

        with open(custom_requirements) as f:
            req_text = f.read()

    this_dir = Path(os.path.dirname(os.path.realpath(__file__)))
    with open(this_dir.parent / "additional-requirements.txt", "a") as f:
        for req_line in req_text.split("\n"):
            f.write(req_line+"\n")