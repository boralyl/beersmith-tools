# beersmith-tools

Tools for working with beersmith beer XML data.

## Tools

### Convert a Beer XML file to Markdown

First export your recipe from beersmith in the Beer XML format.

```bash
$ python xml_to_md.py --help
Usage: xml_to_md.py [OPTIONS] BEER_XML_PATH

  Outputs markdown from a beer xml file.

Arguments:
  BEER_XML_PATH  Path to beer xml file  [required]

```

## Installing Python Requirements

First install `pip-tools`.

```bash
$ pip install pip-tools
$ pip-sync *.txt
```

### Add new requirement

To add a new requirement edit either `requirements.in` or `dev-requirements.in`
depending if the depdnency is for prod or development. Add the package name and
optionally a version range. Then re-generate either the `requirements.txt` or
`dev-requirements.txt`.

```
$ pip-compile --generate-hashes requirements.in
```

### Upgrading a requirement

You can update all requirements by running:

```
$ pip-compile --upgrade requirements.in
```

Or a single package:

```
$ pip-compile --upgrade-package fastapi requirements.in
```
