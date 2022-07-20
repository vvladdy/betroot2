print('Task 1')


# A Person class

# Make a class called Person. Make the __init__() method take firstname,
# lastname, and age as parameters and add them as attributes. Make another
# method called talk() which makes prints a greeting from the person
# containing, for example like this: “Hello, my name is Carl Johnson and  I’m
# 26 years old”.

class Person:

    def __init__(self, firstname, lastname, age):
        self.name = firstname
        self.lastname = lastname
        self.age = age

    def showinfo(self):
        print(
            f'Hello, my name is {self.name} {self.lastname} and  I’m {self.age} '
            f'years old')


if __name__ == '__main__':
    dude = Person('Max', 'Johnson', 30)
    dude1 = Person('Alexey', 'Ivanov', 28)
    dude.showinfo()
    dude1.showinfo()

print('\nTask 2')


# Doggy age

# Create a class Dog with class attribute `age_factor` equals to 7.  Make
# __init__() which takes values for a dog’s age. Then create a method
# `human_age` which returns the dog’s age in human equivalent.

class DoggyAge:

    def __init__(self, dogname, man_age, age_factor=7):
        self.dogage = None
        self.dog_name = dogname
        self.human_age = man_age
        self.age_factor = age_factor

    def calc(self):
        self.dogage = round((self.human_age / self.age_factor), 2)

    def showinfo(self):
        print(f"Age of dog '{self.dog_name}' in human's {self.human_age} years "
              f"equivalent dogs {self.dogage} years")


if __name__ == "__main__":
    dog = DoggyAge('Jack', 70)
    dog1 = DoggyAge('Dog', 27)
    dog.calc()
    dog1.calc()
    dog.showinfo()
    dog1.showinfo()


print('\nTask 3')

# TV controller
#
# Create a simple prototype of a TV controller in Python. It’ll use the
# following commands:

# - first_channel() - turns on the first channel from the list.
# - last_channel() - turns on the last channel from the list.
# - turn_channel(N) - turns on the N channel. Pay attention that the channel
#   numbers start from 1, not from 0.
# - next_channel() - turns on the next channel. If the current channel is the
#   last one, turns on the first channel.
# - previous_channel() - turns on the previous channel. If the current channel
#   is the first one, turns on the last channel.
# - current_channel() - returns the name of the current channel.
# - is_exist(N/'name') - gets 1 argument - the number N or the string 'name'
#   and returns "Yes", if the channel N or 'name' exists in the list, or "No"
#   in the other case.

# The default channel turned on before all commands is №1.

# Your task is to create the TVController class and methods described above.


class TVController:

    def __init__(self, CHANNELS, but_fst_ch, but_lst_ch, but_turn_ch,
                 but_nxt_ch, but_prv_ch, but_cur_ch, but_alphabet):
        self.CHANNELS = CHANNELS
        self.buttom_firs_chan = but_fst_ch
        self.buttom_last_chan = but_lst_ch
        self.turn_chan = but_turn_ch
        self.next_chan = but_nxt_ch
        self.prev_channel = but_prv_ch
        self.curr_channel = but_cur_ch
        self.name_channel = but_alphabet

    def first_ch(self):
        print('First channel    : ', self.buttom_firs_chan[0])

    def last_ch(self):
        print('Last Channel     : ', self.buttom_last_chan[-1])

    def turn_channel(self, a):
        global cur_chan
        print('Turn to channel  : ', self.turn_chan[a-1])
        cur_chan = a

    def next_channel(self):
        if cur_chan <= (len(self.CHANNELS)-1):
            print('Next channel     : ', self.next_chan[cur_chan])
        else:
            print('Next channel     : ', self.next_chan[cur_chan - len(
                self.CHANNELS)])

    def previous_channel(self):
        if cur_chan >= (len(self.CHANNELS)-1):
            print('Previous channel : ', self.next_chan[cur_chan-1])
        else:
            print('Previous channel : ', self.next_chan[(cur_chan-1) - len(
                self.CHANNELS)])

    def current_channel(self):
        print("Current channel  : ", self.curr_channel[cur_chan-1])

    def is_exist(self, a):
        if a.isdigit() and 1 <= int(a) < (len(self.CHANNELS)):
            print('Name of channel  : ', self.name_channel[int(a)])
        elif a.isalpha() and a in self.CHANNELS:
            print(f'YES, channel {a} is in list')
        else:
            print(f'NO, channel {a} does not in list')


if __name__ == '__main__':
    CHANNELS = ["BBC", "Discovery", "TV1000"]
    controller = TVController(CHANNELS, CHANNELS, CHANNELS, CHANNELS,
                              CHANNELS, CHANNELS, CHANNELS, CHANNELS)
    print('CHANNELS         : ', CHANNELS)
    controller.first_ch()         # BBC
    controller.last_ch()          # "TV1000"
    controller.turn_channel(1)    # "BBC"
    controller.next_channel()     # "Discovery"
    controller.previous_channel() # "BBC"
    controller.current_channel()  # "BBC"
    controller.is_exist(str(4))   # "No"
    controller.is_exist("BBC")    # "Yes"


