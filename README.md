# 🔍 Splunk RCE + SQLi Detection & Response Automation

A practical threat detection and response system using **Splunk** and a custom **Python-based IP blocker** to detect and mitigate SQL injection and remote code execution (RCE) attacks in real-time.

## 🚀 Features

- ✅ Real-time detection of:
  - SQL Injection (SQLi) attempts
  - Reverse shell payloads
- 🔒 IP auto-blocking with `iptables` and `arptables` via webhook
- 📬 Email alerts with attacker IPs and log details
- 📊 Splunk dashboard with:
  - Top attacker IPs
  - Malicious file access
  - Alert frequency over time
- 🛡️ Whitelisting support for internal/testing IPs

## 📂 Files

- `blocker.py` – Flask API for IP blocking
- `screenshots/` – Visuals of detection, dashboard, and console logs

## 📸 Screenshots

| Splunk Dashboard | Blocker Console |
|------------------|-----------------|
| ![Dashboard](screenshots/Screenshot_2025-07-02_14_19_46.png) | ![Console](screenshots/Screenshot_2025-07-02_14_31_40.png) |

## 💡 Use Case

This project simulates a **real-world threat hunting workflow**, integrating log analytics, alerting, and automated response – ideal for SOC analysts and cybersecurity students.

## 🛠️ Tech Stack

- Splunk 9.x
- Python 3 (Flask, subprocess)
- iptables, arptables
- Git, Linux

## 📬 Contact

Created by [Naif Nizami](https://github.com/Naifnizami) – drop a ⭐ if you found it useful!
