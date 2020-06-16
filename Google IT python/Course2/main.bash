#!/bin/bash
>errorFile.txt
>infoFile.txt
er_logs=$(grep -o "ERROR [a-zA-Z \(\)\. ' ]*" syslog.log | cut -d " " --complement -s -f1)
in_logs=$(grep -o "INFO [a-zA-Z \(\)' ]*\[#\w*\] [a-zA-Z \(\)\.' ]*" syslog.log | cut -d " " --complement -s -f1)
echo "$er_logs"
echo
echo "$in_logs"
echo "$er_logs" > errorFile.txt
echo "$in_logs" > infoFile.txt
