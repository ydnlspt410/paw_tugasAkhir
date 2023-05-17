from pickle import APPEND
from readline import append_history_file

flask = __name__

@append_history_file.route('/')
def main():
    a = 12