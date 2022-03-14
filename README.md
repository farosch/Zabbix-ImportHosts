# Zabbix API Bulk CSV Import
   
## Installation

You will need to install `zabbix-api`, `progressbar` and `pip`:

`pip install zabbix-api`
`pip install lib`
`pip install progressbar`


## How to use - examples

>Structure of the CSV file:

```
hostname;ipaddress
hostname;ipaddress
hostname;ipaddress
hostname;ipaddress
hostname;ipaddress
Localhost;127.0.0.1
```

>Then run 

`python bulkimport.py`
