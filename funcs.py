def func_read(filepath="todos.txt"):
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def func_write(todos_arg, filepath="todos.txt"):
    with open(filepath, "w") as write:
        write.writelines(todos_arg)
    return write