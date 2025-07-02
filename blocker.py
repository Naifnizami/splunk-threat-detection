#!/usr/bin/env python3
from flask import Flask, request, jsonify
import subprocess
from datetime import datetime

app = Flask(__name__)
LOGFILE = "/tmp/blocker_log.txt"
SECRET_TOKEN = "BLOCKME123"  # shared token for basic protection

# 🛡️ Define trusted IPs (like Kali box or internal services)
WHITELIST = {"192.168.1.22","127.0.0.1"}  # Add more if needed

def log(msg):
    timestamp = f"{datetime.now()} - {msg}"
    print(timestamp)
    with open(LOGFILE, "a") as f:
        f.write(timestamp + "\n")
    subprocess.run(["logger", timestamp])  # send to syslog

def iptables_rule_exists(ip):
    result = subprocess.run(
        ["sudo", "iptables", "-C", "INPUT", "-s", ip, "-m", "conntrack", "--ctstate", "NEW,ESTABLISHED", "-j", "DROP"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    return result.returncode == 0

def arptables_rule_exists(ip):
    result = subprocess.run(
        ["sudo", "arptables", "-C", "INPUT", "--source-ip", ip, "-j", "DROP"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    return result.returncode == 0

@app.route("/block", methods=["GET", "POST"])
def block_ip():
    if request.method == "GET":
        ip = request.args.get("ip")
        token = request.args.get("token")
    elif request.method == "POST":
        data = request.get_json(silent=True) or {}
        ip = data.get("ip") or request.args.get("ip")
        token = data.get("token") or request.args.get("token")

    if token != SECRET_TOKEN:
        log("❌ Unauthorized request (invalid token)")
        return jsonify({"status": "error", "message": "Unauthorized"}), 403

    if not ip:
        log("❌ No IP provided in request")
        return jsonify({"status": "error", "message": "No IP provided"}), 400

    # ✅ Whitelist check
    if ip in WHITELIST:
        log(f"🟢 Whitelisted IP, skipping block: {ip}")
        return jsonify({"status": "ok", "blocked_ip": ip, "note": "whitelisted"}), 200

    try:
        already_blocked = False

        if iptables_rule_exists(ip):
            log(f"ℹ IP already blocked in iptables (conntrack): {ip}")
            already_blocked = True
        else:
            subprocess.run([
                "sudo", "iptables", "-I", "INPUT", "-s", ip,
                "-m", "conntrack", "--ctstate", "NEW,ESTABLISHED", "-j", "DROP"
            ])
            log(f"✅ Blocked {ip} in iptables (conntrack)")

        if arptables_rule_exists(ip):
            log(f"ℹ IP already blocked in arptables: {ip}")
            already_blocked = True
        else:
            subprocess.run(["sudo", "arptables", "-A", "INPUT", "--source-ip", ip, "-j", "DROP"])
            log(f"✅ Blocked {ip} in arptables")

        status_msg = "already blocked" if already_blocked else "blocked"
        return jsonify({"status": "success", "blocked_ip": ip, "note": status_msg}), 200

    except Exception as e:
        error_msg = f"❌ Failed to block IP {ip}: {e}"
        log(error_msg)
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    log("🚀 blocker.py started on port 5000")
    app.run(host="0.0.0.0", port=5000)
