def read_file(file_path: str) -> list:
    with open(file_path, 'r') as file:
        return file.readlines()

def sum_calibrations(file_path: str) -> int:
    lines = read_file(file_path)
    total_sum = 0
    for line in lines:
        digits = [i for i, char in enumerate(line) if char.isdigit()]
        combined_value = int(line[digits[0]]) * 10 + int(line[digits[-1]])
        total_sum += combined_value
    return total_sum

def main():
        total_sum = sum_calibrations("input.txt")
        print("Sum of all calibration values is:", total_sum)

if __name__ == "__main__":
    main()
