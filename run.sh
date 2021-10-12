#!/bin/bash

cd doe_sangue || exit

JUMPLINE=""

mapfile -t spiders < <(scrapy list)

echo "================= STARTING SCRAPING ================="

for i in "${spiders[@]}"; do
    echo "${JUMPLINE}"
    echo "Spider ${i}"
    echo "Crawling Spider ${i}..."
    scrapy crawl "${i}"
    echo "Spider ${i} finished scraping"
done
