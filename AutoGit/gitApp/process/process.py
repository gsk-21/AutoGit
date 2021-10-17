from git_automation import Git
from projects import Directories
import os
import sys


class Process:
    def __init__(self, git: Git, directories: Directories):
        self.default_project_name = None
        self.default_project_directory = directories.default_project_directory
        self.git = git
        self.directories = directories
        self.commands = ['pull', 'push', 'add', 'status', 'init', 'commit', 'clone']
        self.commands_with_msg = ['init', 'commit', 'clone']
        self.yes = ['yes', 'y', 'yup', 'yeah', 'yes', 'yep']
        self.no = ['n', 'no', 'nah', 'nope']

    def set_default_project_name(self, project_name):
        self.default_project_name = project_name

    def get_default_project_name(self):
        return self.default_project_name

    def set_default_project_directory(self, project_key):
        self.default_project_directory = self.directories.directories[project_key]
        self.git.project_directory = self.default_project_directory

    def get_default_project_directory(self):
        return self.default_project_directory

    def run_process(self):
        print("\nPROJECT DIRECTORY:")
        print(self.default_project_directory)
        while self.default_project_directory is None:
            directory = input("Enter a valid Project directory:")
            if self.directories.add_directory(directory):
                self.directories.display_directories()
                self.default_project_directory = self.directories.default_project_directory
                print("\nPROJECT DIRECTORY:")
                print(self.default_project_directory)
        while True:
            cmd = None
            user_input = input("Enter your command:")
            if user_input == 'q':
                sys.exit(0)
            for i in self.commands:
                if i in user_input:
                    cmd = i
                    print("Command:", cmd)
                    confirm = input("Do you want to " + cmd + "?")
                    if confirm in self.yes:
                        op = self.git.perform_git(cmd)
                        printer(op)

                    elif confirm in self.no:
                        print("Okay")
                    else:
                        print("No confirmation provide")
                    break


def printer(op):
    # print(op)
    print("Exit code:", op['exit_code'])
    print('stdout:', op['stdout'])
    print('stderr:', op['stderr'])
    print("#" * 80)
    print()