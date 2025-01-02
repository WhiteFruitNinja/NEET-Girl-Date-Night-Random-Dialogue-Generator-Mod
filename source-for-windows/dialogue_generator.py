#Made by WhiteFruitNinja

# Comment from WhiteFruitNinja
# My code is not good. Please don't judge 😔.

from pathlib import Path

import random
import os
import sys
import re
import unrpyc_code


# Determine application directory
def get_script_directory() -> Path:
    """Returns the directory of the running script or executable."""
    if getattr(sys, 'frozen', False):
        return Path(sys.executable).parent
    else:
        return Path(os.path.abspath(__file__)).parent

# Initialize paths
SCRIPT_PATH = get_script_directory()


words = list()
ignore_files = list()
symbols_and_words = list()

characters = []

position_list = ['kara_right', 'koji_right']

allow_random_generated_choices = bool()
allow_random_generated_characters = bool()
allow_max_generated_sentence_limit = bool()
allow_min_generated_sentence_limit = bool()

ignore_files = ['screens.rpy', 'options.rpy', 'gui.rpy', 'custom_styles.rpy', 'custom.rpy']
allowed_symbols_and_words = ['"']
prohibited_symbols_and_words = ['(', ')', '==', '[', ']', '#', 'play sound', 'play music', 'play audio', 'show text', 'play bg']

def check_if_unrenpyc_file_exist():
    if os.path.exists(SCRIPT_PATH / 'game/unrpyc.py'):
        print("the file exist")
    elif not os.path.isdir(SCRIPT_PATH / 'game/unrpyc.py'):
        print("the file doesn't exist")
        with open(SCRIPT_PATH / "game/unrpyc.py", "w") as wf:
            wf.writelines(unrpyc_code.get_unrpyc_code())


def read_txt_file():
    global words
    with open(SCRIPT_PATH / "word_list.txt", "r") as f:
        for line in f:
            line_words = line.strip().splitlines()
            words.extend(line_words)

def return_txt_file():
    read_txt_file()
    return words
    
def create_sentence(length_of_sentence, words):
    sentence = '"' + ' '.join(random.choices(words, k=length_of_sentence)).capitalize() + "." + '"'

    return sentence

def write_sentence_in_rpy_files(text_list,
                                allow_random_generated_choices,
                                allow_random_generated_characters,
                                allow_max_generated_sentence_limit,
                                allow_min_generated_sentence_limit,
                                max_words,
                                min_words):
    filtered_text_list = list()

    # Regex to match multiple words after "show"
    SHOW_COMMAND_PATTERN = re.compile(r'^\s*show\s?((?!\s*text).*(?:\w+\s*)+)')

    # Loops through every text
    for text in text_list:

        # Skip lines that match the show command pattern
        if SHOW_COMMAND_PATTERN.match(text) and allow_random_generated_characters:
            continue

        # Skip lines that end with '":' (indicating a menu option)
        if text.endswith('":\n') and not allow_random_generated_choices:
            filtered_text_list.append(text)
            continue

        # Check if any allowed symbol is in the text
        has_allowed = any(symbol in text for symbol in allowed_symbols_and_words)
        # Check if none of the prohibited symbols are in the text
        has_prohibited = any(symbol in text for symbol in prohibited_symbols_and_words)

        if has_allowed and not has_prohibited:

            # Spaces from beginning
            initial_spaces = True
            spaces = 0
            character_name_abbreviation = True
            character_name = str()
            inside_quote = False
            colon = str()
            if min_words > max_words and allow_max_generated_sentence_limit:
                min_words = max_words
            elif min_words > 20 and not allow_max_generated_sentence_limit:
                min_words = 20

            length_of_sentence = random.randint(min_words if allow_min_generated_sentence_limit else 1, max_words if allow_max_generated_sentence_limit else 20) #20

            generated_sentence = create_sentence(length_of_sentence, words)

            # Every text's symbol loop
            for symbol in text:
                
                # If it encounter double quotation mark ("), it sets 
                if symbol == '"' and not inside_quote:
                    inside_quote = True
                elif symbol == '"' and inside_quote:
                    inside_quote = False

                if symbol == " " and initial_spaces:
                    spaces += 1
                elif not symbol == " " and not symbol == '"' and character_name_abbreviation:
                    initial_spaces = False
                    character_name += symbol
                elif symbol == ":" and not inside_quote:
                    colon = symbol
                else:
                    initial_spaces = False
                    character_name_abbreviation = False
                    continue
            
            if spaces == 8 and not allow_random_generated_choices:
                filtered_text_list.append(f'{spaces * " "}{character_name}{generated_sentence}{colon}\n')
                continue

            if character_name == "":
                if allow_random_generated_characters and not spaces == 8:
                    random_character = random.choice(character_list())
                    random_position = random.choice(position_list)
                    filtered_text_list.append(f'{spaces * " "}show {random_character} at {random_position}\n')
                    filtered_text_list.append(f'\n')
                filtered_text_list.append(f'{spaces * " "}{character_name}{generated_sentence}{colon}\n')
                if allow_random_generated_characters and not spaces == 8:
                    filtered_text_list.append(f'\n')
                    filtered_text_list.append(f'{spaces * " "}hide {random_character} at {random_position}\n')
            else:
                if allow_random_generated_characters and not spaces == 8:
                    random_character = random.choice(character_list())
                    random_position = random.choice(position_list)
                    filtered_text_list.append(f'{spaces * " "}show {random_character} at {random_position}\n')
                    filtered_text_list.append(f'\n')
                filtered_text_list.append(f'{spaces * " "}{character_name} {generated_sentence}{colon}\n')
                if allow_random_generated_characters and not spaces == 8:
                    filtered_text_list.append(f'\n')
                    filtered_text_list.append(f'{spaces * " "}hide {random_character} at {random_position}\n')
        else:
            filtered_text_list.append(text)


    return filtered_text_list

def check_if_copy_of_original_rpy_files_exist():
    text_list = list()
    folder_exist = bool()

    folder_exist = False

    if os.path.isdir('copy_of_original_rpy_files') and os.path.isdir('game'):
        print("the folder exist")
        folder_exist = True
    elif not os.path.isdir('copy_of_original_rpy_files') and os.path.isdir('game'):
        print("the folder doesn't exist")
        folder_exist = False
        os.mkdir('copy_of_original_rpy_files')

    return folder_exist

def read_and_write_rpy_files(allow_random_generated_choices,
                             allow_random_generated_characters,
                             allow_max_generated_sentence_limit,
                             allow_min_generated_sentence_limit,
                             max_words,
                             min_words):
    text_list = list()

    copy_rpy_files_dir = os.path.join(SCRIPT_PATH / "copy_of_original_rpy_files")

    folder_exist = check_if_copy_of_original_rpy_files_exist()

    for root, dirs, files in os.walk(SCRIPT_PATH / "game"):
        for file in files:
            if file in ignore_files or not file.endswith('.rpy'):
                continue
            
            if file.endswith('.rpy'):
                # Reads file
                if not folder_exist:
                    with open(os.path.join(root, file), 'r') as f:
                        text_list.extend(f.readlines())
                    
                    with open(os.path.join(copy_rpy_files_dir, file), 'w') as wf:
                        wf.writelines(text_list)

                    with open(os.path.join(root, file), 'w') as wf:
                        wf.writelines(write_sentence_in_rpy_files(text_list,
                                                                  allow_random_generated_choices,
                                                                  allow_random_generated_characters,
                                                                  allow_max_generated_sentence_limit,
                                                                  allow_min_generated_sentence_limit,
                                                                  max_words,
                                                                  min_words))
                
                if folder_exist:
                    with open(os.path.join(copy_rpy_files_dir, file), 'r') as f:
                        text_list.extend(f.readlines())
                
                    with open(os.path.join(root, file), 'w') as wf:
                        wf.writelines(write_sentence_in_rpy_files(text_list,
                                                                  allow_random_generated_choices,
                                                                  allow_random_generated_characters,
                                                                  allow_max_generated_sentence_limit,
                                                                  allow_min_generated_sentence_limit,
                                                                  max_words,
                                                                  min_words))

                text_list.clear()
                
    words.clear()
    return text_list

def revert_original_rpy_files():
    text_list = list()

    copy_rpy_files_dir = os.path.join(SCRIPT_PATH / "copy_of_original_rpy_files")

    for root, dirs, files in os.walk(SCRIPT_PATH / "game"):
        for file in files:
            if file in ignore_files or not file.endswith('.rpy'):
                continue
            
            if file.endswith('.rpy'):
                with open(os.path.join(copy_rpy_files_dir, file), 'r') as f:
                    text_list.extend(f.readlines())
                
                with open(os.path.join(root, file), 'w') as wf:
                    wf.writelines(text_list)

                text_list.clear()
                
    words.clear()
    return text_list

#Adds name of all character images in list
def character_list():
    specific_folders = {"kara", "koji", "mediocregamedev"}
    image_directory = os.path.join(SCRIPT_PATH / "game/images")

    characters_list = []

    for root, dirs, files in os.walk(image_directory):
        # Get the folder name from the root path
        folder_name = os.path.basename(root)
        
        # Check if the current folder is one of the specific folders we care about
        if folder_name in specific_folders:
            for file in files:
                characters_list.append(file[:-4])

    return characters_list
