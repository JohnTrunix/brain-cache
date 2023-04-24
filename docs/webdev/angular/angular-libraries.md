# Angular First-Party Libraries

| Library              | Description                                                                                                    | Docs                                                         |
| -------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| `Angular Router`     | Advanced client-side navigation and routing based on Angular components.                                       | [Angular Router](https://angular.io/guide/router)            |
| `Angular Forms`      | Uniform system for form participation and validation.                                                          | [Angular Forms](https://angular.io/guide/forms-overview)     |
| `Angular HttpClient` | Robust HTTP client that can power more advanced client-server communication.                                   | [Angular HttpClient](https://angular.io/guide/http)          |
| `Angular Animations` | Rich system for driving animations based on application state.                                                 | [Angular Animations](https://angular.io/guide/animations)    |
| `Angular PWA`        | Tools for building Progressive Web Applications (PWA) including a service worker and Web application manifest. | [Angular PWA](https://angular.io/guide/service-worker-intro) |
| `Angular Schematics` | Automated scaffolding, refactoring, and update tools that simplify development at large scale.                 | [Angular Schematics](https://angular.io/guide/schematics)    |

## Angular Router

-   [Reference](https://angular.io/guide/router)

```terminal
ng generate module app-routing --flat --module=app
```

=== "app.module.ts"

    ```typescript
    import { NgModule } from '@angular/core';
    import { BrowserModule } from '@angular/platform-browser';
    import { RouterModule, Routes } from '@angular/router';

    import { AppComponent } from './app.component';
    import { HomeComponent } from './home/home.component';

    const routes: Routes = [
        { path: 'home', component: HomeComponent },
        { path: '', redirectTo: '/home', pathMatch: 'full'},
        { path: '**', component: PageNotFoundComponent}
    ];

    @NgModule({
        imports:      [ BrowserModule, RouterModule.forRoot(routes) ],
        declarations: [ AppComponent, HomeComponent ],
        bootstrap:    [ AppComponent ]
    })
    export class AppModule { }
    ```

=== ".component.html"

    ```html
    <nav>
        <a routerLink="/">Home</a>
        <a routerLink="/about">About</a>
    </nav>
    <router-outlet></router-outlet>
    ```

## Angular Forms

-   [Reference](https://angular.io/guide/forms-overview)

| Form Control            | Description                                                                                                                                                                 |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `reactive forms`        | provide direct, explicit access to underlying form object model: more robust, more scalable, reusable, testable                                                             |
| `template-driven forms` | rely on directives in template to create/manipulate underlying object: adding simple form to app, straightforward to add to an app, doesn't scale as well as reactive forms |

### Reactive Forms

-   [Reference](https://angular.io/guide/reactive-forms)

=== ".component.ts"

    ```typescript
    import { FormGroup, FormControl } from '@angular/forms';

    ...

    export class Reactive {
        Form = new FormGroup({
            firstName: new FormControl(''),
            lastName: new FormControl(''),
        });
    }
    ```

=== ".component.html"

    ```html
    <form [formGroup]="Form" (ngSubmit)="onSubmit()">

    <label for="first-name">First Name: </label>
    <input id="first-name" type="text" formControlName="firstName">

    <label for="last-name">Last Name: </label>
    <input id="last-name" type="text" formControlName="lastName">

    </form>
    ```

### Template-Driven Forms

-   [Reference](https://angular.io/guide/forms#building-a-template-driven-form)

=== ".component.ts"

    ```typescript
    import { Component } from '@angular/core';

    @Component({
        selector: 'app-template',
        templateURL: 'template.component.html',
    })

    export class Template{
        form = '';
    }
    ```

=== ".component.html"

    ```html
    <input type="text" [formControl]="form">
    ```
