import requests

def purge_cache(zone_id, api_key):
    headers = {
        "X-Auth-Email": "<YOUR-CLOUDFLARE-EMAIL>",
        "X-Auth-Key": api_key,
        "Content-Type": "application/json",
    }

    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache"

    data = {"purge_everything": True}

    response = requests.delete(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Cache purged successfully")
    else:
        print("Failed to purge cache")

# Example usage
purge_cache("<ZONE-ID>", "<YOUR-API-KEY>")
