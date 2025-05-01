import pendulum

# Define start and end datetimes
start = pendulum.datetime(2023, 1, 1)
end = pendulum.datetime(2023, 1, 10)

# Calculate the duration between two datetimes
duration = end - start
print(duration.days)
# 9

# Create a period and iterate through its range
interval = pendulum.period(start, end)
for dt in interval.range('days'):
  print(dt)
  # '2023-01-01T00:00:00+00:00'
  # '2023-01-02T00:00:00+00:00'
  # ...
  # '2023-01-10T00:00:00+00:00'
