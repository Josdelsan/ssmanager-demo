#!/bin/bash

url="$1"
service_id="$2"
priv_key="$3"

output=$(curl --location --request POST "$url" --form "priv_key=$(printf "%q" "$priv_key")" --form "service_id=$(printf "%q" "$service_id")")

input="$output"

output=$(echo "$input" | jq -r '.secrets[] | "\(.name)=\(.value)"' | awk -F '=' '{print $1 "=" $2}')

script_dir=$(dirname "$0")

echo "$output" > "$script_dir/.env"

exit 0