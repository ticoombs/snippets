# Gets Requests/min and sorts by smallest to biggest
zgrep "01/Jan" *.log | cut -d[ -f2 | cut -d] -f1 | awk -F: '{print $2":"$3}' | sort -n | uniq -c | sort -n

# Gets Requests/Hour of that day
zgrep "01/Jan" *.log | cut -d[ -f2 | cut -d] -f1 | awk -F: '{print $2":00"}' | sort -n | uniq -c 
