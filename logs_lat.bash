#!/bin/bash
touch latencies.csv
latency=`cat memcached_logs.csv | grep '.000005' | cut -d\, -f10`
echo "${latency}" > latencies.csv

