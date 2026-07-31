import json
import re

user_json_str = """[
  {
    "title": "Web Attack Investigator",
    "url": "https://app.letsdefend.io/my-rewards/detail/18803afa-8fa3-458e-a382-364b1de7f748",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/web-attacks-badge-2f7551ca-00ea-49e0-ae0c-a508c3c00552.png"
  },
  {
    "title": "Linux Fan",
    "url": "https://app.letsdefend.io/my-rewards/detail/82d6fe7a-4012-48ca-8b61-ef5dd6089e8a",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/badge-linux-101-01963665-e81b-45f9-aae0-f1a1b63392cb.png"
  },
  {
    "title": "Brute Force",
    "url": "https://app.letsdefend.io/my-rewards/detail/6c157f07-3efe-4e49-9c8b-cf8fdbc62fe5",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/brute-force-badge-48517643-fe50-4a92-b328-506c4208a6b1.png"
  },
  {
    "title": "Web Server Analyzer",
    "url": "https://app.letsdefend.io/my-rewards/detail/a2715868-c227-4da6-b4c0-bfb2dc4e00c1",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/hacked-analysis-badge-avatar-4c433f26-e83b-4e2a-8401-3fb32b1fa093.png"
  },
  {
    "title": "MITRE ATT&CK",
    "url": "https://app.letsdefend.io/my-rewards/detail/4e8c5258-9dbb-4579-a7af-baa76f480c63",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/mitre-badge-2-f8edfcce-62c1-4170-95cf-af5fd56562d0.png"
  },
  {
    "title": "Web Hunter",
    "url": "https://app.letsdefend.io/my-rewards/detail/c8bfcf77-dd9b-461c-b225-d479d7b01551",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/web-attacks-2-badge-5ab868c5-0140-4000-b386-f15e747614cf.png"
  },
  {
    "title": "Go Writer",
    "url": "https://app.letsdefend.io/my-rewards/detail/2b757cc6-1847-4078-8050-e7436a56ddd0",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/go-badge-avatar-f8a039ef-d328-49b1-89ad-2e2b4493cacc.png"
  },
  {
    "title": "Secure Network Designer",
    "url": "https://app.letsdefend.io/my-rewards/detail/f20a34c4-c220-4361-9490-55d413992012",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/secure-network-design-badge-8d746f5e-9ec2-4790-9227-f1c48207b21a.png"
  },
  {
    "title": "JWT Attacks and Detection",
    "url": "https://app.letsdefend.io/my-rewards/detail/fbb234b2-556f-40c0-85db-979215f32f2f",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/jwt-badge-38239eae-8bed-451b-911f-449144eafc7f.png"
  },
  {
    "title": "AWS CloudWatch",
    "url": "https://app.letsdefend.io/my-rewards/detail/56a1ee10-4e59-4464-9dd2-f5d8cc4173f8",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/aws-cloudwatch-badge.png"
  },
  {
    "title": "Physical Security",
    "url": "https://app.letsdefend.io/my-rewards/detail/853bd553-4d60-4752-b551-7252b911ad3e",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/physical-sec-badge.png"
  },
  {
    "title": "Red Team Hunter - 2",
    "url": "https://app.letsdefend.io/my-rewards/detail/5e3fb8a7-288b-4b4d-8c5a-7251bef11561",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/red-team-tools-2-858e0eea-5707-460d-b176-3912fdd86aa4.png"
  },
  {
    "title": "PDF Analyzer",
    "url": "https://app.letsdefend.io/my-rewards/detail/0726055f-bf06-497a-b6f0-f87708821244",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/pdf-avatar-9a8f2e62-86dd-4032-a2d5-90ef42f5b04a.png"
  },
  {
    "title": "Browser Extension Analyzer",
    "url": "https://app.letsdefend.io/my-rewards/detail/05a90ca0-4aa3-4a7b-8474-11f9b10fa4ad",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/suspicious-browser-extension-badge-cd7872ab-e178-4a1e-91ee-92eccd0cf809.png"
  },
  {
    "title": "Phishing Analyzer",
    "url": "https://app.letsdefend.io/my-rewards/detail/08923c86-d885-47ab-afe8-4c1fd91fe1e0",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/phishing-challenge-avatart_vQ1645S-19e4e4cb-4f19-45ef-bb63-01c5260c8547.png"
  },
  {
    "title": "AWS Responder",
    "url": "https://app.letsdefend.io/my-rewards/detail/5c2aff9c-45e1-48b3-abf9-b620e54b5f9a",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/aws-badge-b665787c-af28-4502-bf99-8d88dd146e90.png"
  },
  {
    "title": "AWS Incident Handler",
    "url": "https://app.letsdefend.io/my-rewards/detail/f81ee85b-afc8-43cf-80b1-bf7a102ffae1",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/aws-persestence-badge-c5c8649b-0c46-46fd-a78d-34b87f8833e5.png"
  },
  {
    "title": "Docker Forensics",
    "url": "https://app.letsdefend.io/my-rewards/detail/dd2691a6-f489-413c-8715-09cfbc0fb568",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/docker-badge-62df3f55-0589-4bb6-ba71-b344ceced720.png"
  },
  {
    "title": "macOS Malware",
    "url": "https://app.letsdefend.io/my-rewards/detail/b36770ac-0b58-49fd-a490-5603290c3caf",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/macos-malware-badge.png"
  },
  {
    "title": "Discord Forensics",
    "url": "https://app.letsdefend.io/my-rewards/detail/51f72b7f-b714-45b9-a434-c20533c6cc12",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/discord-badge.png"
  },
  {
    "title": "Golang Ransomware",
    "url": "https://app.letsdefend.io/my-rewards/detail/183d448f-a4aa-4703-8700-33dc415dec3f",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/go-ransom-badge.png"
  },
  {
    "title": "AWS Bucketware",
    "url": "https://app.letsdefend.io/my-rewards/detail/fa25e80e-f523-46c8-872a-0ceb06d8ee97",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/aws-bucketware-badge.png"
  },
  {
    "title": "AWS Stacked",
    "url": "https://app.letsdefend.io/my-rewards/detail/7a43febd-d543-4d2c-9a7b-16f778e6ca8d",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/aws-stacked-badge.png"
  },
  {
    "title": "VoIP",
    "url": "https://app.letsdefend.io/my-rewards/detail/b636a9e8-8fa4-4dc6-a9cf-a875877d4d42",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/voip-challenge-badge.png"
  },
  {
    "title": "USB Forensics",
    "url": "https://app.letsdefend.io/my-rewards/detail/dc19c44e-3f48-45aa-85c1-95e482aafa2b",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/usb-forensics-challenge-badge.png"
  },
  {
    "title": "TinyTurla Backdoor",
    "url": "https://app.letsdefend.io/my-rewards/detail/0601442e-6392-4fd2-b756-bd4d0a830866",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/TinyTurla+Backdoor-badge.png"
  },
  {
    "title": "Samba Spy",
    "url": "https://app.letsdefend.io/my-rewards/detail/602e042c-481a-46bb-849b-9694e1d482a1",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/samba-spy-badge.png"
  },
  {
    "title": "Mac Backdoor",
    "url": "https://app.letsdefend.io/my-rewards/detail/681cea81-e89f-4243-afc7-76c07f0dc678",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/mac+backdoor-challenge-badge.png"
  },
  {
    "title": "Hidden Backdoor",
    "url": "https://app.letsdefend.io/my-rewards/detail/60b652ed-5bb1-4a78-a387-3e126e1aa538",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Hidden+Backdoor-challenge-badge.png"
  },
  {
    "title": "Google Cloud Compromise",
    "url": "https://app.letsdefend.io/my-rewards/detail/e34cb954-5320-44a7-8ae2-3cc3428cdb31",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Google+Cloud+Compromise-badge.png"
  },
  {
    "title": "Promptlock Ransomware",
    "url": "https://app.letsdefend.io/my-rewards/detail/46da6361-1397-49d6-b65a-3274f697f3c1",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Promptlock+Ransomware-badge.png"
  },
  {
    "title": "Learn Sigma",
    "url": "https://app.letsdefend.io/my-rewards/detail/ae4ae87a-809c-46c6-8ee3-9a6afa62f167",
    "img": "https://app-ld-img.s3.us-east-2.amazonaws.com/badge/Learn+Sigma-challenge-badge.png"
  },
  {
    "title": "First Blood",
    "url": "https://app.letsdefend.io/my-rewards/detail/d6353f1a-eb02-4524-88e5-204e68eb346e",
    "img": "https://app-ld-img.s3.amazonaws.com/badge/first-badge-6529e305-65c7-41fe-a929-c728f1bee986.png"
  }
]"""

badges_data = json.loads(user_json_str)

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Generate new HTML tags
new_tags = []
for badge in badges_data:
    url = badge['url']
    img = badge['img']
    title = badge['title']
    
    tag = f'''          <a class="orbit-tag" href="{url}" target="_blank">
            <img src="{img}">{title}
          </a>'''
    new_tags.append(tag)

new_tags_html = '\n'.join(new_tags)

pattern = r'(<div class="orbit-label"><span>//</span> letsdefend</div>\s*<div class="orbit-tags">)[\s\S]*?(</div>\s*</div>\s*</div>\s*</div>\s*</section>)'

if re.search(pattern, content):
    content = re.sub(pattern, f"\\1\n{new_tags_html}\n\\2", content)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully replaced LetsDefend orbit tags. Total badges injected: {len(badges_data)}")
else:
    print("Could not find the target HTML section to replace.")
