
# Work Environment

A local environment managment tool designed to address the following.

* Fully automate dependency management.
* Avoid establishing a dependency on any one IDE solution.
* Make it **easy**.
* Allow individual users to easily extend their version of the envionrment to meet their own work processes.

## Managment

Once installed:

* `enter` turns on your work envionrment **and** warns where any dependencies are behind those deployed on live.
* `exit` turns it off.
* `sync` automatically updates all dependencies.

`sync` also updates to the latest version of this tool, so nothing should be required once you've completed installation.

## Use with IDEs

When you `enter` your work env, you'll see `(my-work-envionment)` before your terminal prompt, this means your virtual environment is active. Any command run on that terminal will have access to our full stack.

For Jupyter labs or notebooks just have `(my-work-envionment)` active when you open the notebook or lab.

For dev style IDE's you typically need to point the IDE at `my-work-environment`. For example, in vscode press `cmd+shift+p` then "select python interpreter" from there just selet appropriately (it's a simlar process for PyCharm).

## Installation

Please see [installation]([https://github.com/mikeAdamss/work-env/blob/main/installation.md](https://github.com/mikeAdamss/work-env/blob/main/installation.md))