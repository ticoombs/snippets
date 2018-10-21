## Find all emails grouped by from address

```
$DATE="Oct  1"
$LOG="/var/log/mail.log"
egrep "$DATE.*queue\ active" $LOG | grep -o from=.\*\, | awk -F, '{print $1}' | sort | uniq -c | sort -n
```
