# V2D - Visual Unicode attacks with deep learning

Unlike the classic tools for generating malicious domains (typographical errors), we have created a system to detect similar domains from Unicode. This system does not have a static table with the possible changes, the domains creation are based on the similarity of the characters by means of Deep Learning. Consequently, this provides a greater number of variations and possible updates over time if new characters are created.

## State of Art

This project is based on the initial idea of capturing the differences between Unicode characters through their representation in images. In actual fact, there are some projects which use the standard of Unicode and some repositories have been created. Some interesting projects are:

* Standard: https://unicode.org/cldr/utility/confusables.jsp

* Personal project: http://www.irongeek.com/i.php?page=security/out-of-character-use-of-punycode-and-homoglyph-attacks-to-obfuscate-urls-for-phishing

We based on these repositories to update our tool and try to get more accurate and complete results.


## Research

This tool is the result of the work of the Cybersecurity Lab I4S team within BlueIndico, where we started from the simple idea of comparing images of unicode characters. Initially, the images of all these Unicode characters were needed and this was the first problem as we could not find them on the Internet. So that, we created the first database with the unicode image characters. It can be found on the repository of Unicode images, https://github.com/PantherLab/v2d-unicodeDB. There are 38,880 characters that we will use to compare with Basic Latins characters and select the most similar ones. This is the first public database with the images of the Unicode characters, we would like to share it with the community in order to improve the image recognition. Anyone can download the images from the repository. Any contribution to  improve the algorithms for characters recognition would be appreciated.

![Image repository](/img/repository.png "Image repository.")

After having all the characters, the next step is to calculate the similarity between images of Unicode characters. To accomplish that, we used Transfer Learning with Keras. The full project is available on Github, https://github.com/PantherLab/v2d-similarity. This code extracts image features to compare and create a confusables file that it will be used by the CLI.
Finally, we created a CLI using the result of the previous step. This CLI generates all the possible combinations with each similar letter of each letter in Unicode. On the one hand, as an attacker, it can be used to generate malicious web domains, emails, phishing, etc. On the other hand, as a defender, to check how all these variations affect/impact in a web and if they exist, block them or report them as fraud to State forces.

Repo: https://github.com/PantherLab/v2d-cli

This is the schema of the system:

![Alt text](/img/Architecture.png "Repositories system.")

## V2D - CLI

V2D is the first tool that uses Deep Learning, especially Transfer Learning, to automatically create new variations of inputs using Unicode characters. It is a typical visual attack but in this case the tool uses the power of the machines to select the most similar characters between all possibles.

[![demo](https://asciinema.org/a/oxZKyNJAoblosmwtzWr8Pgchg.png)](https://asciinema.org/a/oxZKyNJAoblosmwtzWr8Pgchg?autoplay=1)


### Prerequisites

Python>=3.5

### Installing

```
pip3 install v2d
```

### Getting started

#### Quick example

```
$ v2d -d example.org -m 10 -c -v


oooooo     oooo   .oooo.   oooooooooo.
 `888.     .8'  .dP""Y88b  `888'   `Y8b
  `888.   .8'         ]8P'  888      888
   `888. .8'        .d8P'   888      888
    `888.8'       .dP'      888      888
     `888'      .oP     .o  888     d88'
      `8'       8888888888 o888bood8P'


    Visual Unicode attacks with Deep Learning
    Version 1.1.0
    Authors: José Ignacio Escribano
    Miguel Hernández (MiguelHzBz)
    Alfonso Muñoz (@mindcrypt)



Similar domains to example.org
exampǀe.org
examp1е.org
examp1ɘ.org
examp1e.org
examp|е.org
examp|ɘ.org
example.org
examplе.org
examp|e.org
examplɘ.org
Checking if domains are up
The domain exampǀe.org does not exist
The domain examp1е.org does not exist
The domain examp1ɘ.org does not exist
The domain examp1e.org does not exist
The domain examp|е.org does not exist
The domain examp|ɘ.org does not exist
The domain example.org exists
The domain examplе.org does not exist
The domain examp|e.org does not exist
The domain examplɘ.org does not exist
Total similar domains to example.org: 10
```
##### Note

> Sometimes the output isn't render, that is because the terminal needs the font, but if you copy the text is correct.

#### Getting help

```
$ v2d -h

oooooo     oooo   .oooo.   oooooooooo.
 `888.     .8'  .dP""Y88b  `888'   `Y8b
  `888.   .8'         ]8P'  888      888
   `888. .8'        .d8P'   888      888
    `888.8'       .dP'      888      888
     `888'      .oP     .o  888     d88'
      `8'       8888888888 o888bood8P'


    Visual Unicode attacks with Deep Learning
    Version 1.1.0
    Authors: José Ignacio Escribano
    Miguel Hernández (MiguelHzBz)
    Alfonso Muñoz (@mindcrypt)



usage: v2d [-h] [-d DOMAIN] [-v] [-c] [-w] [-vt] [-m MAX]
           [-t 75,80,85,90,95,99] [-key API] [-o OUTPUT] [-i FILEINPUT]

v2d-cli: Visual Unicode attacks with Deep Learning - System based on the
similarity of the characters unicode by means of Deep Learning. This provides
a greater number of variations and a possible update over time

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

>$ v2d -d example.com -o dominionsexample.txt
>$ v2d --domain example.com -m 100 -t 85
>$ v2d -i fileexample.txt -c -w -v

```



## Authors

* José Ignacio Escribano Pablos
* Miguel Hernández Boza - @MiguelHzBz
* Alfonso Muñoz Muñoz - @mindcrypt

## Contributing

Any collaboration is welcome!

There're many tasks to do.You can check the [Issues](https://github.com/PantherLab/v2d-cli/issues) and send us a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
