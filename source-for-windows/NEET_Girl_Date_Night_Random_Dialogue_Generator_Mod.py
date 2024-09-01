# Made by WhiteFruitNinja

# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

# Comment from WhiteFruitNinja
# My code is not good. Please don't judge 😔.

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Button, PhotoImage, Toplevel

import webbrowser
import pygame
import dialogue_generator
import os
import sys

# Correctly define the assets and game executable paths
if getattr(sys, 'frozen', False):  # Check if the application is frozen
    # The application is run as a bundle
    script_dir = os.path.dirname(sys.executable)
else:
    # The application is run as a script
    script_dir = os.path.dirname(os.path.abspath(__file__))

ASSETS_PATH = script_dir / Path("assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

game_executable_file_path = script_dir / Path("NEET_Girl_Date_Night.exe")
print(game_executable_file_path)
game_executable_32_file_path = script_dir / Path("NEET_Girl_Date_Night-32.exe")
print(game_executable_32_file_path)

pygame.mixer.init()

# Sounds
click_sound = pygame.mixer.Sound(str(ASSETS_PATH / "sfx/click.mp3"))
hover_sound = pygame.mixer.Sound(str(ASSETS_PATH / "sfx/hover.mp3"))

if not os.path.exists(game_executable_file_path):
    def show_error_message():
        error_window = Tk()
        error_window.title('Error Message')
        error_window.geometry("450x200")
        error_window.configure(bg = "#FFFFFF")
        error_window.iconbitmap(str(ASSETS_PATH / "Icon.ico"))

        def error_button_1_pressed():
            click_sound.play()
            error_window.destroy()

        def on_enter_error_button_1(e):
            hover_sound.play()
            error_button_1.config(image = error_button_image_1_hover)

        def on_leave_error_button_1(e):
            error_button_1.config(image = error_button_image_1)

        error_canvas = Canvas(
        error_window,
        bg = "#FFFFFF",
        height = 200,
        width = 450,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )

        error_canvas.place(x = 0, y = 0)
        error_image_file_not_found_image_1 = PhotoImage(
            file=relative_to_assets("error_image_file_not_found_1.png"))
        error_image_file_not_found_1 = error_canvas.create_image(
            225,
            65,
            image=error_image_file_not_found_image_1
        )
        error_canvas.image = error_image_file_not_found_image_1

        error_button_image_1 = PhotoImage(
            file=relative_to_assets("error_button_1.png"))
        error_button_image_1_hover = PhotoImage(
            file=relative_to_assets("error_button_1_hover.png"))
        error_button_1 = Button(
            error_window,
            image=error_button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=error_button_1_pressed,
            relief="flat"
        )
        error_button_1.place(
            x=260.0,
            y=139,
            width=160.0,
            height=50.0
        )
        error_button_1.bind("<Enter>", on_enter_error_button_1)
        error_button_1.bind("<Leave>", on_leave_error_button_1)

        error_image_image_2 = PhotoImage(
            file=relative_to_assets("error_image_2.png"))
        error_image_2 = error_canvas.create_image(
            225.0,
            163.0,
            image=error_image_image_2
        )
        error_canvas.image2 = error_image_image_2

        error_window.resizable(False, False)
        error_window.mainloop()

    show_error_message()
else:
    window = Tk()
    window.title('NEET Girl Date Night: Random Dialogue Generator Mod')
    window.geometry("600x600")
    window.configure(bg = "#FFC0CB")
    window.iconbitmap(str(ASSETS_PATH / "Icon.ico"))

    # Music
    musicname = "Aria Bare - New Special Interest.mp3"

    # Plays music when program starts
    pygame.mixer.music.load(str(ASSETS_PATH / "music/Aria Bare - New Special Interest.mp3"))
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(loops=-1)

    def button_1_pressed():
        click_sound.play()
        canvas.itemconfig(image_2,
                          image = image_image_6)
        button_1.config(image=button_image_7_hover,
                        command=button_7_pressed)
        pygame.mixer.music.pause()
        button_1.bind("<Enter>", on_enter_button_7)
        button_1.bind("<Leave>", on_leave_button_7)

    def button_7_pressed():
        click_sound.play()
        canvas.itemconfig(image_2,
                          image = image_image_2)
        button_1.config(image=button_image_1_hover,
                        command=button_1_pressed)
        pygame.mixer.music.unpause()
        button_1.bind("<Enter>", on_enter_button_1)
        button_1.bind("<Leave>", on_leave_button_1)

    # Run 32-bit mode
    def button_3_pressed():
        click_sound.play()
        os.startfile(script_dir + "/NEET_Girl_Date_Night-32.exe")
        global window
        window.quit()

    # Run 64-bit mode
    def button_6_pressed():
        click_sound.play()
        os.startfile(script_dir + "/NEET_Girl_Date_Night.exe")
        global window
        window.quit()

    # Generates random dialogues
    def generate_random_dialogues():
        click_sound.play()
        dialogue_generator.read_txt_file()
        try:
            dialogue_generator.check_if_unrenpyc_file_exist()
            dialogue_generator.read_and_write_rpy_files()
            show_success_generation_message()
        except:
            def show_restore_error_message():
                error_window = Toplevel(window)
                error_window.title('Error Message')
                error_window.geometry("450x200")
                error_window.configure(bg = "#FFFFFF")
                error_window.iconbitmap(str(ASSETS_PATH / "Icon.ico"))

                def error_button_1_pressed():
                    click_sound.play()
                    error_window.destroy()

                def on_enter_error_button_1(e):
                    hover_sound.play()
                    error_button_1.config(image = error_button_image_1_hover)

                def on_leave_error_button_1(e):
                    error_button_1.config(image = error_button_image_1)

                error_canvas = Canvas(
                error_window,
                bg = "#FFFFFF",
                height = 200,
                width = 450,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
                )

                error_canvas.place(x = 0, y = 0)
                error_image_file_not_found_image_3 = PhotoImage(
                    file=relative_to_assets("error_image_file_not_found_3.png"))
                error_image_file_not_found_3 = error_canvas.create_image(
                    225,
                    65,
                    image=error_image_file_not_found_image_3
                )
                error_canvas.image = error_image_file_not_found_image_3

                error_button_image_1 = PhotoImage(
                    file=relative_to_assets("error_button_1.png"))
                error_button_image_1_hover = PhotoImage(
                    file=relative_to_assets("error_button_1_hover.png"))
                error_button_1 = Button(
                    error_window,
                    image=error_button_image_1,
                    borderwidth=0,
                    highlightthickness=0,
                    command=error_button_1_pressed,
                    relief="flat"
                )
                error_button_1.place(
                    x=260.0,
                    y=139,
                    width=160.0,
                    height=50.0
                )
                error_button_1.bind("<Enter>", on_enter_error_button_1)
                error_button_1.bind("<Leave>", on_leave_error_button_1)

                error_image_image_2 = PhotoImage(
                    file=relative_to_assets("error_image_2.png"))
                error_image_2 = error_canvas.create_image(
                    225.0,
                    163.0,
                    image=error_image_image_2
                )
                error_canvas.image2 = error_image_image_2

                error_window.resizable(False, False)
            show_restore_error_message()
        print("Generating.")

    # Restores original dialogues
    def restore_original_dialogues():
        click_sound.play()
        dialogue_generator.read_txt_file()
        try:
            dialogue_generator.check_if_unrenpyc_file_exist()
            try:
                dialogue_generator.revert_original_rpy_files()
                show_success_revert_message()
            except:
                def show_folder_missing_error_message():
                    error_window = Toplevel(window)
                    error_window.title('Error Message')
                    error_window.geometry("450x200")
                    error_window.configure(bg = "#FFFFFF")
                    error_window.iconbitmap(str(ASSETS_PATH / "Icon.ico"))
    
                    def error_button_1_pressed():
                        click_sound.play()
                        error_window.destroy()
    
                    def on_enter_error_button_1(e):
                        hover_sound.play()
                        error_button_1.config(image = error_button_image_1_hover)
    
                    def on_leave_error_button_1(e):
                        error_button_1.config(image = error_button_image_1)
    
                    error_canvas = Canvas(
                    error_window,
                    bg = "#FFFFFF",
                    height = 200,
                    width = 450,
                    bd = 0,
                    highlightthickness = 0,
                    relief = "ridge"
                    )
    
                    error_canvas.place(x = 0, y = 0)
                    error_image_file_not_found_image_2 = PhotoImage(
                        file=relative_to_assets("error_image_file_not_found_2.png"))
                    error_image_file_not_found_2 = error_canvas.create_image(
                        225,
                        65,
                        image=error_image_file_not_found_image_2
                    )
                    error_canvas.image = error_image_file_not_found_image_2
    
                    error_button_image_1 = PhotoImage(
                        file=relative_to_assets("error_button_1.png"))
                    error_button_image_1_hover = PhotoImage(
                        file=relative_to_assets("error_button_1_hover.png"))
                    error_button_1 = Button(
                        error_window,
                        image=error_button_image_1,
                        borderwidth=0,
                        highlightthickness=0,
                        command=error_button_1_pressed,
                        relief="flat"
                    )
                    error_button_1.place(
                        x=260.0,
                        y=139,
                        width=160.0,
                        height=50.0
                    )
                    error_button_1.bind("<Enter>", on_enter_error_button_1)
                    error_button_1.bind("<Leave>", on_leave_error_button_1)
    
                    error_image_image_2 = PhotoImage(
                        file=relative_to_assets("error_image_2.png"))
                    error_image_2 = error_canvas.create_image(
                        225.0,
                        163.0,
                        image=error_image_image_2
                    )
                    error_canvas.image2 = error_image_image_2
    
                    error_window.resizable(False, False)
                show_folder_missing_error_message()
        except:
            def show_folder_missing_error_message():
                error_window = Toplevel(window)
                error_window.title('Error Message')
                error_window.geometry("450x200")
                error_window.configure(bg = "#FFFFFF")
                error_window.iconbitmap(str(ASSETS_PATH / "Icon.ico"))

                def error_button_1_pressed():
                    click_sound.play()
                    error_window.destroy()

                def on_enter_error_button_1(e):
                    hover_sound.play()
                    error_button_1.config(image = error_button_image_1_hover)

                def on_leave_error_button_1(e):
                    error_button_1.config(image = error_button_image_1)

                error_canvas = Canvas(
                error_window,
                bg = "#FFFFFF",
                height = 200,
                width = 450,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
                )

                error_canvas.place(x = 0, y = 0)
                error_image_file_not_found_image_3 = PhotoImage(
                    file=relative_to_assets("error_image_file_not_found_3.png"))
                error_image_file_not_found_3 = error_canvas.create_image(
                    225,
                    65,
                    image=error_image_file_not_found_image_3
                )
                error_canvas.image = error_image_file_not_found_image_3

                error_button_image_1 = PhotoImage(
                    file=relative_to_assets("error_button_1.png"))
                error_button_image_1_hover = PhotoImage(
                    file=relative_to_assets("error_button_1_hover.png"))
                error_button_1 = Button(
                    error_window,
                    image=error_button_image_1,
                    borderwidth=0,
                    highlightthickness=0,
                    command=error_button_1_pressed,
                    relief="flat"
                )
                error_button_1.place(
                    x=260.0,
                    y=139,
                    width=160.0,
                    height=50.0
                )
                error_button_1.bind("<Enter>", on_enter_error_button_1)
                error_button_1.bind("<Leave>", on_leave_error_button_1)

                error_image_image_2 = PhotoImage(
                    file=relative_to_assets("error_image_2.png"))
                error_image_2 = error_canvas.create_image(
                    225.0,
                    163.0,
                    image=error_image_image_2
                )
                error_canvas.image2 = error_image_image_2

                error_window.resizable(False, False)
            show_folder_missing_error_message()
        

        print("Restoring.")

    # Shows credits
    def show_credits():
        click_sound.play()
        credits_window = Toplevel(window)
        credits_window.title('Credits')
        credits_window.geometry("500x400")
        credits_window.configure(bg = "#FFC0CB")
        credits_window.iconbitmap(str(ASSETS_PATH / "Icon.ico"))

        credits_canvas = Canvas(
        credits_window,
        bg = "#FFC0CB",
        height = 400,
        width = 500,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )

        credits_canvas.place(x = 0, y = 0)
        credits_image_image_1 = PhotoImage(
            file=relative_to_assets("credits_image_1.png"))
        credits_image_1 = credits_canvas.create_image(
            250,
            200,
            image=credits_image_image_1
        )
        credits_canvas.image = credits_image_image_1

        def credits_button_1_pressed(e):
            click_sound.play()
            url = 'https://x.com/WhiteFruitNinja'
            webbrowser.open(url)

        def on_enter_credits_button_1(e):
            hover_sound.play()
            credits_canvas.itemconfig(credits_button_1,
                                      image=credits_button_image_1_hover)

        def on_leave_credits_button_1(e):
            credits_canvas.itemconfig(credits_button_1,
                                      image=credits_button_image_1)
            
        def credits_button_2_pressed(e):
            click_sound.play()
            url = 'https://x.com/hitsujigoods'
            webbrowser.open(url)

        def on_enter_credits_button_2(e):
            hover_sound.play()
            credits_canvas.itemconfig(credits_button_2,
                                      image=credits_button_image_2_hover)

        def on_leave_credits_button_2(e):
            credits_canvas.itemconfig(credits_button_2,
                                      image=credits_button_image_2)

        def credits_button_3_pressed(e):
            click_sound.play()
            url = 'https://github.com/CensoredUsername'
            webbrowser.open(url)

        def on_enter_credits_button_3(e):
            hover_sound.play()
            credits_canvas.itemconfig(credits_button_3,
                                      image=credits_button_image_3_hover)

        def on_leave_credits_button_3(e):
            credits_canvas.itemconfig(credits_button_3,
                                      image=credits_button_image_3)

        def credits_button_4_pressed(e):
            click_sound.play()
            url = 'https://github.com/CensoredUsername/unrpyc'
            webbrowser.open(url)

        def on_enter_credits_button_4(e):
            hover_sound.play()
            credits_canvas.itemconfig(credits_button_4,
                                      image=credits_button_image_4_hover)

        def on_leave_credits_button_4(e):
            credits_canvas.itemconfig(credits_button_4,
                                      image=credits_button_image_4)
        
        def credits_button_5_pressed(e):
            click_sound.play()
            url = 'https://github.com/first20hours'
            webbrowser.open(url)

        def on_enter_credits_button_5(e):
            hover_sound.play()
            credits_canvas.itemconfig(credits_button_5,
                                      image=credits_button_image_5_hover)

        def on_leave_credits_button_5(e):
            credits_canvas.itemconfig(credits_button_5,
                                      image=credits_button_image_5)
            
        def credits_button_6_pressed(e):
            click_sound.play()
            url = 'https://github.com/first20hours/google-10000-english'
            webbrowser.open(url)

        def on_enter_credits_button_6(e):
            hover_sound.play()
            credits_canvas.itemconfig(credits_button_6,
                                      image=credits_button_image_6_hover)

        def on_leave_credits_button_6(e):
            credits_canvas.itemconfig(credits_button_6,
                                      image=credits_button_image_6)
        
        def credits_button_7_pressed(e):
            click_sound.play()
            url = 'https://x.com/raidengaembing'
            webbrowser.open(url)

        def on_enter_credits_button_7(e):
            hover_sound.play()
            credits_canvas.itemconfig(credits_button_7,
                                      image=credits_button_image_7_hover)

        def on_leave_credits_button_7(e):
            credits_canvas.itemconfig(credits_button_7,
                                      image=credits_button_image_7)
            
        def credits_button_8_pressed(e):
            click_sound.play()
            url = 'https://github.com/raidengugga/Neet-Girl-Date-Night-PSVITA'
            webbrowser.open(url)

        def on_enter_credits_button_8(e):
            hover_sound.play()
            credits_canvas.itemconfig(credits_button_8,
                                      image=credits_button_image_8_hover)

        def on_leave_credits_button_8(e):
            credits_canvas.itemconfig(credits_button_8,
                                      image=credits_button_image_8)

        credits_button_image_1 = PhotoImage(
            file=relative_to_assets("credits_button_1.png"))
        credits_button_image_1_hover = PhotoImage(
            file=relative_to_assets("credits_button_1_hover.png"))
        credits_button_1 = credits_canvas.create_image(
            278.0,
            87.5,
            image=credits_button_image_1,
        )
        credits_canvas.image2 = credits_button_image_1

        credits_canvas.tag_bind(credits_button_1, "<Button-1>", credits_button_1_pressed)
        credits_canvas.tag_bind(credits_button_1, "<Enter>", on_enter_credits_button_1)
        credits_canvas.tag_bind(credits_button_1, "<Leave>", on_leave_credits_button_1)

        credits_button_image_2 = PhotoImage(
            file=relative_to_assets("credits_button_2.png"))
        credits_button_image_2_hover = PhotoImage(
            file=relative_to_assets("credits_button_2_hover.png"))
        credits_button_2 = credits_canvas.create_image(
            301.0,
            120.5,
            image=credits_button_image_2,
        )
        credits_canvas.image3 = credits_button_image_2

        credits_canvas.tag_bind(credits_button_2, "<Button-1>", credits_button_2_pressed)
        credits_canvas.tag_bind(credits_button_2, "<Enter>", on_enter_credits_button_2)
        credits_canvas.tag_bind(credits_button_2, "<Leave>", on_leave_credits_button_2)

        credits_button_image_3 = PhotoImage(
            file=relative_to_assets("credits_button_3.png"))
        credits_button_image_3_hover = PhotoImage(
            file=relative_to_assets("credits_button_3_hover.png"))
        credits_button_3 = credits_canvas.create_image(
            94.0,
            191.0,
            image=credits_button_image_3,
        )
        credits_canvas.image4 = credits_button_image_3

        credits_canvas.tag_bind(credits_button_3, "<Button-1>", credits_button_3_pressed)
        credits_canvas.tag_bind(credits_button_3, "<Enter>", on_enter_credits_button_3)
        credits_canvas.tag_bind(credits_button_3, "<Leave>", on_leave_credits_button_3)

        credits_button_image_4 = PhotoImage(
            file=relative_to_assets("credits_button_4.png"))
        credits_button_image_4_hover = PhotoImage(
            file=relative_to_assets("credits_button_4_hover.png"))
        credits_button_4 = credits_canvas.create_image(
            208.0,
            194.0,
            image=credits_button_image_4,
        )
        credits_canvas.image5 = credits_button_image_4

        credits_canvas.tag_bind(credits_button_4, "<Button-1>", credits_button_4_pressed)
        credits_canvas.tag_bind(credits_button_4, "<Enter>", on_enter_credits_button_4)
        credits_canvas.tag_bind(credits_button_4, "<Leave>", on_leave_credits_button_4)

        credits_button_image_5 = PhotoImage(
            file=relative_to_assets("credits_button_5.png"))
        credits_button_image_5_hover = PhotoImage(
            file=relative_to_assets("credits_button_5_hover.png"))
        credits_button_5 = credits_canvas.create_image(
            71.0,
            231.0,
            image=credits_button_image_5,
        )
        credits_canvas.image6 = credits_button_image_5

        credits_canvas.tag_bind(credits_button_5, "<Button-1>", credits_button_5_pressed)
        credits_canvas.tag_bind(credits_button_5, "<Enter>", on_enter_credits_button_5)
        credits_canvas.tag_bind(credits_button_5, "<Leave>", on_leave_credits_button_5)

        credits_button_image_6 = PhotoImage(
            file=relative_to_assets("credits_button_6.png"))
        credits_button_image_6_hover = PhotoImage(
            file=relative_to_assets("credits_button_6_hover.png"))
        credits_button_6 = credits_canvas.create_image(
            215.0,
            232.0,
            image=credits_button_image_6,
        )
        credits_canvas.image7 = credits_button_image_6

        credits_canvas.tag_bind(credits_button_6, "<Button-1>", credits_button_6_pressed)
        credits_canvas.tag_bind(credits_button_6, "<Enter>", on_enter_credits_button_6)
        credits_canvas.tag_bind(credits_button_6, "<Leave>", on_leave_credits_button_6)

        credits_button_image_7 = PhotoImage(
            file=relative_to_assets("credits_button_7.png"))
        credits_button_image_7_hover = PhotoImage(
            file=relative_to_assets("credits_button_7_hover.png"))
        credits_button_7 = credits_canvas.create_image(
            130.0,
            272.0,
            image=credits_button_image_7,
        )
        credits_canvas.image8 = credits_button_image_7

        credits_canvas.tag_bind(credits_button_7, "<Button-1>", credits_button_7_pressed)
        credits_canvas.tag_bind(credits_button_7, "<Enter>", on_enter_credits_button_7)
        credits_canvas.tag_bind(credits_button_7, "<Leave>", on_leave_credits_button_7)

        credits_button_image_8 = PhotoImage(
            file=relative_to_assets("credits_button_8.png"))
        credits_button_image_8_hover = PhotoImage(
            file=relative_to_assets("credits_button_8_hover.png"))
        credits_button_8 = credits_canvas.create_image(
            143.5,
            287.0,
            image=credits_button_image_8,
        )
        credits_canvas.image9 = credits_button_image_8

        credits_canvas.tag_bind(credits_button_8, "<Button-1>", credits_button_8_pressed)
        credits_canvas.tag_bind(credits_button_8, "<Enter>", on_enter_credits_button_8)
        credits_canvas.tag_bind(credits_button_8, "<Leave>", on_leave_credits_button_8)

        credits_window.resizable(False, False)
        print("Showing credits.")

    def on_enter_button_1(e):
        hover_sound.play()
        button_1.config(image = button_image_1_hover)

    def on_leave_button_1(e):
        button_1.config(image = button_image_1)

    def on_enter_button_2(e):
        hover_sound.play()
        button_2.config(image = button_image_2_hover)

    def on_leave_button_2(e):
        button_2.config(image = button_image_2)

    def on_enter_button_3(e):
        hover_sound.play()
        button_3.config(image = button_image_3_hover)

    def on_leave_button_3(e):
        button_3.config(image = button_image_3)

    def on_enter_button_4(e):
        hover_sound.play()
        button_4.config(image = button_image_4_hover)

    def on_leave_button_4(e):
        button_4.config(image = button_image_4)

    def on_enter_button_5(e):
        hover_sound.play()
        button_5.config(image = button_image_5_hover)

    def on_leave_button_5(e):
        button_5.config(image = button_image_5)

    def on_enter_button_6(e):
        hover_sound.play()
        button_6.config(image = button_image_6_hover)

    def on_leave_button_6(e):
        button_6.config(image = button_image_6)

    def on_enter_button_7(e):
        hover_sound.play()
        button_1.config(image = button_image_7_hover)

    def on_leave_button_7(e):
        button_1.config(image = button_image_7)

    def show_success_generation_message():
        success_window = Toplevel(window)
        success_window.title('Success Message')
        success_window.geometry("450x200")
        success_window.configure(bg = "#FFFFFF")
        success_window.iconbitmap(str(ASSETS_PATH / "Icon.ico"))

        def success_button_1_pressed():
            click_sound.play()
            success_window.destroy()

        def on_enter_success_button_1(e):
            hover_sound.play()
            success_button_1.config(image = success_button_image_1_hover)

        def on_leave_success_button_1(e):
            success_button_1.config(image = success_button_image_1)

        success_canvas = Canvas(
        success_window,
        bg = "#FFFFFF",
        height = 200,
        width = 450,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )

        success_canvas.place(x = 0, y = 0)
        success_image_image_1 = PhotoImage(
            file=relative_to_assets("success_image_1.png"))
        success_image_1 = success_canvas.create_image(
            225,
            65,
            image=success_image_image_1
        )
        success_canvas.image = success_image_image_1

        success_button_image_1 = PhotoImage(
            file=relative_to_assets("error_button_1.png"))
        success_button_image_1_hover = PhotoImage(
            file=relative_to_assets("error_button_1_hover.png"))
        success_button_1 = Button(
            success_window,
            image=success_button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=success_button_1_pressed,
            relief="flat"
        )
        success_button_1.place(
            x=260.0,
            y=139,
            width=160.0,
            height=50.0
        )
        success_button_1.bind("<Enter>", on_enter_success_button_1)
        success_button_1.bind("<Leave>", on_leave_success_button_1)

        success_image_image_2 = PhotoImage(
            file=relative_to_assets("error_image_2.png"))
        success_image_2 = success_canvas.create_image(
            225.0,
            163.0,
            image=success_image_image_2
        )
        success_canvas.image2 = success_image_image_2

        success_window.resizable(False, False)

    def show_success_revert_message():
        success_window = Toplevel(window)
        success_window.title('Success Message')
        success_window.geometry("450x200")
        success_window.configure(bg = "#FFFFFF")
        success_window.iconbitmap(str(ASSETS_PATH / "Icon.ico"))

        def success_button_1_pressed():
            click_sound.play()
            success_window.destroy()

        def on_enter_success_button_1(e):
            hover_sound.play()
            success_button_1.config(image = success_button_image_1_hover)

        def on_leave_success_button_1(e):
            success_button_1.config(image = success_button_image_1)

        success_canvas = Canvas(
        success_window,
        bg = "#FFFFFF",
        height = 200,
        width = 450,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )

        success_canvas.place(x = 0, y = 0)
        success_image_image_1 = PhotoImage(
            file=relative_to_assets("success_image_2.png"))
        success_image_2 = success_canvas.create_image(
            225,
            65,
            image=success_image_image_1
        )
        success_canvas.image = success_image_image_1

        success_button_image_1 = PhotoImage(
            file=relative_to_assets("error_button_1.png"))
        success_button_image_1_hover = PhotoImage(
            file=relative_to_assets("error_button_1_hover.png"))
        success_button_1 = Button(
            success_window,
            image=success_button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=success_button_1_pressed,
            relief="flat"
        )
        success_button_1.place(
            x=260.0,
            y=139,
            width=160.0,
            height=50.0
        )
        success_button_1.bind("<Enter>", on_enter_success_button_1)
        success_button_1.bind("<Leave>", on_leave_success_button_1)

        success_image_image_2 = PhotoImage(
            file=relative_to_assets("error_image_2.png"))
        success_image_2 = success_canvas.create_image(
            225.0,
            163.0,
            image=success_image_image_2
        )
        success_canvas.image2 = success_image_image_2

        success_window.resizable(False, False)

    canvas = Canvas(
        window,
        bg = "#FFC0CB",
        height = 600,
        width = 600,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        300.0,
        380.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_image_1_hover = PhotoImage(
        file=relative_to_assets("button_1_hover.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=button_1_pressed,
        relief="flat"
    )
    button_1.place(
        x=430.0,
        y=171.0,
        width=160.0,
        height=50.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_image_7_hover = PhotoImage(
        file=relative_to_assets("button_7_hover.png"))

    button_1.bind("<Enter>", on_enter_button_1)
    button_1.bind("<Leave>", on_leave_button_1)

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_image_2_hover = PhotoImage(
        file=relative_to_assets("button_2_hover.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=show_credits,
        relief="flat"
    )
    button_2.place(
        x=12.0,
        y=541.0,
        width=160.0,
        height=50.0
    )

    button_2.bind("<Enter>", on_enter_button_2)
    button_2.bind("<Leave>", on_leave_button_2)

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_image_3_hover = PhotoImage(
        file=relative_to_assets("button_3_hover.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=button_3_pressed,
        relief="flat"
    )
    button_3.place(
        x=186.0,
        y=477.0,
        width=160.0,
        height=50.0
    )

    button_3.bind("<Enter>", on_enter_button_3)
    button_3.bind("<Leave>", on_leave_button_3)

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_image_4_hover = PhotoImage(
        file=relative_to_assets("button_4_hover.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=generate_random_dialogues,
        relief="flat"
    )
    button_4.place(
        x=12.0,
        y=477.0,
        width=160.0,
        height=50.0
    )

    button_4.bind("<Enter>", on_enter_button_4)
    button_4.bind("<Leave>", on_leave_button_4)

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_image_5_hover = PhotoImage(
        file=relative_to_assets("button_5_hover.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=restore_original_dialogues,
        relief="flat"
    )
    button_5.place(
        x=12.0,
        y=413.0,
        width=160.0,
        height=50.0
    )

    button_5.bind("<Enter>", on_enter_button_5)
    button_5.bind("<Leave>", on_leave_button_5)

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_image_6_hover = PhotoImage(
        file=relative_to_assets("button_6_hover.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=button_6_pressed,
        relief="flat"
    )
    button_6.place(
        x=186.0,
        y=541.0,
        width=160.0,
        height=50.0
    )

    button_6.bind("<Enter>", on_enter_button_6)
    button_6.bind("<Leave>", on_leave_button_6)


    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        473.0,
        410.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        300.0,
        71.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        302.0,
        150.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        30.0,
        150.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))

    window.resizable(False, False)
    window.mainloop()
