
# Work Environment

A virtual environment managment tool for building and running our data transformation pipelines. 

* Fully automate dependency management.
* Updates itself, once installed you don't need to keep track of anything.
* Loudly **warn users** where key dependencies are out of sync with live.
* Avoid establishing a dependency on any one IDE solution.
* Make it **easy**.
* Allow individual users to easily extend their virtual env with personal preferences, i.e support additional per-user packages where there's an element of personal choice involved (for example: I like to use `better-exceptions` but not everyone does).
* Create a convenient script runner cli to share useful functionality across the whole team

This tool handles all that via shell and simple python scripts and boils it all down to _four_ simple commands.

Note - **requires you to be using a macbook**.


## Usage

Once installed:

* `enter` turns on your work virtual envionment **and** warns where any specified dependencies are behind the versions deployed on live.
* `exit` turns it off.
* `sync` automatically updates all dependencies or syncronises your venv after a change of branch. Also updates to this latest version of this tool.
* `cli` (when you've got "my-work-environment" turned on, i.e after using `enter`) lists details and commands for all the built in scripts.

The virtual env is always based on the Pipfile.lock in [databaker-docker](https://github.com/GSS-Cogs/databaker-docker). By default it will use the `master` branch, but you can alter that via an evironment variable, example `export WORK_ENV_BRANCH=test` (you will then need to `sync`).

## Use with IDEs

When you `enter` your work env, you'll see `(my-work-environment)` before your terminal prompt, this means your virtual environment is active. Any command run on that terminal will have access to our full transform stack plus development packages and any personal preference packages you've specified.

For Jupyter labs or notebooks just have `(my-work-environment)` active when you open the notebook or lab.

For dev style IDE's you typically need to point the IDE at `my-work-environment`. For example, in vscode press `cmd+shift+p` then "select python interpreter" from there just select appropriately (the venv is named, just type "my-work-environment" and it'll pop up - I believe it's a simlar process for PyCharm).

## Installation

Please see [installation](https://github.com/GSS-Cogs/work-env/blob/master/installation.md).
