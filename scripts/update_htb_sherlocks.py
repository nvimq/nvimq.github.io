#!/usr/bin/env python3
import json
import re
import sys
import os

# 1. Читаем JSON-файл с ответом от API HTB
json_file = "htb_sherlocks.json"
html_file = "../index.html" # Путь к index.html (скрипт лежит в папке scripts)

# Если запускаем из корня, путь к index.html будет просто "index.html"
if os.path.exists("index.html"):
    html_file = "index.html"

if not os.path.exists(json_file):
    print(f"❌ Файл {json_file} не найден!")
    print("👉 Как получить файл:")
    print("1. Зайди на HTB Sherlocks (https://labs.hackthebox.com/sherlocks)")
    print("2. Открой Network (Сеть) в DevTools браузера (F12)")
    print("3. Обнови страницу, найди запрос 'sherlocks' и скопируй весь ответ (Response)")
    print(f"4. Сохрани этот текст в файл {json_file} и запусти скрипт снова.")
    sys.exit(1)

with open(json_file, "r", encoding="utf-8") as f:
    htb_data = json.load(f)

sherlocks = htb_data.get("data", [])
# Если структура ответа немного другая (например, data.data)
if not isinstance(sherlocks, list) and "data" in sherlocks:
    sherlocks = sherlocks["data"]

# Фильтруем только те, что решены (прогресс 100% или owned)
solved_sherlocks = [s for s in sherlocks if s.get("progress") == 100 or s.get("is_owned") or s.get("authUserHasCompleted")]

if not solved_sherlocks:
    print("⚠️ Не найдено ни одного пройденного Шерлока в JSON.")
    sys.exit(1)

# Твой HTB User ID (нужен для генерации ссылок на ачивки)
HTB_USER_ID = "2541400"

html_tags = []
for item in solved_sherlocks:
    url = f"https://labs.hackthebox.com/achievement/sherlock/{HTB_USER_ID}/{item['id']}"
    # Генерируем HTML-тег для бейджа
    html_tags.append(f'          <a class="orbit-tag" href="{url}" target="_blank">\n            <img src="{item["avatar"]}">{item["name"]}\n          </a>')

replacement_html = '        <div class="orbit-tags">\n' + '\n'.join(html_tags) + '\n        </div>'

# 2. Обновляем index.html
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# Ищем блок htb solved и заменяем в нем <div class="orbit-tags">...</div>
pattern = r'(<div class="orbit-label"><span>//</span> htb solved</div>\s*)<div class="orbit-tags">.*?</div>'

if re.search(pattern, content, flags=re.DOTALL):
    new_content = re.sub(pattern, r'\1' + replacement_html, content, flags=re.DOTALL)
    
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"✅ Успешно обновлено! Добавлено {len(solved_sherlocks)} Шерлоков в {html_file}.")
else:
    print(f"❌ Не удалось найти блок '// htb solved' в {html_file}.")
    print("Проверь, что в HTML есть <div class=\"orbit-label\"><span>//</span> htb solved</div>")

