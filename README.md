A convenience for managing a virtual env for work.

## Usage

* `sync` to create or update a virtual env with all dependencies installed.
* `enter` to turn it on.
* `exit` to turn it off.

You'll know when its turned on as `(my-work-environment)` will appear at the start of your command line.

_Note - it'll take 5-15 minutes to "sync". Be aware, go make a coffee._

## How do I use it

If you open a `jupyter lab` or `jupyter notebook` or `code` or `pycharm` (via the terminal) while you've got `(my-work-environment)` turned on, all the right thing we be installed.

## How do I know if I need to update my dependencies?

Every time you `enter` it checks, if you're out of date it'll shout at you.

## How do I update my dependencies?

`sync`

## Install

You'll need to have `docker` and `pipenv` installed.

To install:
* git clone https://github.com/mikeAdamss/work-env ~/.work-env
* `chmod +x ~/.work-env/setup.sh`
* IF you're using bash, do `~/.work-env/setupbash.sh` **or** IF you're using zshell, do `~/.work-env/setupzshell.sh`

Then close down and reopen your terminal.
ß