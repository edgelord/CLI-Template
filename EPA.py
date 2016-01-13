from dispatcher import Dispatcher


def diversify():
    print("This may not solve the problem, but it's a good start.")
    raw_input('\nPress return to coninue.')

def protect_workers():
    print("Those EPA employees certainly earned it.")
    raw_input('\nPress return to coninue.')

def triple_funding():
    print("The money well be handled responsibly.")
    raw_input('\nPress return to coninue.')

def gun_control():
    print('Stop complaining, you can still own muskets.\n'
          '(But owning black powder is illegal. Common Sense.)')
    raw_input('\nPress return to coninue.')

def run():
    message = ('The EPA just dumped a bunch of shit in the Colorado River.\n'
               'The Water Supply for 45 million Americans will be tainted for decades.\n'
               'Clearly we must:')

    d = Dispatcher(message)
    d.add_option('Hire more blacks and hispanics.', diversify)
    d.add_option('Give EPA workers huge pensions.', protect_workers)
    d.add_option('Increase the budget for the EPA.', triple_funding)
    d.add_option('Enact common sense gun regulations.', gun_control)
    d.run()
