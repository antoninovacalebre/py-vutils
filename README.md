## Utilizzo
Nella cartella `site-packages` di Python aggiungi un file con estensione `.pth` contenente la cartella con i moduli
	- Per anaconda la cartella è in `C:\Users\<NOME UTENTE>\anaconda3\envs\<NOME ENV>\Lib\site-packages`

File `my_modules.pth` di esempio:
```
C:\Users\Antonino\Python-Modules
```

## Note
Quando fai un modulo aggiungi in fondo ai file
```python
if __name__ == "__main__":
    pass
```
