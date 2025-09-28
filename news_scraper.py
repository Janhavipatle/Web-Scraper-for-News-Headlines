import requests
from bs4 import BeautifulSoup

# Step 1: Website choose karo
URL = "https://www.bbc.com/news"

# Step 2: Website ka HTML fetch karo
response = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})
html = response.text

# Step 3: HTML parse karo
soup = BeautifulSoup(html, "html.parser")

# Step 4: Headlines nikaalo (BBC me <h2> tags me hote hain)
headlines = soup.find_all("h2")

# Step 5: File me save karo
with open("headlines.txt", "w", encoding="utf-8") as f:
    for i, h in enumerate(headlines, start=1):
        text = h.get_text(strip=True)
        if text:
            f.write(f"{i}. {text}\n")

print("✅ Headlines headlines.txt file me save ho gayi!")
