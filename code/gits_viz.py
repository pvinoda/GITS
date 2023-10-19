import subprocess
from subprocess import PIPE


def gits_viz_func(args):
    """
    Function that commit files as staged
    in the git command line internface
    Performs operation as similar to git
    commit command. Future additions : user can specify if the commit should be rejected , if the unit test fails.
    """
    try:
        subprocess_command = list()
        subprocess_command_1 = list()
        subprocess_command.append("git")
        subprocess_command_1 = list()
        subprocess_command_1.append("git")
        visualize_output = args.g
        output_graph_file_name = args.f
        output_graph_method = args.s
        subprocess_command.append("log")
        if visualize_output:
            subprocess_command_1.append("big-picture")
            if output_graph_method:
                subprocess_command_1.append("--simplify")
            subprocess_command_1.append("-o")
            if output_graph_file_name:
                subprocess_command_1.append(str(output_graph_file_name))
            else:
                subprocess_command_1.append("output.png")

        # print(subprocess_command)
        process = subprocess.Popen(
            subprocess_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        print(stdout.decode("UTF-8"))
        if len(subprocess_command_1) > 1:
            process_1 = subprocess.Popen(
                subprocess_command_1, stdout=PIPE, stderr=PIPE)
            stdout, stderr = process.communicate()

    except Exception as e:
        print("ERROR: gits viz command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
