
# Work Environment

A virtual environment managment tool for building and running our data transformation pipelines. 

* Fully automate dependency management.
* Loudly **warn users** where key dependencies are out of sync with live.
* Avoid establishing a dependency on any one IDE solution.
* Make it **easy**.
* Allow individual users to easily extend their virtual env with personal preferences, i.e support additional per-user packages where there's an element of personal choice involved (for example: I like to use `better-exceptions` but not everyone does).
* Create a convenient script runner cli to share useful functionality across the whole team

This tool handlers all that via shell and simple python scripts and boils it all down to _four_ simple commands.

Note - **requires you to be using a macbook**.


## Usage

Once installed:

* `enter` turns on your work virtual envionment **and** warns where any specified dependencies are behind the versions deployed on live. Once you've `enter`ed the venv "(my-work-environment)" will appear before your command prompt.
* `exit` turns it off.
* `sync` automatically updates all dependencies.
* `cli` (when you've got "my-work-environment" turned on) lists details and commands for all the built in scripts.

`sync` also updates to the latest version of this tool, so everything should be very hands off once you've completed installation.

_Note: `sync` is thorough but slow, don't do it trivially and do go make a coffee because it'll be 10-20 minutes._

## Use with IDEs

When you `enter` your work env, you'll see `(my-work-environment)` before your terminal prompt, this means your virtual environment is active. Any command run on that terminal will have access to our full transform stack plus development packages and any personal preference packages you've specified.

For Jupyter labs or notebooks just have `(my-work-envionment)` active when you open the notebook or lab.

For dev style IDE's you typically need to point the IDE at `my-work-environment`. For example, in vscode press `cmd+shift+p` then "select python interpreter" from there just select appropriately (it's a simlar process for PyCharm).

## Installation

Please see [installation](https://github.com/mikeAdamss/work-env/blob/main/installation.md).
