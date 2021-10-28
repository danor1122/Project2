20.10.2021
version number - PEP 440 specification in every python package
N[.N]+[{a|b|c|rc}N][.postN][.devN]
Semantic Versioning - similar to PEP 440
- 4 spaces every tab
- wiersz max 79 letters
- 2 lines gap after def ald class def
- ASCII or UTF-8 coding in files
- every module imported in seperate instruction imported on the begining of the files
- firstly import of standard libiarys, then zewnetrzne, on the end local libiarys
- in nawiasy okragle and kwadratowe badz klamrowe or przed przecinkami NO spaces
- Class names CamelCase
- function(def) names started with small letter and spaced by _

PEP 8 - code writed in that specification
pep8 - tool installed by pip can be used to check any phyton file if it is coded regarding to the PEP 8 rules
pep8 hello.py
...
echo $?
PEP 7 - python styles
Pyflakes - tool search for programistic errors
Pylint - checking PEP 8 zgodnosc
flake8 łączy pyflakes and pep 8 in one command

pip - exist from python 3.4,  can install or uninstall packages from repos Python Packaging Index(PyPI)
 archiwum tar (tarball) lub archiwum Whell 
 pip install --user voluptuos *-- user installing packages to user catalogues directory, so system cataloges are not rubbished
 pip freeze *show list of packages installed
 pip uninstall pika-pool * package uninstall
 pip install -e * install package without copying files to the package
-e or other -f -s -agf - those are called flags
