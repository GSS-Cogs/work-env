
# Scripts

Various things I use occasionally but don't want to keep track of.


### Check Dependencies

Checks if the `gssutils` and `databaker` commit ids you have installed match the latest released as defined in the Pipfile.lock here: [https://github.com/GSS-Cogs/databaker-docker](https://github.com/GSS-Cogs/databaker-docker) 

_Note: if you're using the `work-env` helper this runs hands free whenever you `enter` the work-env, so you shouldn't need to manually run it, but you can always do `python3 ~/.work-env/scripts/check_dependencies.py` if you need to._


### Stopit

Clean the Jenkins build queue on our Jenkins server. You need to have two environment variables installed:

* JENKINS_USER - you jenkins user name,
* JENKINS_API_TOKEN - an api token you've created via the Jenkins UI.

You also need to have python **requests** installed (if whatever environment you're using in work doesn't have that you have larger problems that stopping Jenkins jobs).

To run via work env do `python3 ~/.work-env/scripts/stopit.py`

To run stand alone: `curl https://raw.githubusercontent.com/mikeAdamss/work-env/main/scripts/stopit.py --output stopit.py && python3 ./stopit.py && rm .
/stopit.py`

_Note: the second option is literally download>run>delete so subtle as a hammer but it works._
