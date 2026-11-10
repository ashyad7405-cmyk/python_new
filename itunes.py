import sys

try:
    import requests
except ImportError:
    print("Missing dependency: 'requests'. Install with: pip install requests")
    sys.exit(1)

from urllib.parse import quote_plus


def main():
    if len(sys.argv) != 2:
        print("Usage: python itunes.py <search term>")
        print("Example: python itunes.py \"Beatles\"")
        return

    term = quote_plus(sys.argv[1])
    url = f"https://itunes.apple.com/search?entity=song&limit=50&term={term}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Request failed:", e)
        return

    try:
        o = response.json()
    except ValueError:
        print("Failed to parse JSON response")
        return

    results = o.get("results", [])
    if not results:
        print("No results found.")
        return

    for result in results:
        # iTunes API uses 'trackName' (case-sensitive)
        name = result.get("trackName") or result.get("collectionName") or "(unknown)"
        print(name)


if __name__ == "__main__":
    main()