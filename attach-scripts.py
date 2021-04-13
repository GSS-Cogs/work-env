
with open("Pipfile") as f:

    # find out where the [requires] bit of the pipfile starts
    for i, line in enumerate(f):
        if "[requires]" in line:
            req_line = i-1

    new_pipfile_lines = []
    for i, line in enumerate(f):
        if i == req_line:
            with open("./convenience/scripts") as f2:
                for line2 in f2:
                    new_pipfile_lines.append(line2)
        new_pipfile_lines.append(line)

with open("Pipfile2") as f:
    for line in new_pipfile_lines:
        f.write(line, "\n")
