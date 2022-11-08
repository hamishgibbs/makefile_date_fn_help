# makefile_date_fn_help

How can I apply the rule in the Makefile to every file in the `data/raw` directory and maintain the one-to-one dependency between input and output files?

Generate data with:

```{python}
python src/gen_raw_data.py
```

Process data with:

```{python}
make
```


Some helpful makefile things:
`%` (Pattern matching)  
`?=` (Optionally setting variable)  
`-k` (Multiprocessing)  
