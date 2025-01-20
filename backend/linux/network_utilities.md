# Table of contents 
- [Table of contents](#table-of-contents)
- [Network Utilities](#network-utilities)
  - [Interacting with Files Hosted Online](#interacting-with-files-hosted-online)
  - [Checking Network Connectivity](#checking-network-connectivity)
  - [DNS Resolution](#dns-resolution)
  - [Network Interface Status](#network-interface-status)

# Network Utilities 
The linux shell makes it easy to communicate with content on the internet from the command line, and for the user to check on important network status information. 

## Interacting with Files Hosted Online

How to access files from the internet in the command line? Usin `curl` or `wget`. 

Either command lets us establish a connection with a server. For example: 

```bash 
curl "exampleurl.com"
```

This command display the contents of the file at the url in terminal 

The option -O or --output combined with a desired name will write the contents of the online file to the filename 

```bash 
curl "exampleurl" --output filename 
```

Or 

```bash 
curl -O "exampleurl"
```

## Checking Network Connectivity 
How can we check whether two devices connected to the same network can communicate with one another? we use `ping`. 

```bash 
ping [options] domain_or_ip
```

This command sends packets to the target host and waits for replies. If the ping command returns with a failure, that means the target is unreachable. 


## DNS Resolution 
What if we wanted to find out the IP address for any given domain name or vice versa? This process is known as **DNS lookup or DNS resolution** and the `host` command lets us do that. 

The syntax is: 
```bash 
host domain_or_ip
```

This will display information about the specified domain.


## Network Interface Status
The `ifconfig` command or interface configurator is one of the network inspection commands available on Linux. Running it will display IP addresses, MAC addresses, and some more relevant details. 

```bash
ifconfig
```