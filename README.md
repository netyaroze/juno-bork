![Juno]

junobork
===========

Find new releases from http://www.juno.co.uk/.

---

## Install

```bash
$ python setup.py install
```

## Usage

The script performs three functions:

- Generates a CSV of release information
- Downloads images of new releases
- Downloads audio samples of new releases

```bash
$ junobork drone-ambient
$ junobork deep-house today 10
$ junobork minimal-tech-house eight-weeks 500
$ junobork house this-week 50
```

Check out the help for all available arguments:

```bash
$ junobork --help
```

## Examples

Run this weekly with `cron` to browse new releases via iTunes:

```bash
python junobork.py deep-house this-week 500 && \
    mv deep-house/*.mp3 \
    ~/Music/iTunes/iTunes\ Media/Automatically\ Add\ to\ iTunes.localized/ && \
    rm -rf deep-house
```
