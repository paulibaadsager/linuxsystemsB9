#!/bin/bash
./hs100/hs100.sh discover > plugIPlist.txt
while read -r line
do
	echo "$line"
./hs100/hs100.sh -i "$line" check >> pluginfo.txt
./hs100/hs100.sh -i "$line" emeter >> pluginfo.txt
./hs100/hs100.sh -i "$line" status  >> pluginfo.txt
done < plugIPlist.txt
