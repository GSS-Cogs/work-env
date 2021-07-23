from box import Box
import sys

# To add a new script see comments 1.), 2.) and 3.) below.
# one day this will be config :)

def run_script(choice: str, additional_args: list):
    """
    Runs another python script based on the name passed in
    via the choice str
    """

    # 1.) Define command plus short form alternative(s)
    # NOTE: do include lower case form of each key
    commands = Box({
        "JenkinsClearQueue": ["jcq", "jenkinsclearqueue"],
        "CheckDependencies": ["check", "checkdependencies"],
        "ViewSnippets": ["brain", "snip", "viewsnippets"]
    })

    # 2.) Simple default help
    if choice in ["", "-h", "--help", "help", "h"]:
        print("""
        Work env currently has the following scripts registered:

        Command               Short Form(s)       Description 
        --------------------------------------------------------------------------------
        JenkinsClearQueue     jcq                 Clear the current jenkins build queue

        CheckDependencies     check               Check your GSS-Cogs venv dependencies are 
                                                  up to date with the databaker-docker master

        ViewSnippets          brain, snip         View and filter code snippets by tag.

        Note: Casing in commands is ignored.
        """)


    # 3.) Import and call each specified script
    elif choice.lower() in commands.JenkinsClearQueue:
        from stopit import clean_jenkins_queue
        clean_jenkins_queue()

    elif choice.lower() in commands.CheckDependencies:
        from check_dependencies import check_deps
        check_deps()

    elif choice.lower() in commands.ViewSnippets:
        from brain import find_thoughts
        find_thoughts(additional_args)

    else:
        print(f'''\nUnrecognised command "{choice}". 
        
Use "cli" without arguments to see a list of your installed scripts. 
If you don\'t have a script you were expecting make sure to "sync" 
to update work-env. Current commands are:\n''')

        print("Long Form".ljust(20), "Short Form(s)")
        print("-----------------------------------------")

        for command, trigger_words in commands.items():
            print(command.ljust(20), ",".join(trigger_words))
        print()

if __name__ == "__main__":
    try:
        choice = sys.argv[1]
        additional_args = sys.argv[2:]
    except IndexError:
        choice = ""
        additional_args = []
    run_script(choice, additional_args)
