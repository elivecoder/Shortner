import string
import random

# Storage for URL mappings
url_database = {}

# Domain for the short URL
BASE_URL = "http://short.ly/"

def generate_short_code(length=6):
    """Generates a random short code"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def shorten_url(long_url):
    """Shortens a given long URL"""
    short_code = generate_short_code()
    
    # Ensure uniqueness
    while short_code in url_database:
        short_code = generate_short_code()

    url_database[short_code] = long_url
    return BASE_URL + short_code

def expand_url(short_url):
    """Expands a shortened URL back to the original"""
    short_code = short_url.replace(BASE_URL, "")
    return url_database.get(short_code, "URL not found.")

def main():
    print("🔗 URL Shortener")
    while True:
        print("\n1. Shorten URL\n2. Expand URL\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            long_url = input("Enter the long URL: ")
            short_url = shorten_url(long_url)
            print(f"Shortened URL: {short_url}")

        elif choice == '2':
            short_url = input("Enter the short URL: ")
            original_url = expand_url(short_url)
            print(f"Original URL: {original_url}")

        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the script
if __name__ == "__main__":
    main()

