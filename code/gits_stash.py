import subprocess
from subprocess import PIPE
import helper


def gits_stash(args):
    """
    This function is used to execute stash operations and also
    track your stashes easily in a visual manner
    Usage: gits stash
    """
    try:
        stash_decision = input("Do you want to label your stash to identify the contents in future? (Y/N)")
        if stash_decision == "Y":
            stash_label: str = input("Please enter the message label now !!\n")
            stash_executor: list = ["git", "stash", "save", stash_label]
        else:
            stash_executor: list = ["git", "stash"]

        process0 = subprocess.Popen(stash_executor,
                                    stdout=PIPE, stderr=PIPE)
        stdout, stderr = process0.communicate()
        print(stdout.decode("utf-8"))

        if stderr:
            print(f"Error encountered in saving stash file: {stderr}")

        stash_list_executor: list = ["git", "stash", "list"]

        process1 = subprocess.Popen(stash_list_executor, stdout=PIPE,
                                    stderr=PIPE)
        stdout, stderr = process1.communicate()

        print("Here's what your current stash looks like...\n")
        print(stdout.decode("utf-8"))

    except Exception as e:
        print("ERROR: gits stash command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
