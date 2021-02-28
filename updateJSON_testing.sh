#!/bin/bash
./hs100/hs100.sh discover > plugIPlist.txt
while read -r line
do
	echo -e "{\n\t \"plug-ip\": $line"
	echo "{ " >> pluginfo.txt
	#
	#experiment... ikke testet, da ingen kontakt til plugs... begin
	powerstatus='unknown'
	if [[ "ON" == *"$(./hs100/hs100.sh -i "$line" check)*" ]]; then
		powerstatus='ON'
	else
		powerstatus='OFF'
	fi
	echo -e "\"power_status\": $powerstatus" >> pluginfo.txt
	#experiment... ingen kontakt til plugs... end
	#
	./hs100/hs100.sh -i "$line" check >> pluginfo.txt
	./hs100/hs100.sh -i "$line" emeter >> pluginfo.txt
	./hs100/hs100.sh -i "$line" status  >> pluginfo.txt
	echo -e "\n}" >> pluginfo.txt
done < plugIPlist.txt
