# ios_pmap_bps

This set of scripts is designed to read bps values from a Cisco IOS policy-map interface output, conver it into 2 different graphs, and email them.

Scripts:
1) run.py - Loops indefinitely every 5 minutes to screenscrape some output from a Cisco IOS policy-map interface output.  It gathers info for 5 different queues and adds them to a text file.  Kill the script to stop it. The script gathers data from the Gi1/5.52 interface.  Change in the script to the correct interface.

- Parameters:
-- 1) Device IP
-- 2) Username
-- 3) Password

2) run-chart-series.py & run-chart-stacked.py - These 2 scripts take the output from the run.py script and turn it into 2 seperate charts.  Examples are included in the Examples folder.

3) run-email.py - Takes the 2 graphs and emails them.

- Parameters:
-- 1) Mail from
-- 2) Mail to (rcpt)
-- 3) SMTP server


These scripts were built in a virtualenv.
Required modules:
 - netmiko  (run.py)
 - matplotlib  (run-chart-series.py & run-chart-stacked.py)
