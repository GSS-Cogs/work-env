
# Work Environment

A local environment managment tool designed to address the following.

* Fully automate dependency management.
* Loudly **warn users** where key dependencies are out of sync with live.
* Avoid establishing a dependency on any one IDE solution.
* Make it **easy**.
* Allow individual users to easily extend their version of the envionrment to meet their own work processes.
* Create a central scripts repository for all users.

### How does it work?

We're using the `Pipfile.lock` that informs the (databaker-docker)[https://github.com/GSS-Cogs/databaker-docker] container (the container Jenkins uses to run data transforms) as our principle source of truth.

On top of that we add any standard team-wide python packages we only want when developing, plus any per-uspecific-ser packages (for example, I use better-exception in my evn, but not everyone will - work-env supports this).

## Usage

Once installed:

* `enter` turns on your work virtual envionment **and** warns where any specified dependencies are behind the versions deployed on live.
* `exit` turns it off.
* `sync` automatically updates all dependencies.

`sync` also updates to the latest version of this tool, so neverything should be very hands off once you've completed installation.

_Note: `sync` is thorough but slow, don't do it trivially and do go make a coffee because it'll be 10-20 minutes._

## Use with IDEs

When you `enter` your work env, you'll see `(my-work-environment)` before your terminal prompt, this means your virtual environment is active. Any command run on that terminal will have access to our full stack.

For Jupyter labs or notebooks just have `(my-work-envionment)` active when you open the notebook or lab.

For dev style IDE's you typically need to point the IDE at `my-work-environment`. For example, in vscode press `cmd+shift+p` then "select python interpreter" from there just select appropriately (it's a simlar process for PyCharm).

## Installation

Please see [installation](https://github.com/mikeAdamss/work-env/blob/main/installation.md).
