#!/bin/bash
for counter in $(seq 1 30)
do
    cacheKeysForPR=$(gh actions-cache list -L 30 -R raultrombin/navigator-lib | cut -f 1 )
    for cacheKey in $cacheKeysForPR
    do
        gh actions-cache delete $cacheKey --confirm -R raultrombin/navigator-lib
        done
        echo "Done"
done
