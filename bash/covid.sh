#!/bin/bash

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DEATH=$(echo $DATA | jq '.[0].deathIncrease')
TOTALDEATH=$(echo $DATA | jq '.[0].death')
TODAY=$(date)

echo "On $TODAY"
echo "There were $POSITIVE positive COVID cases."
echo "There were $NEGATIVE negative COVID cases."
echo "There were $DEATH deaths due to COVID today."
echo "The total COVID death count int the USA is $TOTALDEATH"

