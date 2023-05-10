import csvUtils as csvUtils
import jsonUtils as jsonUtils
import textUtils as textUtils
import roman


# Add ASCII text logo and main menu
def display_logo():
    logo = r"""
  ______                                 __                 
 /      \                               |  \                
|  $$$$$$\  _______   ______    ______  | $$____   __    __ 
| $$___\$$ /       \ /      \  /      \ | $$    \ |  \  |  \
 \$$    \ |  $$$$$$$|  $$$$$$\|  $$$$$$\| $$$$$$$\| $$  | $$
 _\$$$$$$\| $$      | $$  | $$| $$  | $$| $$  | $$| $$  | $$
|  \__| $$| $$_____ | $$__/ $$| $$__/ $$| $$__/ $$| $$__/ $$
 \$$    $$ \$$     \ \$$    $$ \$$    $$| $$    $$ \$$    $$
  \$$$$$$   \$$$$$$$  \$$$$$$   \$$$$$$  \$$$$$$$  _\$$$$$$$
                                                  |  \__| $$
                                                   \$$    $$
                                                    \$$$$$$ 
    """
    print(logo)


def display_main_menu():
    display_logo()
    print("ScoobyDooCSVTool Main Menu:")
    print("1. Split long plots")
    print("2. Remove specific characters")
    print("3. Story plots data preparation to a JSON")
    print("4. Generate a text file")
    print("5. Exit")


def display_character_removal_menu():
    print("Remove specific characters:")
    print("1. Remove non-breaking spaces (NBSP)")
    print("2. Remove custom character")
    print("3. Remove season and episode indicators")


def main():
    while True:
        display_main_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            # Split long plots
            input_file = input("Enter the input CSV file path: ")
            output_file = input("Enter the output CSV file path: ")
            max_tokens = int(input("Enter the maximum tokens per plot chunk (default: 1000): "))
            csvUtils.split_long_plots(input_file, output_file, max_tokens)
            print("Plots have been split successfully.\n")

        elif choice == "2":
            # Remove specific characters
            display_character_removal_menu()
            subchoice = input("Enter your choice (1-3): ")

            input_file = input("Enter the input CSV file path: ")
            output_file = input("Enter the output CSV file path: ")

            if subchoice == "1":
                # Remove non-breaking spaces (NBSP)
                csvUtils.remove_nbsp(input_file, output_file)
                print("Non-breaking spaces have been removed successfully.\n")

            elif subchoice == "2":
                # Remove custom character
                custom_char = input("Enter the custom character to remove: ")
                csvUtils.remove_custom_character(input_file, output_file, custom_char)
                print(f"Custom character '{custom_char}' has been removed successfully.\n")

            elif subchoice == "3":
                # Remove season and episode indicators
                csvUtils.remove_season_episode_indicators(input_file, output_file)
                print("Season and episode indicators have been removed successfully.\n")

            else:
                print("Invalid choice. Please try again.\n")

        elif choice == "3":
            # Story plots data preparation to a JSON
            input_file = input("Enter the input CSV file path: ")
            num_json_objects = int(input("Enter the number of JSON data objects to generate (default: all CSV data): "))
            jsonUtils.prepare_story_plots(input_file, num_json_objects)
            print("story_plots.json has been generated successfully.\n")

        elif choice == "4":
            # Generate a text file
            input_file = input("Enter the input CSV file path: ")
            num_story_inputs = int(input("Enter the number of story inputs to include (default: all CSV data): "))
            textUtils.generate_text_file(input_file, num_story_inputs)
            print("story_plots.txt has been generated successfully.\n")

        elif choice == "5":
            # Exit
            print("Exiting ScoobyDooCSVTool.")
            break

        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
