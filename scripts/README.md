
# Scripts

Various things I use occasionally but don't want to keep track of. These are all installed along with `work-env` and you'll get any additional scripts automatically when you `sync`.


## Script Usage

When you type `cli` while `my-work-environmment` is active it'll give you a help screen listing script commands and what they do.

A few of these scripts will require environment variables and the like (things that interact with Jenkins, git etc). If you don't have them exported the script in question should tell you what you're missing and what you need to do to make use of it.

---
## Scripts

Currently installed scripts in no particular order.


#### Script: Check Dependencies

Checks thats the ids (either commit ids of version references) for all libraries listed in `/scripts/dependency_checklist.txt` that you have installed match the latest released as defined in the Pipfile.lock here: [https://github.com/GSS-Cogs/databaker-docker](https://github.com/GSS-Cogs/databaker-docker).

_Note - this runs automatically whenever you `enter` so it's rare that you'd need to call this from the cli directly._



#### Script: Clear Jenkins Build Queue

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


#### Script: Snippet Manager (Brain)

A tag based cli snippet manager. Each snippet is stored as a "thought" (an approriately named txt file) inside `/scripts/thoughts` and the format is pretty self explanatory. To add additional snippets you can either:

* PR them at the main branch (recommended).
* Expand the shared snippets by exporting the path to a local directory of your own personal "thoughts" using the environment variable `ADDITIONAL_BRAIN_SNIPPETS`.

Note: the odd name is because its a copy paste from another somewhat facetious pet project called [brain](https://github.com/mikeAdamss/brain) and (at some point) it'll just be installed from there rather than the current copy-paste over.
