import xlwt
import datetime

from xlwt import Workbook

wb = Workbook()


steps_log = wb.add_sheet("problem_solving")

date_start_string = "13/07/2022"
date_start = datetime.datetime.strptime(date_start_string, "%d/%m/%Y")

print(date_start.date())
steps_log.write(0, 0, "Date")
steps_log.write(0, 1, "Steps")

for i in range(34):
    print(date_start.date())
    stes = input("Enter steps: ")
    steps_log.write(i+1, 0, str(date_start.date()))
    steps_log.write(i+1, 1, stes)
    date_start += datetime.timedelta(days=1)
    



wb.save('problem_solving.xlsx')