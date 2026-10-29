###  Python Linux Log Analyzer


### About

A Python-based security project that analyzes Linux authentication logs to detect failed login attempts, successful logins, and potentially suspicious IP addresses.

### Features

- Reads Linux authentication log files
- Detects failed login attempts
- Detects successful login attempts
- Counts failed login attempts by IP address
- Identifies suspicious IP addresses
- Extracts date and time of failed login activity
- Generates CSV reports
- Records analysis results using Python Logging
- Handles file errors using Try-Except

### Technologies Used

- Python 3
- CSV Module
- Logging Module
- File Handling
- Exception Handling

### Project Structure

Python_Linux_Log_Analyzer/
├── log_analyzer.py
├── sample_auth.log
├── failed_logins.csv
├── analyzer.log
├── README.md
└── Screenshots/
    ├── 01_code_output.png
    ├── 02_csv_report.png
    └── 03_logging.png

### How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open the project directory.
4. Make sure "sample_auth.log" is in the project folder.
5. Run the following command:

python log_analyzer.py

Sample Analysis Results

Analysis| Result
Total log entries| 7
Failed login attempts| 5
Successful login attempts| 2
Suspicious IP| 192.168.1.10

Note: An IP address is marked as suspicious when it has 3 or more failed login attempts. This is a practice threshold used in this project.

### Output Files

- "failed_logins.csv" — Stores IP addresses, failed login counts, and their status.
- "analyzer.log" — Stores analysis information and logging records.

### Screenshots

The "Screenshots/" folder contains:

- Code execution and analysis output
- CSV report
- Logging report

### Disclaimer

This project uses sample authentication log data for educational purposes. The suspicious IP threshold is a demonstration setting and not a universal security rule.

### Author

Shahriar Prodhan