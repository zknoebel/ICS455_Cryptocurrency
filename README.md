# ICS455_Cryptocurrency
This repository is for the final project for ICS455 at the University of Hawaii at Manoa.

##Block Chain
The block chain will be stored in json format.

####example block
```
{
    "index" : 1,
    "timestamp" : 1506057125.900785,
    "transactions" : [
        ...
    ],
    "proof" : 324984774000,
    "previous_hash" : "2cf24dba5fb0a30e26e83b2ac5b9e29"
}
```

####example transaction
```
{
    "sender" : "MIICWwIBAAKBgHztyBDR5al" ,
    "receiver" : "wvfYvNSFAwOFVV4B3o1kxsSY" ,
    "amount" : 100,
    "signature" : "2cf24dba5fb0a30e26e83b2ac5b9e29"
}
```
