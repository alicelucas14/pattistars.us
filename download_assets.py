import urllib.request
import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# find all asset paths
urls = re.findall(r'(?:src|href|content)=["\'](/images/[^"\'>\s]+|/uploads/[^"\'>\s]+)["\']', html)
urls += re.findall(r'url\(["\']?(/images/[^"\'>\s\)]+|/uploads/[^"\'>\s\)]+)["\']?\)', html)
# also look for any relative .webp, .png, .jpg, .svg, .mov, .mp4
urls += re.findall(r'["\'](/[^"\'>\s]+\.(?:png|jpg|jpeg|webp|svg|gif|mov|mp4|ico))["\']', html)
urls = sorted(list(set(urls)))

print('Found assets:', len(urls))
for u in urls:
    print(' -', u)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

for path in urls:
    full_url = 'https://teenpattistars.io' + path
    local_path = path.lstrip('/')
    dir_name = os.path.dirname(local_path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    try:
        req = urllib.request.Request(full_url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = resp.read()
        with open(local_path, 'wb') as f:
            f.write(data)
        print(f'Downloaded: {path} ({len(data)} bytes)')
    except Exception as e:
        print(f'Failed {path}: {e}')
