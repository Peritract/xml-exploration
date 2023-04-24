# XML exploration

A toy project to practice working with XML data.

The project scaffold contains code to download an XML file from S3.

## Installation

`python -r requirements.txt`

## Environment variables

This project expects a `.env` file at project root, containing the following keys:

```sh
AWS_ACCESS_KEY_ID=XXXXXXXXXX
AWS_SECRET_ACCESS_KEY=XXXXXXXXXX
S3_BUCKET_NAME=XXXXXXXXXX
SOURCE_FILE=XXXXXXXXXX
DATA_FOLDER=data
DST_FILE=XXXXXXXXXX
```

Replace `XXXXXXXXXX` with your sensitive/specific data as appropriate.

## Data sourcing

Run `python3 ingestion.py` to download remote data for access.

## Useful links

- [XML specification](https://www.w3.org/TR/REC-xml/)
- [XPATH specification](https://www.w3.org/TR/2017/REC-xpath-31-20170321/)
- [Python XML API documentation](https://docs.python.org/3/library/xml.etree.elementtree.html)
