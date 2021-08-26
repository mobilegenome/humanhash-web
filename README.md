# humanhash-web

A little webserver running on web.py returning a human-readable hash. 

based on: https://github.com/zacharyvoase/humanhash/ 

## Start web-server

`python3 app.py` 

## Usage

- retrieve one two-word hash: `http://0.0.0.0:8080/hash/`

### Advanced usage

- retrieve multiple hashes: `http://0.0.0.0:8080/hash/<N>` , where N is a number between 1 and 256
- retrieve longer hashes: `http://0.0.0.0:8080/hash/<N>/length/<L>` , where L is a number between 1 and 4

Statistical uniqueness:

| Length | Uniqueness |
|--------|------------|
|   1    |  1/256     |
|   2    |  1/65536   |
|   3    |  $`5.9^-8`$    |
|   4    |  $`2.3^-10`$ |




## Dependecies

```
pip3 install web.py
pip3 install humanhash3
```
