from L1008 import Variables as Week01a
from L1008 import Branching as Week01b
from L1014 import Exercises as Week01e
from L1015 import Loops as Week02
from L1021 import Exercises as Week02e
from L1022 import Strings as Week03a
from L1022 import Functions as Week03b
from L1104 import Homework01 as Week03HW
from L1104 import Exercises as Week03e
from L1105 import Lists as Week04
from L1111 import Exercises as Week04e
from L1112 import Dictionaries as Week05
from L1112 import Mastermind as Week05mm

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

def week03_examples():
    Week03a.raw_multiline_strings()
    Week03a.indexing_and_slicing()
    Week03a.string_operators()
    Week03a.string_methods()
    Week03b.function_basics()
    Week03b.named_param_and_scoping()
    Week03b.find_nth_substr()

def week03_exercises():
    Week03HW.question01()
    Week03HW.question02()
    Week03e.exercise01()
    Week03e.exercise02()

def week04_examples():
    Week04.list_creation()
    Week04.indexing_and_slicing()
    Week04.list_operators()
    Week04.list_methods()
    Week04.tuples()
    Week04.exceptions()
    Week04.references()

def week04_exercises():
    Week04e.test_gcd()
    Week04e.test_stdev()
    Week04e.test_dot_product()
    Week04e.test_read_matrix()
    Week04e.test_print_transpose()

def week05_examples():
    Week05.dict_creation()
    Week05.dict_iteration()
    Week05mm.mastermind_game()

if __name__ == "__main__":
    #week01_examples()
    #week01_exercises()
    #week02_examples()
    #week02_exercises()
    #week03_examples()
    #week03_exercises()
    #week04_examples()
    #week04_exercises()
    week05_examples()