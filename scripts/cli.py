from box import Box
import sys


def run_script(choice: str):
    """
    Runs another python script based on the name passed in
    via the choice str
    """

    commands = Box({
        "JenkinsClearQueue": ["jcq"],
        "CheckDependencies": ["check"]
    })

    # Simple default help
    if choice in ["", "-h", "--help", "help", "h"]:
        print("""
        Work env currently has the following scripts registered:

        Command               Short Form(s)       Description 
        --------------------------------------------------------------------------------
        JenkinsClearQueue     jcq                 Clear the current jenkins build queue

        CheckDependencies     check               Check your GSS-Cogs venv dependencies are 
                                                  up to date with the databaker-docker master

        Note: Casing in commands is ignored.
        """)


    elif choice.lower() in commands.JenkinsClearQueue or choice.lower() == "checkdependencies":
        from check_dependencies import check_deps
        check_deps()

    elif choice.lower() in commands.CheckDependencies or choice.lower() == "jenkinsclearqueue":
        from stopit import clean_jenkins_queue
        clean_jenkins_queue()

    else:
        print(f'''\nUnrecognised command {choice}. 
        
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
    except IndexError:
        choice = ""
    run_script(choice)