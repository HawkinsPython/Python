#!/usr/bin/env python3

from prompt_toolkit.shortcuts import radiolist_dialog
import os

def main():
    ## main path
    dir_root = "~/Desktop/rich_presentations"
    ## path for testing locally
    # dir_root = "/home/michael.a.hutchings98/Desktop/Hutchings/practice/python_examples_for_class"


    def python_or_sdr():
        return radiolist_dialog(
        title='Rich Presentation Launcher',
        text='Select a module!',
        values=[
            ("Python", "Python"),
            ("SDR", "SDR"),
            ],
            ).run()
    
    
    def quiz_or_lecture():
        return radiolist_dialog(
        title='Rich Presentation Launcher',
        text='Which would you like to do?',
        values=[
            ("Lectures", "Lectures"),
            ("Quizzes", "Quizzes"),
            ],
            ).run()
    

    def act_on_choice(choice: str):
        os.system(f"python3 {dir_root}/{choice}")
        
        
    def get_user_choice_python_lecture() -> str:
        return radiolist_dialog(
        title='Main Menu',
        text=f'Choose a Presentation to launch.',
        values=[
            ("lec_01a_01b_prints_inputs_variables_student.py", "Prints and Inputs"),
            ("lec_02a_02b_number_systems_operators_student.py", "Number Systems"),
            ("lec_03a_if_else_student.py", "IF-Else"),
            ("lec_03b_if_else_common_mistakes_student.py", "IF-Else common mistakes"),
            ("lec_04a_lists_student.py", "Lists"),
            ("lec_04b_file_writing_student.py", "File writing"),
            ("lec_04c_for_loops_student.py", "For loops"),
            ("lec_05a_random_student.py", "Random module"),
            ("lec_05b_while_loops_student.py", "While loops"),
            ("lec_06a_classes_student.py", "Dataclasses"),
            ("lec_06b_dictionaries_student.py", "Dictionaries"),
            ("lec_06c_functions_student.py", "Functions"),
            ],
            ).run()


    def get_user_choice_python_quiz() -> str:
        return radiolist_dialog(
        title='Main Menu',
        text=f'Choose a Quiz to launch.',
        values=[
            ("quiz_01_print_input.py", "Prints and Inputs"),
            ("quiz_02_number_system_operator.py", "Number Systems and Operators"),
            ("quiz_03_if_else.py", "IF Else"),
            ("quiz_04a_lists.py", "Lists"),
            ("quiz_04b_file_writing.py", "File Writing"),
            ("quiz_04c_for_loops.py", "For Loops"),
            ("quiz_05a_randomness.py", "Randomness"),
            ("quiz_05b_while_loops.py", "While Loops"),
            ("quiz_06a_dataclasses.py", "Dataclasses"),
            ("quiz_06b_dictionaries.py", "Dictionaries"),
            ("quiz_06c_functions.py", "Functions"),
            ],
            ).run()
    

    def get_user_choice_sdr_lecture() -> str:
        return radiolist_dialog(
        title='Main Menu',
        text=f'Choose a Presentation to launch.',
        values=[
            ("lec_sdr_01a_intro.py", "Beginnings"),
            ("lec_sdr_02a_modulation.py", "Modulation"),
            ("lec_sdr_03a_sampling.py", "Sampling"),
            ],
            ).run()


    def get_user_choice_sdr_quiz() -> str:
        return radiolist_dialog(
        title='Main Menu',
        text=f'Choose a Quiz to launch.',
        values=[
            ("quiz_sdr_01_intro.py", "Beginnings"),
            ("quiz_sdr_02_modulation.py", "Modulation"),
            ("quiz_sdr_03_sampling.py", "Sampling"),
            ],
            ).run()


    mod = python_or_sdr()
    result = quiz_or_lecture()
    if mod == "Python":
        if result == "Lectures":
            while True:
                choice = get_user_choice_python_lecture()
                act_on_choice(choice)
                if choice == None:
                    main()
                    if choice == None:
                        break
        elif result == "Quizzes":
            while True:
                choice = get_user_choice_python_quiz()
                act_on_choice(choice)
                if choice == None:
                    main()
                    if choice == None:
                        break
    elif mod == "SDR":
        if result == "Lectures":
            while True:
                choice = get_user_choice_sdr_lecture()
                act_on_choice(choice)
                if choice == None:
                    main()
                    if choice == None:
                        break
        elif result == "Quizzes":
            while True:
                choice = get_user_choice_sdr_quiz()
                act_on_choice(choice)
                if choice == None:
                    main()
                    if choice == None:
                        break

if __name__ == "__main__":
    main()    