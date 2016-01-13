from dispatcher import Dispatcher


def diversify():
    print('Good choice. Diversity is our greatest strength.')
    raw_input('\nPress return to coninue.')

def combat_islamophobia():
    print('We cannot have peace and equality in the west until '
          'everyone is wearing burka.')
    raw_input('\nPress return to coninue.')

def gun_control():
    print('The answer is always gun control.')
    raw_input('\nPress return to coninue.')
    
def cultural_suicide():
    print('The answer is always gun control.\n'
          'Allahu Akbar.')
    raw_input('\nPress return to coninue.')
    
    
def run():
    message = ('A father left peaceful territory in Turkey '
               'so he could get free dental care in Germany.'
               '\nHis toddler drowned.\nClearly we must:')

    d = Dispatcher(message)
    d.add_option('Allow millions of refugees to pour into the west', diversify)
    d.add_option('Blame white women when migrants attempt'
                 ' to culturally enrich them.', combat_islamophobia)
    d.add_option('Enact common sense gun regulations.', gun_control)
    d.add_option('Disarm the populace before importing ISIS.', cultural_suicide)
    d.run()
