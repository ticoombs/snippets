# If a site is hit over 1000 times to wp-login, find all occurances against that site.
# Sort & uniq all IPs. If there is over *200 tries total* against our server, ban them. 

One Liner:
```
for file in /var/log/nginx/*access.log ; do amount=$(grep wp-login.php $file | wc -l); [[ "$amount" -gt "1000" ]] && grep wp-login.php $file | awk '{print $1}'; done | sort | uniq -c | sort -n | grep -E ^\ \ \ \ [2-9][0-9][0-9] | awk '{print $2}' | while read ip; do sudo fail2ban-client set recidive banip $ip; done
```

"Pretty"
```
for file in /var/log/nginx/*access.log ; do 
    amount=$(grep wp-login.php $file | wc -l); 
    [[ "$amount" -gt "1000" ]] && grep wp-login.php $file | awk '{print $1}'; 
done | \
    sort | uniq -c | sort -n | grep -E ^\ \ \ \ [2-9][0-9][0-9] | awk '{print $2}' | \
    while read ip; do 
      sudo fail2ban-client set recidive banip $ip; 
    done
```
