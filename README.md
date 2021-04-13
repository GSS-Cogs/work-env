A convenience for managing a virtual env for work.

## Usage

* `enter` to turn on a virtual env with all dependencies updated.
* `exit` to turn it off.

You'll know when its turned on as `(my-work-environment)` will appear at the start of your command line.

## How do I update things?

You don't, just `exit` then `enter` again, it'll update itself.

## Install

It's just an alias to some bash commands. you'll need to add the following to either your `~/.bashrc` or `~/.zshrc` file, depending on which you're using (just do eg `code ~./zshrc` and add it at the bottom then save and exit).

```bash]
alias enter=start_dir=$(PWD) \
mkdir -p ~/.work-env/my-work-environment \
curl https://raw.githubusercontent.com/GSS-Cogs/databaker-docker/master/Pipfile -o ~/.work-env/my-work-environment/Pipfile \
curl https://raw.githubusercontent.com/GSS-Cogs/databaker-docker/master/Pipfile.lock -o ~/.work-env/my-work-environment/Pipfile.lock \
export PIPENV_PIPFILE=~/.work-env//my-work-environment/Pipfile \
pipenv install \
pipenv shell "/c cd $start_dir"
```
