from os import _exit
import os


class Dispatcher():

    def __init__(self, message=None, cycle=False):
        self.message = message
        self.options = []
        self.cycle = cycle
        if cycle:
            self.options.append(('Exit', lambda: _exit(0)))

    def add_option(self, description, function):
        self.options.append((description, function))

    def show_options(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.message:
            print(self.message)
        for i, (desc, _) in enumerate(self.options):
            print(("{0}) {1}".format(i, desc)))

    def run_once(self):
        self.show_options()
        choice = raw_input()
        valid_choices = range(len(self.options))
        while not choice.isdigit() or int(choice) not in valid_choices:
            errormsg = '\nPlease select the number (0-{0}) corresponding to your desired option.\n'
            choice = raw_input(errormsg.format(len(self.options)))
            
        option_fn = self.options[int(choice)][1]
        option_fn()
        
        
    def run(self):
        while self.cycle:
            self.run_once()
        else:
            self.run_once()
