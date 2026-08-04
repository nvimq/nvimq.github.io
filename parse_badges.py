import re
import json

data = [
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/homepage",
    "img": "https://app.letsdefend.io/images/hb_logo.svg"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/certificate/aws-security-example.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/certificate/career-switch-cert-sample.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/certificate/cysa-cert-sample+(1).png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/web-attacks-badge-2f7551ca-00ea-49e0-ae0c-a508c3c00552.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/badge-linux-101-01963665-e81b-45f9-aae0-f1a1b63392cb.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/brute-force-badge-48517643-fe50-4a92-b328-506c4208a6b1.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/hacked-analysis-badge-avatar-4c433f26-e83b-4e2a-8401-3fb32b1fa093.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/mitre-badge-2-f8edfcce-62c1-4170-95cf-af5fd56562d0.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/web-attacks-2-badge-5ab868c5-0140-4000-b386-f15e747614cf.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/go-badge-avatar-f8a039ef-d328-49b1-89ad-2e2b4493cacc.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/secure-network-design-badge-8d746f5e-9ec2-4790-9227-f1c48207b21a.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/jwt-badge-38239eae-8bed-451b-911f-449144eafc7f.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/aws-cloudwatch-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/physical-sec-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/red-team-tools-2-858e0eea-5707-460d-b176-3912fdd86aa4.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/pdf-avatar-9a8f2e62-86dd-4032-a2d5-90ef42f5b04a.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/suspicious-browser-extension-badge-cd7872ab-e178-4a1e-91ee-92eccd0cf809.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/phishing-challenge-avatart_vQ1645S-19e4e4cb-4f19-45ef-bb63-01c5260c8547.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/aws-badge-b665787c-af28-4502-bf99-8d88dd146e90.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/aws-persestence-badge-c5c8649b-0c46-46fd-a78d-34b87f8833e5.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/docker-badge-62df3f55-0589-4bb6-ba71-b344ceced720.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/macos-malware-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/discord-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/go-ransom-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/aws-bucketware-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/aws-stacked-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/voip-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/usb-forensics-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/TinyTurla+Backdoor-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/samba-spy-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/mac+backdoor-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Hidden+Backdoor-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Google+Cloud+Compromise-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Promptlock+Ransomware-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Learn+Sigma-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/first-badge-6529e305-65c7-41fe-a929-c728f1bee986.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/linux-responder-6a8b2652-c294-485c-8a2c-8d165a5dd340.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/windows-response-badge_3g6UVGR-67644fcf-2240-412c-8b53-18722774ba60.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/soc-fundamentals-badge-0101ea06-51bf-4f94-8e2f-1b363f78dbb2.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/3-a2e2f4ae-241a-42f8-af89-e5d1a2a8a0f5.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/siem-badge-avatar-c5ab3e19-5da3-4ee9-89dc-a11c8788a592.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/malware-analysis-badge-63fefb51-8715-4ecb-bc9f-1ce42187bfad.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/ims-avatar-b730b7a7-d848-4e2c-b108-528f08e8f34a.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/cti-badge-avatar-413f3a51-19b2-4d08-81e7-688b900262c6.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/dynamic-avatar-7ccd1f91-fc62-4d28-a072-aefab8adb47e.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/wireshark-avatar-73ca2edf-93b5-4cb3-b1b4-472953d16fe4.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/win101-avatar-9f584b0b-6442-498f-829b-5af622742b9f.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/crisis-avatar-c9c9dfe7-6e47-4077-80ef-bcb482fb6965.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/virustotal-for-soc-analysts-badge-4920215e-7d37-41ba-b247-31ff70ad08c3.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/Cryptographer-avatar-42075aa5-9c2f-490f-8a63-01f64a4fe6bd.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/report-badge-avatar-ad2b9af4-32e4-4984-a0dd-fe79bcf09e16.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/avatar-log-badge-26f2fa0d-5256-490f-92be-d34edd73227e.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/badge-avatar-job-hunting-b6e07278-b34f-4406-8a66-3be873e9e489.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/lab-build-badge-avatar-cdd9d6c7-8510-462d-bcc4-6fc8f1cc4caf.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/network-fundamentals-badge-avatar-f3b45304-987d-4d47-87d9-291c0d288238.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/splunk-badge-avatar-72021ad3-5988-4287-93e0-078b072ecddc.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/it-sec-badge-avatar-6879bfe5-5253-46b9-a011-9fd50ef12566.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/network-fun-2-badge-c5c0069a-d7d3-46ba-ac0c-c7f48fe2e908.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/memory-forensics-badge-avatar-8691b8fd-1c45-4d3a-83bd-f6c1af4d89e1.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/sysmon-badge-ca936b36-55fe-4278-b07b-9e3a680069d0.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/soc-lab-avatar-fc29f3e3-8d51-46b8-97fc-6c22a87447f8.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/network-protocols-badge-94c1af12-7d74-48c6-bb47-8614261e855c.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/security-solution-badge_ZRZN79Q-6d2033e4-bc4b-4178-8342-46b680e8c2e6.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/browser-forensics-badge-0df0d712-1275-49e3-bee0-bdd2f015d9e0.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/network-protocols-2-badge-avatar-9b1798cb-a04f-47a4-b60f-4bf585b2c8bc.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/event-log-analysis-badge-avatar-47bc51bf-16ef-4343-8912-50a22feda072.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/registry-forensics-badge-459dcee9-5284-4663-a174-0d5c3c43c6f6.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/mal-doc-badge-6cbd02ef-ee38-4d8d-9f45-39ed61db8d2d.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/acq-badge-0c7e6f2c-db5f-4c1c-ba95-b975722cfb52.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/ad-attack-badge-b193ea40-84c3-46b7-870d-f66a551e7c59.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/cyber-inc-badge-56cb0c55-9073-4509-8248-b9b1374a81db.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/gtfo-badge-avatar-8f4b1787-6f6c-4cb3-a723-a4c70ed72c21.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/rev-badge-13056943-92c3-4ee4-9a20-112af3063c58.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/ckc-badge-e7f2b13b-5a09-4340-93f1-de53c7e5e904.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/static-malware-badge-d14fec92-5ec8-4035-bfdc-a0a655c829fb.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/wazuh-badge-bf11f34d-7c6b-46bf-b9df-cb6269fcac9a.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/badge-win-forensics-bb2ef21b-17e1-4cc6-9900-31b983a7c187.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/rev-2-badge-e692f456-9665-48e2-9fac-cdb76674774b.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/badge-network-packet-5a9e234a-7fc7-4d61-8d31-b3fa0c94186a.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/adv-badge-a0f237fb-667a-4a03-906e-767dbd39b521.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/reg-2-badge-f66a466f-7fa4-4767-8aeb-cb904150f3f9.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/log4shell-badge-44b15e3a-1d0f-41a6-8452-56e5fb1cdbf9.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/data-management-badge-fd707527-515d-43e2-b9f6-f3eb3955a6f1.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/text-4-shell-badge-91cb20c0-b611-4ab5-8ecb-0fe9b738f49c.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/f5-1b290a5c-a5c4-437c-a762-4cb631405459.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/network-design-sec-pro-badge_1-2c7d09a8-4045-426e-8d73-7ff0a2132c6d.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/saml-badge-4b5d641e-db84-4522-b614-b13f1058ece3.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/hunting-rem0te-badge-a56b1bdf-b444-4494-a47c-6808d639ec60.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/win-disk-badge-de7df726-2db4-4756-99a8-e80d84748108.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/linux-sec-badge-bc6fe6b1-a17d-4494-b18c-04971fbcaa2f.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/badge-Deserialization-ee50e5df-2b65-4392-896f-96b06ad54351.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/into-net-badge-179688a8-c738-4642-9619-4e1e1d636ec7.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/intro-system-sec-badge-ec02de20-ecd3-42df-85fc-8097db2bbb90.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/spring4shell-badge-be457284-cf8a-4638-b5b2-9cb9658859f1.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/system-sec-2-badge-8249c18b-f669-4bc9-a19a-dd3fe1a9490e.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/auth-autz-badge-3fa9d6cf-38c3-463a-bfbb-550ed1117378.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/password-management-badge-446b8385-4401-4220-8263-b4d8ccd28259.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/win-system-sec-badge_1-35fe12f1-8c16-4ba9-bc2d-1cb6ef75592f.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/win-2-sec-badge-dadf79b1-1472-480c-9657-c8965c0444d4.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/adv-linux-sec-538429c0-a9b8-4ac6-8614-b3c572dfb9b4.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/bash-1-badge-1521c4e1-958e-44ed-b8fa-f7b483484a2e.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/adv-bash-badge-6176a662-94a9-495f-a1ae-ee14c92aa5a1.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/bash-3-badge-e559e40a-f2b6-40d7-b40b-c3695cd96d73.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/powershell-1-badge-3b64f20a-33a7-4555-bb3d-72907fc34654.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/ps2-badge-4c56119c-e693-443f-9daa-7cb4c3937e04.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/ps3-badge-906df856-9032-4d3f-b7f1-7794dd81bd86.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/py-badge-39b360a9-3efd-4951-a74b-7e62017462d8.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/py2-badge-eb4d6107-10ee-4c25-b613-53f688a13901.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/edr-1-badge-9c1eaf19-77bd-4bd2-abbd-949685bc536d.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/edr-badge-db648508-b879-4265-9623-2a27c6681200.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/edr-3-badge-feb7c400-f591-4693-8e8e-cf90d7aa81e8.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/asm-badge-2f9dd434-78c1-49b5-a61d-e613e339a29f.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/cti-badge-c7292e3a-422c-467f-92af-afdeb4dd0a5a.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/vm-badge-416454f1-7012-4c17-96c3-afa50d346ace.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/siem-1-badge-51cadef0-b1a3-49d9-a611-2d1aadecbfb5.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/siem2-badge-c8258d4a-5f79-474a-9d45-c3bdbdee6312.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/siem4-badge-d71a3c09-e995-42e2-a79e-63626e73b46f.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/siem5-badge-3d0ca776-8928-4734-b919-4d9ed6451da1.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/soar-1-badge-8bc0cbaa-bbc6-473a-8b8e-dcca5c182385.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/soar-2-badge-ee6f9fe1-ba99-42c6-bd5e-21882e1fb356.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/soar-3-badge-e01ba647-6206-4cef-af73-6ef822a36b9e.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/siem3-badge-6fd24563-7f70-4e7b-861d-c278c628fb0a.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/1-sysmon-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/org-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/s3-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Confluence-badge+(1).png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/aws-waf-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/usb-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/google-logging-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/guardduty-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/aws-vpc-badge-v2.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/rita-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/infosec-badge-1.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/cloudtrail-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/gcp-armor-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/risk-managemen-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/aws-incident-manager-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/adv-event-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/aws-iam-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/audit-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/linux-mem-badge+(1).png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/sys-hard-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/win-mem-badge-1.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://ld-images-2.s3.us-east-2.amazonaws.com/Network+Forensics/net-for-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/crime-badge+(1).png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/anti-for-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/crypto-algo-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/dfir-win-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/guide-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/email-for-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/how-to-siem-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/aws-shield-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/adv-win-for-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/business-man-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/dfir-w-edr-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/asset-man-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/dfir-on-linux-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/identity-course-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/adv-linux-for-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/next-it-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/android-for-course-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/sdlc-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/hard-disks-file-system-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/understanding-malware-badge+(1).png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/1-ios-for-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/win-data-acq-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/before-dfir-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/reversing-malware-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/aws-forensics-badge-dfir.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/macos-forensics-course-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/google-cloud-forensics-course-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/azure-forensics-course-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/linux-data-acq-badge-course.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/mastering-yara-malware-detec-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/data-recovery-course-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/static-code-analysis-course-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/intro-tn-course-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/dynamic-code-analysis-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/threat-hunting-tools-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/anti-analysis-malware-course-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/understanding-malwar-ebadge-comp.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/th-with-siem-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Threat+Hunting+with+Deception-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Identifying+Threats+and+Malicious+Software-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/th-with-edr-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/hardening-sec-plus-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/th-with-cti-course-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/host-based-sec-course-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/RDP+Lateral+Movement+Detection-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/wireless-security-course-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Threat+Hunting+with+Firewalls-course-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Application+Security+for+Security%2B.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Public+Key+Infrastructure-course-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Introduction+to+IDA-course-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Virtualization+and+Cloud+Security-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Threat+Hunting+with+IPSIDS-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Monitoring+and+Auditing-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Threat+Hunting+with+WAF-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Cabling+and+Connectors-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Threat+Hunting+with+Email+Security-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Ethernet+Basics-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Threat+Hunting+with+DNS-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Ethernet+Improvements-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Introduction+to+Security%2B-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/NICs+and+Physical+Network+Cabling-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Threat+Hunting+for+Email-Based+Attacks-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Routing+Protocols+and+NAT-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Threat+Hunting+for+Ransomware+Attacks-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Domain+Name+System+Fundamentals-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Threat+Hunting+for+Web+Attacks-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Securing+TCPIP-course-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Threat+Hunting+for+Network-Based+Attacks-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Switches+and+VLANS-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Threat+Hunting+for+Privilege+Escalation-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/ipv6-course-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Threat+Hunting+for+Data+Exfiltration+Attacks-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Wide+Area++Networks+(WAN)-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Threat+Hunting+for+Password-Based+Attacks-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Wireless+Networking-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Threat+Hunting+for+Insider+Threats-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Introduction+to+MalwareBazaar-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Threat+Hunting+for+DNS+Tunneling+Activities-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Malware+Obfuscation+Techniques-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Exploring+the+Cyber+Threat+Landscape-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Threat+Intelligence+for+SOC+Managers-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Digital+Forensics+with+EricZimmerman+Suite-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Threat+Intelligence+Feeds+and+Platforms-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Threat+Intelligence+Reports-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Introduction+to+Network%2B-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Digital+Footprint+Assessment+for+SOC+Managers-badge+(1).png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Security+Product+Selection-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/soc-degisgn-couse-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Emerging+Trends+in+Cybersecurity-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Technology+Roadmapping-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/SOC+Strategy-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/SOC+Team+Management-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Alternative+Staffing+Models-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/SOC+Contingency+Planning-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/conti-avatar-7117e377-408a-4a9f-8a96-30d3f2aa8aab.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/macro-avatar-c623f123-0366-4a8e-87b8-45a48fee4396.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/web-log-avatar-40f2e906-2189-4286-80dc-4c52e0a24a50.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/icedid-48f42ad2-6735-46fe-9689-1ad0384fa6bd.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/cobalt-strike-avatar-b6d2ed51-ccfa-4e28-8109-dd283adc7b4f.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/mshtml-avatar-3af3f470-746d-4fff-aa41-365e25f48cc2.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/malicious-doc-avatar-cf10b106-7871-46c1-ae1c-2bc282af9e8c.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/vba-malware-1b95b130-9278-4514-a58c-17ac727b1cbb.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/port-scan-avatar-cdb607b2-2015-4d74-8136-b1aec1b6d626.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/ppt-avatar-63069694-bfd5-42d8-ab3a-793d4bd301ff.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/printnightmare-e1def599-d575-4bd6-9ddb-4fc83fab125b.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/revil-badge-7af381d1-27a0-4db4-a904-4410c11b5aad.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/ransom-avatar-7c85a027-84e6-4159-ad88-2eff1f8fb79f.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/red-team-tools-1-c425a3a5-9e90-49ec-99dd-a72985231772.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/xls-file-avatar-7e3a13d1-21ad-4593-a825-c62434dcd932.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/shellshock-avatar_qzcN1wq-39412660-46cb-403b-9800-06d703b665d1.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/web-avatar-53ef2563-358c-4534-a0e1-a3c220a9f6ac.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/ram-avatar-35637289-b5d6-491d-a82e-9262322b3984.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/win-forensics-avatar-73438550-4c38-4930-9b8f-a82665a9da4f.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/email-analysis-badge-7f969987-4816-4671-a8f6-9d0617e8d66b.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/qakbot-badge-214505c5-de94-483b-b261-9451cc027c5d.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/wanna-cry-badge-avatar-1a1764e3-5346-41fc-aa6a-e272d850fb85.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/blue-stealer-badge-avatar-52ba1267-0cf0-4480-93cc-62b7807c8d17.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/randev-badge-0b0835d2-98f7-4b2f-b828-6468a8496edb.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/lock-bit-d205ee49-635e-448b-907b-a79afce75d57.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/linux-forensics-badge-avatar-989ded13-7b90-4191-8a96-5e6e440270b3.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/ransom-reverse_1-4967e1e6-c038-4706-9b7d-ce0c8f8056fc.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/anti-analysis-badge-9181d817-8ef6-400d-89d8-5b7ea73ae53d.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/Kimsuky-badge-e806611a-2c89-4e4f-a501-15a7f8612caa.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/Badges_2-a2e01e50-3a7c-4c3d-b7fb-2b1aeaf5a3e5.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/adobe-rce-badge-92dc6b21-53ef-47ec-8249-e2503a5eefba.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/winrar-badge-195342f2-47f8-4e3f-ae57-b7e3331c38a9.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/powershell-badge-1d980dc9-db1e-4c32-8067-3fa9e7976aa4.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/python-stealert-badge-caf977af-e701-491b-bf97-c0199d9655ee.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/royal-badge-25828bd3-9854-4538-b7e3-6c040a5f3335.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/cl0p-badge-cd57e4d2-ed0d-4a40-8e45-c6f24ca94883.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/rapid-badge-fadd8ddf-8a59-4420-8131-923793a47772.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/google-badge_1-8c4bead6-f60c-4f30-8c5a-aacddf42f884.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/lin-disk-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/backstore-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/cl0p-malw-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/win-memory-dmp-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Agniane+Stealer-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/chrome-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/conf-badge-cve.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/pcap-analysis-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/astasia-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/pdfuri-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/challenge/Stegano-badge+(1).png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/serpent-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/ads-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/challenge/dll-stealer-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/linux-mem-badge-challenge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/yara-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/cpp-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/wp-plugin-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/obf-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/php-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/ics-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/tv-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/batch-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/bf-challenge-badge+(1).png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/rev-rat-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/mal-web-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/downloader-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/printer-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/sysmon-challenge-badge+(1).png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/autoit-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/chat-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/bash-challange-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/sus-py-package-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Upstyle-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/kernel-exp-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/java-shellcode-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/browser-exp-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/windows-theme-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/nuget-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/linux-downloader-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/ios-forensics-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/obfuscated-hta-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/ai-cluster-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/ntfs-forensics-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/risen-ransom-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/windows-registry-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/obs-javascript-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/biotech-ransom-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/th-splunk-badge-challenge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/procdump-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/spicerat-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/velociraptor-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/heartbeat-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/poseidon-macos-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Spymax+Telegram+Rat-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/mac-forensics-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Android+Infostealer-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Android+Forensics-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/PowerShell+Keylogger-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Mandrake+Spyware-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/bingomod-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/RDP+Bitmap+Cache-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Wordpress+Web+Forensics-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Kerberoasting-challenge-badge+(1).png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Interlock+Ransomware-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/NTLM+Relay-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/LDAP+Enumeration-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/golden-ticket-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/AS-REP+Challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Helldown+Ransomware-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/ICS+FuelStation-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/MemLoot-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/octorat-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Silent+Update-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Remote+Access+Regret-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Koredos-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Shadow+of+LiteLLM-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Silent+Drain-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Odyssey+Stealer-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Phantom+Validation-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Apple+Rot-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/drone-forensics-challenge-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/ShadowDrop+Loader-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Orbit+Breach-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Stagecomp-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Support+Bot-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/lionv1_pk4WuxR-1d840a1a-5d5a-4440-8faf-3a55cf7b5f30.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/lionv2-b0ec839b-6a93-424f-8e2e-aa1d42a8eb23.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/hunter-mascot-aada9c5f-ca0a-455e-9cb3-f5b105661ca8.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/hunter-2-mascot-a5a201a0-24c1-485f-ad08-0d0dca6e62e6.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/non-stop-mascot-727838bb-f046-46ff-9d94-54866aba202b.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/student-badge-34f9d1de-f4a6-410d-832b-8a2cac5621e8.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/soc-path-badge-0c3ad9ef-2788-44cd-bfe5-7a8be230526f.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/ir-path-badge-2efa4ec6-6363-40c5-ab31-6b7d21fe65f9.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/malware-skill-badge-4fcebb5f-8392-4925-a83b-e8c21370a693.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/detection-badge-4e9898d0-84c0-44bf-9f8f-e441b105d46c.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/cysa-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/google-cert-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/coding-path-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/aws-sec-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/siem-eng-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/dfir-path-badge+(1).png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/infosec-path-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/career-switch-path-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/web-detection-path-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/comptia-security%2B-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Threat+Hunting+Learning+Path-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/CompTIA+Network%2B+Preparation+Path-badge.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/streak-badge-04b846d9-a8fd-4999-afbe-dca38a4e82bc.png"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app.letsdefend.io/_next/image?url=https%3A%2F%2Fld-app-images.s3.us-east-2.amazonaws.com%2FGeneral%2Ffooter-qr.png&w=256&q=75"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://apps.apple.com/us/app/letsdefend/id6741323626?ref=letsdefend",
    "img": "https://app.letsdefend.io/images/appstore.svg"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://play.google.com/store/apps/details?id=com.letsdefend.app&referrer=letsdefend",
    "img": "https://app.letsdefend.io/images/googleplay.svg"
  },
  {
    "title": "LetsDefend Badge",
    "url": "https://app.letsdefend.io/my-rewards",
    "img": "https://app.letsdefend.io/images/footer_sub.svg"
  }
]


# deduplicate
unique_data = []
seen_imgs = set()
for d in data:
    if d['img'] not in seen_imgs:
        seen_imgs.add(d['img'])
        unique_data.append(d)

data = unique_data

html_tags = []
for item in data:
    img = item['img']
    # Skip noisy/unrelated images
    if any(x in img for x in ['hb_logo', 'appstore', 'googleplay', 'footer', 'streak', '_next', 'default']):
        continue
        
    filename = img.split('/')[-1].split('?')[0].lower()
    
    # Skip paths
    if 'path' in filename or 'path' in item['title'].lower():
        continue

    # Clean name
    name = filename.replace('.png', '').replace('.svg', '').replace('%2b', '+')
    
    # Extract UUID to clean it from the name
    uuid_match = re.search(r'([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})', img)
    if uuid_match:
        name = name.replace(uuid_match.group(1), '')

    url = item.get('url', 'https://app.letsdefend.io/user/nvimq')
    
    # If the URL from JSON is just the generic my-rewards, 
    # fallback to public profile to avoid confusion, 
    # unless it explicitly has a detail UUID inside it.
    if url.endswith('/my-rewards') or url == 'https://app.letsdefend.io/homepage':
        url = 'https://app.letsdefend.io/user/nvimq'

    # Remove extra words from name
    words_to_remove = ['badge', 'avatar', 'challenge', 'mascot', 'course', 'example', 'sample']
    for w in words_to_remove:
        name = name.replace(w, '')
        
    name = name.replace('-', ' ').replace('+', ' ').replace('_', ' ').strip()
    name = ' '.join(name.split()) # compress multiple spaces
    
    # Specific exceptions/overrides
    if 'cve' in filename: name = "CVE"
    if 'cysa' in filename: name = "CySA+"
    if 'security' in filename: name = "Security+"
    if 'siem' in filename: name = "SIEM"
    if 'dfir' in filename: name = "DFIR"
    if 'soc' in filename: name = "SOC"
    if 'yara' in filename: name = "YARA"
    if 'mac' in filename: name = "macOS"
    if 'win' in filename: name = "Windows"
    if 'aws' in filename: name = "AWS"
    if 'linux' in filename: name = "Linux"
    if 'pcap' in filename: name = "PCAP"
    
    name = name.strip(' -_')
    if not name: name = "LetsDefend"
    name = name.title()
    
    # Fix casing for specific words
    replaces = {
        "Cysa": "CySA+", "Siem": "SIEM", "Dfir": "DFIR", "Soc": "SOC",
        "Yara": "YARA", "Aws": "AWS", "Pcap": "PCAP", "Macos": "macOS",
        "It Sec": "IT Sec", "Win101": "Windows 101"
    }
    for k, v in replaces.items():
        if name == k or name.startswith(k + " "):
            name = name.replace(k, v)
            
    if len(name) > 22:
        name = name[:19] + "..."
        
    html_tags.append(f'          <a class="orbit-tag" href="{url}" target="_blank">\n            <img src="{img}">{name}\n          </a>')

html_content = '''    <div class="zone-right">
      <div class="orbit-section" style="max-height: 800px; overflow-y: auto;">
        <div class="orbit-label"><span>//</span> letsdefend</div>
        <div class="orbit-tags">
''' + "\n".join(html_tags) + '''
        </div>
      </div>
    </div>'''

with open('index.html', 'r') as f:
    content = f.read()

# We need to find the SECOND <div class="zone-right">
first_idx = content.find('<div class="zone-right">')
start_idx = content.find('<div class="zone-right">', first_idx + 1)
end_idx = content.find('</div>\n  </div>\n</section>', start_idx)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + html_content + "\n" + content[end_idx:]
    with open('index.html', 'w') as f:
        f.write(new_content)
    print(f"Successfully replaced. Total unique non-path badges: {len(html_tags)}")
else:
    print("Could not find replacement bounds")
