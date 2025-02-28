# Reduce file size of PDF files

This would require `gs` to be installed.

```bash
compresspdf() {
    echo 'Usage: compresspdf [input file] [output file] [screen|ebook|printer|prepress]'
    gs -sDEVICE=pdfwrite -dNOPAUSE -dQUIET -dBATCH -dPDFSETTINGS=/${3:-"screen"} -dCompatibilityLevel=1.4 -sOutputFile="$2" "$1"
}
```

and then do:

```bash
compresspdf uncompressed-file.pdf compressed-file.pdf screen
```
