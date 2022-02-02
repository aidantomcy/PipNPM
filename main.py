import os
import sys
import json


def init():
    json_data = """{
  "name": "pipnpm",
  "description": "",
  "scripts": {
    "testScript": "echo Hello World"
  },
  "requirements": {},
  "author": ""
}
"""

    if not os.path.exists("pyproject.json"):
        with open("pyproject.json", "w") as file:
            file.write(json_data)
        print("Created pyproject.json")
        print(json_data)
    else:
        with open("pyproject.json", "w") as file:
            file.seek(0)
            file.write(json_data)
            file.truncate()
        print("Created pyproject.json")
        print(json_data)


def install():
    pass


def list_packages():
    pass


def main():
    try:
        command = sys.argv[1]
        if command == "" or command == "help":
            print("PipNPM v1.0")
            print("Usage: pipnpm <command>")
            print("\nCommands:")
            print("init - Initialize a new project")
            print("install - Install requirements")
            print("list - List requirements")
            print("help - Show help")
        elif command == "init":
            init()
        elif command == "install":
            install()
        elif command == "list":
            list_packages()
    except IndexError:
        pass


if __name__ == "__main__":
    main()