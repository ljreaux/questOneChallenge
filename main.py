import csv

def main():
    file_name = "city-of-seattle-2012-expenditures-dollars.csv"
    department_totals = {}

    def convert_to_float(string):
        try:
            return float(string)
        except ValueError:
            return 0

    with open(file_name) as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            department = line[0]
            expenses = convert_to_float(line[3])

            # catches blank lines
            if not department:
                continue

            # continues with the total if dept is already in dict
            if department_totals.get(department):
                department_totals[department] += expenses
            else: department_totals[department] = expenses

    for department, expenses in department_totals.items():
        print(f"{department} ${expenses:,.2f}")

if __name__ == "__main__":
    main()