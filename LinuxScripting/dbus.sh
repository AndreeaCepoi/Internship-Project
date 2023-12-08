#!/bin/bash

check_charging_status() {
	dbus-monitor --system "type=signal,interface=org.freedesktop.UPower.Device" |
	
	while read -r line
	do
		status=$(upower -i /org/freedesktop/UPower/devices/battery_BAT0 | grep "state:" | awk '{print $2}')
		if [ "$status" == "charging" ]
		then
			echo "This machine is currently plugged in"
		elif [ "$status" == "discharging" ]
		then
			echo "This machine is currently using the battery"
		fi
	done
}
check_charging_status

#acepoi@Ubuntu22:~/Internship-Project/LinuxScripting$ sudo ./dbus.sh
#This machine is currently plugged in

#acepoi@Ubuntu22:~/Internship-Project/LinuxScripting$ sudo ./dbus.sh
#This machine is currently using the battery
