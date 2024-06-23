# Build tags in Golang

A build tag is a line comment starting with // +build
  and can be executed by `go build -tags="foo bar"` command.
  Build tags are placed before the package clause near or at the top of the file
  followed by a blank line or other line comments.

Example:

```go
// +build windows,!linux
package main
...
```

In this example, // +build windows,!linux is used to specify that this code should only be built on Windows and not on Linux.

You can also use multiple build tags by separating them with a comma.

Example:

```go
// +build prod, dev, test
package main
...
```

In the above example, the code will be built only when running the command with either "prod" or "dev" or "test" as an argument.

```bash
go build -tags="prod"
```
