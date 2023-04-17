# Angular Modules

!!! note

    Angular Modules are containers with different purposes

    - [Reference](https://angular.io/guide/architecture-modules)

Create a module:

```terminaml
ng generate module <module-name>
```

```typescript title="module-name.module.ts"
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

@NgModule({
  imports:      [ BrowserModule ],
  providers:    [ Logger ],
  declarations: [ AppComponent ],
  exports:      [ AppComponent ],
  bootstrap:    [ AppComponent ]
})
export class <module-name> { }
```
