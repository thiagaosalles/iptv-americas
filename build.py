import urllib.request
from pathlib import Path

SOURCES = {
    'Brasil': 'https://iptv-org.github.io/iptv/countries/br.m3u',
    'USA': 'https://iptv-org.github.io/iptv/countries/us.m3u',
    'Canada': 'https://iptv-org.github.io/iptv/countries/ca.m3u',
}

def entries(text):
    lines = [line.strip() for line in text.splitlines()]
    for i, line in enumerate(lines):
        if line.startswith('#EXTINF:'):
            j = i + 1
            extras = []
            while j < len(lines) and lines[j].startswith('#'):
                extras.append(lines[j]); j += 1
            if j < len(lines) and lines[j].startswith(('https://', 'http://')):
                yield line, extras, lines[j]

def main():
    result = ['#EXTM3U']
    seen = set()
    for country, url in SOURCES.items():
        try:
            request = urllib.request.Request(url, headers={'User-Agent':'IPTV-Americas/0.1'})
            with urllib.request.urlopen(request, timeout=25) as response:
                content = response.read().decode('utf-8-sig', errors='replace')
        except Exception as error:
            print(f'Could not fetch {country}: {error}')
            continue
        count = 0
        for meta, extras, stream in entries(content):
            if stream in seen:
                continue
            seen.add(stream)
            # Preserve original channel metadata and group labels from upstream.
            result.extend([meta, *extras, stream])
            count += 1
        print(f'{country}: {count} unique streams')
    if len(result) == 1:
        raise SystemExit('No sources fetched; refusing to overwrite output')
    Path('BR_US_CA.m3u').write_text('\n'.join(result) + '\n', encoding='utf-8')
    print(f'Wrote {len(seen)} streams')

if __name__ == '__main__':
    main()
