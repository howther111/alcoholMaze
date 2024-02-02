# coding: UTF-8

import json
import random

import requests

def main():
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"

    api_id      = "1002559749369439117" # applicationIdを入力
    genreId     = "510901"
    out_format  = "json"
    min_price = "1000"
    max_price = "10000"
    hits = 30
    pagemax = 100
    page_rnd = str(random.randint(1, pagemax))

    first_response = requests.get(url, params = {
                                            "applicationId": api_id,
                                            "genreId"      : genreId,
                                            "format"       : out_format,
                                            "minPrice"    : min_price,
                                            "maxPrice"    : max_price,
                                            "hits"        : str(hits),
                                            "page"        : page_rnd
                                          }).json()

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(first_response, f, indent=4, ensure_ascii=False)

    #print(first_response["count"])
    hitsminus = hits - 1
    item_num = random.randint(0, hitsminus)
    choice_item = first_response["Items"][item_num]
    print(choice_item["Item"]["itemName"])
    print(choice_item["Item"]["itemCaption"])
    print("価格:" + str(choice_item["Item"]["itemPrice"]) + "円")
    print("商品画像:" + choice_item["Item"]["mediumImageUrls"][0]["imageUrl"])

if __name__ == "__main__":
    main()