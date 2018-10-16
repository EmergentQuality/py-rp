from datetime import datetime

datetime_for_string = datetime(2018, 10, 1, 0, 0)
datetime_string_format = '%B %d, %Y'

print(datetime.strftime(datetime_for_string, datetime_string_format))
