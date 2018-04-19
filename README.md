# V2D - Visual Unicode attacks with deep learning

Unlike the classic tools for generating malicious domains (typographical errors), we have created a system to detect similar domains from Unicode. This system does not have a static table in the code with the changes but they are based on the similarity of the characters by means of Deep Learning. This provides a greater number of variations and a possible update over time.

## State of Art

This project is based on the initial idea of capturing the differences between Unicode characters through their representation in images, for which the following system of repositories has been created. This is a hard difference with others projects who use the standard of Unicode. We based on this to update our tool and try to get a better result.

Some interesting proyects are:

Standard: https://unicode.org/cldr/utility/confusables.jsp

Personal project: http://www.irongeek.com/i.php?page=security/out-of-character-use-of-punycode-and-homoglyph-attacks-to-obfuscate-urls-for-phishing


## Research

We based our tool in the last article because we thinks is important to understand the problems with this type of symbols, but we use other point of view and don't take the standard to the similar symbols because this is too old and controllated by the systems, with this variations we have a personal system to create multiples variations without restriction and we can update any of the parts of the system to get better results.

This is the schema of the system:

![Alt text](/img/Architecture.png "Repositories system.")

The first repository is that of the Unicode images, we have 38,880 characters that we will use to search from their images which are more similar to those that interest us (Basic Latin).

This is the first public database with the images of the Unicode characters, we'll like to shared it to improve the recognize images database for the community. Any can download all the images in the following repository:

![Alt text](/img/repository.png "Image repository.")

Repo: https://github.com/jiep/unicode-image-database

The images are available for all the community to improve the algorithms to recognize characters.

To calculate the similarity between images of Unicode characters, we use Transfer Learning with Keras, all this project are available in Github:

Repo: https://github.com/jiep/unicode-similarity

This code extract all the image features to compare and create a confusables file that we used in the CLI.

Finally, we use the result of this repository to create a CLI to generate all the possible combinations with each similar letter of each letter in Unicode. As an attacker, it can be used to generate malicious web domains, emails, phishing, etc. On the other hand, as a defender, you can check if all these variations are working to block and inform.

The code is available in Github

Repo: https://github.com/jiep/unicode

## V2D - CLI

V2D is the first tool that used Deep Learning, in special Transfer Learning, to create automaticaly new variations of inputs used Unicode characters, its a typical visual attack but in this case this tool use the power of the machines to select the most similar character between all possibles.

[![demo](https://asciinema.org/a/oxZKyNJAoblosmwtzWr8Pgchg.png)](https://asciinema.org/a/oxZKyNJAoblosmwtzWr8Pgchg?autoplay=1)


### Prerequisites

Python3
pip3
Generate the file confusables.pickle

### Installing

```
git clone https://github.com/jiep/unicode
cd Unicode
pip3 install -e .
```
##### Note

> v2d need a confusables.pickle. Be sure that the file is generated!

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
    Version 0.0.1
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
    Version 0.0.1
    Authors: José Ignacio Escribano
    Miguel Hernández (MiguelHzBz)
    Alfonso Muñoz (@mindcrypt)



usage: v2d [-h] [-d DOMAIN] [-v] [-c] [-w] [-m MAX] [-t 75,80,85,90,95,99]
           [-o OUTPUT] [-i FILEINPUT]

v2d-cli: Visual Unicode attacks with deep learning - System based on the
similarity of the characters unicode by means of Deep Learning. This provides
a greater number of variations and a possible update over time

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        check similar domains to this one
  -v, --verbose
  -c, --check           check if this domain is alive
  -w, --whois           check whois
  -m MAX, --max MAX     maximum number of similar domains
  -t 75,80,85,90,95,99, --threshold 75,80,85,90,95,99
                        Similarity threshold
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

There're many tasks to do.You can check the [Issues](https://github.com/jiep/unicode/issues) and send us a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
