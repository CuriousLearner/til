# Reduce file size of PDF files

This requires `gs` (Ghostscript) to be installed.

```bash
compresspdf() {
    if [ $# -lt 2 ]; then
        echo "Usage: compresspdf INPUT.pdf OUTPUT.pdf [dpi]"
        echo "Default dpi = 200 (good for scanned docs / visa uploads)"
        return 1
    fi

    local input="$1"
    local output="$2"
    local dpi="${3:-200}"   # third arg optional, default 200

    command gs \
      -sDEVICE=pdfwrite \
      -dNOPAUSE -dQUIET -dBATCH \
      -dCompatibilityLevel=1.6 \
      -dDetectDuplicateImages=true \
      -dDownsampleColorImages=true \
      -dColorImageDownsampleType=/Average \
      -dColorImageResolution="$dpi" \
      -dDownsampleGrayImages=true \
      -dGrayImageDownsampleType=/Average \
      -dGrayImageResolution="$dpi" \
      -dDownsampleMonoImages=true \
      -dMonoImageDownsampleType=/Average \
      -dMonoImageResolution=300 \
      -sOutputFile="$output" \
      "$input"
}
```

## Usage

```bash
# Default 200 DPI (good for scanned docs, visa uploads)
compresspdf input.pdf output.pdf

# Custom DPI for higher quality
compresspdf input.pdf output.pdf 300
```

## What each option does

| Option                                | Description                                                       |
| ------------------------------------- | ----------------------------------------------------------------- |
| `-sDEVICE=pdfwrite`                   | Output device - writes a new PDF file                             |
| `-dNOPAUSE`                           | Don't pause between pages (normally gs waits for input)           |
| `-dQUIET`                             | Suppress startup messages and page numbers                        |
| `-dBATCH`                             | Exit after processing (don't enter interactive mode)              |
| `-dCompatibilityLevel=1.6`            | PDF version 1.6 - supports better compression than older versions |
| `-dDetectDuplicateImages=true`        | Find identical images and store them only once                    |
| `-dDownsampleColorImages=true`        | Reduce resolution of color images                                 |
| `-dColorImageDownsampleType=/Average` | Use averaging when reducing (smoother than `/Subsample`)          |
| `-dColorImageResolution=<dpi>`        | Target DPI for color images                                       |
| `-dDownsampleGrayImages=true`         | Reduce resolution of grayscale images                             |
| `-dGrayImageDownsampleType=/Average`  | Averaging for grayscale (smoother results)                        |
| `-dGrayImageResolution=<dpi>`         | Target DPI for grayscale images                                   |
| `-dDownsampleMonoImages=true`         | Reduce resolution of black & white images                         |
| `-dMonoImageDownsampleType=/Average`  | Averaging for mono images                                         |
| `-dMonoImageResolution=300`           | Keep mono at 300 DPI (text/line art needs more resolution)        |
| `-sOutputFile=<file>`                 | Output file path                                                  |

## Why 200 DPI default?

200 DPI is enough for on-screen viewing and most document uploads (visa applications, forms, etc.) while significantly reducing file size. Increase to 300 DPI if you need to print the document.
