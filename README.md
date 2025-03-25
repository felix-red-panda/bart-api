# BARTpy

A Python library and CLI for accessing BART (Bay Area Rapid Transit) real-time departure information

## Installation

```bash
pip install git+https://github.com/felix-red-panda/bart-api.git
```

## Usage

### Python Library

```python
from BART import BART

# create a BART instance (optional API key, defaults to a hardcoded API key)
bart = BART()

# get information for a station by name or abbreviation
station = bart["24th"]  # 24th St. Mission station

# access departures
for departure in station.departures:
    print(f"Departures to {departure.destination}")
    for train in departure.trains:
        print(f"{len(train)} car train in {train.minutes}")
```

### Command Line Interface

```bash
# list all station names and abbreviations
python3 cli-bart.py --list

# get departure information for a station
python3 cli-bart.py --station 24th

# disable terminal colors
python3 cli-bart.py --station embr --no-color
```

## Station Abbreviations

The package uses abbreviations for station names. Here are some common ones, a full list is in the BART.py:

- `24th`: 24th St. Mission
- `embr`: Embarcadero
- `mont`: Montgomery St.
- `powl`: Powell St.
- `civc`: Civic Center
- `16th`: 16th St. Mission

Use the `python3 cli-bart.py --list` option in the CLI to see all available stations.

## API Key

The library uses a public BART API key by default for demo purposes. You should register your own [here](https://api.bart.gov/api/register.aspx)

```python
bart = BART(api_key="YOUR-API-KEY")
```

## Requirements

- Python 3.6+
- requests

## Contributing

Contributions are welcome! Please feel free to submit a pull request
