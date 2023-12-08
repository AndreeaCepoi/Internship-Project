#!/bin/bash

let "a = $1 * $2"
echo "Method1 (let): $a"

b=$(expr $1 \* $2)
echo "Method2 (expr): $b"

c=$(( $1 * $2 ))
echo "Method3 (\$(( ))): $c"

d=$(($1*$2))
echo "Method4 (\${#var}): ${#d}"
