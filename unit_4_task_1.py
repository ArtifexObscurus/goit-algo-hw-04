from pathlib import Path

def total_salary(path: str | Path) -> tuple[int, float]:
    """
    Calculate the total and average salary of all employees from a text file.

    The input file must contain one employee per line in the following format:
        name,salary

    Args:
        path: Path to the text file containing employees' salaries.

    Returns:
        A tuple containing:
            - total salary (imt)
            - average salary (float)

        Returns (0, 0) if the file cannot be processed. 
    """
    path = Path(path)

    total_salary = 0
    employees_count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                _, salary = line.strip().split(",")

                total_salary += int(salary)
                employees_count += 1

        average_salary = (total_salary / employees_count if employees_count else 0)

        return total_salary, average_salary

    except FileNotFoundError:
        print(f"Error: File '{path}' was not found.")
        return 0, 0

    except (ValueError, IndexError):
        print("Error: Invalid file format.")
        return 0, 0

