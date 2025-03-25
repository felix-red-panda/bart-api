#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# <bitbar.title>BART</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Moloch</bitbar.author>
# <bitbar.author.github>moloch--</bitbar.author.github>
# <bitbar.desc>Get BART times.</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>

TITLE = "🚈"
STATION = "24th"

# Code
from BART import BART
bart = BART()

print(f"{TITLE} | dropdown=false")
print("---")
print(f"{BART.STATION_NAMES[STATION]}")

for departure in bart[STATION].departures:
    print("---")
    print(f"{departure.destination} | color=white")
    for index, train in enumerate(departure.trains):
        print(f"{index + 1}) {len(train)} car train in {train.minutes} | color={train.color}")
