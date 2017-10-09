# Hits distribution on your amavis logs
`sudo zgrep -hoE Hits\:\ \(-\)?[0-9]\.[0-9]+\, /var/log/amavis.log* | cut -b7 | sort | uniq -c`
```  
 207188 -  
  17194 0  
   9679 1  
   6304 2  
   8601 3  
   9952 4  
  15203 5  
  16303 6  
  18252 7  
  15151 8  
   8870 9  
```
