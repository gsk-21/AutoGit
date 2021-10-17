import subprocess as sp
from subprocess import Popen, PIPE


class Git:

    def __init__(self, project_directory=None):
        self.project_directory = str(project_directory) + ' '
        self.git = ['git']

        self.init_cmd = ['init']

        self.pull_cmd = ['pull']
        self.pull_origin_cmd = ['pull','origin']
        self.pull_upstream_cmd = ['pull','upstream']

        self.push_cmd = ['push']
        self.push_origin_cmd = ['push','origin']

        self.stash_cmd = ['stash']
        self.stash_apply_cmd = ['stash','apply']

        self.checkout_cmd = ['checkout']
        self.checkout_new_cmd = ['checkout','-b']

        self.add_all_cmd = ['add', '.']

        self.commit_cmd = ['commit', '-m']
        self.commit_ammend_cmd = ['commit', '--amend']

        self.fetch_upstream_cmd = ['fetch', 'upstream']

        self.clone_cmd = ['clone']

        self.status_cmd = ['status']

        self.remove_index_lock_cmd = ['rm', '-f', '.git/index.lock']

        # print("Project Directory:", self.project_directory)

    def run_process(self, task):
        result = {'exit_code': None, 'stdout': None, 'stderr': None}
        try:
            cmd = self.git + task
            process = sp.Popen(cmd, stderr=PIPE, stdout=PIPE, cwd=self.project_directory)
            stdout, stderr = process.communicate()
            exit_code = process.wait()
            result['exit_code'] = exit_code
            result['stdout'] = stdout.decode('utf-8')
            result['stderr'] = stderr.decode('utf-8')
        except Exception as e:
            print("Error Occured")
            print(e)
            result['exit_code'] = 123
            result['stderr'] = str(e)
        return result

    def init(self, init_project_name=""):
        init_cmd = []
        init_cmd = self.init_cmd
        init_cmd.append(str(init_project_name))
        return self.run_process(init_cmd)

    def pull(self):
        return self.run_process(self.pull_cmd)

    def pull_upstream(self,branchname):
        self.pull_upstream_cmd.append(str(branchname))
        print(self.pull_upstream_cmd)
        op = self.run_process(self.pull_upstream_cmd)
        self.pull_upstream_cmd.pop()
        return op


    def pull_origin(self,branchname):
        self.pull_origin_cmd.append(str(branchname))
        print(self.pull_origin_cmd)
        op = self.run_process(self.pull_origin_cmd)
        self.pull_origin_cmd.pop()
        return op


    def checkout(self,branchname):
        self.checkout_cmd.append(str(branchname))
        print(self.checkout_cmd)
        op = self.run_process(self.checkout_cmd)
        self.checkout_cmd.pop()
        return op


    def checkout_new(self,branchname):
        self.checkout_new_cmd.append(str(branchname))
        print(self.checkout_new_cmd)
        op = self.run_process(self.checkout_new_cmd)
        self.checkout_new_cmd.pop()
        return op

    def push(self):
        return self.run_process(self.push_cmd)

    def push_origin(self,branchname):
        self.push_origin_cmd.append((str(branchname)))
        print(self.push_origin_cmd)
        op = self.run_process(self.push_origin_cmd)
        self.push_origin_cmd.pop()
        return op

    def stash(self):
        return self.run_process(self.stash_cmd)

    def stash_apply(self):
        return self.run_process(self.stash_apply_cmd)

    def add_all(self):
        return self.run_process(self.add_all_cmd)

    def commit(self, message):
        print("Commit Message:", message)
        self.commit_cmd.append(str(message))
        print(self.commit_cmd)
        op = self.run_process(self.commit_cmd)
        self.commit_cmd.pop()
        return op

    def clone(self, clone_path="https://github.com/gsk-21/git-automation.git"):
        clone_cmd = []
        clone_cmd = self.clone_cmd
        clone_cmd.append(str(clone_path))
        return self.run_process(clone_cmd)

    def status(self):
        return self.run_process(self.status_cmd)

    def fetch_upstream(self,branchname):
        self.fetch_upstream_cmd.append(str(branchname))
        print(self.fetch_upstream_cmd)
        op = self.run_process(self.fetch_upstream_cmd)
        self.fetch_upstream_cmd.pop()
        return op

    def perform_git(self, cmd):
        try:
            operations = {
                'pull': self.pull,
                'push': self.push,
                'add': self.add_all,
                'commit': self.commit,
                'clone': self.clone,
                'status': self.status
            }

            if cmd == 'commit':
                msg = input('Add a summary to commit:')
                print(msg)
                return self.commit(msg)
            elif cmd == 'init':
                project_name = input("Provide a project name:")
                print(project_name)
                return self.init(project_name)
            elif cmd == 'clone':
                repo = input("Provide the repo name to clone")
                print(repo)
                return self.clone(repo)
            else:
                return operations[cmd]()

        except Exception as e:
            result = {'exit_code': None, 'stdout': None, 'stderr': None}
            result['exit_code'] = 123
            result['stderr'] = str(e)
            return result
