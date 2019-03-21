# Simple script to modify your VPC ACL to block a list of subnets, such as... say a country?
## Assumptions:

You need to make sure you move your default ALLOW rule from the standard 100
to something like 10000. (Maximum number of 32766 as defined by [vpc-acl aws docs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)
As with standard firewalls they read top to bottom, so if you block a country, your allow is 100, 
and their list is 8000+ 

```
id=1; ACL=aclid; ACTION="deny"; list=your-list-of-subnets-one-per-line.txt;
while read block; do 
  aws ec2 create-network-acl-entry --cidr-block "$block" --ingress --network-acl-id "$ACL" --protocol -1 --rule-action $ACTION --rule-number $id; 
  echo "$ACTION: $BLOCK with id: $id"
  ((id++)); 
  sleep 1; 
done < $list
```
