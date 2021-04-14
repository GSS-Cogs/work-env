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

You'll need to know if your terminal is using bash of zshell, you can check this via `echo $SHELL`. 

To install:
* git clone https://github.com/mikeAdamss/work-env ~/.work-env

Then **if you're using zshell**
* `chmod +x ~/.work-env/setupzshell.sh`
* `~/.work-env/setupzshell.sh`

Or **if you're using bash**
* `chmod +x ~/.work-env/setupbash.sh`
* `~/.work-env/setupbash.sh`

Then close down and reopen your terminal.
