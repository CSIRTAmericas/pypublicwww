PUBLICWWW Python Library   
========================

This is a simple package to search https://publicwww.com, you need a valid key to search in publicwww

Installation
------------

```bash
pip3 install pypublicwww
```

Usage as command
================

```bash
    publicwww [-h] [-apikey APIKEY] [-query QUERY] [-snippets] [-output [OUTPUT]] action
    positional arguments:
      action            Set action: init, info, search
```

SEARCH EXAMPLES
---------------

* Query for all Wordpress in domains .ar getting snippets

```bash
publicwww search -query 'site:ar "Wordpress"' -snippets
```

* Query for all Wordpress in domains .ar getting url

```bash
publicwww search -query 'site:ar "Wordpress"' 
```
If you add -ouput you will get the results in result.csv or -output /tmp/whatever.csv to get the result in /tmp/whatever.csv 

Usage as library
================

* Print account information

```python
import pypublicwww
api = PyPublicWWW(apikey)
print(api.info())
```

* Search for query and getting an export, you can add or not snippets

```python
import pypublicwww
publicwww. = PyPublicWWW(apikey)
publicwww._search_websites( 'site:ar "Wordpress"', csv=True, snippets=True)
```
