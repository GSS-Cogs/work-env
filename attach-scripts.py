
import os
this_path = os.path.dirname(os.path.realpath(__file__))

print("trying", this_path + "/my-work-environment/Pipfile")
new_pipfile_lines = []
with open(this_path + "/my-work-environment/Pipfile") as f:

    # find out where the [requires] bit of the pipfile starts
    for i, line in enumerate(f):
        if "[requires]" in line:
            req_line = i-1

with open(this_path + "/my-work-environment/Pipfile") as f:
    for i, line in enumerate(f):
        if i == req_line:
            new_pipfile_lines.append("\n")
            with open(this_path + "/convenience/scripts") as f2:
                for line2 in f2:
                    new_pipfile_lines.append(line2)
        new_pipfile_lines.append(line)

with open(this_path + "/my-work-environment/Pipfile", "w") as f:
    for line in new_pipfile_lines:
        f.write(line)

