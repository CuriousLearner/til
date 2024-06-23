# Import package without using it via underscore (`_`)

In Go, using `_` in imports allows you to import packages solely for their side effects, bypassing the Go compiler's `unused import error`. This is particularly useful when you need to execute code in the imported package's `init()` functions or register with a global state.

Example:
```go
package main

import _ "github.com/some/package" // Importing for side effects

func main() {
    // Your main program logic
}
```
