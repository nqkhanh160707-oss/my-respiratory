def count_non_blank_lines(filename: str) -> int:
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