import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import csvUtils
import jsonUtils


def story_plots_data_preparation():
    input_file = filedialog.askopenfilename(title="Select the input CSV file")
    if not input_file:
        return

    num_json_objects = tk.simpledialog.askinteger("Number of JSON data objects",
                                                  "Enter the number of JSON data objects to generate (default: all CSV data):",
                                                  minvalue=1)
    if not num_json_objects:
        return

    jsonUtils.prepare_story_plots(input_file, num_json_objects)
    messagebox.showinfo("Success", "story_plots.json has been generated successfully.")


def remove_season_episode_indicators():
    input_file = filedialog.askopenfilename(title="Select the input CSV file")
    if not input_file:
        return

    output_file = filedialog.asksaveasfilename(title="Select the output CSV file")
    if not output_file:
        return

    csvUtils.remove_season_episode_indicators(input_file, output_file)
    messagebox.showinfo("Success", "Season and episode indicators have been removed successfully.")


def remove_custom_character():
    input_file = filedialog.askopenfilename(title="Select the input CSV file")
    if not input_file:
        return

    output_file = filedialog.asksaveasfilename(title="Select the output CSV file")
    if not output_file:
        return

    custom_char = tk.simpledialog.askstring("Remove custom character", "Enter the custom character to remove:")
    if not custom_char:
        return

    csvUtils.remove_custom_character(input_file, output_file, custom_char)
    messagebox.showinfo("Success", f"Custom character '{custom_char}' has been removed successfully.")


def remove_nbsp():
    input_file = filedialog.askopenfilename(title="Select the input CSV file")
    if not input_file:
        return

    output_file = filedialog.asksaveasfilename(title="Select the output CSV file")
    if not output_file:
        return

    csvUtils.remove_nbsp(input_file, output_file)
    messagebox.showinfo("Success", "Non-breaking spaces have been removed successfully.")


def split_long_plots():
    # Define the dialog to get the input CSV file
    input_file = filedialog.askopenfilename(title="Select the input CSV file")
    if not input_file:
        return

    # Define the dialog to get the output CSV file
    output_file = filedialog.asksaveasfilename(title="Select the output CSV file")
    if not output_file:
        return

    # Ask for the maximum tokens per plot chunk
    max_tokens = tk.simpledialog.askinteger("Maximum tokens",
                                            "Enter the maximum tokens per plot chunk (default: 1000):", minvalue=1)
    if not max_tokens:
        return

    csvUtils.split_long_plots(input_file, output_file, max_tokens)
    messagebox.showinfo("Success", "Plots have been split successfully.")


class ScoobyDooCSVToolGUI(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("ScoobyDoo CSV Tool")
        self.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        # Create main frame
        main_frame = ttk.Frame(self)
        main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Add the welcome label
        welcome_label = ttk.Label(main_frame, text="Welcome to ScoobyDoo CSV Tool!", font=("Helvetica", 16, "bold"))
        welcome_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Add the options label
        options_label = ttk.Label(main_frame, text="Choose an option:", font=("Helvetica", 14))
        options_label.grid(row=1, column=0, pady=10)

        # Add the Split long plots button
        split_long_plots_button = ttk.Button(main_frame, text="1. Split long plots", command=split_long_plots)
        split_long_plots_button.grid(row=2, column=0, pady=5)

        # Add the Remove specific characters button
        remove_specific_characters_button = ttk.Button(main_frame, text="2. Remove specific characters",
                                                       command=self.remove_specific_characters)
        remove_specific_characters_button.grid(row=3, column=0, pady=5)

        # Add the Story plots data preparation to a JSON button
        story_plots_data_preparation_button = ttk.Button(main_frame, text="3. Story plots data preparation to a JSON",
                                                         command=story_plots_data_preparation)
        story_plots_data_preparation_button.grid(row=4, column=0, pady=5)

        # Add the Exit button
        exit_button = ttk.Button(main_frame, text="4. Exit", command=self.confirm_exit)
        exit_button.grid(row=5, column=0, pady=5)

    def remove_specific_characters(self):
        # Create a new Top-level window
        remove_characters_window = tk.Toplevel(self)
        remove_characters_window.title("Remove specific characters")

        remove_characters_frame = ttk.Frame(remove_characters_window)
        remove_characters_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Add the options label
        options_label = ttk.Label(remove_characters_frame, text="Choose an option:", font=("Helvetica", 14))
        options_label.grid(row=0, column=0, pady=10)

        # Add the Remove non-breaking spaces (NBSP) button
        remove_nbsp_button = ttk.Button(remove_characters_frame, text="1. Remove non-breaking spaces (NBSP)",
                                        command=remove_nbsp)
        remove_nbsp_button.grid(row=1, column=0, pady=5)

        # Add the Remove custom character button
        remove_custom_character_button = ttk.Button(remove_characters_frame, text="2. Remove custom character",
                                                    command=remove_custom_character)
        remove_custom_character_button.grid(row=2, column=0, pady=5)

        # Add the Remove season and episode indicators button
        remove_season_episode_indicators_button = ttk.Button(remove_characters_frame,
                                                             text="3. Remove season and episode indicators",
                                                             command=remove_season_episode_indicators)
        remove_season_episode_indicators_button.grid(row=3, column=0, pady=5)

    def confirm_exit(self):
        answer = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if answer:
            self.quit()


if __name__ == "__main__":
    app = ScoobyDooCSVToolGUI()
    app.mainloop()
