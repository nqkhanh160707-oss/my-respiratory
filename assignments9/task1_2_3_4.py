from fileinput import filename


def count_non_blank_lines(filename: str) -> int:
    """
    Opens a text file and returns the number of non-blank lines.
    Blank lines (only whitespace) are ignored.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            count = 0
            for line in f:
                if line.strip():  
                    count += 1
            return count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0


def find_keyword_lines(filename: str, keyword: str, case_sensitive: bool = True) -> list[int]:
    """
    Returns a list of 1-based line numbers where the keyword appears.
    """
    results = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                search_line = line if case_sensitive else line.lower()
                search_keyword = keyword if case_sensitive else keyword.lower()
                if search_keyword in search_line:
                    results.append(line_num)
        return results
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []


def calculate_average_score(filename: str) -> float:
    """
    Reads a file where each line is "Name,Score" and returns the average score.
    Ignores invalid lines gracefully.
    """
    total = 0.0
    count = 0
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue  # skip 
                
                parts = line.split(',', 1)  # split on comma
                if len(parts) != 2:
                    print(f"Warning: Skipping invalid line {line_num}: {line}")
                    continue
                
                try:
                    score = float(parts[1].strip())
                    total += score
                    count += 1
                except ValueError:
                    print(f"Warning: Invalid score on line {line_num}: {line}")
        
        if count == 0:
            print("No valid scores found.")
            return 0.0
        return total / count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0.0
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 0.0