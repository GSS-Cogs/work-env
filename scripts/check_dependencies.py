import os
import sys 
import subprocess
import requests


unmatched_commit = 'Library {} is outdated. Expected {}, got {}'


def check_deps():
    r = requests.get("https://raw.githubusercontent.com/GSS-Cogs/databaker-docker/master/Pipfile.lock")
    if r.status_code != 200:
        print('Unable to get lock file for dependencies. Aborting check.')
    else:

        dir_path = os.path.dirname(os.path.realpath(__file__))
        lib_commit_dir = {}
        lock = r.json()

        # Create a dict of {<wanted_library>: <expected_commit>}
        with open(f'{dir_path}/dependency_checklist.txt') as f:
            for line in f.readlines():
                lib_name = line.strip()
                try:
                    # Installed from github, so looking for commit if ref
                    lib_commit_dir[lib_name] = lock["default"][lib_name]["ref"]
                except KeyError:
                    try:
                        # Installed from pypi so looking for version
                        lib_commit_dir[lib_name] = lock["default"][lib_name]["version"]
                    except KeyError:
                        print(f"Aborting checks for {lib_name}. No such library defined in Pipfile.lock!")

        # Use a pip freeze to check we're for what we need
        process = subprocess.Popen(['pip', 'freeze'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, _ = process.communicate()

        bad_matches = []

        for req in output.decode("utf-8").split("\n"):

            for lib_name, id_expected in lib_commit_dir.items():
                if req.startswith(lib_name):

                    if "@" in req:
                        id_got = req.split("@")[2].strip()
                    else:
                        id_got = req[req.index("="):]
                        
                    if id_expected != id_got:
                        bad_matches.append(unmatched_commit.format(lib_name, id_expected, id_got))
                    break

        if len(bad_matches) > 0:
            for bad_match in bad_matches:
                for _ in range(6):
                    print(f'{bad_match}, you need to run the "sync" command!')
        else:
            print("You Dependencies are up to date.")


if __name__ == "__main__":
    check_deps()