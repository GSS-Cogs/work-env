
# Installation

You'll need to have `pipenv` installed.

I'd also **strongly recommend** you manage your python installs with [pyenv](https://github.com/pyenv/pyenv) (so you can easily change when the projects bumps its in-use python version).

Before you install `work-env` you need to know if your terminal is using bash of zshell, you can check this via `echo $SHELL`. 

---

To install:
* `git clone https://github.com/mikeAdamss/work-env ~/.work-env`

Then **if you're using zshell**
* `chmod +x ~/.work-env/setupzshell.sh`
* `~/.work-env/setupzshell.sh`

Or **if you're using bash**
* `chmod +x ~/.work-env/setupbash.sh`
* `~/.work-env/setupbash.sh`

Then close down and reopen your terminal.

You'll need to do at last one `sync` before you can `enter` the virtual env.

## Custom Environments

You can add additional python dependencies by specifing a python requirments (.txt) file path (or url) via setting the envionment variable `WORKENV_CUSTOM_REQS`.

For covenience I've added a directory to this repo that my own extras are in, which ive got exported with:

```
export WORKENV_CUSTOM_REQS="https://raw.githubusercontent.com/mikeAdamss/work-env/main/user-reqs/mike.txt"
```

Which installs `better-exceptions` (at time of writing) on top of the standard work dependencies.

## Scripts

I'm gradually adding useful scripts to this work-env but its needs one more line of setup. To see what they are and set that up see [https://github.com/mikeAdamss/work-env/blob/main/scripts/README.md](https://github.com/mikeAdamss/work-env/blob/main/scripts/README.md).