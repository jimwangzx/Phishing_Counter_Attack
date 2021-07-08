# API_Poisoning
This repository contains data collection against an attempted phising attack.
-----------------------------------------------------------------------------

**urls** directory contains a file noting the different urls attempted to use to trick users into submitting
their data.

**list** directory contains an xml payload used by the curl_brute_force.sh script

**recon** directory contains data from various scans, site directories, port data, etc..

curl_brute_force.sh
-------------------
Bombards the phising xml endpoint with a curl request in attempts
to brute force the login credentials.

request_spammer.py
------------------
Sends post requests with fake credentials generated from various wordlists
in order to poison the malicious actors stolen data pool.

1. The API endpoint was found through inspecting the network traffic in a web browser when submitting fake data.
2. From there Postman was used to construct identical POST request headers and payload.
3. Once a valid POST request was confirmed. A quick python script was written to spam the malicious actors API
