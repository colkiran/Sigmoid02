
months = ['dec', 'apr', 'oct', 'aug', 'sep', 'jan', 'nov', 'may', 'feb', 'jul', 'mar', 'jun']

# sort these months
from calendar import month_abbr
print(f"month_abbr :{list(month_abbr)}")

res_asc = sorted(months, key=list(map(lambda x: x.lower(), month_abbr)).index)
print(f"sorted months :{res_asc}")