# Made by WhiteFruitNinja

from pathlib import Path

from tkinter import Tk, Canvas, Button, PhotoImage, Toplevel, END, ttk, constants, Spinbox
from PIL import Image, ImageTk

import tkinter as tk
import webbrowser
import pygame
import dialogue_generator
import default_word_list
import secret_image_code_list
import os
import sys
import base64
import io

# Constants for window configuration
ERROR_WINDOW_WIDTH = 450
ERROR_WINDOW_HEIGHT = 200
ERROR_WINDOW_BG_COLOR = "#FFFFFF"
MAIN_WINDOW_WIDTH = 600
MAIN_WINDOW_HEIGHT = 600
MAIN_WINDOW_BG_COLOR = "#FFC0CB"
CREDITS_WINDOW_WIDTH = 500
CREDITS_WINDOW_HEIGHT = 400
CREDITS_WINDOW_BG_COLOR = "#FFC0CB"
SUCCESS_WINDOW_WIDTH = 450
SUCCESS_WINDOW_HEIGHT = 200
SUCCESS_WINDOW_BG_COLOR = "#FFFFFF"
SECRETS_WINDOW_WIDTH = 500
SECRETS_WINDOW_HEIGHT = 400
SECRETS_WINDOW_BG_COLOR = "#FFC0CB"
OPTIONS_WINDOW_WIDTH = 600
OPTIONS_WINDOW_HEIGHT = 600
OPTIONS_WINDOW_BG_COLOR = "#FFC0CB"
EDITOR_WINDOW_WIDTH = 600
EDITOR_WINDOW_HEIGHT = 600
EDITOR_WINDOW_BG_COLOR = "#FFC0CB"
HINTS_WINDOW_WIDTH = 500
HINTS_WINDOW_HEIGHT = 400
HINTS_WINDOW_BG_COLOR = "#FFC0CB"

# Datas for settings TODO
settings = {}

# Constants for default settings
DEFAULT_SETTINGS_LIST = ['allow_random_generated_choices=False', 'allow_random_generated_characters=False',
                         'allow_max_generated_sentence_limit=False', 'allow_min_generated_sentence_limit=False',
                         'maximum_word_limit=20', 'minimum_word_limit=1']

# Music settings
music_pause_count = 0
MAX_MUSIC_PAUSE_COUNT = 30

# Determine application directory
def get_script_directory() -> Path:
    """Returns the directory of the running script or executable."""
    if getattr(sys, 'frozen', False):
        return Path(sys.executable).parent
    else:
        return Path(os.path.abspath(__file__)).parent

# Initialize paths
SCRIPT_PATH = get_script_directory()
WORD_LIST_PATH = SCRIPT_PATH / "word_list.txt"
SETTINGS_PATH = SCRIPT_PATH / "settings.txt"
ASSETS_PATH = SCRIPT_PATH / "assets"
GAME_EXECUTABLE_FILE_PATH = SCRIPT_PATH / "NEET_Girl_Date_Night.exe"
GAME_EXECUTABLE_32_FILE_PATH = SCRIPT_PATH / "NEET_Girl_Date_Night-32.exe"
ICON_PATH = str(ASSETS_PATH / "Icon.ico")

# Initialize Pygame
def initialize_pygame():
    """Initializes Pygame's mixer and loads sounds."""
    pygame.mixer.init()
    try:
        click_sound = pygame.mixer.Sound(str(ASSETS_PATH / "sfx/click.mp3"))
        hover_sound = pygame.mixer.Sound(str(ASSETS_PATH / "sfx/hover.mp3"))
        return click_sound, hover_sound
    except pygame.error as e:
        print(f"Error loading sound: {e}")
        return None, None

# Define asset paths
SOUND_CLICK_PATH = str(ASSETS_PATH / "sfx/click.mp3")
SOUND_HOVER_PATH = str(ASSETS_PATH / "sfx/hover.mp3")
SOUND_SUCCESS_PATH = str(ASSETS_PATH / "sfx/success.mp3")
SOUND_FAILURE_PATH = str(ASSETS_PATH / "sfx/failure.mp3")
SOUND_EDITOR_SUCCESS_PATH = str(ASSETS_PATH / "sfx/editor_success.mp3")
SOUND_BARK_PATH = str(ASSETS_PATH / "sfx/bark.mp3")
ERROR_IMAGE_NOT_FOUND_PATH = str(ASSETS_PATH / "error_image_file_not_found_1.png")
ERROR_IMAGE_2_PATH = str(ASSETS_PATH / "error_image_2.png")
OK_BUTTON_IMAGE_PATH = str(ASSETS_PATH / "ok_button_1.png")
OK_BUTTON_IMAGE_HOVER_PATH = str(ASSETS_PATH / "ok_button_1_hover.png")
MUSIC_PATH = str(ASSETS_PATH / "music/Aria Bare - New Special Interest.mp3")
MAIN_IMAGE_1_PATH = str(ASSETS_PATH / "image_1.png")
MAIN_IMAGE_2_PATH = str(ASSETS_PATH / "image_2.png")
MAIN_IMAGE_3_PATH = str(ASSETS_PATH / "image_3.png")
MAIN_BUTTON_IMAGE_1_PATH = str(ASSETS_PATH / "button_1.png")
MAIN_BUTTON_IMAGE_2_PATH = str(ASSETS_PATH / "button_2.png")
MAIN_BUTTON_IMAGE_3_PATH = str(ASSETS_PATH / "button_3.png")
MAIN_BUTTON_IMAGE_4_PATH = str(ASSETS_PATH / "button_4.png")
MAIN_BUTTON_IMAGE_5_PATH = str(ASSETS_PATH / "button_5.png")
MAIN_BUTTON_IMAGE_6_PATH = str(ASSETS_PATH / "button_6.png")
MAIN_BUTTON_IMAGE_7_PATH = str(ASSETS_PATH / "button_7.png")
MAIN_BUTTON_IMAGE_8_PATH = str(ASSETS_PATH / "button_8.png")
MAIN_BUTTON_IMAGE_9_PATH = str(ASSETS_PATH / "button_9.png")
MAIN_BUTTON_IMAGE_1_HOVER_PATH = str(ASSETS_PATH / "button_1_hover.png")
MAIN_BUTTON_IMAGE_2_HOVER_PATH = str(ASSETS_PATH / "button_2_hover.png")
MAIN_BUTTON_IMAGE_3_HOVER_PATH = str(ASSETS_PATH / "button_3_hover.png")
MAIN_BUTTON_IMAGE_4_HOVER_PATH = str(ASSETS_PATH / "button_4_hover.png")
MAIN_BUTTON_IMAGE_5_HOVER_PATH = str(ASSETS_PATH / "button_5_hover.png")
MAIN_BUTTON_IMAGE_6_HOVER_PATH = str(ASSETS_PATH / "button_6_hover.png")
MAIN_BUTTON_IMAGE_7_HOVER_PATH = str(ASSETS_PATH / "button_7_hover.png")
MAIN_BUTTON_IMAGE_8_HOVER_PATH = str(ASSETS_PATH / "button_8_hover.png")
MAIN_BUTTON_IMAGE_9_HOVER_PATH = str(ASSETS_PATH / "button_9_hover.png")
WARNING_IMAGE_1_PATH = str(ASSETS_PATH / "warning_image_1.png")
CREDITS_IMAGE_1_PATH = str(ASSETS_PATH / "credits_image_1.png")
CREDITS_BUTTON_IMAGE_1_PATH = str(ASSETS_PATH / "credits_button_1.png")
CREDITS_BUTTON_IMAGE_2_PATH = str(ASSETS_PATH / "credits_button_2.png")
CREDITS_BUTTON_IMAGE_3_PATH = str(ASSETS_PATH / "credits_button_3.png")
CREDITS_BUTTON_IMAGE_4_PATH = str(ASSETS_PATH / "credits_button_4.png")
CREDITS_BUTTON_IMAGE_5_PATH = str(ASSETS_PATH / "credits_button_5.png")
CREDITS_BUTTON_IMAGE_6_PATH = str(ASSETS_PATH / "credits_button_6.png")
CREDITS_BUTTON_IMAGE_7_PATH = str(ASSETS_PATH / "credits_button_7.png")
CREDITS_BUTTON_IMAGE_8_PATH = str(ASSETS_PATH / "credits_button_8.png")
CREDITS_BUTTON_IMAGE_1_HOVER_PATH = str(ASSETS_PATH / "credits_button_1_hover.png")
CREDITS_BUTTON_IMAGE_2_HOVER_PATH = str(ASSETS_PATH / "credits_button_2_hover.png")
CREDITS_BUTTON_IMAGE_3_HOVER_PATH = str(ASSETS_PATH / "credits_button_3_hover.png")
CREDITS_BUTTON_IMAGE_4_HOVER_PATH = str(ASSETS_PATH / "credits_button_4_hover.png")
CREDITS_BUTTON_IMAGE_5_HOVER_PATH = str(ASSETS_PATH / "credits_button_5_hover.png")
CREDITS_BUTTON_IMAGE_6_HOVER_PATH = str(ASSETS_PATH / "credits_button_6_hover.png")
CREDITS_BUTTON_IMAGE_7_HOVER_PATH = str(ASSETS_PATH / "credits_button_7_hover.png")
CREDITS_BUTTON_IMAGE_8_HOVER_PATH = str(ASSETS_PATH / "credits_button_8_hover.png")
SUCCESS_IMAGE_1_PATH = str(ASSETS_PATH / "success_image_1.png")
SUCCESS_IMAGE_2_PATH = str(ASSETS_PATH / "success_image_2.png")
SUCCESS_IMAGE_3_PATH = str(ASSETS_PATH / "success_image_3.png")
ERROR_IMAGE_FILE_NOT_FOUND_3_PATH = str(ASSETS_PATH / "error_image_file_not_found_3.png")
ERROR_IMAGE_FILE_NOT_FOUND_2_PATH = str(ASSETS_PATH / "error_image_file_not_found_2.png")
ERROR_IMAGE_1_PATH = str(ASSETS_PATH / "error_image_1.png")
SECRETS_IMAGE_1_PATH = str(ASSETS_PATH / "secrets_image_1.png")
SECRETS_BUTTON_IMAGE_1_PATH = str(ASSETS_PATH / "secrets_button_1.png")
SECRETS_BUTTON_IMAGE_1_HOVER_PATH = str(ASSETS_PATH / "secrets_button_1_hover.png")
SECRET_GUESSED_IMAGE_1_PATH = str(ASSETS_PATH / "secret_guessed_image_1.png")
SECRET_GUESSED_IMAGE_2_PATH = str(ASSETS_PATH / "secret_guessed_image_2.png")
OPTIONS_IMAGE_1_PATH = str(ASSETS_PATH / "options_image_1.png")
OPTIONS_SETTINGS_IMAGE_1_PATH = str(ASSETS_PATH / "options_settings_image_1.png")
OPTIONS_SETTINGS_IMAGE_2_PATH = str(ASSETS_PATH / "options_settings_image_2.png")
OPTIONS_SETTINGS_DISABLED_IMAGE_3_PATH = str(ASSETS_PATH / "options_settings_disabled_image_3.png")
OPTIONS_SETTINGS_ENABLED_IMAGE_3_PATH = str(ASSETS_PATH / "options_settings_enabled_image_3.png")
OPTIONS_SETTINGS_DISABLED_IMAGE_4_PATH = str(ASSETS_PATH / "options_settings_disabled_image_4.png")
OPTIONS_SETTINGS_ENABLED_IMAGE_4_PATH = str(ASSETS_PATH / "options_settings_enabled_image_4.png")
OPTIONS_BUTTON_IMAGE_1_PATH = str(ASSETS_PATH / "options_button_1.png")
OPTIONS_BUTTON_IMAGE_1_HOVER_PATH = str(ASSETS_PATH / "options_button_1_hover.png")
OPTIONS_BUTTON_IMAGE_2_PATH = str(ASSETS_PATH / "options_button_2.png")
OPTIONS_BUTTON_IMAGE_2_HOVER_PATH = str(ASSETS_PATH / "options_button_2_hover.png")
OPTIONS_BUTTON_IMAGE_3_PATH = str(ASSETS_PATH / "options_button_3.png")
OPTIONS_BUTTON_IMAGE_3_HOVER_PATH = str(ASSETS_PATH / "options_button_3_hover.png")
SUCCESS_OPTIONS_IMAGE_1_PATH = str(ASSETS_PATH / "success_options_image_1.png")
EDITOR_IMAGE_1_PATH = str(ASSETS_PATH / "editor_image_1.png")
EDITOR_BUTTON_1_PATH = str(ASSETS_PATH / "editor_button_1.png")
EDITOR_BUTTON_1_HOVER_PATH = str(ASSETS_PATH / "editor_button_1_hover.png")
EDITOR_BUTTON_2_PATH = str(ASSETS_PATH / "editor_button_2.png")
EDITOR_BUTTON_2_HOVER_PATH = str(ASSETS_PATH / "editor_button_2_hover.png")
EDITOR_BUTTON_3_PATH = str(ASSETS_PATH / "editor_button_3.png")
EDITOR_BUTTON_3_HOVER_PATH = str(ASSETS_PATH / "editor_button_3_hover.png")
EDITOR_BUTTON_4_PATH = str(ASSETS_PATH / "editor_button_4.png")
EDITOR_BUTTON_4_HOVER_PATH = str(ASSETS_PATH / "editor_button_4_hover.png")
EDITOR_BUTTON_5_PATH = str(ASSETS_PATH / "editor_button_5.png")
EDITOR_BUTTON_5_HOVER_PATH = str(ASSETS_PATH / "editor_button_5_hover.png")
EDITOR_CONFIRMATION_IMAGE_1_PATH = str(ASSETS_PATH / "editor_confirmation_image_1.png")
EDITOR_CONFIRMATION_BUTTON_1_PATH = str(ASSETS_PATH / "editor_confirmation_button_1.png")
EDITOR_CONFIRMATION_BUTTON_1_HOVER_PATH = str(ASSETS_PATH / "editor_confirmation_button_1_hover.png")
EDITOR_CONFIRMATION_BUTTON_2_PATH = str(ASSETS_PATH / "editor_confirmation_button_2.png")
EDITOR_CONFIRMATION_BUTTON_2_HOVER_PATH = str(ASSETS_PATH / "editor_confirmation_button_2_hover.png")
EDITOR_INFORMATION_IMAGE_1_PATH = str(ASSETS_PATH / "editor_information_image_1.png")
EDITOR_INFORMATION_IMAGE_2_PATH = str(ASSETS_PATH / "editor_information_image_2.png")
EDITOR_INFORMATION_IMAGE_2_NOT_FOUND_PATH = str(ASSETS_PATH / "editor_information_image_2_not_found.png")
EDITOR_INFORMATION_IMAGE_3_PATH = str(ASSETS_PATH / "editor_information_image_3.png")
EDITOR_INFORMATION_IMAGE_4_PATH = str(ASSETS_PATH / "editor_information_image_4.png")
EDITOR_INFORMATION_IMAGE_4_ALREADY_EXISTS_PATH = str(ASSETS_PATH / "editor_information_image_4_already_exists.png")
CHECKBUTTON_CHECKED_PATH = str(ASSETS_PATH / "checkbutton_checked.png")
CHECKBUTTON_UNCHECKED_PATH = str(ASSETS_PATH / "checkbutton_unchecked.png")
HINTS_IMAGE_1_PATH = str(ASSETS_PATH / "hints_image_1.png")
SECRETS_BUTTON_IMAGE_2_PATH = str(ASSETS_PATH / "secrets_button_2.png")
SECRETS_BUTTON_IMAGE_2_HOVER_PATH = str(ASSETS_PATH / "secrets_button_2_hover.png")
SECRETS_INFORMATION_IMAGE_1_PATH = str(ASSETS_PATH / "secrets_information_image_1.png")
SECRETS_INFORMATION_IMAGE_2_PATH = str(ASSETS_PATH / "secrets_information_image_2.png")



click_sound, hover_sound = initialize_pygame()


class ErrorMessage(tk.Frame):
    """Frame displaying an error message with an exit button."""

    def __init__(self, master=None):
        super().__init__(master)
        self.load_assets()  # Call load_assets first
        self.create_canvas()  # Then create the canvas

        self.master.protocol("WM_DELETE_WINDOW", self.on_close)

        self.focus_set()
        self.bind("<Return>", self.on_enter_key)

    def load_assets(self):
        """Load sound effects and images for the error message."""
        self.click_sound = pygame.mixer.Sound(SOUND_CLICK_PATH)
        self.hover_sound = pygame.mixer.Sound(SOUND_HOVER_PATH)
        self.error_image_not_found = PhotoImage(file=ERROR_IMAGE_NOT_FOUND_PATH)
        self.ok_button_image = PhotoImage(file=OK_BUTTON_IMAGE_PATH)
        self.ok_button_image_hover = PhotoImage(file=OK_BUTTON_IMAGE_HOVER_PATH)
        self.another_error_image = PhotoImage(file=ERROR_IMAGE_2_PATH)

    def create_canvas(self):
        """Creates the error message canvas and its elements."""
        self.error_canvas = tk.Canvas(self, bg=ERROR_WINDOW_BG_COLOR, height=ERROR_WINDOW_HEIGHT, width=ERROR_WINDOW_WIDTH,
                                       bd=0, highlightthickness=0, relief="ridge")
        self.error_canvas.place(x=0, y=0)
        self.error_canvas.create_image(225, 64, image=self.error_image_not_found)

        self.setup_button()
        self.error_canvas.create_image(225.0, 163.0, image=self.another_error_image)

    def setup_button(self):
        """Setup the error button."""
        self.error_button = tk.Button(self, image=self.ok_button_image, borderwidth=0,
                                       highlightthickness=0, command=self.error_button_pressed, relief="flat")
        self.error_button.place(x=260.0, y=139, width=160.0, height=50.0)
        self.error_button.bind("<Enter>", self.on_enter_error_button)
        self.error_button.bind("<Leave>", self.on_leave_error_button)

    def error_button_pressed(self):
        """Handles the error button press action."""
        self.click_sound.play()
        self.quit()

    def on_enter_error_button(self, event):
        """Handles the mouse enter event for the button."""
        self.hover_sound.play()
        event.widget.config(image=self.ok_button_image_hover)

    def on_leave_error_button(self, event):
        """Handles the mouse leave event for the button."""
        event.widget.config(image=self.ok_button_image)
        
    def on_enter_key(self, event):
        self.click_sound.play()
        self.quit()
    
    def on_close(self):
        self.master.destroy()


class Main(tk.Frame):
    """Main application frame."""

    def __init__(self, master=None):
        super().__init__(master)
        self.load_settings(settings)
        self.load_music()
        self.load_assets()
        self.create_canvas()

        self.master.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def load_assets(self):
        """Load sound effects and images for the main application."""
        self.click_sound = pygame.mixer.Sound(SOUND_CLICK_PATH)
        self.hover_sound = pygame.mixer.Sound(SOUND_HOVER_PATH)
        self.success_sound = pygame.mixer.Sound(SOUND_SUCCESS_PATH)
        self.failure_sound = pygame.mixer.Sound(SOUND_FAILURE_PATH)
        self.bark_sound = pygame.mixer.Sound(SOUND_BARK_PATH)
        self.image_image_1 = PhotoImage(file=MAIN_IMAGE_1_PATH)
        self.image_image_2 = PhotoImage(file=MAIN_IMAGE_2_PATH)
        self.image_image_3 = PhotoImage(file=MAIN_IMAGE_3_PATH)
        self.main_button_image_1 = PhotoImage(file=MAIN_BUTTON_IMAGE_1_PATH)
        self.main_button_image_2 = PhotoImage(file=MAIN_BUTTON_IMAGE_2_PATH)
        self.main_button_image_3 = PhotoImage(file=MAIN_BUTTON_IMAGE_3_PATH)
        self.main_button_image_4 = PhotoImage(file=MAIN_BUTTON_IMAGE_4_PATH)
        self.main_button_image_5 = PhotoImage(file=MAIN_BUTTON_IMAGE_5_PATH)
        self.main_button_image_6 = PhotoImage(file=MAIN_BUTTON_IMAGE_6_PATH)
        self.main_button_image_7 = PhotoImage(file=MAIN_BUTTON_IMAGE_7_PATH)
        self.main_button_image_8 = PhotoImage(file=MAIN_BUTTON_IMAGE_8_PATH)
        self.main_button_image_9 = PhotoImage(file=MAIN_BUTTON_IMAGE_9_PATH)
        self.main_button_image_1_hover = PhotoImage(file=MAIN_BUTTON_IMAGE_1_HOVER_PATH)
        self.main_button_image_2_hover = PhotoImage(file=MAIN_BUTTON_IMAGE_2_HOVER_PATH)
        self.main_button_image_3_hover = PhotoImage(file=MAIN_BUTTON_IMAGE_3_HOVER_PATH)
        self.main_button_image_4_hover = PhotoImage(file=MAIN_BUTTON_IMAGE_4_HOVER_PATH)
        self.main_button_image_5_hover = PhotoImage(file=MAIN_BUTTON_IMAGE_5_HOVER_PATH)
        self.main_button_image_6_hover = PhotoImage(file=MAIN_BUTTON_IMAGE_6_HOVER_PATH)
        self.main_button_image_7_hover = PhotoImage(file=MAIN_BUTTON_IMAGE_7_HOVER_PATH)
        self.main_button_image_8_hover = PhotoImage(file=MAIN_BUTTON_IMAGE_8_HOVER_PATH)
        self.main_button_image_9_hover = PhotoImage(file=MAIN_BUTTON_IMAGE_9_HOVER_PATH)

    def load_settings(self, settings):
        with open(SETTINGS_PATH, 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                if key == 'maximum_word_limit' or key == 'minimum_word_limit':
                    settings[key] = int(value)  # Ensure this value is stored as an integer
                else:
                    settings[key] = value.lower() == 'true'
        print(settings)
        return settings

    def create_canvas(self):
        """Creates the main canvas and its elements."""
        self.main_canvas = tk.Canvas(self, bg=MAIN_WINDOW_BG_COLOR, height=MAIN_WINDOW_HEIGHT, width=MAIN_WINDOW_WIDTH,
                                       bd=0, highlightthickness=0, relief="ridge")
        self.main_canvas.place(x=0, y=0)

        self.main_canvas.create_image(300.0, 300.0, image=self.image_image_1)
        self.main_canvas.create_image(473.0, 410.0, image=self.image_image_2)

        self.setup_buttons()

    def setup_buttons(self):
        """Setup the main buttons."""
        # Setup 'Pause/Unpause' button
        self.main_button_1 = self.create_button(
            self.main_button_image_1,
            self.main_button_image_1_hover,
            self.main_button_1_pressed,
            430.0, 171.0
        )
        # Setup 'Credits' button
        self.main_button_2 = self.create_button(
            self.main_button_image_2,
            self.main_button_image_2_hover,
            self.main_button_2_pressed,
            12.0, 541.0
        )
        # Setup 'Run 32-bit mode' button
        self.main_button_3 = self.create_button(
            self.main_button_image_3,
            self.main_button_image_3_hover,
            self.main_button_3_pressed,
            186.0, 477.0
        )
        # Setup 'Generate random dialogues' button
        self.main_button_4 = self.create_button(
            self.main_button_image_4,
            self.main_button_image_4_hover,
            self.main_button_4_pressed,
            12.0, 477.0
        )
        # Setup 'Restore original dialogues' button
        self.main_button_5 = self.create_button(
            self.main_button_image_5,
            self.main_button_image_5_hover,
            self.main_button_5_pressed,
            12.0, 413.0
        )
        # Setup 'Run' button
        self.main_button_6 = self.create_button(
            self.main_button_image_6,
            self.main_button_image_6_hover,
            self.main_button_6_pressed,
            186.0, 541.0
        )
        # Setup 'Generator Options' button
        self.main_button_8 = self.create_button(
            self.main_button_image_8,
            self.main_button_image_8_hover,
            self.main_button_8_pressed,
            186.0, 413.0
        )
        # Setup 'Secrets' button
        self.main_button_9 = self.create_button(
            self.main_button_image_9,
            self.main_button_image_9_hover,
            self.main_button_9_pressed,
            12.0, 171.0
        )

    def create_button(self, image, hover_image, command, x, y):
        """Helper method to create a button with common properties."""
        button = tk.Button(self, image=image, borderwidth=0,
                           highlightthickness=0, command=command, relief="flat")
        button.place(x=x, y=y, width=160.0, height=50.0)
        button.bind("<Enter>", lambda event: self.on_enter_button(event, hover_image))
        button.bind("<Leave>", lambda event: self.on_leave_button(event, image))
        return button

    def on_enter_button(self, event, hover_image):
        """Handles the mouse enter event for the button with hover effect."""
        self.hover_sound.play()  # Play hover sound
        event.widget.config(image=hover_image)  # Change to hover image

    def on_leave_button(self, event, original_image):
        """Handles the mouse leave event for the button."""
        event.widget.config(image=original_image)  # Change back to original image

    def main_button_1_pressed(self):
        """Handles the main button 'Pause' press action."""
        self.click_sound.play()
        pygame.mixer.music.pause()
        
        # Changes the button to 'Unpause'
        self.main_button_1.config(
            image=self.main_button_image_7,
            command=self.main_button_7_pressed
        )
        self.main_button_1.bind("<Enter>", lambda event: self.on_enter_button(event, self.main_button_image_7_hover))
        self.main_button_1.bind("<Leave>", lambda event: self.on_leave_button(event, self.main_button_image_7))

        global music_pause_count 
        music_pause_count = music_pause_count + 1
        if music_pause_count >= MAX_MUSIC_PAUSE_COUNT:
            print('music count reached')
            music_pause_count = 0
            self.bark_sound.play()
            WarningMusicPauseMessage(self)

        # Changes from happy Kara to angry Kara
        self.main_canvas.itemconfig(2, image = self.image_image_3)

    def main_button_2_pressed(self):
        """Handles the main button 'Credits' press action."""
        self.click_sound.play()
        self.main_button_2.config(state="disabled")
        Credits(self)

    
    def main_button_3_pressed(self):
        """Handles the main button 'Run 32-bit mode' press action."""
        self.click_sound.play()
        os.startfile(GAME_EXECUTABLE_32_FILE_PATH)
        self.quit()

    def main_button_4_pressed(self):
        """Handles the main button 'Generate random dialogues' press action."""
        self.click_sound.play()
        dialogue_generator.read_txt_file()
        try:
            dialogue_generator.check_if_unrenpyc_file_exist()
            dialogue_generator.read_and_write_rpy_files(settings['allow_random_generated_choices'], settings['allow_random_generated_characters'],
                                                        settings['allow_max_generated_sentence_limit'], settings['allow_min_generated_sentence_limit'],
                                                        settings['maximum_word_limit'], settings['minimum_word_limit'])
            self.success_sound.play()
            SuccessGenerationMessage(self)
        except FileNotFoundError:
            self.failure_sound.play()
            ErrorGenerationMessage(self)
        except:
            self.failure_sound.play()
            ErrorExceptionMessage(self)

    def main_button_5_pressed(self):
        """Handles the main button 'Restore original dialogues' press action."""
        click_sound.play()
        dialogue_generator.read_txt_file()
        try:
            dialogue_generator.check_if_unrenpyc_file_exist()
            try:
                dialogue_generator.revert_original_rpy_files()
                self.success_sound.play()
                SuccessRestorationMessage(self)
            except FileNotFoundError:
                self.failure_sound.play()
                ErrorRestorationMessage(self)
        except FileNotFoundError:
            self.failure_sound.play()
            ErrorGenerationMessage(self)

    def main_button_6_pressed(self):
        """Handles the main button 'Run' press action."""
        self.click_sound.play()
        os.startfile(GAME_EXECUTABLE_FILE_PATH)
        self.quit()

    def main_button_7_pressed(self):
        """Handles the main button 'Unpause' press action."""
        self.click_sound.play()
        pygame.mixer.music.unpause()

        # Changes the button to 'Pause'
        self.main_button_1.config(
            image=self.main_button_image_1,
            command=self.main_button_1_pressed
        )
        self.main_button_1.bind("<Enter>", lambda event: self.on_enter_button(event, self.main_button_image_1_hover))
        self.main_button_1.bind("<Leave>", lambda event: self.on_leave_button(event, self.main_button_image_1))

        # Changes from angry Kara to happy Kara
        self.main_canvas.itemconfig(2, image = self.image_image_2)

    def main_button_8_pressed(self):
        """Handles the main button 'Generator Options' press action."""
        self.click_sound.play()
        self.main_button_8.config(state="disabled")
        GeneratorOptions(self)

    def main_button_9_pressed(self):
        """Handles the main button 'Secrets' press action."""
        self.click_sound.play()
        self.main_button_9.config(state="disabled")
        Secrets(self)
    
    def load_music(self):
        """Loads and plays background music."""
        pygame.mixer.music.load(MUSIC_PATH)
        pygame.mixer.music.set_volume(0.25)
        pygame.mixer.music.play(loops=-1)
    
    def on_close(self):
        """Handle the window close event for the main window."""
        # Close any Toplevel windows if they exist
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Toplevel):
                widget.destroy()  # Destroy any open Toplevel windows

        self.master.destroy()  # Finally close the main window
    
class WarningMusicPauseMessage(tk.Toplevel):
    """Frame displaying a warning music pause message with an exit button."""

    def __init__(self, master):
        super().__init__(master)
        initialize_window(self, "Warning Message", SUCCESS_WINDOW_WIDTH, SUCCESS_WINDOW_HEIGHT, SUCCESS_WINDOW_BG_COLOR)
        self.load_assets()
        self.create_canvas()

        self.focus_set()
        self.bind("<Return>", self.on_enter_key)

        
        
        master.wait_window(self)
    
    def load_assets(self):
        """Load sound effects and images for the warning music pause message."""
        self.click_sound = pygame.mixer.Sound(SOUND_CLICK_PATH)
        self.hover_sound = pygame.mixer.Sound(SOUND_HOVER_PATH)
        self.warning_image_1 = PhotoImage(file=WARNING_IMAGE_1_PATH)
        self.ok_button_image = PhotoImage(file=OK_BUTTON_IMAGE_PATH)
        self.ok_button_image_hover = PhotoImage(file=OK_BUTTON_IMAGE_HOVER_PATH)
        self.another_error_image = PhotoImage(file=ERROR_IMAGE_2_PATH)
    
    def create_canvas(self):
        """Creates the warning music pause message canvas and its elements."""
        self.warning_canvas = tk.Canvas(self, bg=SUCCESS_WINDOW_BG_COLOR, height=SUCCESS_WINDOW_HEIGHT, width=SUCCESS_WINDOW_WIDTH,
                                       bd=0, highlightthickness=0, relief="ridge")
        self.warning_canvas.place(x=0, y=0)
        self.warning_canvas.create_image(225.0, 64.0, image=self.warning_image_1)
        self.warning_canvas.create_image(225.0, 163.0, image=self.another_error_image)

        self.setup_button()
    
    def setup_button(self):
        """Setup the warning music pause button."""
        self.success_button = tk.Button(self, image=self.ok_button_image, borderwidth=0,
                                       highlightthickness=0, command=self.success_button_pressed, relief="flat")
        self.success_button.place(x=260.0, y=139, width=160.0, height=50.0)
        self.success_button.bind("<Enter>", self.on_enter_success_button)
        self.success_button.bind("<Leave>", self.on_leave_success_button)
        self.success_button.bind("<Return>", self.on_enter_key)

    def success_button_pressed(self):
        """Handles the warning music pause button press action."""
        self.click_sound.play()
        self.destroy()

    def on_enter_success_button(self, event):
        """Handles the mouse enter event for the button."""
        self.hover_sound.play()
        event.widget.config(image=self.ok_button_image_hover)

    def on_leave_success_button(self, event):
        """Handles the mouse leave event for the button."""
        event.widget.config(image=self.ok_button_image)

    def on_enter_key(self, event):
        self.click_sound.play()
        self.destroy()

class Credits(tk.Toplevel):
    """Credits frame."""

    def __init__(self, master):
        super().__init__(master)
        initialize_window(self, "Credits", CREDITS_WINDOW_WIDTH, CREDITS_WINDOW_HEIGHT, CREDITS_WINDOW_BG_COLOR)
        self.load_assets()
        self.create_canvas()
        self.setup_buttons()

        

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def load_assets(self):
        """Load sound effects and images for the credits."""
        self.click_sound = pygame.mixer.Sound(SOUND_CLICK_PATH)
        self.hover_sound = pygame.mixer.Sound(SOUND_HOVER_PATH)
        self.credits_image_1 = PhotoImage(file=CREDITS_IMAGE_1_PATH)
        self.credits_button_image_1 = PhotoImage(file=CREDITS_BUTTON_IMAGE_1_PATH)
        self.credits_button_image_2 = PhotoImage(file=CREDITS_BUTTON_IMAGE_2_PATH)
        self.credits_button_image_3 = PhotoImage(file=CREDITS_BUTTON_IMAGE_3_PATH)
        self.credits_button_image_4 = PhotoImage(file=CREDITS_BUTTON_IMAGE_4_PATH)
        self.credits_button_image_5 = PhotoImage(file=CREDITS_BUTTON_IMAGE_5_PATH)
        self.credits_button_image_6 = PhotoImage(file=CREDITS_BUTTON_IMAGE_6_PATH)
        self.credits_button_image_7 = PhotoImage(file=CREDITS_BUTTON_IMAGE_7_PATH)
        self.credits_button_image_8 = PhotoImage(file=CREDITS_BUTTON_IMAGE_8_PATH)
        self.credits_button_image_1_hover = PhotoImage(file=CREDITS_BUTTON_IMAGE_1_HOVER_PATH)
        self.credits_button_image_2_hover = PhotoImage(file=CREDITS_BUTTON_IMAGE_2_HOVER_PATH)
        self.credits_button_image_3_hover = PhotoImage(file=CREDITS_BUTTON_IMAGE_3_HOVER_PATH)
        self.credits_button_image_4_hover = PhotoImage(file=CREDITS_BUTTON_IMAGE_4_HOVER_PATH)
        self.credits_button_image_5_hover = PhotoImage(file=CREDITS_BUTTON_IMAGE_5_HOVER_PATH)
        self.credits_button_image_6_hover = PhotoImage(file=CREDITS_BUTTON_IMAGE_6_HOVER_PATH)
        self.credits_button_image_7_hover = PhotoImage(file=CREDITS_BUTTON_IMAGE_7_HOVER_PATH)
        self.credits_button_image_8_hover = PhotoImage(file=CREDITS_BUTTON_IMAGE_8_HOVER_PATH)
        
    def create_canvas(self):
        """Creates the error message canvas and its elements."""
        self.credits_canvas = tk.Canvas(self, bg=CREDITS_WINDOW_BG_COLOR, height=CREDITS_WINDOW_HEIGHT, width=CREDITS_WINDOW_WIDTH,
                                       bd=0, highlightthickness=0, relief="ridge")
        self.credits_canvas.place(x=0, y=0)

        self.credits_canvas.create_image(250.0, 200.0, image=self.credits_image_1)
    
    def create_image_button(self, image, hover_image, command, x, y):
        """Helper method to create a image with common properties."""
        image_id = self.credits_canvas.create_image(x, y, image=image)

        # Bind hover events to the created image
        self.credits_canvas.tag_bind(image_id, "<Enter>", lambda event: self.on_enter_button(event, hover_image, image_id))
        self.credits_canvas.tag_bind(image_id, "<Leave>", lambda event: self.on_leave_button(event, image, image_id))

        # Bind the click event to call the command
        self.credits_canvas.tag_bind(image_id, "<Button-1>", lambda event: command())

        return image_id
    
    def on_enter_button(self, event, hover_image, image_id):
        """Handles the mouse enter event for the button with hover effect."""
        self.hover_sound.play()  # Play hover sound
        self.credits_canvas.itemconfig(image_id, image=hover_image)  # Change to hover image

    def on_leave_button(self, event, original_image, image_id):
        """Handles the mouse leave event for the button."""
        self.credits_canvas.itemconfig(image_id, image=original_image)  # Change back to original image

    def setup_buttons(self):
        """Setup buttons in the credits window."""
        self.credits_button_1 = self.create_image_button(
            self.credits_button_image_1,
            self.credits_button_image_1_hover,
            self.credits_button_1_pressed,
            278.0, 87.5
        )
        self.credits_button_2 = self.create_image_button(
            self.credits_button_image_2,
            self.credits_button_image_2_hover,
            self.credits_button_2_pressed,
            297.0, 120.5
        )
        self.credits_button_3 = self.create_image_button(
            self.credits_button_image_3,
            self.credits_button_image_3_hover,
            self.credits_button_3_pressed,
           94.0, 191.0
        )
        self.credits_button_4 = self.create_image_button(
            self.credits_button_image_4,
            self.credits_button_image_4_hover,
            self.credits_button_4_pressed,
            208.0, 194.0
        )
        self.credits_button_5 = self.create_image_button(
            self.credits_button_image_5,
            self.credits_button_image_5_hover,
            self.credits_button_5_pressed,
            71.0, 231.0
        )
        self.credits_button_6 = self.create_image_button(
            self.credits_button_image_6,
            self.credits_button_image_6_hover,
            self.credits_button_6_pressed,
            215.0, 232.0
        )
        self.credits_button_7 = self.create_image_button(
            self.credits_button_image_7,
            self.credits_button_image_7_hover,
            self.credits_button_7_pressed,
            130.0, 272.0
        )
        self.credits_button_8 = self.create_image_button(
            self.credits_button_image_8,
            self.credits_button_image_8_hover,
            self.credits_button_8_pressed,
            143.5, 287.0
        )
    
    def credits_button_1_pressed(self):
        self.click_sound.play()
        URL = 'https://x.com/WhiteFruitNinja'
        webbrowser.open(URL)
    
    def credits_button_2_pressed(self):
        self.click_sound.play()
        URL = 'https://x.com/hitsujigoods'
        webbrowser.open(URL)
    
    def credits_button_3_pressed(self):
        self.click_sound.play()
        URL = 'https://github.com/CensoredUsername'
        webbrowser.open(URL)
    
    def credits_button_4_pressed(self):
        self.click_sound.play()
        URL = 'https://github.com/CensoredUsername/unrpyc'
        webbrowser.open(URL)
    
    def credits_button_5_pressed(self):
        self.click_sound.play()
        URL = 'https://github.com/first20hours'
        webbrowser.open(URL)
    
    def credits_button_6_pressed(self):
        self.click_sound.play()
        URL = 'https://github.com/first20hours/google-10000-english'
        webbrowser.open(URL)
    
    def credits_button_7_pressed(self):
        self.click_sound.play()
        URL = 'https://x.com/raidengaembing'
        webbrowser.open(URL)
    
    def credits_button_8_pressed(self):
        self.click_sound.play()
        URL = 'https://github.com/raidengugga/Neet-Girl-Date-Night-PSVITA'
        webbrowser.open(URL)
    
    def on_close(self):
        """Handle the close event of the Credits window."""
        self.master.main_button_2.config(state="normal")
        self.destroy()  # Close the Credits window
    

class SuccessGenerationMessage(tk.Toplevel):
    """Frame displaying an successful generation message with an exit button."""

    def __init__(self, master):
        super().__init__(master)
        initialize_window(self, "Success Message", SUCCESS_WINDOW_WIDTH, SUCCESS_WINDOW_HEIGHT, SUCCESS_WINDOW_BG_COLOR)
        self.load_assets()
        self.create_canvas()

        self.focus_set()
        self.bind("<Return>", self.on_enter_key)

        
        
        master.wait_window(self)
    
    def load_assets(self):
        """Load sound effects and images for the success generation message."""
        self.click_sound = pygame.mixer.Sound(SOUND_CLICK_PATH)
        self.hover_sound = pygame.mixer.Sound(SOUND_HOVER_PATH)
        self.success_image_1 = PhotoImage(file=SUCCESS_IMAGE_1_PATH)
        self.ok_button_image = PhotoImage(file=OK_BUTTON_IMAGE_PATH)
        self.ok_button_image_hover = PhotoImage(file=OK_BUTTON_IMAGE_HOVER_PATH)
        self.another_error_image = PhotoImage(file=ERROR_IMAGE_2_PATH)
    
    def create_canvas(self):
        """Creates the success generation message canvas and its elements."""
        self.success_generation_canvas = tk.Canvas(self, bg=SUCCESS_WINDOW_BG_COLOR, height=SUCCESS_WINDOW_HEIGHT, width=SUCCESS_WINDOW_WIDTH,
                                       bd=0, highlightthickness=0, relief="ridge")
        self.success_generation_canvas.place(x=0, y=0)
        self.success_generation_canvas.create_image(225.0, 64.0, image=self.success_image_1)
        self.success_generation_canvas.create_image(225.0, 163.0, image=self.another_error_image)

        self.setup_button()
    
    def setup_button(self):
        """Setup the success generation button."""
        self.success_button = tk.Button(self, image=self.ok_button_image, borderwidth=0,
                                       highlightthickness=0, command=self.success_button_pressed, relief="flat")
        self.success_button.place(x=260.0, y=139, width=160.0, height=50.0)
        self.success_button.bind("<Enter>", self.on_enter_success_button)
        self.success_button.bind("<Leave>", self.on_leave_success_button)
        self.success_button.bind("<Return>", self.on_enter_key)

    def success_button_pressed(self):
        """Handles the success generation button press action."""
        self.click_sound.play()
        self.destroy()

    def on_enter_success_button(self, event):
        """Handles the mouse enter event for the button."""
        self.hover_sound.play()
        event.widget.config(image=self.ok_button_image_hover)

    def on_leave_success_button(self, event):
        """Handles the mouse leave event for the button."""
        event.widget.config(image=self.ok_button_image)

    def on_enter_key(self, event):
        self.click_sound.play()
        self.destroy()
        

class ErrorGenerationMessage(tk.Toplevel):
    """Frame displaying an error generation message with an exit button."""

    def __init__(self, master):
        super().__init__(master)
        initialize_window(self, "Error Message", ERROR_WINDOW_WIDTH, ERROR_WINDOW_HEIGHT, ERROR_WINDOW_BG_COLOR)
        self.load_assets()
        self.create_canvas()

        self.focus_set()
        self.bind("<Return>", self.on_enter_key)

        
        
        master.wait_window(self)
    
    def load_assets(self):
        """Load sound effects and images for the error generation message."""
        self.click_sound = pygame.mixer.Sound(SOUND_CLICK_PATH)
        self.hover_sound = pygame.mixer.Sound(SOUND_HOVER_PATH)
        self.error_image_file_not_found_3 = PhotoImage(file=ERROR_IMAGE_FILE_NOT_FOUND_3_PATH)
        self.ok_button_image = PhotoImage(file=OK_BUTTON_IMAGE_PATH)
        self.ok_button_image_hover = PhotoImage(file=OK_BUTTON_IMAGE_HOVER_PATH)
        self.another_error_image = PhotoImage(file=ERROR_IMAGE_2_PATH)
    
    def create_canvas(self):
        """Creates the error generation message canvas and its elements."""
        self.error_generation_canvas = tk.Canvas(self, bg=ERROR_WINDOW_BG_COLOR, height=ERROR_WINDOW_HEIGHT, width=ERROR_WINDOW_WIDTH,
                                       bd=0, highlightthickness=0, relief="ridge")
        self.error_generation_canvas.place(x=0, y=0)
        self.error_generation_canvas.create_image(225.0, 64.0, image=self.error_image_file_not_found_3)
        self.error_generation_canvas.create_image(225.0, 163.0, image=self.another_error_image)

        self.setup_button()
    
    def setup_button(self):
        """Setup the error generation button."""
        self.error_button = tk.Button(self, image=self.ok_button_image, borderwidth=0,
                                       highlightthickness=0, command=self.error_button_pressed, relief="flat")
        self.error_button.place(x=260.0, y=139, width=160.0, height=50.0)
        self.error_button.bind("<Enter>", self.on_enter_error_button)
        self.error_button.bind("<Leave>", self.on_leave_error_button)

    def error_button_pressed(self):
        """Handles the error generation button press action."""
        self.click_sound.play()
        self.destroy()

    def on_enter_error_button(self, event):
        """Handles the mouse enter event for the button."""
        self.hover_sound.play()
        event.widget.config(image=self.ok_button_image_hover)

    def on_leave_error_button(self, event):
        """Handles the mouse leave event for the button."""
        event.widget.config(image=self.ok_button_image)
    
    def on_enter_key(self, event):
        self.click_sound.play()
        self.destroy()

class ErrorExceptionMessage(tk.Toplevel):
    """Frame displaying an error generation message with an exit button."""

    def __init__(self, master):
        super().__init__(master)
        initialize_window(self, "Error Message", ERROR_WINDOW_WIDTH, ERROR_WINDOW_HEIGHT, ERROR_WINDOW_BG_COLOR)
        self.load_assets()
        self.create_canvas()

        self.focus_set()
        self.bind("<Return>", self.on_enter_key)

        
        
        master.wait_window(self)
    
    def load_assets(self):
        """Load sound effects and images for the error exception message."""
        self.click_sound = pygame.mixer.Sound(SOUND_CLICK_PATH)
        self.hover_sound = pygame.mixer.Sound(SOUND_HOVER_PATH)
        self.error_image_1 = PhotoImage(file=ERROR_IMAGE_1_PATH)
        self.ok_button_image = PhotoImage(file=OK_BUTTON_IMAGE_PATH)
        self.ok_button_image_hover = PhotoImage(file=OK_BUTTON_IMAGE_HOVER_PATH)
        self.another_error_image = PhotoImage(file=ERROR_IMAGE_2_PATH)
    
    def create_canvas(self):
        """Creates the error exception message canvas and its elements."""
        self.error_exception_canvas = tk.Canvas(self, bg=ERROR_WINDOW_BG_COLOR, height=ERROR_WINDOW_HEIGHT, width=ERROR_WINDOW_WIDTH,
                                       bd=0, highlightthickness=0, relief="ridge")
        self.error_exception_canvas.place(x=0, y=0)
        self.error_exception_canvas.create_image(225.0, 64.0, image=self.error_image_1)
        self.error_exception_canvas.create_image(225.0, 163.0, image=self.another_error_image)

        self.setup_button()
    
    def setup_button(self):
        """Setup the error exception button."""
        self.error_button = tk.Button(self, image=self.ok_button_image, borderwidth=0,
                                       highlightthickness=0, command=self.error_button_pressed, relief="flat")
        self.error_button.place(x=260.0, y=139, width=160.0, height=50.0)
        self.error_button.bind("<Enter>", self.on_enter_error_button)
        self.error_button.bind("<Leave>", self.on_leave_error_button)

    def error_button_pressed(self):
        """Handles the error exception button press action."""
        self.click_sound.play()
        self.destroy()

    def on_enter_error_button(self, event):
        """Handles the mouse enter event for the button."""
        self.hover_sound.play()
        event.widget.config(image=self.ok_button_image_hover)

    def on_leave_error_button(self, event):
        """Handles the mouse leave event for the button."""
        event.widget.config(image=self.ok_button_image)
    
    def on_enter_key(self, event):
        self.click_sound.play()
        self.destroy()

class SuccessRestorationMessage(tk.Toplevel):
    """Frame displaying an successful restoration message with an exit button."""

    def __init__(self, master):
        super().__init__(master)
        initialize_window(self, "Success Message", SUCCESS_WINDOW_WIDTH, SUCCESS_WINDOW_HEIGHT, SUCCESS_WINDOW_BG_COLOR)
        self.load_assets()
        self.create_canvas()

        self.focus_set()
        self.bind("<Return>", self.on_enter_key)

        
        
        master.wait_window(self)
    
    def load_assets(self):
        """Load sound effects and images for the success restoration message."""
        self.click_sound = pygame.mixer.Sound(SOUND_CLICK_PATH)
        self.hover_sound = pygame.mixer.Sound(SOUND_HOVER_PATH)
        self.success_image_2 = PhotoImage(file=SUCCESS_IMAGE_2_PATH)
        self.ok_button_image = PhotoImage(file=OK_BUTTON_IMAGE_PATH)
        self.ok_button_image_hover = PhotoImage(file=OK_BUTTON_IMAGE_HOVER_PATH)
        self.another_error_image = PhotoImage(file=ERROR_IMAGE_2_PATH)
    
    def create_canvas(self):
        """Creates the success restoration message canvas and its elements."""
        self.success_restoration_canvas = tk.Canvas(self, bg=SUCCESS_WINDOW_BG_COLOR, height=SUCCESS_WINDOW_HEIGHT, width=SUCCESS_WINDOW_WIDTH,
                                       bd=0, highlightthickness=0, relief="ridge")
        self.success_restoration_canvas.place(x=0, y=0)
        self.success_restoration_canvas.create_image(225.0, 64.0, image=self.success_image_2)
        self.success_restoration_canvas.create_image(225.0, 163.0, image=self.another_error_image)

        self.setup_button()

    def setup_button(self):
        """Setup the success restoration button."""
        self.success_button = tk.Button(self, image=self.ok_button_image, borderwidth=0,
                                       highlightthickness=0, command=self.success_button_pressed, relief="flat")
        self.success_button.place(x=260.0, y=139, width=160.0, height=50.0)
        self.success_button.bind("<Enter>", self.on_enter_success_button)
        self.success_button.bind("<Leave>", self.on_leave_success_button)

    def success_button_pressed(self):
        """Handles the success restoration button press action."""
        self.click_sound.play()
        self.destroy()

    def on_enter_success_button(self, event):
        """Handles the mouse enter event for the button."""
        self.hover_sound.play()
        event.widget.config(image=self.ok_button_image_hover)

    def on_leave_success_button(self, event):
        """Handles the mouse leave event for the button."""
        event.widget.config(image=self.ok_button_image)
    
    def on_enter_key(self, event):
        self.click_sound.play()
        self.destroy()


class ErrorRestorationMessage(tk.Toplevel):
    """Frame displaying an error restoration message with an exit button."""

    def __init__(self, master):
        super().__init__(master)
        initialize_window(self, "Error Message", ERROR_WINDOW_WIDTH, ERROR_WINDOW_HEIGHT, ERROR_WINDOW_BG_COLOR)
        self.load_assets()
        self.create_canvas()

        self.focus_set()
        self.bind("<Return>", self.on_enter_key)

        
        
        master.wait_window(self)
    
    def load_assets(self):
        """Load sound effects and images for the error restoration message."""
        self.click_sound = pygame.mixer.Sound(SOUND_CLICK_PATH)
        self.hover_sound = pygame.mixer.Sound(SOUND_HOVER_PATH)
        self.error_image_file_not_found_2 = PhotoImage(file=ERROR_IMAGE_FILE_NOT_FOUND_2_PATH)
        self.ok_button_image = PhotoImage(file=OK_BUTTON_IMAGE_PATH)
        self.ok_button_image_hover = PhotoImage(file=OK_BUTTON_IMAGE_HOVER_PATH)
        self.another_error_image = PhotoImage(file=ERROR_IMAGE_2_PATH)
    
    def create_canvas(self):
        """Creates the error restoration message canvas and its elements."""
        self.error_generation_canvas = tk.Canvas(self, bg=ERROR_WINDOW_BG_COLOR, height=ERROR_WINDOW_HEIGHT, width=ERROR_WINDOW_WIDTH,
                                       bd=0, highlightthickness=0, relief="ridge")
        self.error_generation_canvas.place(x=0, y=0)
        self.error_generation_canvas.create_image(225.0, 64.0, image=self.error_image_file_not_found_2)
        self.error_generation_canvas.create_image(225.0, 163.0, image=self.another_error_image)

        self.setup_button()
    
    def setup_button(self):
        """Setup the error restoration button."""
        self.error_button = tk.Button(self, image=self.ok_button_image, borderwidth=0,
                                       highlightthickness=0, command=self.error_button_pressed, relief="flat")
        self.error_button.place(x=260.0, y=139, width=160.0, height=50.0)
        self.error_button.bind("<Enter>", self.on_enter_error_button)
        self.error_button.bind("<Leave>", self.on_leave_error_button)

    def error_button_pressed(self):
        """Handles the error restoration button press action."""
        self.click_sound.play()
        self.destroy()

    def on_enter_error_button(self, event):
        """Handles the mouse enter event for the button."""
        self.hover_sound.play()
        event.widget.config(image=self.ok_button_image_hover)

    def on_leave_error_button(self, event):
        """Handles the mouse leave event for the button."""
        event.widget.config(image=self.ok_button_image)
    
    def on_enter_key(self, event):
        self.click_sound.play()
        self.destroy()

# TODO: Make 8 secret codes and make 8 hints that are in the boxes. when user press on it, it shows a window with hints.
class Secrets(tk.Toplevel):
    """Secrets frame."""
    
    def __init__(self, master):
        super().__init__(master)
        initialize_window(self, "Secrets", SECRETS_WINDOW_WIDTH, SECRETS_WINDOW_HEIGHT, SECRETS_WINDOW_BG_COLOR)
        self.load_assets()
        self.create_canvas()

        

        self.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def load_assets(self):
        """Load sound effects and images for the secrets."""
        self.click_sound = pygame.mixer.Sound(SOUND_CLICK_PATH)
        self.hover_sound = pygame.mixer.Sound(SOUND_HOVER_PATH)
        self.success_sound = pygame.mixer.Sound(SOUND_SUCCESS_PATH)
        self.secrets_image_1 = PhotoImage(file=SECRETS_IMAGE_1_PATH)
        self.secrets_button_image_1 = PhotoImage(file=SECRETS_BUTTON_IMAGE_1_PATH)
        self.secrets_button_image_1_hover = PhotoImage(file=SECRETS_BUTTON_IMAGE_1_HOVER_PATH)
        self.secrets_button_image_2 = PhotoImage(file=SECRETS_BUTTON_IMAGE_2_PATH)
        self.secrets_button_image_2_hover = PhotoImage(file=SECRETS_BUTTON_IMAGE_2_HOVER_PATH)
        self.secrets_information_image_1 = PhotoImage(file=SECRETS_INFORMATION_IMAGE_1_PATH)
        self.secrets_information_image_2 = PhotoImage(file=SECRETS_INFORMATION_IMAGE_2_PATH)

    def create_canvas(self):
        """Creates the secrets canvas and its elements."""
        self.secrets_canvas = tk.Canvas(self, bg=SECRETS_WINDOW_BG_COLOR, height=SECRETS_WINDOW_HEIGHT, width=SECRETS_WINDOW_WIDTH,
                                       bd=0, highlightthickness=0, relief="ridge")
        self.secrets_canvas.place(x=0, y=0)
        self.secrets_canvas.create_image(250, 200, image=self.secrets_image_1)

        self.setup_button()
        self.setup_input_field()

    def setup_button(self):
        """Setup the secrets button."""
        self.secrets_button_1 = tk.Button(self, image=self.secrets_button_image_1, borderwidth=0,
                                       highlightthickness=0, command=self.secrets_button_1_pressed, relief="flat")
        self.secrets_button_1.place(x=309.0, y=320.0, width=160.0, height=50.0)
        self.secrets_button_1.bind("<Enter>", self.on_enter_secrets_1_button)
        self.secrets_button_1.bind("<Leave>", self.on_leave_secrets_1_button)

        self.secrets_button_2 = tk.Button(self, image=self.secrets_button_image_2, borderwidth=0,
                                       highlightthickness=0, command=self.secrets_button_2_pressed, relief="flat")
        self.secrets_button_2.place(x=34.0, y=320.0, width=160.0, height=50.0)
        self.secrets_button_2.bind("<Enter>", self.on_enter_secrets_2_button)
        self.secrets_button_2.bind("<Leave>", self.on_leave_secrets_2_button)

    def setup_input_field(self):
        """Setup the secrets input field."""
        self.secret_input = tk.Text(self, height=1, width=53, bd=2, wrap='word',background='pink')
        self.secret_input.place(x=36, y=278)

        self.MAX_LENGTH_OF_INPUT_LETTERS = 53
        self.enter_pressed = False

        # Bind the Enter key to the on_enter_key function
        self.secret_input.bind("<Return>", self.on_enter_key)

        # Bind key press events to limit the length
        self.secret_input.bind("<Key>", self.limit_length)

        # Bind key release event to reset the enter_pressed flag
        self.secret_input.bind("<KeyRelease>", self.on_key_release)

        # Disabling copy/paste
        self.secret_input.bind('<Control-v>', lambda _: 'break')
        self.secret_input.bind('<Control-c>', lambda _: 'break')
        


    def secrets_button_1_pressed(self):
        """Handles the secrets button press action."""
        self.click_sound.play()
        self.secret_value = self.secret_input.get("1.0", "end-1c")
        self.secret_value = self.secret_value.lower().replace(" ", "")

        print(self.secret_value)

        self.secret_index = 0
        SECRET_CODES = [
        ("kara", "kara eklund"),
        "koji",
        "mitsu", 
        "vivi", 
        "defcon",
        ("suzihunter", "thespherehunter", "suzi", "spherehunter"), 
        ("hitsuji", "hitsujigoods"),
        ("mitsuvivi", "vivimitsu")
        ]

        is_secret_guessed = False
        
        for i, code in enumerate(SECRET_CODES):
            if self.secret_value in (code if isinstance(code, tuple) else [code]):
                self.success_sound.play()
                self.secret_index = i + 1
                print(f"Secret input: {self.secret_value}")
                is_secret_guessed = True
                SecretGuessed(self)
                break

        if not is_secret_guessed and self.secret_input.get("1.0", tk.END).strip():
            InformationMessage(self, self.secrets_information_image_2)
            print('Wrong code')
        elif not is_secret_guessed and not self.secret_input.get("1.0", tk.END).strip():
            InformationMessage(self, self.secrets_information_image_1)
            print('Wrong code')

        self.secret_input.delete("1.0", END)

    
    def secrets_button_2_pressed(self):
        """Handles the secrets button press action."""
        self.click_sound.play()
        self.secrets_button_2.config(state="disabled")
        Hints(self)

    def on_enter_secrets_1_button(self, event):
        """Handles the mouse enter event for the button."""
        self.hover_sound.play()
        event.widget.config(image=self.secrets_button_image_1_hover)

    def on_leave_secrets_1_button(self, event):
        """Handles the mouse leave event for the button."""
        event.widget.config(image=self.secrets_button_image_1)

    def on_enter_secrets_2_button(self, event):
        """Handles the mouse enter event for the button."""
        self.hover_sound.play()
        event.widget.config(image=self.secrets_button_image_2_hover)

    def on_leave_secrets_2_button(self, event):
        """Handles the mouse leave event for the button."""
        event.widget.config(image=self.secrets_button_image_2)

    def on_enter_key(self, event):
        if not self.enter_pressed:
            self.click_sound.play()
            self.enter_pressed = True
            self.secrets_button_1_pressed()
        return "break"
        
    def on_key_release(self, event):
        if event.keysym == 'Return':
            self.enter_pressed
            self.enter_pressed = False
            self.secret_input.delete("1.0", END)

    def limit_length(self, event):
        if event.keysym in ('BackSpace', 'Delete', 'Up', 'Down', 'Left', 'Right'):
            return

        if len(self.secret_input.get("1.0", "end-1c")) >= self.MAX_LENGTH_OF_INPUT_LETTERS:
            return "break"  # Prevent further input
    
    def on_close(self):
       self.master.main_button_9.config(state="normal")
       self.destroy()



class SecretGuessed(tk.Toplevel):
    """Frame displaying Secret Guessed frame."""

    def __init__(self, master):
        super().__init__(master)
        initialize_window(self, f"Secret {self.master.secret_index}", SECRETS_WINDOW_WIDTH, SECRETS_WINDOW_HEIGHT, SECRETS_WINDOW_BG_COLOR)
        self.load_assets()  # Call load_assets first
        self.create_canvas()  # Then create the canvas

        
        
        master.wait_window(self)

    def load_assets(self):
        """Load sound effects and images for the hint guessed."""
        self.click_sound = pygame.mixer.Sound(SOUND_CLICK_PATH)
        self.hover_sound = pygame.mixer.Sound(SOUND_HOVER_PATH)
        self.secret_guessed_image_1 = PhotoImage(file=SECRET_GUESSED_IMAGE_1_PATH)
        self.secret_guessed_image_2 = PhotoImage(file=SECRET_GUESSED_IMAGE_2_PATH)
        self.secret_image_1 = self.secret_image(1)
        self.secret_image_2 = self.secret_image(2)
        self.secret_image_3 = self.secret_image(3)
        self.secret_image_4 = self.secret_image(4)
        self.secret_image_5 = self.secret_image(5)
        self.secret_image_6 = self.secret_image(6)
        self.secret_image_7 = self.secret_image(7)
        self.secret_image_8 = self.secret_image(8)


    def create_canvas(self):
        """Creates the hint guessed canvas and its elements."""
        self.hint_guessed_canvas = tk.Canvas(self, bg=SECRETS_WINDOW_BG_COLOR, height=SECRETS_WINDOW_HEIGHT, width=SECRETS_WINDOW_WIDTH,
                                       bd=0, highlightthickness=0, relief="ridge")
        self.hint_guessed_canvas.place(x=0, y=0)
        self.hint_guessed_canvas.create_image(250, 200, image=self.secret_guessed_image_1)
        self.hint_guessed_canvas.create_image(250, 200, image=self.secret_guessed_image_2)

        image_attr = f'secret_image_{self.master.secret_index}'
        secret_image = getattr(self, image_attr, None)

        self.hint_guessed_canvas.create_image(250, 200, image=secret_image)

    def get_decoded_image_file(self, base64_string):
        # Decode the base64 string
        image_data = base64.b64decode(base64_string)
        # Create an image using BytesIO, then convert to PhotoImage
        image = Image.open(io.BytesIO(image_data))
        return ImageTk.PhotoImage(image)
    
    def secret_image(self, index):
        return self.get_decoded_image_file(secret_image_code_list.get_image_code_list()[index - 1])

class Hints(tk.Toplevel):
    """Hints frame."""
    
    # TODO: fix a bug when you open one window and inside window you open another window and then close one window, it allows users to  for the main  
    def __init__(self, master):
        super().__init__(master)
        initialize_window(self, "Hints", HINTS_WINDOW_WIDTH, HINTS_WINDOW_HEIGHT, HINTS_WINDOW_BG_COLOR)
        self.load_assets()
        self.create_canvas()

        self.protocol("WM_DELETE_WINDOW", self.on_close)


    def load_assets(self):
        """Load sound effects and images for the hints."""
        self.hints_image_1 = PhotoImage(file=HINTS_IMAGE_1_PATH)

    def create_canvas(self):
        """Creates the hints canvas and its elements."""
        self.hints_canvas = tk.Canvas(self, bg=HINTS_WINDOW_BG_COLOR, height=HINTS_WINDOW_HEIGHT, width=HINTS_WINDOW_WIDTH,
                                       bd=0, highlightthickness=0, relief="ridge")
        self.hints_canvas.place(x=0, y=0)
        self.hints_canvas.create_image(250, 200, image=self.hints_image_1)
    
    def on_close(self):
       self.master.secrets_button_2.config(state="normal")
       self.destroy()

    

class GeneratorOptions(tk.Toplevel):
    """Generator Options frame."""

    def __init__(self, master):
        super().__init__(master)
        initialize_window(self, "Generator Options", OPTIONS_WINDOW_WIDTH, OPTIONS_WINDOW_HEIGHT, OPTIONS_WINDOW_BG_COLOR)
        self.load_settings(settings)
        self.load_assets()
        self.create_canvas()

        self.editor_window = None

        self.setup_buttons()
        self.setup_checkboxes()
        self.setup_spinbox()

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def load_settings(self, settings):
        with open(SETTINGS_PATH, 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                if key == 'maximum_word_limit' or key == 'minimum_word_limit':
                    settings[key] = int(value)  # Ensure this value is stored as an integer
                else:
                    settings[key] = value.lower() == 'true'
        print(settings)
        return settings
    
    def save_settings(self, key, value):
        settings[key] = value
        with open(SETTINGS_PATH, 'w') as f:
            for k, v in settings.items():
                f.write(f"{k}={str(v).lower()}\n")

    def load_assets(self):
        """Load sound effects and images for the options."""
        self.click_sound = pygame.mixer.Sound(SOUND_CLICK_PATH)
        self.hover_sound = pygame.mixer.Sound(SOUND_HOVER_PATH)
        self.success_sound = pygame.mixer.Sound(SOUND_SUCCESS_PATH)
        self.failure_sound = pygame.mixer.Sound(SOUND_FAILURE_PATH)
        self.options_image_1 = PhotoImage(file=OPTIONS_IMAGE_1_PATH)
        self.options_settings_image_1 = PhotoImage(file=OPTIONS_SETTINGS_IMAGE_1_PATH)
        self.options_settings_image_2 = PhotoImage(file=OPTIONS_SETTINGS_IMAGE_2_PATH)
        self.options_settings_disabled_image_3 = PhotoImage(file=OPTIONS_SETTINGS_DISABLED_IMAGE_3_PATH)
        self.options_settings_enabled_image_3 = PhotoImage(file=OPTIONS_SETTINGS_ENABLED_IMAGE_3_PATH)
        self.options_settings_disabled_image_4 = PhotoImage(file=OPTIONS_SETTINGS_DISABLED_IMAGE_4_PATH)
        self.options_settings_enabled_image_4 = PhotoImage(file=OPTIONS_SETTINGS_ENABLED_IMAGE_4_PATH)
        self.options_button_image_1 = PhotoImage(file=OPTIONS_BUTTON_IMAGE_1_PATH)
        self.options_button_image_1_hover = PhotoImage(file=OPTIONS_BUTTON_IMAGE_1_HOVER_PATH)
        self.options_button_image_2 = PhotoImage(file=OPTIONS_BUTTON_IMAGE_2_PATH)
        self.options_button_image_2_hover = PhotoImage(file=OPTIONS_BUTTON_IMAGE_2_HOVER_PATH)
        self.options_button_image_3 = PhotoImage(file=OPTIONS_BUTTON_IMAGE_3_PATH)
        self.options_button_image_3_hover = PhotoImage(file=OPTIONS_BUTTON_IMAGE_3_HOVER_PATH)
        self.checkbutton_image_unchecked = PhotoImage(file=CHECKBUTTON_UNCHECKED_PATH)
        self.checkbutton_image_checked = PhotoImage(file=CHECKBUTTON_CHECKED_PATH)

    
    def create_canvas(self):
        """Creates the options canvas and its elements."""
        self.options_canvas = tk.Canvas(self, bg=OPTIONS_WINDOW_BG_COLOR, height=OPTIONS_WINDOW_HEIGHT, width=OPTIONS_WINDOW_WIDTH,
                                       bd=0, highlightthickness=0, relief="ridge")
        self.options_canvas.place(x=0, y=0)
        self.options_canvas.create_image(300, 300, image=self.options_image_1)

        self.options_canvas.create_image(300, 83, image=self.options_settings_image_1)
        self.options_canvas.create_image(300, 128, image=self.options_settings_image_2)
        self.options_canvas.create_image(300, 188, image=self.options_settings_disabled_image_3 if settings['allow_max_generated_sentence_limit'] == False else self.options_settings_enabled_image_3)
        self.options_canvas.create_image(300, 263, image=self.options_settings_disabled_image_4 if settings['allow_min_generated_sentence_limit'] == False else self.options_settings_enabled_image_4)


    def setup_buttons(self):
        """Setup the options button."""
        self.options_button_1 = self.create_button(
            self.options_button_image_1,
            self.options_button_image_1_hover,
            self.options_button_1_pressed,
            420.0, 530.0,
            160.0, 50.0
        )
        self.options_button_2 = self.create_button(
            self.options_button_image_2,
            self.options_button_image_2_hover,
            self.options_button_2_pressed,
            420.0, 460.0,
            160.0, 50.0
        )
        self.options_button_3 = self.create_button(
            self.options_button_image_3,
            self.options_button_image_3_hover,
            self.options_button_3_pressed,
            20.0, 530.0,
            160.0, 50.0
        )

    def setup_checkboxes(self):
        self.options_checkbox_1 = self.create_checkbox_button(
            self.checkbutton_image_checked if settings['allow_random_generated_choices'] == True else self.checkbutton_image_unchecked,
            self.checkbox_checked_1_pressed if settings['allow_random_generated_choices'] == True else self.checkbox_unchecked_1_pressed,
            25, 72
        )
        self.options_checkbox_2 = self.create_checkbox_button(
            self.checkbutton_image_checked if settings['allow_random_generated_characters'] == True else self.checkbutton_image_unchecked,
            self.checkbox_checked_2_pressed if settings['allow_random_generated_characters'] == True else self.checkbox_unchecked_2_pressed,
            25, 117
        )
        self.options_checkbox_3 = self.create_checkbox_button(
            self.checkbutton_image_checked if settings['allow_max_generated_sentence_limit'] == True else self.checkbutton_image_unchecked,
            self.checkbox_checked_3_pressed if settings['allow_max_generated_sentence_limit'] == True else self.checkbox_unchecked_3_pressed,
            25, 162
        )
        self.options_checkbox_4 = self.create_checkbox_button(
            self.checkbutton_image_checked if settings['allow_min_generated_sentence_limit'] == True else self.checkbutton_image_unchecked,
            self.checkbox_checked_4_pressed if settings['allow_min_generated_sentence_limit'] == True else self.checkbox_unchecked_4_pressed,
            25, 237
        )

    def setup_spinbox(self):
        self.validate_cmd = self.register(self.validate_input)
        var = tk.IntVar(value=settings['maximum_word_limit'])
        self.max_words_spinbox = tk.Spinbox(self, from_=1, to=99, background='pink', width=2, textvariable=var,
                                            validate='key', validatecommand=(self.validate_cmd, '%P'))
        self.max_words_spinbox.place(x=231, y=193)
        self.max_words_spinbox.configure(state="disabled" if settings['allow_max_generated_sentence_limit'] == False else "normal")
        self.max_words_spinbox.bind("<Return>", self.on_value_max_change)

        self.validate_cmd_1 = self.register(self.validate_input)
        var1 = tk.IntVar(value=settings['minimum_word_limit'])
        self.min_words_spinbox = tk.Spinbox(self, from_=1, to=99, background='pink', width=2, textvariable=var1,
                                            validate='key', validatecommand=(self.validate_cmd_1, '%P'))
        self.min_words_spinbox.place(x=231, y=268)
        self.min_words_spinbox.configure(state="disabled" if settings['allow_min_generated_sentence_limit'] == False else "normal")
        

    def on_value_max_change(self, event):
        value = self.max_words_spinbox.get()
        print(f"Selected Max Words: {value}")
    
    def on_value_min_change(self, event):
        value = self.min_words_spinbox.get()
        print(f"Selected Min Words: {value}")

    def validate_input(self, new_value):
        # Allow empty input
        if new_value == "":
            return True
        
        # Check if the new value is a number and is within the range of 0-99
        if new_value.isdigit() and 1 <= int(new_value) <= 99:
            # Prevent input if the length exceeds 2 digits
            if len(new_value) > 2:
                return False
            return True
        
        return False
    
    def create_button(self, image, hover_image, command, x, y, width, height):
        """Helper method to create a button with common properties."""
        button = tk.Button(self, image=image, borderwidth=0,
                           highlightthickness=0, command=command, relief="flat")
        button.place(x=x, y=y, width=width, height=height)
        button.bind("<Enter>", lambda event: self.on_enter_button(event, hover_image))
        button.bind("<Leave>", lambda event: self.on_leave_button(event, image))
        return button

    def create_checkbox_button(self, image, command, x, y):
        """Helper method to create a button with common properties."""
        checkbox = tk.Button(self, image=image, borderwidth=0,
                           highlightthickness=0, command=command, relief="flat")
        checkbox.place(x=x, y=y, width=22.0, height=22.0)
        return checkbox
    
    def on_enter_button(self, event, hover_image):
        """Handles the mouse enter event for the button with hover effect."""
        self.hover_sound.play()  # Play hover sound
        event.widget.config(image=hover_image)  # Change to hover image

    def on_leave_button(self, event, original_image):
        """Handles the mouse leave event for the button."""
        event.widget.config(image=original_image)  # Change back to original image

    def options_button_1_pressed(self):
        self.click_sound.play()
        if not os.path.exists(WORD_LIST_PATH):
            word_list = default_word_list.get_default_list_of_words()
            with open(WORD_LIST_PATH, "w") as f:
                f.writelines('\n'.join(word_list))
        self.options_button_1.config(state="disabled")
        self.editor_window = Editor(self)
    
    def options_button_2_pressed(self):
        self.click_sound.play()
        word_list = default_word_list.get_default_list_of_words()
        with open(WORD_LIST_PATH, "w") as f:
            f.writelines('\n'.join(word_list))
            self.success_sound.play()
            if self.editor_window is not None and self.editor_window.winfo_exists():
                self.editor_window.load_words_from_file(WORD_LIST_PATH)
            SuccessWordListRestorationMessage(self)
        

    
    def options_button_3_pressed(self):
        self.click_sound.play()
        print(self.max_words_spinbox.get())

        if not os.path.exists(SETTINGS_PATH):
            with open(SETTINGS_PATH, "w") as f:
                f.writelines('\n'.join(DEFAULT_SETTINGS_LIST))
        self.save_settings('allow_random_generated_choices', True if self.options_checkbox_1.cget('image') == str(self.checkbutton_image_checked) else False)
        self.save_settings('allow_random_generated_characters', True if self.options_checkbox_2.cget('image') == str(self.checkbutton_image_checked) else False)
        self.save_settings('allow_max_generated_sentence_limit', True if self.options_checkbox_3.cget('image') == str(self.checkbutton_image_checked) else False)
        self.save_settings('allow_min_generated_sentence_limit', True if self.options_checkbox_4.cget('image') == str(self.checkbutton_image_checked) else False)
        self.save_settings('maximum_word_limit', self.max_words_spinbox.get()) if self.max_words_spinbox.cget('state') == "normal" else None
        self.save_settings('minimum_word_limit', self.min_words_spinbox.get()) if self.min_words_spinbox.cget('state') == "normal" else None
        self.load_settings(settings)
        self.success_sound.play()
        ChangesAppliedMessage(self)

    
    def checkbox_unchecked_1_pressed(self):
        self.click_sound.play()
        self.options_checkbox_1.config(command=self.checkbox_checked_1_pressed, image=self.checkbutton_image_checked)

    def checkbox_checked_1_pressed(self):
        self.click_sound.play()
        self.options_checkbox_1.config(command=self.checkbox_unchecked_1_pressed, image=self.checkbutton_image_unchecked)

    def checkbox_unchecked_2_pressed(self):
        self.click_sound.play()
        self.options_checkbox_2.config(command=self.checkbox_checked_2_pressed, image=self.checkbutton_image_checked)

    def checkbox_checked_2_pressed(self):
        self.click_sound.play()
        self.options_checkbox_2.config(command=self.checkbox_unchecked_2_pressed, image=self.checkbutton_image_unchecked)

    def checkbox_unchecked_3_pressed(self):
        self.click_sound.play()
        self.options_checkbox_3.config(command=self.checkbox_checked_3_pressed, image=self.checkbutton_image_checked)

        self.options_canvas.itemconfig(4, image=self.options_settings_enabled_image_3)
        self.max_words_spinbox.configure(state="normal")

    def checkbox_checked_3_pressed(self):
        self.click_sound.play()
        self.options_checkbox_3.config(command=self.checkbox_unchecked_3_pressed, image=self.checkbutton_image_unchecked)
        
        self.options_canvas.itemconfig(4, image=self.options_settings_disabled_image_3)
        self.max_words_spinbox.configure(state="disabled")
    
    def checkbox_unchecked_4_pressed(self):
        self.click_sound.play()
        self.options_checkbox_4.config(command=self.checkbox_checked_4_pressed, image=self.checkbutton_image_checked)

        self.options_canvas.itemconfig(5, image=self.options_settings_enabled_image_4)
        self.min_words_spinbox.configure(state="normal")

    def checkbox_checked_4_pressed(self):
        self.click_sound.play()
        self.options_checkbox_4.config(command=self.checkbox_unchecked_4_pressed, image=self.checkbutton_image_unchecked)
        
        self.options_canvas.itemconfig(5, image=self.options_settings_disabled_image_4)
        self.min_words_spinbox.configure(state="disabled")
    
    def on_close(self):
       self.master.main_button_8.config(state="normal")
       self.destroy()

class ChangesAppliedMessage(tk.Toplevel):
    """Frame displaying applied changes message with an exit button."""
    def __init__(self, master):
        super().__init__(master)
        initialize_window(self, "Success Message", SUCCESS_WINDOW_WIDTH, SUCCESS_WINDOW_HEIGHT, SUCCESS_WINDOW_BG_COLOR)
        self.load_assets()
        self.create_canvas()
        self.setup_button()

        self.focus_set()
        self.bind("<Return>", self.on_enter_key)

        
        
        master.wait_window(self)
    
    def load_assets(self):
        """Load sound effects and images for the applied changes message."""
        self.click_sound = pygame.mixer.Sound(SOUND_CLICK_PATH)
        self.hover_sound = pygame.mixer.Sound(SOUND_HOVER_PATH)
        self.success_button = pygame.mixer.Sound(SOUND_SUCCESS_PATH)
        self.success_options_image_1 = PhotoImage(file=SUCCESS_OPTIONS_IMAGE_1_PATH)
        self.ok_button_image = PhotoImage(file=OK_BUTTON_IMAGE_PATH)
        self.ok_button_image_hover = PhotoImage(file=OK_BUTTON_IMAGE_HOVER_PATH)
        self.another_error_image = PhotoImage(file=ERROR_IMAGE_2_PATH)
    
    def create_canvas(self):
        """Creates the applied changes message canvas and its elements."""
        self.success_generation_canvas = tk.Canvas(self, bg=SUCCESS_WINDOW_BG_COLOR, height=SUCCESS_WINDOW_HEIGHT, width=SUCCESS_WINDOW_WIDTH,
                                       bd=0, highlightthickness=0, relief="ridge")
        self.success_generation_canvas.place(x=0, y=0)
        self.success_generation_canvas.create_image(225.0, 64.0, image=self.success_options_image_1)
        self.success_generation_canvas.create_image(225.0, 163.0, image=self.another_error_image)

    def setup_button(self):
        """Setup the applied changes button."""
        self.success_button = tk.Button(self, image=self.ok_button_image, borderwidth=0,
                                       highlightthickness=0, command=self.success_button_pressed, relief="flat")
        self.success_button.place(x=260.0, y=139, width=160.0, height=50.0)
        self.success_button.bind("<Enter>", self.on_enter_success_button)
        self.success_button.bind("<Leave>", self.on_leave_success_button)

    def success_button_pressed(self):
        """Handles the applied changes button press action."""
        self.click_sound.play()
        self.destroy()

    def on_enter_success_button(self, event):
        """Handles the mouse enter event for the button."""
        self.hover_sound.play()
        event.widget.config(image=self.ok_button_image_hover)

    def on_leave_success_button(self, event):
        """Handles the mouse leave event for the button."""
        event.widget.config(image=self.ok_button_image)
    
    def on_enter_key(self, event):
        self.click_sound.play()
        self.destroy()


class SuccessWordListRestorationMessage(tk.Toplevel):
    """Frame displaying an successful word list restoration message with an exit button."""
    def __init__(self, master):
        super().__init__(master)
        initialize_window(self, "Success Message", SUCCESS_WINDOW_WIDTH, SUCCESS_WINDOW_HEIGHT, SUCCESS_WINDOW_BG_COLOR)
        self.load_assets()
        self.create_canvas()
        self.setup_button()

        self.focus_set()
        self.bind("<Return>", self.on_enter_key)

        
        
        master.wait_window(self)
    
    def load_assets(self):
        """Load sound effects and images for the success word list restoration message."""
        self.click_sound = pygame.mixer.Sound(SOUND_CLICK_PATH)
        self.hover_sound = pygame.mixer.Sound(SOUND_HOVER_PATH)
        self.success_image_3 = PhotoImage(file=SUCCESS_IMAGE_3_PATH)
        self.ok_button_image = PhotoImage(file=OK_BUTTON_IMAGE_PATH)
        self.ok_button_image_hover = PhotoImage(file=OK_BUTTON_IMAGE_HOVER_PATH)
        self.another_error_image = PhotoImage(file=ERROR_IMAGE_2_PATH)
    
    def create_canvas(self):
        """Creates the success restoration message canvas and its elements."""
        self.success_restoration_canvas = tk.Canvas(self, bg=SUCCESS_WINDOW_BG_COLOR, height=SUCCESS_WINDOW_HEIGHT, width=SUCCESS_WINDOW_WIDTH,
                                       bd=0, highlightthickness=0, relief="ridge")
        self.success_restoration_canvas.place(x=0, y=0)
        self.success_restoration_canvas.create_image(225.0, 64.0, image=self.success_image_3)
        self.success_restoration_canvas.create_image(225.0, 163.0, image=self.another_error_image)

    def setup_button(self):
        """Setup the success restoration button."""
        self.success_button = tk.Button(self, image=self.ok_button_image, borderwidth=0,
                                       highlightthickness=0, command=self.success_button_pressed, relief="flat")
        self.success_button.place(x=260.0, y=139, width=160.0, height=50.0)
        self.success_button.bind("<Enter>", self.on_enter_success_button)
        self.success_button.bind("<Leave>", self.on_leave_success_button)

    def success_button_pressed(self):
        """Handles the success restoration button press action."""
        self.click_sound.play()
        self.destroy()

    def on_enter_success_button(self, event):
        """Handles the mouse enter event for the button."""
        self.hover_sound.play()
        event.widget.config(image=self.ok_button_image_hover)

    def on_leave_success_button(self, event):
        """Handles the mouse leave event for the button."""
        event.widget.config(image=self.ok_button_image)
    
    def on_enter_key(self, event):
        self.click_sound.play()
        self.destroy()


class Editor(tk.Toplevel):
    """Editor frame."""
    
    # TODO: fix a bug when you open one window and inside window you open another window and then close one window, it allows users to  for the main  
    def __init__(self, master):
        super().__init__(master)
        initialize_window(self, "Word List Editor", EDITOR_WINDOW_WIDTH, EDITOR_WINDOW_HEIGHT, EDITOR_WINDOW_BG_COLOR)
        self.load_assets()
        self.create_canvas()

        self.create_tree()
        self.setup_buttons()
        self.setup_input_field()

        

        self.protocol("WM_DELETE_WINDOW", self.on_close)


    def load_assets(self):
        """Load sound effects and images for the editor."""
        self.click_sound = pygame.mixer.Sound(SOUND_CLICK_PATH)
        self.hover_sound = pygame.mixer.Sound(SOUND_HOVER_PATH)
        self.editor_success_sound = pygame.mixer.Sound(SOUND_EDITOR_SUCCESS_PATH)
        self.editor_image_1 = PhotoImage(file=EDITOR_IMAGE_1_PATH)
        self.editor_button_image_1 = PhotoImage(file=EDITOR_BUTTON_1_PATH)
        self.editor_button_image_1_hover = PhotoImage(file=EDITOR_BUTTON_1_HOVER_PATH)
        self.editor_button_image_2 = PhotoImage(file=EDITOR_BUTTON_2_PATH)
        self.editor_button_image_2_hover = PhotoImage(file=EDITOR_BUTTON_2_HOVER_PATH)
        self.editor_button_image_3 = PhotoImage(file=EDITOR_BUTTON_3_PATH)
        self.editor_button_image_3_hover = PhotoImage(file=EDITOR_BUTTON_3_HOVER_PATH)
        self.editor_button_image_4 = PhotoImage(file=EDITOR_BUTTON_4_PATH)
        self.editor_button_image_4_hover = PhotoImage(file=EDITOR_BUTTON_4_HOVER_PATH)
        self.editor_button_image_5 = PhotoImage(file=EDITOR_BUTTON_5_PATH)
        self.editor_button_image_5_hover = PhotoImage(file=EDITOR_BUTTON_5_HOVER_PATH)

        self.editor_information_image_1 = PhotoImage(file=EDITOR_INFORMATION_IMAGE_1_PATH)
        self.editor_information_image_2 = PhotoImage(file=EDITOR_INFORMATION_IMAGE_2_PATH)
        self.editor_information_image_2_not_found = PhotoImage(file=EDITOR_INFORMATION_IMAGE_2_NOT_FOUND_PATH)
        self.editor_information_image_3 = PhotoImage(file=EDITOR_INFORMATION_IMAGE_3_PATH)
        self.editor_information_image_4 = PhotoImage(file=EDITOR_INFORMATION_IMAGE_4_PATH)
        self.editor_information_image_4_already_exists = PhotoImage(file=EDITOR_INFORMATION_IMAGE_4_ALREADY_EXISTS_PATH)
    
    def create_canvas(self):
        """Creates the editor canvas and its elements."""
        self.editor_canvas = tk.Canvas(self, bg=EDITOR_WINDOW_BG_COLOR, height=EDITOR_WINDOW_HEIGHT, width=EDITOR_WINDOW_WIDTH,
                                       bd=0, highlightthickness=0, relief="ridge")
        self.editor_canvas.place(x=0, y=0)
        self.editor_canvas.create_image(300, 300, image=self.editor_image_1)
    
    def create_button(self, image, hover_image, command, x, y, width, height):
        """Helper method to create a button with common properties."""
        button = tk.Button(self, image=image, borderwidth=0,
                           highlightthickness=0, command=command, relief="flat")
        button.place(x=x, y=y, width=width, height=height)
        button.bind("<Enter>", lambda event: self.on_enter_button(event, hover_image))
        button.bind("<Leave>", lambda event: self.on_leave_button(event, image))
        return button

    def on_enter_button(self, event, hover_image):
        """Handles the mouse enter event for the button with hover effect."""
        self.hover_sound.play()  # Play hover sound
        event.widget.config(image=hover_image)  # Change to hover image

    def on_leave_button(self, event, original_image):
        """Handles the mouse leave event for the button."""
        event.widget.config(image=original_image)  # Change back to original image
    
    def setup_buttons(self):
        """Setup the editor buttons."""
        self.editor_button_1 = self.create_button(
            self.editor_button_image_1,
            self.editor_button_image_1_hover,
            self.editor_button_1_pressed,
            20.0, 530.0,
            125.0, 50.0
        )
        self.editor_button_2 = self.create_button(
            self.editor_button_image_2,
            self.editor_button_image_2_hover,
            self.editor_button_2_pressed,
            165.0, 530.0,
            125.0, 50.0
        )
        self.editor_button_3 = self.create_button(
            self.editor_button_image_3,
            self.editor_button_image_3_hover,
            self.editor_button_3_pressed,
            310.0, 530.0,
            125.0, 50.0
        )
        self.editor_button_4 = self.create_button(
            self.editor_button_image_4,
            self.editor_button_image_4_hover,
            self.editor_button_4_pressed,
            455.0, 530.0,
            125.0, 50.0
        )
        self.editor_button_5 = self.create_button(
            self.editor_button_image_5,
            self.editor_button_image_5_hover,
            self.editor_button_5_pressed,
            20.0, 460.0,
            125.0, 50.0
        )
        
    
    def create_tree(self):
        # Frame to hold Treeview and Scrollbar
        frame = ttk.Frame(self, width=100, height=550)
        frame.config()
        frame.place(x=185, y=60)

        # Create a ttk.Style object
        self.style = ttk.Style()

        self.style.theme_use("clam")

        # Configure the Treeview style for normal and selected row
        self.style.configure("Pink.Treeview",
                        background='pink',
                        foreground='black',
                        rowheight=25,
                        fieldbackground='pink')
        self.style.map("Pink.Treeview", 
                  background=[('selected', 'lightpink'), ('!selected', 'pink')],
                  foreground=[('selected', 'black'), ('!selected', 'black')],
                  fieldbackground=[('selected', 'lightpink'), ('!selected', 'pink')])

        # Add a Treeview widget
        self.word_list_tree = ttk.Treeview(frame, column=("c1", "c2"), show='headings', height=14, style="Pink.Treeview")

        self.curItem = None

        def selectItem(a, event=None):
            # Get currently focused item
            current_item = self.word_list_tree.focus()
            
            # Clear previous selection if any
            if self.curItem is not None:
               self.word_list_tree.item(self.curItem, tags='')  # Optionally remove tags or change some attributes if needed

            # Update the current item
            self.curItem = current_item

            # Highlight the selected item
            if self.curItem:
                item_values = self.word_list_tree.item(self.curItem, tags=('selected',))  # You can add a specific tag or change the item's appearance
                item_text = ' '.join(item_values)
                print(item_text)

                # Highlight the selected item and retrieve the word
                if self.curItem:
                    item_values = self.word_list_tree.item(self.curItem, 'values')  # Get the values of the selected item
                    if item_values:  # Check if there are valid values
                        item_text = item_values[1]  # Get the word from the second column (index 1)
                        print(item_text)  # Output the word for debugging

                        # Highlight the selected item visually
                        self.word_list_tree.item(self.curItem, tags=('selected',))  # Highlighting the selected item

                        # Insert the selected word into the input field
                        self.editor_input.delete('1.0', tk.END)  # Clear previous text
                        self.editor_input.insert(tk.END, item_text)  # Insert the new text into editor input
                    else:
                        print("Selected item has no valid values.")

        self.word_list_tree.column("#1", anchor=constants.CENTER, width=70, minwidth=70)
        self.word_list_tree.heading("#1", anchor=constants.CENTER, text="ID")
        self.word_list_tree.column("#2", anchor=constants.W, width=308, minwidth=308)
        self.word_list_tree.heading("#2", anchor=constants.W, text="Word")

        scrollbar_vertical = ttk.Scrollbar(self, orient="vertical", command=self.word_list_tree.yview)
        scrollbar_horizontal = ttk.Scrollbar(self, orient="horizontal", command=self.word_list_tree.xview)

        # Keybinds
        self.word_list_tree.bind('<ButtonRelease-1>', selectItem)
        self.word_list_tree.bind('<Up>', selectItem)
        self.word_list_tree.bind('<KeyRelease-Up>', selectItem)
        self.word_list_tree.bind('<Down>', selectItem)
        self.word_list_tree.bind('<KeyRelease-Down>', selectItem)
        self.word_list_tree.bind('<Delete>', self.editor_button_1_pressed)

        self.word_list_tree.config(selectmode="extended")

        self.load_words_from_file(WORD_LIST_PATH)
        
        self.word_list_tree.pack(side=tk.LEFT, fill=tk.X)
        scrollbar_vertical.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_horizontal.pack(side=tk.BOTTOM, fill=tk.X, expand=True)

        # Manually place scrollbars poisition
        scrollbar_vertical.place(relx=0.945, rely=0.100, width=15, height=393)
        scrollbar_horizontal.place(relx=0.308, rely=0.732, width=382, height=15)

        # It changes thunb size based on treelist size
        self.word_list_tree.configure(yscrollcommand=scrollbar_vertical.set)
        self.word_list_tree.configure(xscrollcommand=scrollbar_horizontal.set)

        scrollbar_horizontal.config(command=self.word_list_tree.xview)
        scrollbar_vertical.config(command=self.word_list_tree.yview)

    def load_words_from_file(self, file_path):
        # Clear the current contents of the Treeview
        for item in self.word_list_tree.get_children():
            self.word_list_tree.delete(item)

        try:
            with open(file_path, "r") as f:
                for index, line in enumerate(f, start=1):
                    word = line.strip()  # Remove surrounding whitespace
                    if word:  # Ensure that the word is not empty
                        self.word_list_tree.insert('', 'end', iid=index, text=index, values=(index, word))
            print("Words loaded from file successfully.")

        except FileNotFoundError:
            print(f"The file at {file_path} does not exist.")
        except Exception as e:
            print(f"An error occurred while loading the word file: {e}")
        
    def delete_word_from_file(self, line_number):
        """Delete the word at the specified line number from the file."""
        try:
            with open(WORD_LIST_PATH, "r") as f:
                lines = f.readlines()

            # Remove the specific line (line number is 1-based)
            if 0 < line_number <= len(lines):  # Ensure the line number is valid
                removed_word = lines[line_number - 1].strip()  # Get the word to display in the log
                lines.pop(line_number - 1)  # Remove the line from the list

                # Write the updated words back to the file
                with open(WORD_LIST_PATH, "w") as f:
                    f.writelines(lines)

                print(f"Deleted '{removed_word}' from line {line_number} in the file.")
            else:
                print("Line number is out of range.")

        except Exception as e:
            print(f"An error occurred while updating the word file: {e}")
    
    def update_word_in_file(self, line_number, new_word):
        """Update the word file by replacing the word at the specified line number."""
        try:
            with open(WORD_LIST_PATH, "r") as f:
                lines = f.readlines()

            # Update the specific line number (line_number is 1-based, so subtract 1 for 0-based index)
            if 0 < line_number <= len(lines):  # Ensure line_number is within the valid range
                lines[line_number - 1] = new_word + "\n"  # Replace with the new word and add newline

                # Write the updated words back to the file
                with open(WORD_LIST_PATH, "w") as f:
                    f.writelines(lines)

                print(f"Updated line {line_number} to '{new_word}' in the file.")
            else:
                print("Line number is out of range.")

        except Exception as e:
            print(f"An error occurred while updating the word file: {e}")

    
    def delete_item_from_file(self, item_to_delete):
        try:
            with open('items.txt', 'r') as file:
                lines = file.readlines()
            updated_lines = [line for line in lines if line.strip() != item_to_delete]
            with open('items.txt', 'w') as file:
                file.writelines(updated_lines)
            print(f"Item {item_to_delete} deleted from file.")
        except Exception as e:
            print(f"An error occurred: {e}")  # Exception handling
    
    def setup_input_field(self):
        """Setup the editor input field."""
        self.editor_input = tk.Text(self, height=1, width=51, bd=2, wrap='word',background='pink')
        self.editor_input.place(x=165, y=474)

        self.MAX_LENGTH_OF_INPUT_LETTERS = 51
        self.enter_pressed = False

        # Bind the Enter key to the on_enter_key function
        self.editor_input.bind("<Return>", self.on_enter_key)

        # Bind key press events to limit the length
        self.editor_input.bind("<Key>", self.limit_length)

        # Bind key release event to reset the enter_pressed flag
        self.editor_input.bind("<KeyRelease>", self.on_key_release)
        
        # Disabling copy/paste
        self.editor_input.bind('<Control-v>', lambda _: 'break')
        self.editor_input.bind('<Control-c>', lambda _: 'break')

    def on_enter_key(self, event):
        if not self.enter_pressed:
            self.click_sound.play()
            self.editor_button_4_pressed()
            self.editor_input.delete("1.0", END)
            self.enter_pressed = True
        
    def on_key_release(self, event):
        if event.keysym == 'Return':
            self.enter_pressed
            self.enter_pressed = False
            self.editor_input.delete("1.0", END)

    def limit_length(self, event):
        if event.keysym in ('BackSpace', 'Delete', 'Up', 'Down', 'Left', 'Right'):
            return

        if len(self.editor_input.get("1.0", "end-1c")) >= self.MAX_LENGTH_OF_INPUT_LETTERS:
            return "break"  # Prevent further input
            
    
    def update_ids_in_tree(self):
        """Update the IDs in the Treeview to ensure they are sequential."""
        for index, item in enumerate(self.word_list_tree.get_children(), start=1):
            # Update the ID in the item's text (the first column)
            self.word_list_tree.item(item, text=index, values=(index, self.word_list_tree.item(item)['values'][1]))

    def editor_button_1_pressed(self, event=None):
        self.click_sound.play()  # Play the click sound
        if self.curItem:  # Check if an item is selected
            word_text = self.word_list_tree.item(self.curItem)['values'][1].strip()  # Get the word from the selected item's values
            line_number = self.word_list_tree.item(self.curItem)['values'][0]  # Get the line number (ID)

            # Get the current index before deleting
            current_index = self.word_list_tree.index(self.curItem)

            self.word_list_tree.delete(self.curItem)  # Delete from Treeview
            print(f"Deleted word: {word_text}")

            self.delete_word_from_file(line_number)  # Remove from file using line number
            self.curItem = None  # Clear reference

            # Select the next item if available, otherwise select the previous one
            new_item = None
            children = self.word_list_tree.get_children()  # Store references to current children
            if current_index < len(children):
                # Select the next item
                new_item = children[current_index] if current_index < len(children) else None
            elif current_index > 0:
                # Select the previous item
                new_item = children[current_index - 1]

            # Update the IDs of remaining items
            self.update_ids_in_tree()

            self.curItem = new_item  # Update the current item reference
            if self.curItem:
                self.word_list_tree.selection_set(self.curItem)  # Select the new item
                self.word_list_tree.focus(self.curItem)  # Set focus to the new item
            else:
                print("No more items in the list.")
        else:
            print("No item selected to delete.")
            InformationMessage(self, self.editor_information_image_1)
    
    def editor_button_2_pressed(self):
        self.click_sound.play()
        inputed_word = self.editor_input.get("1.0", "end-1c").strip()
    
        if inputed_word:
        
            # Get the list of children once
            children = self.word_list_tree.get_children()
    
            for index, item in enumerate(children, start=1):
                word_in_list = self.word_list_tree.item(item)['values'][1].strip()  # Get the word from the current item
                
                if word_in_list == inputed_word:
                    self.curItem = item  # Update the current item
                    self.word_list_tree.selection_set(self.curItem)
    
                    self.word_list_tree.focus(self.curItem)  # Set focus to the matching item
                    self.word_list_tree.see(self.curItem)
                    print(f"Selected word: '{inputed_word}'")
                    break
                
                # Check if the current item is the last item in the list
                if index == len(children) - 1:
                    print(f"'{inputed_word}' was not found.")
                    InformationMessage(self, self.editor_information_image_2_not_found)
        else:
            print("No word provided to search.")
            InformationMessage(self, self.editor_information_image_2)
    
    def editor_button_3_pressed(self):
        self.click_sound.play()
        if self.curItem is not None:  # Check if an item is selected
            new_word = self.editor_input.get("1.0", "end-1c").strip()  # Get the edited word from the input field
            old_word = self.word_list_tree.item(self.curItem)['values'][1].strip()  # Get the current word from the selected item
            line_number = self.word_list_tree.item(self.curItem)['values'][0]  # Get the line number based on ID

            if new_word:  # Proceed only if the input is valid
                # Update the Treeview item
                self.word_list_tree.item(self.curItem, values=(line_number, new_word))  # Update Treeview with new word

                # Update the underlying data file using the line number
                self.update_word_in_file(line_number, new_word)

                print(f"Updated word: '{old_word}' to '{new_word}' successfully.")
            else:
                InformationMessage(self, self.editor_information_image_3)
                print("No word provided to update.")  # Handle empty input
        else:
            print("No item selected to update.")
            InformationMessage(self, self.editor_information_image_3)
        
    def editor_button_4_pressed(self, event=None):
        """Add a word from the input field to the Treeview and the file."""
        self.click_sound.play()
        # Get the word from the Text widget
        new_word = self.editor_input.get("1.0", "end-1c").strip()  # Get the text, removing extra whitespace
        
        
        if new_word:  # Only proceed if there is a valid word
            if new_word:  # Only proceed if there is a valid word
                # Check if the new_word already exists in the file
                with open(WORD_LIST_PATH, "r") as f:
                    existing_words = [line.strip() for line in f.readlines()]  # Read existing words from the file

                if new_word in existing_words:
                    print(f"The word '{new_word}' already exists in the word list.")
                    InformationMessage(self, self.editor_information_image_4_already_exists)
                    return  # Exit the method without adding the word

            # Add the new word to the Treeview
            current_index = len(self.word_list_tree.get_children()) + 1  # Get current number of items to use as index
            new_item = self.word_list_tree.insert('', 'end', values=(current_index, new_word))  # Insert into Treeview
            print(f"Added word: {new_word}")
    
            # Append the new word to the file
            with open(WORD_LIST_PATH, "a") as f:
                f.write(new_word + "\n")  # Append the new word with a newline
            
            # After inserting, ensure the new item is visible
            self.word_list_tree.see(new_item)  # Scroll to the newly added item
            self.word_list_tree.selection_set(new_item)  # Select the new item
            self.word_list_tree.focus(new_item)  # Set focus to the new item

            # Clear the input field after adding
            self.editor_input.delete("1.0", "end")  # Clear the Text widget
        else:
            InformationMessage(self, self.editor_information_image_4)
            print("No word provided to add.")
    
    def editor_button_5_pressed(self):
        self.click_sound.play()  # Play the click sound for feedback
        DeleteAllConfirmationMessage(self)
    
    def on_close(self):
       self.master.options_button_1.config(state="normal")
       self.destroy()

class DeleteAllConfirmationMessage(tk.Toplevel):
    """Frame displaying a delete all confirmation message with an exit button."""
    def __init__(self, master):
        super().__init__(master)
        initialize_window(self, "Confirmation Message", SUCCESS_WINDOW_WIDTH, SUCCESS_WINDOW_HEIGHT, SUCCESS_WINDOW_BG_COLOR)
        self.load_assets()
        self.create_canvas()
        self.setup_button()

        self.focus_set()

        
        
        master.wait_window(self)
    
    def load_assets(self):
        """Load sound effects and images for the delete all confirmation message."""
        self.click_sound = pygame.mixer.Sound(SOUND_CLICK_PATH)
        self.hover_sound = pygame.mixer.Sound(SOUND_HOVER_PATH)
        self.editor_confirmation_image_1 = PhotoImage(file=EDITOR_CONFIRMATION_IMAGE_1_PATH)
        self.editor_confirmation_button_1 = PhotoImage(file=EDITOR_CONFIRMATION_BUTTON_1_PATH)
        self.editor_confirmation_button_1_hover = PhotoImage(file=EDITOR_CONFIRMATION_BUTTON_1_HOVER_PATH)
        self.editor_confirmation_button_2 = PhotoImage(file=EDITOR_CONFIRMATION_BUTTON_2_PATH)
        self.editor_confirmation_button_2_hover = PhotoImage(file=EDITOR_CONFIRMATION_BUTTON_2_HOVER_PATH)
        self.another_error_image = PhotoImage(file=ERROR_IMAGE_2_PATH)
    
    def create_canvas(self):
        """Creates the delete all confirmation message canvas and its elements."""
        self.editor_confirmation_canvas = tk.Canvas(self, bg=SUCCESS_WINDOW_BG_COLOR, height=SUCCESS_WINDOW_HEIGHT, width=SUCCESS_WINDOW_WIDTH,
                                       bd=0, highlightthickness=0, relief="ridge")
        self.editor_confirmation_canvas.place(x=0, y=0)
        self.editor_confirmation_canvas.create_image(225.0, 64.0, image=self.editor_confirmation_image_1)
        self.editor_confirmation_canvas.create_image(225.0, 163.0, image=self.another_error_image)

    def setup_button(self):
        """Setup the delete all confirmation buttons."""
        self.no_button = tk.Button(self, image=self.editor_confirmation_button_1, borderwidth=0,
                                       highlightthickness=0, command=self.no_button_pressed, relief="flat")
        self.no_button.place(x=260, y=139, width=160.0, height=50.0)
        self.no_button.bind("<Enter>", self.on_enter_no_button)
        self.no_button.bind("<Leave>", self.on_leave_no_button)

        self.yes_button = tk.Button(self, image=self.editor_confirmation_button_2, borderwidth=0,
                                       highlightthickness=0, command=self.yes_button_pressed, relief="flat")
        self.yes_button.place(x=30, y=139, width=160.0, height=50.0)
        self.yes_button.bind("<Enter>", self.on_enter_yes_button)
        self.yes_button.bind("<Leave>", self.on_leave_yes_button)

    def no_button_pressed(self):
        """Handles the delete all confirmation action."""
        self.click_sound.play()
        self.destroy()

    def on_enter_no_button(self, event):
        """Handles the mouse enter event for the button."""
        self.hover_sound.play()
        event.widget.config(image=self.editor_confirmation_button_1_hover)

    def on_leave_no_button(self, event):
        """Handles the mouse leave event for the button."""
        event.widget.config(image=self.editor_confirmation_button_1)

    def yes_button_pressed(self):
        """Handles the delete all confirmation action."""
        self.click_sound.play()
        try:
            # Create a list to hold all the words in the Treeview for writing to file
            updated_words = []
    
            # Write the updated words back to the file
            with open(WORD_LIST_PATH, "w") as f:
                f.writelines(updated_words)
    
            self.master.load_words_from_file(WORD_LIST_PATH)
            self.cur_item = None
            print("Word list updated successfully.")
            self.master.editor_success_sound.play()
        except Exception as e:
            print(f"An error occurred while updating the word file: {e}")
        self.destroy()

    def on_enter_yes_button(self, event):
        """Handles the mouse enter event for the button."""
        self.hover_sound.play()
        event.widget.config(image=self.editor_confirmation_button_2_hover)

    def on_leave_yes_button(self, event):
        """Handles the mouse leave event for the button."""
        event.widget.config(image=self.editor_confirmation_button_2)
    
    def on_enter_key(self, event):
        self.click_sound.play()
        self.destroy()

class InformationMessage(tk.Toplevel):
    """Frame displaying an editor information message with an exit button."""
    def __init__(self, master, info_image):
        super().__init__(master)
        initialize_window(self, "Information Message", SUCCESS_WINDOW_WIDTH, SUCCESS_WINDOW_HEIGHT, SUCCESS_WINDOW_BG_COLOR)
        self.info_image = info_image
        self.load_assets()
        self.create_canvas()
        self.setup_button()

        self.focus_set()
        self.bind("<Return>", self.on_enter_key)

        
        
        master.wait_window(self)
    
    def load_assets(self):
        """Load sound effects and images for the editor information message."""
        self.click_sound = pygame.mixer.Sound(SOUND_CLICK_PATH)
        self.hover_sound = pygame.mixer.Sound(SOUND_HOVER_PATH)

        self.ok_button_image = PhotoImage(file=OK_BUTTON_IMAGE_PATH)
        self.ok_button_image_hover = PhotoImage(file=OK_BUTTON_IMAGE_HOVER_PATH)
        self.another_error_image = PhotoImage(file=ERROR_IMAGE_2_PATH)
    
    def create_canvas(self):
        """Creates the editor information message canvas and its elements."""
        self.message_canvas = tk.Canvas(self, bg=SUCCESS_WINDOW_BG_COLOR, height=SUCCESS_WINDOW_HEIGHT, width=SUCCESS_WINDOW_WIDTH,
                                       bd=0, highlightthickness=0, relief="ridge")
        self.message_canvas.place(x=0, y=0)
        self.message_canvas.create_image(225.0, 64.0, image=self.info_image)
        self.message_canvas.create_image(225.0, 163.0, image=self.another_error_image)
    
    def setup_button(self):
        """Setup the editor information button."""
        self.information_button = tk.Button(self, image=self.ok_button_image, borderwidth=0,
                                       highlightthickness=0, command=self.information_button_pressed, relief="flat")
        self.information_button.place(x=260, y=139, width=160.0, height=50.0)
        self.information_button.bind("<Enter>", self.on_enter_information_button)
        self.information_button.bind("<Leave>", self.on_leave_information_button)
    
    def information_button_pressed(self):
        """Handles the editor information action."""
        self.click_sound.play()
        self.destroy()

    def on_enter_information_button(self, event):
        """Handles the mouse enter event for the button."""
        self.hover_sound.play()
        event.widget.config(image=self.ok_button_image_hover)

    def on_leave_information_button(self, event):
        """Handles the mouse leave event for the button."""
        event.widget.config(image=self.ok_button_image)

    def on_enter_key(self, event):
        self.click_sound.play()
        self.destroy()



def initialize_window(root, title, width, height, background_color):
    """Initialize a Tkinter window with specified parameters."""
    root.title(title)
    root.geometry(f'{width}x{height}+{(root.winfo_screenwidth() // 2) - (width // 2)}+'
                  f'{(root.winfo_screenheight() // 2) - (height // 2)}')
    root.configure(bg=background_color)
    root.iconbitmap(ICON_PATH)
    root.resizable(False, False)


def main():
    root = tk.Tk()  # Initialize the main Tkinter window

    if not os.path.exists(GAME_EXECUTABLE_FILE_PATH):
        initialize_window(root, 'Error Message', ERROR_WINDOW_WIDTH, ERROR_WINDOW_HEIGHT, ERROR_WINDOW_BG_COLOR)
        main_frame = ErrorMessage(root)  # Show error message
    else:
        if not os.path.exists(WORD_LIST_PATH):
            word_list = default_word_list.get_default_list_of_words()
            with open(WORD_LIST_PATH, "w") as f:
                f.writelines('\n'.join(word_list))

        if not os.path.exists(SETTINGS_PATH):
            with open(SETTINGS_PATH, "w") as f:
                f.writelines('\n'.join(DEFAULT_SETTINGS_LIST))


        initialize_window(root, 'NGDN: RDGM 1.1v', MAIN_WINDOW_WIDTH, MAIN_WINDOW_HEIGHT, MAIN_WINDOW_BG_COLOR)
        main_frame = Main(root)  # Show main application

    main_frame.pack(fill=tk.BOTH, expand=True)  # Pack the main frame
    root.mainloop()  # Start the event loop


if __name__ == '__main__':
    main()  # Run the main function