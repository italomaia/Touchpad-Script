#
# 22/07/2011
# script by Italo Maia
# http://www.italomaia.com
#

device_id=`xinput list | grep -i touchpad | grep -o 'id=[0-9][0-9]*' | sed s/id=//`

if [ $# == 1 ]
then
    if [ $1 == "ON" ] || [ $1 == "OFF" ]
    then
        if [ $1 == "ON" ]
        then
            user_opt=1
        else
            user_opt=0
        fi

        xinput set-prop $device_id "Device Enabled" $user_opt
    else
        echo "WHAT?"
    fi
else
    echo "Turn touchpad ON or OFF?"
fi
