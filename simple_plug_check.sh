#!/bin/bash
# Assumes plugs are listed in /etc/hosts with names plug1, plug2, ... , plug4
for i in {1..4}
do
	./hs100/hs100.sh -i "plug"$i check;
done
