import psutil
import time

def collect_system_metrics(interval, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        # Collect CPU usage as a percentage
        cpu_percent = psutil.cpu_percent(interval=interval)

      

        print(f"CPU Usage: {cpu_percent}%")
       

        time.sleep(interval)

if __name__ == "__main__":
    # Set the interval (in seconds) for metric collection
    interval = 5  # Collect metrics every 5 seconds

    # Set the duration (in seconds) for metric collection
    duration = 30  # Collect metrics for 30 seconds

    print(f"Collecting system metrics every {interval} seconds for {duration} seconds...")
    collect_system_metrics(interval, duration)
