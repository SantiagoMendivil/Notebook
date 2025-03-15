from datetime import datetime

def time_elapsed(saved_date):
    """
    Calculates the time elapsed from a given date until now.
    :param saved_date: str, date in format 'YYYY-MM-DD HH:MM:SS'
    :return: str, time elapsed in years, months, days, hours, minutes, and seconds.
    """
    saved_date = datetime.strptime(saved_date, '%Y-%m-%d %H:%M:%S')
    now = datetime.now()
    difference = now - saved_date
    
    days = difference.days
    total_seconds = difference.seconds
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    return f"Time elapsed: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

# Example usage
example_date = "2024-03-01 12:30:00"
print(time_elapsed(example_date))
