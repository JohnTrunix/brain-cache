# Angular Testing

!!! info

    - Test files need to be named with the `.spec.ts` extension.
    - Also it is recommended to place test files in same directory as the file being tested.
    - [Reference](https://angular.io/guide/testing)

```terminal
ng test <project-name>
```

Create custom config `karma.conf.js`:

```terminal
ng generate config karma
```

## Continuous Integration (CI)

-   [Reference](https://angular.io/guide/testing#testing-in-continuous-integration)

```terminal
ng test --no-watch --no-progress
```
