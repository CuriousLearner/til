# Remove PDF Password

Install `qpdf` via brew like:

```
brew install qpdf
```

and then run:

```
qpdf --decrypt --password=xxxxx encrypted-filename.pdf decrypted-filename.pdf
```
