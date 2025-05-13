import pytest
from file_reader import read_employee_data


def create_test_file(file_path, data):
    """Creates a test CSV file with the given data."""
    with open(file_path, 'w') as f:
        f.write(data)


def test_read_employee_data_success(tmp_path):
    file_path = tmp_path / "employees.csv"
    test_data = "name,department,hours_worked,rate\nAlice,Engineering,40,30"
    create_test_file(file_path, test_data)

    result = read_employee_data(str(file_path))
    assert result == [
        {'name': 'Alice', 'department': 'Engineering', 'hours': 40.0, 'rate': 30.0}
    ]


def test_header_normalization(tmp_path):
    file_path = tmp_path / "employees.csv"
    test_data = "name,department,hours_worked,salary\nBob,Sales,35,25"
    create_test_file(file_path, test_data)

    result = read_employee_data(str(file_path))
    assert 'rate' in result[0]


def test_invalid_file_path():
    with pytest.raises(FileNotFoundError):
        read_employee_data("nonexistent.csv")



