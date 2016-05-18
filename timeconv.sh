#!/bin/bash
## https://www.hackerrank.com/challenges/time-conversion

read STR
var1=$(echo $STR | cut -f1 -d:)
var2=$(echo $STR | cut -f2 -d:)
var3=$(echo $STR | cut -f3 -d:)
if [[ "${STR}" == *PM ]] && [[ $var1 != 12 ]]
then
    var1=$(expr $var1 + 12)
    echo "$var1:$var2:${var3::-2}"
elif [[ "${STR}" == *AM ]] && [[ $var1 != 12 ]]
then
    echo ${STR::-2}
elif [[ "${STR}" == *PM ]] && [[ $var1 == 12 ]]
then
    echo ${STR::-2}
else
    echo "00:$var2:${var3::-2}"    
fi
