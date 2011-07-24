#
# 22/07/2011
# script by Italo Maia
# http://www.italomaia.com
#

device_id=`xinput list | grep -i touchpad | grep -o 'id=[0-9][0-9]*' | sed s/id=//`

if [ $# == 1 ]
then
    opt=$(echo $1|tr '[:lower:]' '[:upper:]')

    if [ $opt == "ON" ] || [ $opt  == "OFF" ]
    then
        if [ $opt == "ON" ]
        then
            opt_code=1
        else
            opt_code=0
        fi

        xinput set-prop $device_id "Device Enabled" $opt_code
    else
        echo "WHAT?"
    fi
else
    echo "Turn touchpad ON or OFF?"
fi
