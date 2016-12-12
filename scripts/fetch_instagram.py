#!/usr/bin/env python3
"""Fetch picture dump from any API."""

import requests
import json

# Globals
URL = "https://www.instagram.com/explore/tags/konzertparty2016/?__a=1"
# Global operators
op_result_table = op("url_in")


def offToOn(channel, sampleIndex, val, prev):
    """Listen 1 to 0 value change."""
    fetch_api(URL)
    return


# TODO:
# + Implement pic dumping to fs
# + Implement additional APIs (facebook, twitter)
def fetch_api(url):
    """Perform API request."""
    if url is not None and url is not "":
        response = requests.get(url)
        print("RESPONSE:")
        print("Status: %s" % response.status_code)
        op_result_table.clear()
        json_data = response.json()
        nodes = json_data["tag"]["media"]["nodes"]
        for i in nodes:
            image = i["display_src"]
            op_result_table.appendRow(image)
        return
