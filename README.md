## Installare un pacchetto

```bash
pip install git+https://github.com/antoninovacalebre/py-vutils.git
```

## Creare un pacchetto

Struttura la cartella in modo che si abbia

```
root/
	setup.py
	package_name/
		__init__.py
		module1.py
		module2.py
```

Dove `__init__.py` è un file vuoto, mentre `setup.py` contiene codice del tipo

``` python
import setuptools

setuptools.setup(name='vutils',
                 version='1.0',
                 description='Useful stuff',
                 url='#',
                 author='av',
                 install_requires=[],
                 author_email='',
                 packages=setuptools.find_packages(),
                 zip_safe=False)
```

## Note

Quando fai un modulo aggiungi in fondo ai file
```python
if __name__ == "__main__":
    pass
```
