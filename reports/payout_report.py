from typing import List, Dict, Any
from reports.base_report import BaseReport

class PayoutReport(BaseReport):
    def generate(self, employees: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        """
        Overrides the generate method to calculate 'payout' for each employee.
        """
        report = super().generate(employees)
        for department, employees in report.items():
            for emp in employees:
                emp['payout'] = emp['hours'] * emp['rate']
        return report

    def format_row(self, emp: Dict[str, Any]) -> str:
        """
        Custom row formatting to include '$' for payout field.
        """
        columns = [key for key in emp.keys() if key != 'department']
        column_widths = [self.get_column_width(emp[col]) for col in columns]
        row_format = "".join([f"{{:<{w}}}" for w in column_widths])

        formatted_values = []
        for col in columns:
            value = emp[col]
            if col == 'payout':
                formatted_values.append(f"${value:<9.0f}")
            else:
                formatted_values.append(str(value))

        return f"{'-' * 15} " + row_format.format(*formatted_values)

    def department_summary(self, department: str, employees: List[Dict[str, Any]]) -> str:
        """
        Provides department-level summary: total hours and total payout.
        """
        total_hours = sum(emp['hours'] for emp in employees)
        total_payout = sum(emp['payout'] for emp in employees)
        return f"{' ' * 35} {total_hours:<9.0f}{' ':<9}${total_payout:<9.0f}"