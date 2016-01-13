from dispatcher import Dispatcher
import roadtrip_crisis as SC
import national_defense as ND
import EPA


def main():
    # Top level dispatcher
    intro_msg = ('This simulation will simulate the thought process of an enlightened mind.\n'
                 'From this menu, select a complex issue you wish to solve. ')
    top_level = Dispatcher(intro_msg, cycle=True)
    top_level.add_option('Environmental Crisis', EPA.run)
    top_level.add_option('Syrian Crisis', SC.run)
    top_level.add_option('National Defense', ND.run)
    top_level.run()

main()
