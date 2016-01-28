from dispatcher import Dispatcher
import roadtrip_crisis as SC
import national_defense as ND
import EPA


# Template used for demo functions
def user_input_template(fn, T=str, prompt='', err="Input was invalid."):
    inp = raw_input(prompt)
    try:
        x = T(inp)
        print("The answer is {0}\n".format(fn(x)))
    except:
        print(err)

# Math functions
def square_input():
    square = lambda x: x**2
    user_input_template(square, T=float, prompt='Enter the number you wish to square. '
                        , err= 'Please enter a valid number.')
def double_input():
    double = lambda x: x*2
    user_input_template(double, T=float, prompt='Enter the number you wish to double. '
                        , err= 'Please enter a valid number.')
def negate_input():
    double = lambda x: -x
    user_input_template(double, T=float, prompt='Enter the number you wish to negate. '
                        , err= 'Please enter a valid number.')

# String functions
def downcase_input():
    downcase = lambda s: s.lower()
    user_input_template(downcase, prompt='Enter the word(s) you wish to downcase. ')


def repeat_input():
    downcase = lambda s: s*3
    user_input_template(downcase, prompt='Enter the word(s) you wish to have repeated. ')

def reverse_input():
    downcase = lambda s: s[::-1]
    user_input_template(downcase, prompt='Enter the word(s) you wish to have reversed. ')


# Dispatcher demo
def main():
    # Setting up dispatcher for math operations.
    math_opts = [('Square', square_input),
                 ('Double', double_input),
                 ('Negate', negate_input)]
    math_level = Dispatcher("Which math function would you like to use? ", options=math_opts)

    # Setting up dispatcher for string operations
    str_opts = [('Downcase', downcase_input),
                ('Repeat', repeat_input),
                ('Reverse',reverse_input)]
    str_level = Dispatcher("Which string operation do you need? 1", options = str_opts)

    # Top level dispatcher
    top_opts = [('Math functions', math_level.run),
                ('String functions', str_level.run)]
    top_level = Dispatcher('CLI Template demo', cycle=True, clear=False, options=top_opts)
    top_level.run()

if __name__ == "__main__":
    main()
