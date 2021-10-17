from git_automation import Git
import os


# def driver():
#     directories = dict()
#     default_project = 0
#     default_project_directory = None
#     t = 0
#     while t != 5:
#         directory = input("Enter Project Directory:")
#         if os.path.isdir(directory):
#             i = len(directories)
#             directories[i + 1] = directory.replace('\\', '\\\\')
#             t = t + 1
#         else:
#             print("Invalid directory")
#
#     for k, v in directories.items():
#         print(k, ":", v)
#
#     if len(directories) != 0:
#         default_project = 1
#         default_project_directory = directories[default_project]
#     print("Default Project Directory:", default_project_directory)
#
#     change_project = input("Change Project?:Y/N")
#     if change_project.lower() == 'y':
#         project = int(input("Enter the directory number:"))
#         if project in directories:
#             default_project = project
#             default_project_directory = directories[default_project]
#         else:
#             print("Get lost")
#     print("Default Project Directory:", default_project_directory)
#

class Directories:

    def __init__(self, git: Git):
        self.directories = dict()
        self.total_directories = len(self.directories)
        self.default_project_key = 0
        self.default_project_directory = None
        self.git = git

    def add_directory(self, directory):
        print(directory)
        print(os.path.isdir(directory))
        if os.path.isdir(directory):
            print(self.total_directories)
            self.directories[self.total_directories + 1] = directory.replace('\\', '\\\\')
            self.total_directories = len(self.directories)
            print(self.directories)
            if self.total_directories == 1:
                self.default_project_directory = self.directories[self.total_directories]
            return True
        else:
            return False

    def remove_directory(self, directory):

        if directory in self.directories:
            if self.default_project_key == directory:
                self.default_project_key = 0
            self.directories.pop(directory)

            directory_list = []
            for k, v in self.directories.items():
                directory_list.append(v)

            self.directories = dict()
            self.total_directories = 0
            for directory in directory_list:
                self.directories[self.total_directories + 1] = directory.replace('\\', '\\\\')
            self.total_directories = len(self.directories)
            return True
        else:
            return False

    def set_default_project(self, project):
        self.default_project_key = project
        self.default_project_directory = self.directories[self.default_project_key]
        self.git.project_directory = self.default_project_directory

    def display_directories(self):
        for k, v in self.directories.items():
            print(k, ":", v)
