# nslookup

```bash
$ nslookup www.mit.edu
Server:         127.0.1.1
Address:        127.0.1.1#53

Non-authoritative answer:
www.mit.edu     canonical name = www.mit.edu.edgekey.net.
www.mit.edu.edgekey.net canonical name = e9566.dscb.akamaiedge.net.
Name:   e9566.dscb.akamaiedge.net
Address: 23.2.132.180

$ nslookup -type=NS mit.edu
Server:         127.0.1.1
Address:        127.0.1.1#53

Non-authoritative answer:
mit.edu nameserver = use2.akam.net.
mit.edu nameserver = ns1-37.akam.net.
mit.edu nameserver = ns1-173.akam.net.
mit.edu nameserver = eur5.akam.net.
mit.edu nameserver = use5.akam.net.
mit.edu nameserver = usw2.akam.net.
mit.edu nameserver = asia1.akam.net.
mit.edu nameserver = asia2.akam.net.

Authoritative answers can be found from:


$ nslookup www.mit.edu 8.8.8.8
Server:         8.8.8.8
Address:        8.8.8.8#53

Non-authoritative answer:
www.mit.edu     canonical name = www.mit.edu.edgekey.net.
www.mit.edu.edgekey.net canonical name = e9566.dscb.akamaiedge.net.
Name:   e9566.dscb.akamaiedge.net
Address: 184.26.244.21

$ nslookup www.aiit.or.kr 8.8.8.8
Server:         8.8.8.8
Address:        8.8.8.8#53

Non-authoritative answer:
Name:   www.aiit.or.kr
Address: 58.229.6.225
```

# Flush DNS cache in Ubuntu 16.04

```bash
$ sudo apt-get install nscd
$ sudo /etc/init.d/nscd restart
```
