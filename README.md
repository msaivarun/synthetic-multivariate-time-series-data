**System Metrics Monitoring and Anomaly Detection**
This project collects real-time system metrics using the Open Hardware Monitor (OHM) and Python libraries such as wmi and psutil. It detects anomalies in the system's behavior (e.g., CPU temperature, usage, memory, and power) and visualizes the anomalies with graphs.

Features
Collects real-time system metrics such as:
CPU Temperature
CPU Usage
CPU Load
Memory Usage
CPU Power Consumption
Detects anomalies using a simple statistical method.
Visualizes the data and highlights anomalies in a clear and intuitive way.
Requirements
System Requirements

Operating System: Windows (required for Open Hardware Monitor and WMI functionality).
Open Hardware Monitor: Installed and running on your system.
Python Libraries Ensure you have the following Python libraries installed:

wmi
psutil
pandas
matplotlib
Install them using the following command:

bash
Copy code
pip install wmi psutil pandas matplotlib
Setup Instructions
Step 1: Install and Run Open Hardware Monitor
Download Open Hardware Monitor:

Download the latest version from Open Hardware Monitor.
Run Open Hardware Monitor as Administrator:

Extract the downloaded ZIP file.
Right-click OpenHardwareMonitor.exe and select "Run as Administrator".
Keep Open Hardware Monitor running during the script execution.
Verify Sensor Data:

Ensure you can see live system metrics such as CPU temperature, load, and power in the Open Hardware Monitor window.
Step 2: Clone and Run the Project
Clone this repository:

bash
Copy code
git clone <your-repository-url>
cd <your-repository-folder>
Run the script:

Open the project in your code editor (e.g., VS Code).
Execute the Python script:
bash
Copy code
python main.py
How the Code Works
1. Real-Time Data Collection
The script uses:

wmi to fetch hardware sensor data (e.g., CPU temperature and power) via the Open Hardware Monitor.
psutil to get system resource usage such as CPU and memory usage.
The collected data includes:

CPU Temperature: Captured via WMI from OHM.
CPU Usage: Retrieved using psutil.cpu_percent.
CPU Load: Average system load over 1 minute.
Memory Usage: Percentage of system memory in use.
CPU Power Consumption: Captured via WMI from OHM.
This data is stored in a Pandas DataFrame and saved to real_time_data.csv.

2. Anomaly Detection
Anomalies are detected in the metrics using the mean ± 3 * standard deviation method:

If a data point deviates significantly from the average, it is flagged as an anomaly.
The threshold can be adjusted for more or fewer anomalies.
3. Visualization
The script generates graphs for each metric (e.g., CPU temperature, usage, etc.):

The data is plotted in blue.
Anomalies are highlighted with red dots.
Example:

(Replace <insert-image-link-here> with the image URL after uploading to GitHub.)

Code Overview
Main Sections
Data Collection

python
Copy code
w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
sensor_info = w.Sensor()
cpu_temp = [sensor.Value for sensor in sensor_info if sensor.SensorType == "Temperature" and "CPU" in sensor.Name]
Anomaly Detection

python
Copy code
def detect_anomalies(series, threshold=3):
    mean = series.mean()
    std_dev = series.std()
    anomalies = (series > mean + threshold * std_dev) | (series < mean - threshold * std_dev)
    return anomalies
Visualization

python
Copy code
def visualize_anomalies(df, metrics, anomaly_flags):
    for metric in metrics:
        plt.scatter(anomalies, df.loc[anomalies, metric], color='red', label='Anomalies')
Usage
Customizing Data Collection
Modify these parameters in the collect_real_time_data function:

duration_minutes: Total duration for data collection (default: 5 minutes).
sampling_rate_hz: Sampling frequency in Hz (default: 2 samples/second).
Customizing Anomaly Detection
Adjust the threshold in detect_anomalies:

Higher values (e.g., 4) result in fewer anomalies.
Lower values (e.g., 2) result in more anomalies.
