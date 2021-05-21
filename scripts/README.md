
# Scripts

Various things I use occasionally but don't want to keep track of.

These are intended for use in my my `work-env` toy which has all the correct dependencies, but I've included standalone one-liners as preferences tend to vary (if you're running stand alone you'll just need to have the dependencies installed, python will tell you fairly promptly if you don't).

The one liners are all variations of download>run>delete, which while not exactly subtle its viable and good enough for now.

_Note: will be adding a convenience ci when there's enough tricks in this bag to warrant it but its dependant on bordeome and free time._


### Check Dependencies

Checks if the `gssutils` and `databaker` commit ids you have installed match the latest released as defined in the Pipfile.lock here: [https://github.com/GSS-Cogs/databaker-docker](https://github.com/GSS-Cogs/databaker-docker) 

_Note: if you're using the `work-env` helper this runs hands free whenever you `enter` the work-env, so you shouldn't need to manually run it, but you can always do `python3 ~/.work-env/scripts/check_dependencies.py` if you need to._

**Stand alone one liner:** `curl https://raw.githubusercontent.com/mikeAdamss/work-env/main/scripts/check_dependencies.py --output check_dependencies.py && python3 ./check_dependencies.py && rm ./check_dependencies.py`

### Stopit

Clean the Jenkins build queue on our Jenkins server. You need to have two environment variables installed:

* JENKINS_USER - you jenkins user name,
* JENKINS_API_TOKEN - an api token you've created via the Jenkins UI.

You also need to have python **requests** installed (if whatever environment you're using in work doesn't have that you have larger problems that stopping Jenkins jobs).

To run via work env do `python3 ~/.work-env/scripts/stopit.py`

**Stand alone one liner:** `curl https://raw.githubusercontent.com/mikeAdamss/work-env/main/scripts/stopit.py --output stopit.py && python3 ./stopit.py && rm ./stopit.py`
