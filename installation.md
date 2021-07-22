
# Installation

You'll need to have `pipenv` installed.

I'd also **strongly recommend** you manage your underlying python install with [pyenv](https://github.com/pyenv/pyenv) (so you can easily change when the projects bumps its in-use python version).

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

You can add additional python dependencies by specifying a python requirments (.txt) file path (or url to same) via setting the envionment variable `WORKENV_CUSTOM_REQS`.

For example: I've added a directory to this repo that my own extras are in which I've currently got exported via:

```
export WORKENV_CUSTOM_REQS="https://raw.githubusercontent.com/mikeAdamss/work-env/main/user-reqs/mike.txt"
```

Which (at time of writing) installs my own preference of using `better-exceptions` on top of the standard work dependencies.

Feel free to pr your own preference choices in 👍

## Scripts

I'm gradually adding useful scripts to this work-env. They are installed (and updated when new ones are added) automatically. For more infomation see [scripts](https://github.com/mikeAdamss/work-env/blob/main/scripts/README.md).
