import os
from typing import List, Dict

def read_employee_data(file_path: str) -> List[Dict[str, object]]:
    """
    Reads a CSV file and returns a list of normalized employee dictionaries.
    Normalizes column names and converts numeric fields to appropriate types.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' does not exist.")

    employees: List[Dict[str, object]] = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        lines = file.readlines()

        if not lines:
            return []

        header = lines[0].strip().split(',')

        # Normalize possible variations of the salary column to 'rate'
        normalized_header = [
            'rate' if col in ['hourly_rate', 'rate', 'salary'] else col
            for col in header
        ]

        for line in lines[1:]:
            values = line.strip().split(',')
            if len(values) == len(normalized_header):
                employee = dict(zip(normalized_header, values))

                try:
                    # Normalize and convert types
                    employee_normalized: Dict[str, object] = {
                        'name': employee.get('name', ''),
                        'department': employee.get('department', ''),
                        'hours': int(employee.get('hours_worked')),
                        'rate': int(employee.get('rate')),
                    }
                    employees.append(employee_normalized)

                except ValueError as e:
                    print(f"Warning: could not convert data types: {e}")
            else:
                print(f"Warning: the row has an incorrect number of columns: {line}")

    return employees