import requests
from requests.exceptions import RequestException
from datetime import datetime
from typing import List

GAMMA_ENDPOINT = "https://gamma-api.polymarket.com/markets"
CLOB_ENDPOINT = "https://clob.polymarket.com"


def fetch_markets(start_date_min: str) -> List[dict]:
    params = {
        "active": "true",
        "closed": "false",
        "archived": "false",
        "start_date_min": start_date_min,
    }
    try:
        resp = requests.get(GAMMA_ENDPOINT, params=params)
        resp.raise_for_status()
    except RequestException as exc:
        print(f"Failed to fetch markets: {exc}")
        return []
    return resp.json()


def fetch_tokens(condition_id: str) -> List[str]:
    url = f"{CLOB_ENDPOINT}/markets/{condition_id}"
    try:
        resp = requests.get(url)
        resp.raise_for_status()
    except RequestException:
        print(f"Market {condition_id} not found")
        return []
    market = resp.json().get("market", {})
    tokens = market.get("tokens", [])
    return [t.get("token_id") for t in tokens]


def fetch_prices(token_ids: List[str]) -> dict:
    params = {"params": [{"token_id": tid, "side": "BUY"} for tid in token_ids]}
    try:
        resp = requests.post(f"{CLOB_ENDPOINT}/prices", json=params)
        resp.raise_for_status()
    except RequestException as exc:
        print(f"Failed to fetch prices: {exc}")
        return {}
    return resp.json()


def main():
    start_date = "2025-06-27T00:00:00Z"
    markets = fetch_markets(start_date)
    if not markets:
        print("Keine passenden Märkte gefunden.")
        return

    print("Gefundene Märkte:")
    for m in markets:
        print(f"- {m['id']}: {m['slug']} (Start: {m['start_date']})")

    cont = input("Fortfahren und Preise abrufen? [j/N] ").strip().lower()
    if cont != "j":
        return

    all_tokens = []
    for m in markets:
        tokens = fetch_tokens(str(m["id"]))
        all_tokens.extend(tokens)

    prices = fetch_prices(all_tokens)
    print("Preise:")
    for asset, sides in prices.items():
        price = sides.get("BUY")
        print(f"Token {asset}: {price}")


if __name__ == "__main__":
    main()
