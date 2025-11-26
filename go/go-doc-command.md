# Using `go doc` to Read Package Documentation

The `go doc` command lets you read Go package documentation directly from the terminal without opening a browser.

## Basic Usage

```bash
# View documentation for an entire package
go doc fmt

# View documentation for a specific function
go doc fmt.Println

# View documentation for a type
go doc json.Encoder

# View documentation for a method
go doc json.Encoder.Encode
```

## Useful Flags

```bash
# Show all exported symbols (not just the summary)
go doc -all fmt

# Show source code alongside documentation
go doc -src fmt.Println

# Show unexported symbols too
go doc -u fmt
```

## Examples

```bash
$ go doc fmt.Println
package fmt // import "fmt"

func Println(a ...any) (n int, err error)
    Println formats using the default formats for its operands and writes to
    standard output. Spaces are always added between operands and a newline
    is appended. It returns the number of bytes written and any write error
    encountered.
```

## Why Use `go doc`?

- **Fast** – No browser needed, stays in your terminal workflow
- **Offline** – Works without internet once packages are downloaded
- **Precise** – Jump directly to a specific function or type
