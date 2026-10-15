import psutil
import logging
import sys

# Configure logging
logging.basicConfig(
    filename='system_health.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define thresholds
CPU_THRESHOLD = 80.0  # Percentage
MEMORY_THRESHOLD = 80.0  # Percentage
DISK_THRESHOLD = 85.0  # Percentage

def check_system_health():
    # 1. CPU Usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        alert_msg = f"HIGH CPU USAGE DETECTED: {cpu_usage}%"
        print(alert_msg)
        logging.warning(alert_msg)
    else:
        print(f"CPU Usage is normal: {cpu_usage}%")

    # 2. Memory Usage
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        alert_msg = f"HIGH MEMORY USAGE DETECTED: {memory_usage}%"
        print(alert_msg)
        logging.warning(alert_msg)
    else:
        print(f"Memory Usage is normal: {memory_usage}%")

    # 3. Disk Space Usage
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        alert_msg = f"HIGH DISK USAGE DETECTED: {disk_usage}%"
        print(alert_msg)
        logging.warning(alert_msg)
    else:
        print(f"Disk Usage is normal: {disk_usage}%")

    # 4. Running Processes count check
    process_count = len(psutil.pids())
    logging.info(f"Current running processes count: {process_count}")

if __name__ == "__main__":
    check_system_health()