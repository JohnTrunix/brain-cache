# Angular Dependency Injection

!!! note

    Dependency Injection is a design pattern that separates dependencies of a class from its environment. It is used to provide services, components and dependencies. DI containers create instances of dependencies.

    - [Reference](https://angular.io/guide/dependency-injection)

## Service

```terminal
ng generate service <service-name>
```

=== ".service.ts"

    ```typescript
    @Injectable({
        providedIn: 'root',
    })
    class Service {}
    ```

    Note: `providedIn: 'root'` is used to make the service available to the entire application as Singleton Instance.

=== ".component.ts"

    ```typescript
    @Component({
        selector: 'component',
        template: '...',
        providers: [Service]
    })
    class ComponentClass {}
    ```

=== ".module.ts"

    ```typescript
    @NgModule({
        declarations: [ComponentClass],
        imports: [CommonModule],
        providers: [Service]
    })
    class ModuleClass {}
    ```
