# Go Commands

## Build / Compile / Run

**Compile, execute and delete the binary:**

```terminal
go run main.go
```

**Build binary:**

```terminal
go build main.go
```

!!! note

    Rename binary with `-o <name>` flag:

**Run binary:**

```terminal
./main
```

**Download Packages:**

```terminal
go install github.com/rakyll/hey@latest
```

!!! note

    Change Version with `@<version>`

## Linting / Formatting

**Format Code:**

```terminal
go fmt
```

**Group Imports:**

```terminal
goimports -l -w
```

**Lint Code:**

```terminal
golint ./...
```

**Vet Code:**

Syntax is correct but may have other issues

```terminal
go vet ./...
```

**All in one Linting:**

```terminal
golangci-lint run
```

!!! note

    This is a wrapper for many linters and can check code in parallel

    [Guide](https://golangci-lint.run/)
