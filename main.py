import os
import sys


def help(*args):
    exit()


def path_to_python(*args):
    if len(args) == 0:
        path_to_env = sys.prefix
        is_env = os.getenv
        if is_env is None:
            print(
                "You need to activate ENV first or use -n/--name flag to specify ENV name")
            exit()
    elif len(args) == 1:
        current_dir = os.getcwd()
        path_to_env = os.path.join(current_dir, args[0])
    else:
        print("Too much arguments, use -h/--help flag to get help")
        exit()
    return os.path.join(path_to_env, "bin", "python")


def write_shebang(file_name, name):
    if name:
        shebang = f"#!{path_to_python(name)}"
    else:
        shebang = f"#!{path_to_python()}"
    with open(os.path.join(os.getcwd(), file_name), "r+") as file:
        content = file.read()
        if "#!" in file.readline().strip():
            print("File already has shebang")
            exit()
        file.seek(0)
        file.write(f"{shebang}\n{content}")
    exit()


flags = {"-h": help, "--help": help, "-n": write_shebang}


def main(*args):
    if len(args) < 1:
        exit(help())
    if args[0] in ["-h", "--help"]:
        help()
    if args[0] in ["-n", "--name"]:
        if len(args) == 3:
            write_shebang(args[-1], args[1])
        elif len(args) < 3:
            print("Not enought arguments, see --help")
        elif len(args) > 3:
            print("Too much arguments, see --help")
    write_shebang(args[-1], None)


if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)
