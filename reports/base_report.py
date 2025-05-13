from typing import List, Dict, Any

class BaseReport:
    """Base class for generating a standard report."""

    def generate(self, employees: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        """
        Groups employees by department.
        """
        report: Dict[str, List[Dict[str, Any]]] = {}
        for row in employees:
            department = row['department']
            if department not in report:
                report[department] = []
            report[department].append(row)
        return report

    def get_column_width(self, value: Any) -> int:
        """
        Returns the appropriate width for a column based on the data type.
        """
        return 9 if isinstance(value, (int, float)) else 20

    def generate_report_text(self, report: Dict[str, List[Dict[str, Any]]]) -> str:
        """
        Generates and formats the full report as a string.
        """
        output: List[str] = []

        # Get sample data to determine column headers and widths
        first_dept = list(report.values())[0] if report else []
        headers = [key for key in first_dept[0].keys() if key != 'department'] if first_dept else []
        sample_employee = first_dept[0] if first_dept else {}
        column_widths = [self.get_column_width(sample_employee.get(header, '')) for header in headers]

        # Build header line
        header_format = f"{' ' * 16}" + "".join([f"{{:<{w}}}" for w in column_widths])
        output.append(header_format.format(*headers))

        # Build rows for each department
        for dept, employees in report.items():
            output.append(f"{dept}")
            for emp in employees:
                row = self.format_row(emp)
                output.append(row)

            # Add department summary if defined in subclass
            department_summary = self.department_summary(dept, employees)
            if department_summary:
                output.append(department_summary)

        return "\n".join(output)

    def format_row(self, emp: Dict[str, Any]) -> str:
        """
        Default row formatting. Can be overridden by subclasses.
        """
        columns = [key for key in emp.keys() if key != 'department']
        column_widths = [self.get_column_width(emp[col]) for col in columns]
        row_format = "".join([f"{{:<{w}}}" for w in column_widths])
        formatted_values = [str(emp[col]) for col in columns]

        return f"{'-' * 15} " + row_format.format(*formatted_values)

    def department_summary(self, department: str, employees: List[Dict[str, Any]]) -> str:
        """
        Optional summary per department. Can be overridden.
        """
        return ""

    def print_report(self, report: Dict[str, List[Dict[str, Any]]]) -> None:
        """
        Prints the formatted report to stdout.
        """
        formatted_report = self.generate_report_text(report)
        print(formatted_report)

