#!/bin/bash

curl --location-trusted -u root: \
    -H "Expect:100-continue" \
    -H "column_separator:," \
    -H "format:csv_with_names" \
    -T ./output/plates_1.csv \
    -XPUT http://localhost:8031/api/zhaav/iranian_plate_generated/_stream_load


sleep 100
