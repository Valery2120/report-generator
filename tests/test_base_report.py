from reports.base_report import BaseReport

def test_generate_groups_by_department():
    employees = [
        {"name": "John", "department": "Engineering", "hours": 40, "rate": 20},
        {"name": "Jane", "department": "HR", "hours": 30, "rate": 25},
    ]
    report = BaseReport()
    result = report.generate(employees)
    assert "Engineering" in result
    assert "HR" in result
    assert len(result["Engineering"]) == 1

def test_generate_report_text_structure():
    employees = [
        {"name": "John", "department": "Engineering", "hours": 40, "rate": 20},
    ]
    report = BaseReport()
    grouped = report.generate(employees)
    text = report.generate_report_text(grouped)
    assert "Engineering" in text
    assert "John" in text
    assert "$" not in text  # базовый отчёт не добавляет payout

def test_get_column_width():
    report = BaseReport()
    assert report.get_column_width(123) == 9
    assert report.get_column_width("text") == 20