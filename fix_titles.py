import json

titles_str = """Web Attack Investigator
Linux Fan
Brute Force
Web Server Analyzer
MITRE ATT&CK
Web Hunter
Go Writer
Secure Network Designer
JWT Attacks and Detection
AWS CloudWatch
Physical Security
Red Team Hunter - 2
PDF Analyzer
Browser Extension Analyzer
Phishing Analyzer
AWS Responder
AWS Incident Handler
Docker Forensics
macOS Malware
Discord Forensics
Golang Ransomware
AWS Bucketware
AWS Stacked
VoIP
USB Forensics
TinyTurla Backdoor
Samba Spy
Mac Backdoor
Hidden Backdoor
Google Cloud Compromise
Promptlock Ransomware
Learn Sigma
First Blood"""

titles = [t.strip() for t in titles_str.split('\n') if t.strip()]

with open('update_badges.py', 'r') as f:
    content = f.read()

# Instead of relying on the bad split, just replace it with explicit array
titles_array_str = json.dumps(titles)
content = content.replace("titles = [t.strip() for t in user_titles_str.split('\\\\n') if t.strip()]", f"titles = {titles_array_str}")
content = content.replace("titles = [t.strip() for t in user_titles_str.split('\\n') if t.strip()]", f"titles = {titles_array_str}")

with open('update_badges.py', 'w') as f:
    f.write(content)
