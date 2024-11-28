import pyfiglet

# ANSI color codes
COLOR_CODES = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "purple": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "gray": "\033[90m",
    "reset": "\033[0m"  # Resets color back to default
}

def get_user_input():
    text = input("Enter a word or phrase to convert into ASCII art: ")
    characters = input("Enter a set of characters for ASCII art background (e.g., @#*): ")
    width = int(input("Enter the width of ASCII art (e.g., 40): "))
    height = int(input("Enter the height of ASCII art (e.g., 10): "))
    alignment = input("Enter alignment (left, center, right): ").lower()
    color_option = input("Choose color option (black and white, grayscale, or a color: red, green, yellow, blue, purple, cyan, white, gray): ").lower()
    font = input("Choose a font for your ASCII art (e.g., 'slant', 'block', 'standard'): ").lower()
    return text, characters, width, height, alignment, color_option, font

def validate_dimensions(width, height, max_width=100, max_height=40):
    if width > max_width or height > max_height:
        print(f"Dimensions exceed the limit {max_width}x{max_height}. Please use smaller sizes.")
        return False
    return True

def generate_ascii_art(text, font):
    # Generate ASCII art text using pyfiglet with the selected font
    figlet = pyfiglet.Figlet(font=font)
    ascii_art = figlet.renderText(text)
    return ascii_art

def display_ascii_art(ascii_art):
    print("\nYour ASCII Art:\n")
    print(ascii_art)

def save_to_file(ascii_art, filename="ascii_art.txt"):
    with open(filename, "w") as file:
        file.write(ascii_art)
    print(f"ASCII art has been saved to {filename}.")

def apply_color(ascii_art, color_option):
    # Apply color if it's a valid color option
    color_code = COLOR_CODES.get(color_option, COLOR_CODES["reset"])
    colored_ascii_art = f"{color_code}{ascii_art}{COLOR_CODES['reset']}"
    return colored_ascii_art

def preview_ascii_art(ascii_art):
    print("Preview of ASCII Art:\n")
    print(ascii_art)
    confirm = input("Do you want to save this? (yes/no): ")
    return confirm.lower() == 'yes'

def main():
    text, characters, width, height, alignment, color_option, font = get_user_input()
    
    if not validate_dimensions(width, height):
        return
    
    ascii_art = generate_ascii_art(text, font)
    ascii_art = apply_color(ascii_art, color_option)
    
    if preview_ascii_art(ascii_art):
        save_to_file(ascii_art)
    else:
        print("Save canceled.")
    display_ascii_art(ascii_art)

if __name__ == "__main__":
    main()
