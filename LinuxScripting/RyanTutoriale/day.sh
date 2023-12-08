#!/bin/bash

day=$(date +"%u")

case $day in
    1)
        echo "Happy Monday!"
        ;;
    2)
        echo "Happy Tuesday!"
        ;;
    3)
        echo "Happy Wednesday!"
        ;;
    4)
        echo "Happy Thursday!"
        ;;
    5)
        echo "TGIF! Happy Friday!"
        ;;
    6)
        echo "Happy Saturday!"
        ;;
    7)
        echo "Happy Sunday!"
        ;;
esac
