# System Metrics Monitoring and Anomaly Detection

This project collects real-time system metrics using the **Open Hardware Monitor** (OHM) and Python libraries such as **wmi** and **psutil**. It detects anomalies in the system's behavior (e.g., CPU temperature, usage, memory, and power) and visualizes the anomalies with graphs.

## Features

- Collects real-time system metrics such as:
  - **CPU Temperature**
  - **CPU Usage**
  - **CPU Load**
  - **Memory Usage**
  - **CPU Power Consumption**

- Detects anomalies using a simple statistical method.
- Visualizes the data and highlights anomalies in a clear and intuitive way.

## Requirements

### System Requirements
- **Operating System**: Windows (required for Open Hardware Monitor and WMI functionality).
- **Open Hardware Monitor**: Installed and running on your system.

### Python Libraries
Ensure you have the following Python libraries installed:

- `wmi`
- `psutil`
- `pandas`
- `matplotlib`

You can install them using the following command:

```bash
pip install wmi psutil pandas matplotlib
