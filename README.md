# Python Port Scanner

## Overview

The **Python Port Scanner** is a cybersecurity project that automates TCP port scanning for one or more IP addresses. It reads a list of target IPs, checks selected ports to determine whether they are open or closed, and displays the results in a clear, organized format.

This project was built to strengthen Python programming skills while introducing basic networking and cybersecurity concepts such as socket programming, port scanning, file handling, and automation.

> **Disclaimer:** This tool is intended for educational purposes and should only be used to scan systems that you own or have explicit permission to test.

---

## Features

- Read target IP addresses from a text file
- Scan multiple IP addresses automatically
- Check common TCP ports
- Identify open and closed ports
- Display scan results in the terminal
- Save scan results to a file
- Handle invalid IP addresses and connection errors gracefully

---

## Project Structure

```text
Python-Port-Scanner/
│
├── ip_list.txt          # List of target IP addresses
├── scanner.py           # Main scanning script
├── scan_results.txt     # Generated scan results
└── README.md
```

---

## How It Works

```text
Read IP Addresses
        │
        ▼
Validate Targets
        │
        ▼
Scan Selected TCP Ports
        │
        ▼
Determine Open/Closed Ports
        │
        ▼
Display & Save Results
```

---

## Python Concepts Used

- Functions
- Loops
- Conditional Statements
- File Handling
- Exception Handling
- Lists
- Socket Programming
- Time Module

---

## Example Output

```text
===================================
Python Port Scanner
===================================

Scanning: 192.168.1.10

Port 22   OPEN
Port 80   OPEN
Port 443  OPEN
Port 3389 CLOSED

-----------------------------------

Scanning: 192.168.1.20

Port 22   CLOSED
Port 80   OPEN
Port 443  CLOSED

===================================
Scan Complete
===================================
```

---

## Skills Learned

- Python Programming
- Network Programming
- TCP/IP Fundamentals
- Socket Programming
- Port Scanning Automation
- Basic Cybersecurity Concepts
- Error Handling

---

## Future Improvements

- Scan custom port ranges
- Multithreaded scanning for faster performance
- Export results to CSV or JSON
- Banner grabbing
- Service detection
- Command-line arguments with `argparse`
- Progress bar and colored output

---

## License

This project is for educational purposes only. Use it only on systems you own or have explicit authorization to test.
