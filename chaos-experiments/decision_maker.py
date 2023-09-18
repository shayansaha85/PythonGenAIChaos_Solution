import psutil
import time

def collect_system_metrics(interval, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        # Collect CPU usage as a percentage
        cpu_percent = psutil.cpu_percent(interval=interval)

        # Print CPU usage
        print(f"CPU Usage: {cpu_percent}%")

        # Check if CPU usage exceeds the threshold
        threshold = get_threshold()
        if cpu_percent > threshold:
            handle_high_cpu_usage(cpu_percent, threshold)

        time.sleep(interval)

def get_threshold():
    try:
        threshold = float(input("Enter the CPU usage threshold (e.g., 80 for 80%): "))
        return threshold
    except ValueError:
        print("Invalid input. Please enter a valid threshold.")
        return get_threshold()

def handle_high_cpu_usage(cpu_percent, threshold):
    print(f"CPU usage ({cpu_percent}%) exceeds the threshold ({threshold}%).")
    # Add your decision-making logic here, such as sending alerts or taking actions.

if __name__ == "__main__":
    # Set the interval (in seconds) for metric collection
    interval = 5  # Collect metrics every 5 seconds

    # Set the duration (in seconds) for metric collection
    duration = 30  # Collect metrics for 30 seconds

    print(f"Collecting system metrics every {interval} seconds for {duration} seconds...")
    collect_system_metrics(interval, duration)
