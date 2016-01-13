from dispatcher import Dispatcher


def diversify():
    print('We need women and homosexuals in the military to ensure it functions properly.')
    raw_input('\n Press return to coninue.')

def combat_islamophobia():
    print('We cannot have peace and equality in the west until'
          'everyone is wearing burka.')
    raw_input('\n Press return to coninue.')

def gun_control():
    print('As our glorious leader has said, stopping terrorists'
          'is "not that different" from stopping mass shootings')
    raw_input('\n Press return to coninue.')

def destroy_leadership():
    print ('Excellent progress being made on this front.'
           'Check out http://www.rense.com/general96/listof.html for more details')
    raw_input('\n Press return to coninue.')

def run():
    message = ('With the world on fire, national defense has become a top priority.\n'
               'Clearly we must:')

    d = Dispatcher(message)
    d.add_option('Get women and homosexuals to enlist in the military.', diversify)
    d.add_option('Fire top generals for no reason', destroy_leadership)
    d.add_option('Continue accepting immigrants and refugees from radicalized territories.',
                 combat_islamophobia)
    d.add_option('Enact common sense gun regulations.', gun_control)
    d.run()
