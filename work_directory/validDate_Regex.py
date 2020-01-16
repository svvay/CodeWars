# Your task is to write a regular expression (regex) that will match a string only if
# it contains at least one valid date, in the format [mm-dd] (that is, a two-digit month,
# followed by a dash, followed by a two-digit date, surrounded by square brackets).
#
# You should assume the year in question is not a leap year. Therefore, the number of days each month should have are as follows:
#
# 1. January - 31 days
# 2. February - 28 days (leap years are ignored)
# 3. March - 31 days
# 4. April - 30 days
# 5. May - 31 days
# 6. June - 30 days
# 7. July - 31 days
# 8. August - 31 days
# 9. September - 30 days
# 10. October - 31 days
# 11. November - 30 days
# 12. December - 31 days
# All text outside a valid date can be ignored, including other invalid dates.

import re

months_30 = '(04|06|09|11)'
months_31 = '(01|03|05|07|08|10|12)'
months_28 = '02'
days_30 = '(0[1-9]|[1-2][0-9]|30)'
days_31 = '(0[1-9]|[12][0-9]|3[01])'
days_28 = '(0[1-9]|1[0-9]|2[0-8])'
valid_date = re.compile('\[(%s-%s|%s-%s|%s-%s)\]' % (months_30, days_30, months_31, days_31, months_28, days_28))

