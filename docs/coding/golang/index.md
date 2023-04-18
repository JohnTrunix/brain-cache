---
hide:
    - toc
---

# Go

Code Review Comments: [CodeReviewComments golang/go](https://github.com/golang/go/wiki/CodeReviewComments)

## Installation & Setup

Installation instructions: [golang.org/doc/install](https://golang.org/doc/install)

## Environment Variables

```terminal
setx GOPATH %USERPROFILE%\go
setx path "%path%;%USERPROFILE%\bin"
```

## Important Packages

Adnvanced Formatter

```terminal
go install golang.go/x/tools/cmd/goimports@latest
```

Linter

```terminal
go install golang.org/x/lint/golint@latest
```
