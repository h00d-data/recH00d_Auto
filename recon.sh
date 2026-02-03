#!/bin/bash

DOMAINS=("$@")
TS=$(date +"%Y%m%d_%H%M%S")

source stealth.conf 2>/dev/null

mkdir -p output/{raw,resolved,data,reports}

random_sleep() {
  if [[ "$random_delay" == "true" ]]; then
    sleep $((RANDOM % max_delay + min_delay))
  fi
}

for DOMAIN in "${DOMAINS[@]}"; do
  echo "[+] Recon em $DOMAIN"

  RAW="output/raw/${DOMAIN}_$TS.txt"
  RES="output/resolved/${DOMAIN}_$TS.csv"

  assetfinder --subs-only $DOMAIN >> $RAW
  random_sleep
  subfinder -d $DOMAIN -silent >> $RAW
  random_sleep
  amass enum -passive -d $DOMAIN >> $RAW
  random_sleep
  findomain -t $DOMAIN -q >> $RAW

  sort -u $RAW > ${RAW}.uniq

  while read sub; do
    IP=$(dig +short $sub | head -n 1)
    if [[ ! -z "$IP" ]]; then
      echo "$DOMAIN,$sub,$IP,$TS" >> $RES
    fi
  done < ${RAW}.uniq
done

python3 db/ingest_mysql.py
python3 reports/report.py
