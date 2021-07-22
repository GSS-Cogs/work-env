
# Scripts

Various things I use occasionally but don't want to keep track of.

## Install The Cli

If you're using `work-env` you can install as follows (if new scripts are added they'll become availible automatically when you `sync`).

Using **bash** run `echo alias cli="python3 ~/.work-env/scripts/cli.py"  >> ~/.bashrc`

_or_

Using **zshell** run `echo alias cli="python3 ~/.work-env/scripts/cli.py"  >> ~/.zshrc`

Then restart your terminal. From the on when you type `cli` while `my-work-environemnt` is active it'll give you a help screen listing the commands and calling args.

A few of these scripts will require environment variables and the like (things that interact with Jenkins, git etc). If you don't have them exported the script will tell you what you're missing and how to set it up when you go to run it.


### Check Dependencies

Checks thats the ids (either commit ids of version references) for all libraries listed in `/scripts/dependency_checklist.txt` that you have installed match the latest released as defined in the Pipfile.lock here: [https://github.com/GSS-Cogs/databaker-docker](https://github.com/GSS-Cogs/databaker-docker).

_Note - this runs automatically wheneer you `enter` so it's rare that you'd need to call this from the cli directly._


### Clear Jenkins Build Queue

Clears the Jenkins build queue on our Jenkins server. You need to have two environment variables exported:

* JENKINS_USER - you jenkins user ID, you can find this by clicking your name after your logging into our Jenkins server.
* JENKINS_API_TOKEN - an api token you've created via the Jenkins UI. To make one click the little down arrow next to your name on the Jenkins UI (it'll appear when you hover over your name after logging in). Select `configure` then add a new token.

Export both variables via:
```sh
export JENKINS_USER=<your user name>
export JENKINS_API_TOKEN=<your user token>
```

I'd suggest you also those lines to `~/.bashrc` or `~/.zshrc` directly, save repeating yourself if you need to clear the queue again.

You can also run this one with a **stand alone one liner:**

```curl https://raw.githubusercontent.com/mikeAdamss/work-env/main/scripts/stopit.py --output stopit.py && python3 ./stopit.py && rm ./stopit.py```
