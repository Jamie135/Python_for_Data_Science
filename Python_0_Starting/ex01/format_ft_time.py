import time as t
import datetime as dt


current_time = (
        f"Seconds since January 1, 1970: {t.time():,.4f} or "
        f"{t.time():.2e} in scientific notation"
)
current_date = f"{dt.datetime.today():%b %d %Y}"

print(current_time)
print(current_date)
