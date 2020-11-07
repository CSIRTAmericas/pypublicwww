PUBLICWWW Python Library   
========================

This is a simple package to search https://publicwww.com, you need a valid key to search in publicwww

Usage as command
================

    publicwww [-h] [-apikey APIKEY] [-query QUERY] [-snippets] [-output [OUTPUT]] action
    
    positional arguments:
      action            Set action: init, info, search
    
    optional arguments:
      -h, --help        show this help message and exit
    
    init arguments:
      -apikey APIKEY    Set API KEY for init
    
    search arguments:
      -query QUERY      Enter query to be issue in publicwww
      -snippets         Add snippet to results
      -output [OUTPUT]  Output File
    
    
    EXAMPLES:
    
    publicwww init -apikey 0123456789abcdef
    publicwww info
    publicwww search -query query
    For include snippets:
    publicwww search -query query -snippets
    For define filename to output, without -output it prints on terminal:
    publicwww search -query query -snippets -output (default results.csv)
    publicwww search -query query -snippets -output file_results.csv
    

SEARCH EXAMPLES
---------------

* Query for all Wordpress in domains .ar getting snippets

```console
publicwww search -query 'site:ar "Wordpress"' -snippets
```

* Query for all Wordpress in domains .ar getting url

```console
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
