A convenience for managing a virtual env for work.

## Usage

* `sync` to create or update a virtual env with all dependencies installed.
* `enter` to turn it on.
* `exit` to turn it off.

You'll know when its turned on as `(my-work-environment)` will appear at the start of your command line.

_Note - it'll take 5-15 minutes to "sync". Be aware, go make a coffee._

## How do I make sure everything is up to date with the currently deployed Jenkins pipelines?

`sync`

## How do I use it

If you open a `jupyter lab` or `jupyter notebook` or `code` or `pycharm` you're got the `(my-work-environment)` virtual environment turned on, all the right thing we be installed.

## Install

You'll need to have `docker` and `pipenv` installed.

Note - you'll either be using bash or zshell (if your not sure you're probably using bash). To edit the bashrc or zshrc (as mentioned below) then open up the relevant file with your favourite text editor, example only: `code ~/.zshrc` or `nano ~/.bashrc`. If the file thus opened is empty, it's probably the wrong one or you've typo'd the command. Just add the command(s) to the end of the file, save and exit.

To install:
* git clone https://github.com/mikeAdamss/work-env ~/.work-env
* `chmod +x ~/.work-env/setup.sh`
* `chmod +x ~/.work-env/sync.sh`
* `alias enter=~/.work-env/enter.sh` to your bashrc or zshrc
* `alias sync=~/.work-env/sync.sh` to your bashrc or zshrc

Then close down and reopen your terminal.
