
new_pipfile_lines = []
with open("Pipfile") as f:

    # find out where the [requires] bit of the pipfile starts
    for i, line in enumerate(f):
        if "[requires]" in line:
            req_line = i-1

with open("Pipfile") as f:
    for i, line in enumerate(f):
        if i == req_line:
            new_pipfile_lines.append("\n")
            with open("./convenience/scripts") as f2:
                for line2 in f2:
                    new_pipfile_lines.append(line2)
        new_pipfile_lines.append(line)

with open("Pipfile2", "w") as f:
    for line in new_pipfile_lines:
        f.write(line)
