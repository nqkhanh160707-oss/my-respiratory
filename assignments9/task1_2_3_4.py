def count_non_blank_lines(filename: str) -> int:
    """
    Opens a text file and returns the number of non-blank lines.
    Blank lines (only whitespace) are ignored.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            count = 0
            for line in f:
                if line.strip():  # Removes leading/trailing whitespace and checks if anything remains
                    count += 1
            return count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0