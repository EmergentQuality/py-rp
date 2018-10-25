import csv

employees = [['Bill', 'Lumbergh', 'Vice President', '1985', 'excellent', ],
             ['Michael', 'Bolton', 'Programmer', '1995', 'poor', ],
             ['Peter', 'Gibbons', 'Programmer', '1989', 'poor'],
             ['Samir', 'Nagheenanajar', 'Programmer', '1974', 'fair', ],
             ['Milton', 'Waddams', 'Collator', '1974', 'does he even work here?', ],
             ['Bob', 'Porter', 'Consultant', '1999', 'excellent', ],
             ['Bob', 'Slydell', 'Consultant', '1999', 'excellent', ]]

with open('tps_report.csv_1', mode='w', newline='') as report:
    fieldnames = [
        'first_name',
        'last_name',
        'job_title',
        'hire_date',
        'performance_review',
    ]
    writer = csv.DictWriter(report, fieldnames=fieldnames)
    writer.writeheader()

    for employee in employees:
        writer.writerow(dict(zip(fieldnames, employee)))
