import argparse
import sys
from typing import List, Dict, Type

from file_reader import read_employee_data
from reports.base_report import BaseReport
from reports.payout_report import PayoutReport

# Available report types mapped to their corresponding classes
REPORTS: Dict[str, Type[BaseReport]] = {
    'payout': PayoutReport
}

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate salary reports from CSV files."
    )
    parser.add_argument(
        "files", metavar="FILE", nargs="+", help="CSV file(s) with employee data"
    )
    parser.add_argument(
        "--report", choices=REPORTS.keys(), required=True, help="Type of report to generate"
    )
    args = parser.parse_args()

    try:
        employees: List[Dict[str, object]] = []

        # Read and accumulate employee data from all provided files
        for file in args.files:
            employees.extend(read_employee_data(file))

        report_cls = REPORTS.get(args.report)
        if not report_cls:
            print(f"Report type '{args.report}' is not supported.")
            sys.exit(1)

        report: BaseReport = report_cls()
        grouped_data: Dict[str, List[Dict[str, object]]] = report.generate(employees)
        report.print_report(grouped_data)

    except Exception as e:
        # General error handler
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()