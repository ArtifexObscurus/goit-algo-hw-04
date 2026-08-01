from pathlib import Path
import sys

from colorama import init, Fore, Style

# Initialize Colorama for cross-platform colored output.
init(autoreset=True)

def print_directory_tree(dir_path: Path, indent: str = "") -> None:
    """
    Recursively walks through and visualizes the directory structure.

    Directories are displayed in bright blue, while files are displayed in green.

    Args:
        dir_path: Path to the directory to display.
        indent: String prefix used for proper hierarchy indentation. 
    """
    try:
        # Get a sorted list of all items inside the directory.
        # Group directories first, than files, for a cleaner structure.
        items = sorted(dir_path.iterdir(),key=lambda path: (path.is_file(), path.name.lower()))
    except PermissionError:
        # Handle cases where the user lacks read permissions for the folder.
        print(f"{indent}{Fore.RED}[Access denied]")
        return 

    items_count = len(items)
    for index, item in enumerate(items):
        # Determine if the item is last one in the current directory listing.
        is_last = (index == items_count - 1)

        # Select the drawing character based on position.
        connector = "┗" if is_last else "┣"
        next_indent = indent + ("   " if is_last else "┃   ")

        if item.is_dir():
            # Apply bright blue color for directories
            print(f"{indent}{connector}{Fore.BLUE}{Style.BRIGHT}📂 {item.name}/{Style.RESET_ALL}")
            print_directory_tree(item, next_indent)
        else:
            # Apply green color for files
            print(f"{indent}{connector}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}") 

def main() -> None:
    """
    Main function to validate arguments and start the visualization.
    """
    # Verified that a directory path argument was provided
    if len(sys.argv) != 2:
        print(f"{Fore.YELLOW}Usage: python unit_4_task_3.py <directory_path>")
        sys.exit(1)

    # Extract the target path from command line arguments
    target_path = Path(sys.argv[1])

    # Validation: Check if the provided path actually exists
    if not target_path.exists():
        print(f"{Fore.RED}Error: The path '{target_path}' does not exist.")
        sys.exit(1)

    # Validation: Check if the provided path points to a directory
    if not target_path.is_dir():
        print(f"{Fore.RED}Error: The pass '{target_path}' is not a directory.")
        sys.exit(1)

    # Print the absolute root path and start traversing the tree
    print(f"{Fore.BLUE}{Style.BRIGHT}📦 {target_path.name}/{Style.RESET_ALL}")
    print_directory_tree(target_path)

if __name__ == "__main__":
    main()
