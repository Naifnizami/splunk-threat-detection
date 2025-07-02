# 🔍 Splunk RCE + SQLi Detection & Response Automation

A practical threat detection and response system using **Splunk** and a custom **Python-based IP blocker** to detect and mitigate SQL Injection (SQLi) and Remote Code Execution (RCE) attacks in real-time.

---

## 🚀 Features

- ✅ Real-time detection of:
  - SQL Injection (SQLi) attempts  
  - Reverse shell payload access  
- 🔒 IP auto-blocking via `iptables` + `arptables` through webhook  
- 📬 Email alerts with attacker IPs and log evidence  
- 📊 Splunk dashboard panels:
  - Top attacker IPs  
  - Malicious file access  
  - Alert frequency over time  
- 🛡️ Whitelisting for trusted or internal IPs  

---

## 🧠 Use Case

Simulates a **real-world SOC detection-response workflow**, integrating:

- Apache access & auth/syslog monitoring  
- Python-based blocking API  
- Splunk alerting & webhook-driven response  

Ideal for cybersecurity training and portfolio projects.

---

## 🛠 Tech Stack

- Splunk Enterprise (9.x) & Universal Forwarder  
- Python 3 + Flask  
- Linux VMs (Ubuntu, Kali)  
- `iptables`, `arptables`, `curl`, `nc`  
- Git, GitHub

---

## 📥 Installation

1. Install **Splunk Enterprise** on the main analysis host:  
   [Download Splunk Enterprise](https://www.splunk.com/en_us/download/splunk-enterprise.html?locale=en_us)

2. Install **Splunk Universal Forwarder** on the monitored/victim VM(s):  
   [Download UF (previous releases)](https://www.splunk.com/en_us/download/previous-releases-universal-forwarder.html)

3. On victim VMs:
   ```bash
   # Launch vulnerable PHP app in web folder
   # Import database schema:
   mysql -u root -p < db/vulnsite_schema.sql

   # Deploy UF config to monitor logs:
   splunk add forward-server <your-splunk-ip>:9997
   splunk add monitor /var/log/apache2/access.log
   splunk add monitor /var/log/auth.log
   splunk add monitor /var/log/syslog

   # Deploy blocker API
   sudo python3 blocker.py

📂 Project Structure

| File/Folder        | Description                                            |
| ------------------ | ------------------------------------------------------ |
| `blocker.py`       | Flask API to block attackers via firewall              |
| `splunk/`          | SPL queries, saved alerts, alert setup docs            |
| `screenshots/`     | Screenshots of dashboard, alerts, and blocking         |
| `Screenrecording/` | Short video walkthrough (SQLi ➜ RCE detection → block) |
| `web/`             | Vulnerable app source files (PHP, uploads, etc.)       |
| `db/`              | Database schema (vulnsite\_schema.sql)                 |

## 📸 Visuals & Walkthrough

- **Splunk Dashboard** – detection panels:

   ![Splunk Dashboard](Screenshots/Dashboard-2.png)
   *Displays real-time detection of SQLi & RCE attempts, top attacker IPs, and malicious file access.*

- **Blocker Console** – IP block logs:

   ![Blocker Console](Screenshots/Blocker_Console.png)
   *Displays logs of IPs blocked in response to detected attacks.*

- **Email Alert sample**:

   ![Email Alert](Screenshots/Email_Alert.png)
   *Example of an email sent when an attacker is detected.*

- **SPL Query Result showing detected logs:**

   ![SPL Query](Screenshots/SPL.png)
   *Result from the SPL query used to detect malicious activities.*

- **Vulnerable Web Interface** – app used in testing:

   ![Vulnerable Web Interface](Screenshots/Vulnerable_Website.png)
   *Simulated vulnerable web application demonstrating SQLi & RCE exploitation.*

---

## 🎥 Walkthrough Video

Here’s a short video walkthrough of the detection & blocking workflow:

[![Splunk Workflow](Screenrecording/Splunk_Workflow.mkv)](Screenrecording/Splunk_Workflow.mkv)

💡 Setup & Execution Steps

1.Launch the vulnerable PHP app from the web/ folder.

2.Import db/vulnsite_schema.sql into MariaDB.

3.Deploy both Splunk Enterprise & Universal Forwarder.

4.Run blocker.py to listen on port 5000.

5.Create a Splunk alert using the following SPL query to catch malicious activity:
index=* (sourcetype="access_combined" OR sourcetype="access-too_small" OR source="/var/log/auth.log" OR source="/var/log/syslog")
| regex _raw="(?i)(/uploads/ReverseShell.php|session opened.*for user|nc -e|%27.*OR.*%3D|%271%27%3D%271)"
| rex field=_raw "(?<attacker_ip>\d{1,3}(?:\.\d{1,3}){3})"
| search attacker_ip=*
| table _time, attacker_ip, source, sourcetype, _raw

6.Configure the webhook alert action:
http://<target‑ip>:5000/block?ip=$result.attacker_ip$&token=BLOCKME123
(Optional) Enable throttled email alerts for visibility.

🎯 Goal
Demonstrates security automation & response skills using SIEM, scripting, firewall, and alerting—excellent for demonstrating SOC competencies.

✉️ Contact
Created by Naif Nizami · ★ Welcome to ⭐ this repo if you find it useful!


