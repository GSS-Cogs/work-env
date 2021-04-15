import sys 
import subprocess

import requests

r = requests.get("https://raw.githubusercontent.com/GSS-Cogs/databaker-docker/master/Pipfile.lock")
if r.status_code != 200:
    print('Unable to get lock file for dependencies. Aborting check.')
else:

    lock = r.json()
    gssutils_should_be = lock["default"]["gssutils"]["ref"]
    databaker_should_be = lock["default"]["databaker"]["ref"]

    process = subprocess.Popen(['pip', 'freeze'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = process.communicate()

    for req in output.decode("utf-8").split("\n"):

        if req.startswith("gssutils"):
            gss_utils_is = req.split("@")[2].strip()

        if req.startswith("databaker"):
            databaker_is = req.split("@")[2].strip()

    print(f'gss-utils commit is:', gss_utils_is, 'should be:', gssutils_should_be)
    print(f'databaker commit is:', databaker_is, 'should be:', databaker_should_be)

    if databaker_is != databaker_should_be or gssutils_should_be != gss_utils_is:
        for _ in range(20):
            print('Youre dependencies are out of date, you need to run the "sync" command!')
    else:
        print("You Dependencies are up to date.")
