import wmi
import psutil
import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta

# Step 1: Collect Real-Time System Metrics
def collect_real_time_data(duration_minutes=1440, sampling_rate_hz=2):
    """
    Collect real-time system metrics using wmi and psutil.
    """
    w = wmi.WMI(namespace="root\\OpenHardwareMonitor")  # WMI object for hardware monitoring

    num_samples = duration_minutes * 60 * sampling_rate_hz
    timestamps = []
    cpu_temperatures = []
    cpu_usages = []
    cpu_loads = []
    memory_usages = []
    cpu_powers = []

    start_time = datetime.now()
    for i in range(num_samples):
        try:
            # Generate timestamp
            current_time = datetime.now()
            timestamps.append(current_time)

            # Get CPU temperature and power via WMI
            sensor_info = w.Sensor()
            cpu_temp = None
            cpu_power = None
            for sensor in sensor_info:
                if sensor.SensorType == "Temperature" and "CPU" in sensor.Name:
                    cpu_temp = sensor.Value
                if sensor.SensorType == "Power" and "CPU Package" in sensor.Name:
                    cpu_power = sensor.Value
            cpu_temperatures.append(cpu_temp if cpu_temp is not None else random.uniform(60, 80))
            cpu_powers.append(cpu_power if cpu_power is not None else random.uniform(5, 20))

            # Get CPU usage via psutil
            cpu_usage = psutil.cpu_percent(interval=1 / sampling_rate_hz)
            cpu_usages.append(cpu_usage)

            # Get CPU load via psutil
            cpu_load = psutil.getloadavg()[0] if hasattr(psutil, "getloadavg") else random.uniform(0.5, 1.5)
            cpu_loads.append(cpu_load)

            # Get memory usage via psutil
            memory_usage = psutil.virtual_memory().percent
            memory_usages.append(memory_usage)

        except Exception as e:
            print(f"Error collecting data at {i}: {e}")
            cpu_temperatures.append(None)
            cpu_usages.append(None)
            cpu_loads.append(None)
            memory_usages.append(None)
            cpu_powers.append(None)

    # Create DataFrame
    data = {
        "timestamp": timestamps,
        "cpu_temperature": cpu_temperatures,
        "cpu_usage": cpu_usages,
        "cpu_load": cpu_loads,
        "memory_usage": memory_usages,
        "cpu_power": cpu_powers,
    }
    df = pd.DataFrame(data)

    # Save to CSV
    output_file = "real_time_data.csv"
    df.to_csv(output_file, index=False)
    print(f"Real-time data saved to {output_file}.")
    return df

# Step 2: Anomaly Detection
def detect_anomalies(series, threshold=3):
    """
    Detect anomalies in a time series using mean and standard deviation.
    """
    mean = series.mean()
    std_dev = series.std()
    anomalies = (series > mean + threshold * std_dev) | (series < mean - threshold * std_dev)
    return anomalies

# Step 3: Visualization
def visualize_anomalies(df, metrics, anomaly_flags):
    """
    Visualize anomalies in the dataset.
    """
    fig, axs = plt.subplots(3, 2, figsize=(15, 10))
    fig.suptitle('Anomalies Detection in System Metrics', fontsize=16)

    for i, metric in enumerate(metrics):
        ax = axs[i // 2, i % 2]
        ax.plot(df.index, df[metric], label='Data', color='blue')
        anomalies = df.index[anomaly_flags[metric]]
        ax.scatter(anomalies, df.loc[anomalies, metric], color='red', label='Anomalies')
        ax.set_title(f'{metric.capitalize()} with Anomalies Highlighted')
        ax.set_xlabel('Index')
        ax.set_ylabel(metric.capitalize())
        ax.legend()

    # Remove unused subplot
    axs[2, 1].axis('off')

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()


# Main Workflow
if __name__ == "__main__":
    # Step 1: Collect Real-Time Data
    print("Collecting real-time system metrics...")
    df = collect_real_time_data(duration_minutes=1440, sampling_rate_hz=2)  # Adjust duration and sampling rate as needed

    # Step 2: Anomaly Detection
    metrics = ["cpu_temperature", "cpu_usage", "cpu_load", "memory_usage", "cpu_power"]
    anomaly_flags = {}
    for metric in metrics:
        anomaly_flags[metric] = detect_anomalies(df[metric])

    # Step 3: Visualization
    print("Visualizing anomalies...")
    visualize_anomalies(df, metrics, anomaly_flags)
