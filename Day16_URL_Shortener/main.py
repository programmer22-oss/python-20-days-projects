import random
import string

url_map = {}

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def shorten_url(long_url):
    short_code = generate_short_code()
    url_map[short_code] = long_url
    return short_code

def open_url(code):
    return url_map.get(code, "❌ URL not found")

while True:
    print("\n🔗 URL Shortener Menu")
    print("1. Shorten URL")
    print("2. Open URL")
    print("3. View All URLs")
    print("4. Exit")

    choice = input("Choose option (1-4): ")

    if choice == "1":
        long_url = input("Enter long URL: ")
        code = shorten_url(long_url)
        print(f"✅ Short URL code: {code}")

    elif choice == "2":
        code = input("Enter short code: ")
        print("🌐 Long URL:", open_url(code))

    elif choice == "3":
        if not url_map:
            print("No URLs shortened yet.")
        else:
            for code, url in url_map.items():
                print(f"{code} → {url}")

    elif choice == "4":
        print("👋 Exiting URL Shortener")
        break

    else:
        print("⚠️ Invalid choice")
    
    
