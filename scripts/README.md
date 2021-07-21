
# Scripts

Various things I use occasionally but don't want to keep track of.

These are intended for use in my my `work-env` toy which has all the correct dependencies, but I've included standalone one-liners as preferences tend to vary (if you're running as stand alone scripts you'll just need to have the dependencies installed, python will tell you fairly promptly if you don't. I'm keeping everything as light touch as I can).

The one liners are all variations of download>run>delete, which while not exactly subtle its viable.

## Cli

If you're using `work-env` you can install as follows (if new scripts are added they'll become availible automatically when you `sync`).

Using **bash** run `echo alias cli="python3 ~/.work-env/scripts/cli.py"  >> ~/.bashrc`

_or_

Using **zshell** run `echo alias cli="python3 ~/.work-env/scripts/cli.py"  >> ~/.zshrc`

Then restart your terminal. From the on when you type `cli` it'll give you a help screen listing the commands and calling args.

A few of these scripts will require environment variables and the like (things that interact with Jenkins, git etc). If you don't have them exported the script will tell you what you're missing and how to set it up when you go to run it.


### Check Dependencies

Checks if the `gssutils` and `databaker` commit ids you have installed match the latest released as defined in the Pipfile.lock here: [https://github.com/GSS-Cogs/databaker-docker](https://github.com/GSS-Cogs/databaker-docker) 

_Note: if you're using the `work-env` helper this runs hands free whenever you `enter` the work-env, so you shouldn't need to manually run it.

**Stand alone one liner:** `curl https://raw.githubusercontent.com/mikeAdamss/work-env/main/scripts/check_dependencies.py --output check_dependencies.py && python3 ./check_dependencies.py && rm ./check_dependencies.py`

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

You also need to have python **requests** installed (if whatever environment you're using in work doesn't have that you have larger problems that stopping Jenkins jobs).

**Stand alone one liner:** `curl https://raw.githubusercontent.com/mikeAdamss/work-env/main/scripts/stopit.py --output stopit.py && python3 ./stopit.py && rm ./stopit.py`
