from L1008 import Variables as Week01a
from L1008 import Branching as Week01b
from L1014 import Exercises as Week01e
from L1015 import Loops as Week02
from L1021 import Exercises as Week02e
#from L1022 import Strings
from L1022 import Functions

def week01_examples():
    Week01a.variable_declaration()
    Week01a.take_input()
    Week01a.formatting_print()
    Week01b.using_if_statement()
    Week01b.de_morgan_if()

def week01_exercises():
    Week01e.calculate_bmi()
    Week01e.transform_temperature()
    Week01e.ascending_descending()
    Week01e.ascending_descending_2()
    Week01e.leap_year()

def week02_examples():
    Week02.while_loop()
    Week02.for_loop_range()
    Week02.for_loop_iterable()
    Week02.nested_for_loops()
    Week02.guess_the_number()

def week02_exercises():
    Week02e.guess_the_number()
    Week02e.find_minmax()
    Week02e.print_pyramid()
    Week02e.calculate_num_reversed()

if __name__ == "__main__":
    #week01_examples()
    #week01_exercises()
    #week02_examples()
    week02_exercises()