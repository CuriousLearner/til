# Remove PDF Password

Install `qpdf` via brew like:

```bash
brew install qpdf
```

and then run:

```bash
qpdf --decrypt --password=xxxxx encrypted-filename.pdf decrypted-filename.pdf
```
