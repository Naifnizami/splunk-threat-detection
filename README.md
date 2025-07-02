# 🔍 Splunk RCE + SQLi Detection & Response Automation

A practical threat detection and response system using **Splunk** and a custom **Python-based IP blocker** to detect and mitigate SQL Injection (SQLi) and Remote Code Execution (RCE) attacks in real-time.

---

## 🚀 Features

- ✅ Real-time detection of:
  - SQL Injection (SQLi) attempts
  - Reverse shell payload access
- 🔒 IP auto-blocking using `iptables` + `arptables` via webhook
- 📬 Email alerts with attacker IP and log evidence
- 📊 Splunk dashboards with:
  - Top attacker IPs
  - Malicious file access attempts
  - Alert frequency over time
- 🛡️ Whitelisting support for internal/testing IPs

---

## 🧠 Use Case

This project replicates a **real-world SOC detection-response workflow**, integrating:

- Apache log monitoring (access, syslog, auth)
- Python API-based IP blocking mechanism
- Splunk alerts → Webhook trigger for automated blocking

Great for Blue Team projects, SOC labs, and resume-worthy demonstrations.

---

## 📂 Project Structure

| Path               | Description                                         |
|--------------------|-----------------------------------------------------|
| `blocker.py`       | Flask API server that blocks IPs via iptables & arptables |
| `web/`             | Vulnerable PHP site (login, upload, dashboard)     |
| `db/`              | MySQL database schema file (`vulnsite_schema.sql`) |
| `screenshots/`     | Email alert, dashboard panels, SPL, blocker logs   |
| `splunk/`          | SPL queries and Splunk alert configurations        |
| `README.md`        | Project documentation (you’re reading it)          |

---

## 📸 Screenshots

### 🖥️ Splunk Dashboard Panels
- Visuals showing attacker trends, frequency, and accessed files
![Dashboard Panels](screenshots/Dashboard-2.png)

### 🧾 Webhook-Triggered IP Blocking Console
- Confirming IPs getting blocked live
![Blocker Console](screenshots/Blocker_Console.png)

### 📬 Email Alert Example
- Alert with log snippet, attacker IP, and timestamp
![Email Alert](screenshots/Email_Alert.png)

### 🔍 SPL Matching Log Events
- RCE and SQLi activity captured and highlighted
![SPL Results](screenshots/SPL.png)

### 🌐 Vulnerable Web Interface
- Entry point for simulated SQLi and shell uploads
![Web App](screenshots/Vulnerable_Website.png)

---

## 🛠️ Tech Stack

- Splunk 9.x
- Python 3 + Flask
- iptables / arptables
- Apache2 logs (`access.log`, `auth.log`, `syslog`)
- MySQL (vulnsite schema)
- Ubuntu + Kali Linux

---

## ⚙️ Setup Steps

1. **Launch vulnerable PHP web app** (from `/web/` folder).
2. **Import database schema** from `db/vulnsite_schema.sql`.
3. **Deploy Splunk Universal Forwarder** on target machine and monitor:
   - `/var/log/apache2/access.log`
   - `/var/log/auth.log`
   - `/var/log/syslog`
4. **Run `blocker.py`** to listen on port `5000` for block requests.
5. **Set up Splunk alert** using SPL to detect malicious patterns.
6. **Webhook URL** format:
http://<target-ip>:5000/block?ip=$result.attacker_ip$&token=BLOCKME123
7. **Optional: Add throttle & email alert** for visibility.

---

## 📬 Contact

Made with 🛡️ by [Naif Nizami](https://github.com/Naifnizami)  
⭐ Star this project if it helps your security journey or lab demos!

