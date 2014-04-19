import sys

def ask_user_to_play_fizzbuzz():
    usr_inp = int(raw_input())

    # Validate user input based on given contraints.
    if (type(usr_inp) is not int) or (usr_inp <= 0):
        sys.stdout.write(">> Invalid entry. You must enter a positive integer. Try again" + '\n')
        ask_user_to_play_fizzbuzz()
    elif usr_inp >= 10**7:
        sys.stdout.write(">> Too big, try again with a smaller number. (Constraints: N < 10^7)" + '\n')
        ask_user_to_play_fizzbuzz()

    # Do FizzBuzz.
    for i in xrange(1, usr_inp + 1):
        positional_txt = ""
        positional_txt += "Fizz" if i % 3 == 0 else ""
        positional_txt += "Buzz" if i % 5 == 0 else ""
        if positional_txt:
            sys.stdout.write(positional_txt + '\n')
        else:
            sys.stdout.write(str(i) + '\n')

ask_user_to_play_fizzbuzz()
