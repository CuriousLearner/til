# Subresource Integrity (SRI) Hashes

SRI is a security feature that allows browsers to verify that resources fetched from CDNs or external sources haven't been tampered with. It works by comparing a cryptographic hash of the fetched resource against an expected hash you provide.

## Usage

Add the `integrity` attribute to `<script>` or `<link>` tags:

```html
<script src="https://cdn.example.com/library.js"
        integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8wC"
        crossorigin="anonymous"></script>

<link rel="stylesheet" href="https://cdn.example.com/styles.css"
      integrity="sha384-abc123..."
      crossorigin="anonymous">
```

The `crossorigin="anonymous"` attribute is required when loading resources from a different origin.

## Generating SRI Hashes

Using OpenSSL:

```bash
cat library.js | openssl dgst -sha384 -binary | openssl base64 -A
```

Or using shasum:

```bash
shasum -b -a 384 library.js | awk '{ print $1 }' | xxd -r -p | base64
```

You can also use online tools like [srihash.org](https://www.srihash.org/).

## Supported Hash Algorithms

SRI supports SHA-256, SHA-384, and SHA-512. SHA-384 is commonly used as a good balance between security and performance.

You can specify multiple hashes for the same resource (browser uses the strongest one it supports):

```html
<script src="https://cdn.example.com/lib.js"
        integrity="sha256-abc... sha384-xyz..."
        crossorigin="anonymous"></script>
```

## Why Use SRI?

- Protects against compromised CDNs or man-in-the-middle attacks
- Ensures the exact version of a library you tested is what users receive
- Prevents malicious code injection through third-party resources
