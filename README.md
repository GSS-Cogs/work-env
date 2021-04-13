A convenience for managing a virtual env for work.

## Usage

* `sync` to create or update a virtual env with all dependencies installed.
* `enter` to turn it on.
* `exit` to turn it off.

You'll know when its turned on as `(my-work-environment)` will appear at the start of your command line.

_Note - it'll take 5-15 minutes to "sync". Be aware, go make a coffee._

## How do I make sure everything is up to date with the currently deployed Jenkins pipelines?

`sync`

## Install

You'll need to have `docker` and `pipenv` installed.

Note - you'll either be using bash or zshell (if your not sure you're probably using bash). To edit the bashrc or zshellrc (as mentioned below) then open up the relevant file with your favourite text editor, example only: `code ~/.zshrc` or `nano ~/.bashrc`. If the file thus opened is empty, it's probably the wrong one or you've typo'd the command.

Installation:
* `mkdir -p ~/.work-env`
* `curl https://raw.githubusercontent.com/mikeAdamss/work-env/main/setup.sh -o ~/.work-env/sync.sh`
* `curl https://raw.githubusercontent.com/mikeAdamss/work-env/main/setup.sh -o ~/.work-env/enter.sh`
* `chmod +x ~/.work-env/setup.sh`
* `chmod +x ~/.work-env/sync.sh`
* `alias enter=~/.work-env/enter.sh` to your bashrc or zshrc
* `alias sync=~/.work-env/sync.sh` to your bashrc or zshrc

Then close down and reopen your terminal.

## Wizzy Extra Things

If you want to install additional python libraries that we'd use locally (but not on Jenkins) add them to `additional-requirements.txt`.

If you want to add pipenv scripts (sorta like a bash alias, but unique to the virtual env) you can add them in `./convenience/scripts.sh`. As an example I added a `csvlint` command that'll just work out of the box (no other installs or setup necessary).

If you want to be more clever than that, you can add python scripts to `./convenience/python/<scrip-name>` and make them callable on the command line via the prior comment on scripts. Again I've added an example.

If you're trying to do anything more heavy than running a docker container or a few scripts, this is probably not the right avenue.  
