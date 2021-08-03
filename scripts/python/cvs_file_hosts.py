#!/usr/bin/env python3

import csv
hosts = [["localhost","127.0.0.1"],["workstation.local", "192.168.1.100"],["server.domain", "10.2.100.1"]]
with open('host.csv', 'w') as cvs_file_hosts:
    writer = csv.writer(cvs_file_hosts)
    writer.writerows(hosts)
