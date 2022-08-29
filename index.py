import schedule
import time

def task():
    print("Job Executing!")

# for every n minutes
schedule.every(10).minutes.do(task)

# every hour
schedule.every().hour.do(task)

# every daya at specific time
schedule.every().day.at("10:30").do(task)

# schedule by name of day
schedule.every().monday.do(task)

# name of day with time
schedule.every().wednesday.at("13:15").do(task)

while True:
    schedule.run_pending()
    time.sleep(1)