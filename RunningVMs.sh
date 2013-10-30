#!/bin/bash

#

count=`/Applications/VMware\ Fusion.app/Contents/Library/vmrun -T fusion list |head -1`

vm=`/Applications/VMware\ Fusion.app/Contents/Library/vmrun -T fusion list |awk -F "/" '{print $6}'|sed s/.vmwarevm//g`

if [ -x /Applications/VMware\ Fusion.app/Contents/Library/vmrun ];then

echo $count

echo "$vm"

else

logger -s "vmrun not found"

exit 1

fi
