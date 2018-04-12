# Unicode

Unlike the classic tools for generating malicious domains (typographical errors), we have created a system to detect similar domains from unicode. This system does not have a static table in the code with the changes but they are based on the similarity of the characters by means of Deep Learning. This provides a greater number of variations and a possible update over time.

## Getting started

This project is based on the initial idea of capturing the differences between unicode characters through their representation in images, for which the following system of repositories has been created. This is a hard difference with others projects who use the standard of unicode. We based on this to update our tool and try to get a better result.

Some interesting proyects are:

Standard: https://unicode.org/cldr/utility/confusables.jsp

Personal project: http://www.irongeek.com/i.php?page=security/out-of-character-use-of-punycode-and-homoglyph-attacks-to-obfuscate-urls-for-phishing

We based our tool in the last article because we thinks is important to understand the problems with this type of symbols, but we use other point of view and dont take the standard to the similar symbols because this is too old and controllated by the systems, with this variations we have a personal system to create multiples variations without restriction and we can update any of the parts of the system to get better results.

This is the schema of the system:

![Alt text](/img/Architecture.png "Repositories system.")

The first repository is that of the unicode images, we have 38,880 characters that we will use to search from their images which are more similar to those that interest us (Basic Latin).

This is the first public database with the images of the unicode characters, we'll like to shared it to improve the recognise images database for the community. Any can download all the images in the following repository:

Repo: https://github.com/jiep/unicode-image-database

### Prerequisites

TODO

### Installing

TODO

## Authors

* José Ignacio Escribano Pablos
* Miguel Hernández Boza - @MiguelHzBz
* Alfonso Muñoz Muñoz - @mindcrypt

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
