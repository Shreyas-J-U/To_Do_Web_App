FILEPATH = "todos_items.txt"
def get_todos(filepath = FILEPATH):
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos

def write_todos(todos_argument, filepath = FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos_argument)

if (__name__ == "__main__"):
    print("HELLOW")
    print(get_todos())
