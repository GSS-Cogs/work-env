A convenience for managing a virtual env for work.

## Usage

* `enter` to turn on a virtual env with all dependencies updated.
* `exit` to turn it off.

You'll know when its turned on as `(my-work-environment)` will appear at the start of your command line.

## How do I update things?

You don't, just `exit` then `enter` again, it'll update itself.

## Install

Is just an alias to some bash commands. you'll need to add the following to either your `~/.bashrc` or `~/.zshrc` file, depending on which you're using.

```bash
alias enter=start_dir=$(PWD) \
mkdir -p ~/.work-env/my-work-environment \
curl https://raw.githubusercontent.com/GSS-Cogs/databaker-docker/master/Pipfile -o ~/.work-env/my-work-environment/Pipfile \
curl https://raw.githubusercontent.com/GSS-Cogs/databaker-docker/master/Pipfile.lock -o ~/.work-env/my-work-environment/Pipfile.lock \
export PIPENV_PIPFILE=~/.work-env/my-work-environment/Pipfile \
pipenv install \
pipenv shell "/c cd $start_dir"
```

## Wizzy Extra Things

If you want to install additional python libraries that we'd use locally (but not on Jenkins) add them to `additional-requirements.txt`.

If you want to add pipenv scripts (sorta like a bash alias, but unique to the virtual env) you can add them in `./convenience/scripts.sh`. As an example I added a `csvlint` command that'll just work (no other installs or setup necessary).
