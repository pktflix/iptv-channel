import requests

source_url = "https://iptv-org.github.io/iptv/categories/sports.m3u"
output_file = "bd-in-pk-sports.m3u"

# যেসব চ্যানেল রাখতে চান
allowed_channels = [
    "T Sports",
    "Gazi TV",
    "Sony Sports",
    "Star Sports",
    "beIN Sports News",
"beIN Sports 1",
"beIN Sports 2",
"beIN Sports 3",
"beIN Sports 4",
"beIN Sports 5",
"beIN Sports 6",
"beIN Sports 7",
"beIN Sports 8",
    "Ten Sports",
    "PTV Sports",
    "Willow",
    "DD Sports",
    "ARY ZAP",
    "Neo Sports",
    "Sports18"
]

def is_allowed(line):
    return any(channel.lower() in line.lower() for channel in allowed_channels)

def filter_m3u():
    response = requests.get(source_url)
    if response.status_code != 200:
        print("❌ Failed to fetch M3U")
        return

    lines = response.text.splitlines()
    filtered = []

    i = 0
    while i < len(lines):
        if lines[i].startswith("#EXTINF") and is_allowed(lines[i]):
            filtered.append(lines[i])
            if i + 1 < len(lines):
                filtered.append(lines[i + 1])  # Add stream URL
        i += 1

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(filtered))
    print("✅ Filtered M3U created successfully.")

if __name__ == "__main__":
    filter_m3u()
