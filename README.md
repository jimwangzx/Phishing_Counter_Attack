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
* Unfortunately this script fails due to the host blocking requests from your ip address after 11 consecutive attempts

request_spammer.py
------------------
Sends post requests with fake credentials generated from various wordlists
in order to poison the malicious actors stolen data pool.

1. The API endpoint was found through inspecting the network traffic in a web browser while submitting fake data.
2. Postman was used to construct/verify identical POST request headers and payload.
3. Once a valid POST request was confirmed, a quick python script was written to spam the malicious actors API with fake credentials.
* This method of attack was a success! Not only was their data pool tainted with hundreds of thousands of fake credentials,
  the massive amount of requests resulted in a Denial of Service by using up all the endpoint servers bandwidth and shutting it down..for now.
  
  ![Fake_Endpoint](https://raw.githubusercontent.com/chparmley/Phishing_Counter_Attack/main/site_pics/endpoint.png)

Usage
-----
1. Clone this repo:  
`git clone https://github.com/chparmley/Phishing_Counter_Attack.git`  
2. Extract ./Diaz/wordlist/rockyou.zip  
3. Open terminal inside the Phishing_Couter_Attack folder and run with:  
`python3 request_spammer.py`
