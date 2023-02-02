## How to Install

```bash
pip install git+https://github.com/antoninovacalebre/py-vutils.git
```

## Make a package

Create the following folder structure:

```
root/
	setup.py
	package_name/
		__init__.py
		module1.py
		module2.py
```

Where `__init__.py` is an empty file, while `setup.py` contains info about the package itself:

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

## Notes

In each module source code remember to add this.

```python
if __name__ == "__main__":
    pass
```
