# makefile_date_fn_help

Q: How can I apply the rule in the Makefile to every file in the `data/raw` directory and maintain the one-to-one dependency between input and output files?  
A: Pattern matching, `wildcard`, and `subst` (see `Makefile`).

Generate data with:  

```{bash}
mkdir data data/raw data/grouped
python src/gen_raw_data.py
```

Process data with:  

```{bash}
make
```


Some helpful makefile things:  
`%` (Pattern matching)  
`?=` (Optionally setting variable)  
`-k` (Multiprocessing)  
