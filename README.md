<h1 align="center">DeepConfusables</h1>

<p align="center">
  <img src="./images/logo.png" width="30%" />
</p>

> Visual Unicode attacks with deep learning

> `deep-confusables` is the first tool that uses Deep Learning, especially Transfer Learning, to automatically create new variations of inputs using Unicode characters. It is a typical visual attack but in this case the tool uses the power of the machines to select the most similar characters between all possibles.

## Demo

![demo](./images/demo.gif)


## Prerequisites

Python>=3.5

## Installing

```
pip3 install deep-confusables
```

## Getting started

### Quick example

```
$ deep-confusables -d example.org -m 10 -c -v

 __   ___  ___  __      __   __        ___       __        __        ___  __
|  \ |__  |__  |__) __ /  ` /  \ |\ | |__  |  | /__`  /\  |__) |    |__  /__`
|__/ |___ |___ |       \__, \__/ | \| |    \__/ .__/ /~~\ |__) |___ |___ .__/

    Visual Unicode attacks with Deep Learning
    Version 1.1.1
    Created by:
      - José Ignacio Escribano Pablos (@jiep)
      - Miguel Hernández Boza (@Miguel000)
      - Alfonso Muñoz Muñoz (@mindcrypt)

Similar domains to example.org
cxamp1ȅ.org
cxamp1o.org
cxamp1ɕ.org
cxamp1ƈ.org
cxamp1ɔ.org
cxamp1c.org
cxamp1e.org
cxamp1ǝ.org
cxamp1ɘ.org
cxamp1ȇ.org
Checking if domains are up
The domain cxamp1ȅ.org does not exist
The domain cxamp1o.org does not exist
The domain cxamp1ɕ.org does not exist
The domain cxamp1ƈ.org does not exist
The domain cxamp1ɔ.org does not exist
The domain cxamp1c.org does not exist
The domain cxamp1e.org does not exist
The domain cxamp1ǝ.org does not exist
The domain cxamp1ɘ.org does not exist
The domain cxamp1ȇ.org does not exist
Total similar domains to example.org: 10
```
#### Note

> Sometimes the output isn't render, that is because the terminal needs the font, but if you copy the text is correct.

### Getting help

```
$ deep-confusables -h

 __   ___  ___  __      __   __        ___       __        __        ___  __
|  \ |__  |__  |__) __ /  ` /  \ |\ | |__  |  | /__`  /\  |__) |    |__  /__`
|__/ |___ |___ |       \__, \__/ | \| |    \__/ .__/ /~~\ |__) |___ |___ .__/

    Visual Unicode attacks with Deep Learning
    Version 1.1.1
    Created by:
      - José Ignacio Escribano Pablos (@jiep)
      - Miguel Hernández Boza (@Miguel000)
      - Alfonso Muñoz Muñoz (@mindcrypt)

usage: deep-confusables [-h] [-d DOMAIN] [-v] [-c] [-w] [-vt] [-m MAX]
                        [-t 75,80,85,90,95,99] [-key API] [-o OUTPUT]
                        [-i FILEINPUT]

deep-confusables-cli: Visual Unicode attacks with Deep Learning - System based
on the similarity of the characters unicode by means of Deep Learning. This
provides a greater number of variations and a possible update over time

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        check similar domains to this one
  -v, --verbose
  -c, --check           check if this domain is alive
  -w, --whois           check whois
  -vt, --virustotal     check Virus Total
  -m MAX, --max MAX     maximum number of similar domains
  -t 75,80,85,90,95,99, --threshold 75,80,85,90,95,99
                        Similarity threshold
  -key API, --api-key API
                        VirusTotal API Key
  -o OUTPUT, --output OUTPUT
                        Output file
  -i FILEINPUT, --input FILEINPUT
                        List of targets. One input per line.


Examples:

>$ deep-confusables -d example.com -o dominionsexample.txt
>$ deep-confusables --domain example.com -m 100 -t 85
>$ deep-confusables -i fileexample.txt -c -w -v

```

## Contributing

Any collaboration is welcome!

There're many tasks to do.You can check the [Issues](https://github.com/next-security-lab/deep-confusables-cli/issues) and send us a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Authors

* José Ignacio Escribano Pablos - [@jiep](https://github.com/jiep)
* Miguel Hernández Boza - [@Miguel000](https://github.com/Miguel000)
* Alfonso Muñoz Muñoz - [@mindcrypt](https://github.com/mindcrypt)

<!-- Banner -->
<p align="center">
  <img src="./images/banner.png"/>
</p>
<h4 align="center" style="margin: -20px">Made with <span style="color:#e25555;">❤️</span> by <a Cybersecurity Lab @ <a href="https://www.bbvanexttechnologies.com">BBVA Next Technologies</a> </h4>
