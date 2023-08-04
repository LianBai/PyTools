import subprocess

from watchdog.events import FileSystemEventHandler


class GitBranchHandler(FileSystemEventHandler):
    def __init__(self, path, callback):
        super().__init__()
        self.path = path
        self.current_branch = None
        self.callback = callback

    def on_modified(self, event):
        if event.src_path.endswith('.git/HEAD'):
            branch = self.get_current_branch()
            if branch != self.current_branch:
                self.callback()
                self.current_branch = branch

    def get_current_branch(self):
        output = subprocess.check_output(['git', 'symbolic-ref', '--short', 'HEAD'], cwd=self.path)
        return output.decode().strip()
