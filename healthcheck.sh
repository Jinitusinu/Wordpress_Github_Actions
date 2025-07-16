# healthcheck.sh
#!/bin/bash
url="http://localhost:8080"
for i in {1..15}; do
  status=$(curl -s -o /dev/null -w '%{http_code}' $url)
  if [ "$status" == "200" ]; then
    echo "Health OK: $url returned $status" > health.txt
    exit 0
  fi
  sleep 2
done
echo "Health failed" > health.txt
exit 1
