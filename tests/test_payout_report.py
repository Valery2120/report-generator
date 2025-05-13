from reports.payout_report import PayoutReport

def test_payout_report_generation():
    employees = [
        {'name': 'Alice', 'department': 'IT', 'hours': 40, 'rate': 30},
        {'name': 'Bob', 'department': 'IT', 'hours': 38, 'rate': 28},
    ]
    report = PayoutReport()
    grouped = report.generate(employees)

    assert 'payout' in grouped['IT'][0]
    assert grouped['IT'][0]['payout'] == 1200.0  # 40 * 30
    assert grouped['IT'][1]['payout'] == 1064.0  # 38 * 28

def test_format_row_includes_dollar_sign():
    employee = {'name': 'John', 'department': 'Sales', 'hours': 40, 'rate': 20, 'payout': 800.0}
    report = PayoutReport()
    row = report.format_row(employee)
    assert "$800" in row

def test_department_summary():
    employees = [
        {'name': 'Alice', 'department': 'IT', 'hours': 40, 'rate': 30, 'payout': 1200.0},
        {'name': 'Bob', 'department': 'IT', 'hours': 38, 'rate': 28, 'payout': 1064.0},
    ]
    report = PayoutReport()
    summary = report.department_summary("IT", employees)
    assert "$2264" in summary
    assert "78" in summary  # 40 + 38