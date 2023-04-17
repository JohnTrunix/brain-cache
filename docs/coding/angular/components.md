# Angular Components

!!! note

    Components are small building blocks.

    - [Reference](https://angular.io/guide/architecture-components)

## General

Create a component:

```terminal
ng generate component <component-name>
```

=== ".component.ts"

    ```typescript
    import { Component } from "@angular/core";

    @Component({
        selector: "hello-world",
        templateUrl: "hello-world.component.html",
        styleUrls: ["hello-world.component.css"],
    })
    export class HelloWorldComponent {
        // The code in this class drives the component's behavior.
    }
    ```

=== ".component.html"

    ```html
    <h2>Hello World</h2>
    <p>This is my first component!</p>
    <p class="a">Hello!</p>
    ```

=== ".component.css"

    ```css title=".component.css"
    h2 {
        color: blue;
    }
    .a {
        margin: 10px;
    }
    ```

=== "Component Call"

    ```typescript title="other.component.html"
    <app-hello-world></app-hello-world>
    ```

## Interpolation

!!! note

    Displaying `variables` in the html template `{{ variable }}`

    - [Reference](https://angular.io/guide/interpolation)

=== ".component.ts"

    ```typescript
    import { Component } from "@angular/core";

    @Component({
        selector: "hello-world-interpolation",
        templateUrl: "./hello-world-interpolation.component.html",
    })
    export class HelloWorldInterpolationComponent {
        message = "Hello, World!";
    }
    ```

=== ".component.html"

    ```html
    <h2>{{ message }}</h2>
    ```

=== "Output"

    ```html
    <h2>Hello, World!</h2>
    ```

### Data Pipes

!!! note

    Data pipes are used to transform `strings` in the html template `{{ variable | pipe }}`

    - [Reference](https://angular.io/guide/pipes)

| Pipe            | Description                   |
| --------------- | ----------------------------- |
| `DatePipe`      | formats a date value          |
| `UpperCasePipe` | transforms text to upper case |
| `LowerCasePipe` | transforms text to lower case |
| `CurrencyPipe`  | formats a number as currency  |
| `DecimalPipe`   | formats a number as decimal   |
| `PercentPipe`   | formats a number as percent   |

=== ".component.ts"

    ```typescript
    import { Component } from "@angular/core";

    @Component({
        selector: "hello-world-pipes",
        templateUrl: "./hello-world-pipes.component.html",
    })
    export class HelloWorldPipesComponent {
        today = new Date();
        price = 1.23;
        percent = 0.456;
    }
    ```

=== ".component.html"

    ```html
    <h2>{{ today | date }}</h2>
    <p>{{ price | currency }}</p>
    <p>{{ percent | percent }}</p>
    ```

=== "Output"

    ```html
    <h2>2021-03-01</h2>
    <p>$1.23</p>
    <p>45.6%</p>
    ```

### Custom Data Pipes

```terminal
ng generate pipe <pipe-name>
```

```typescript title="pipe-name.pipe.ts"
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({name: 'exponentialStrength})
export class ExponentialStrengthPipe implements PipeTransform {
	transform(value: number, exponent = 1): number {
		return Math.pow(value, exponent);
	}
}
```

## Property Binding

!!! note

    Binding `properties` from the html template `[property]="variable"`

    - [Reference](https://angular.io/guide/property-binding)

=== ".component.ts"

    ```typescript
    ...
    export class HelloWorldBindingsComponent {
    fontColor = 'blue';
    sayHelloId = 1;
    }
    ```

=== ".component.html"

    ```html
    <p
        [id]="sayHelloId"
        [style.color]="fontColor">
        You can set color in the component!
    </p>
    ```

## Event Binding

!!! note

    Binding `events` from the html template `(event)="function"`

    - [Reference](https://angular.io/guide/event-binding)

=== ".component.ts"

    ```typescript
    ...
    export class HelloWorldBindingsComponent {
        canClick = false;
        message = 'Hello, World';
        sayMessage() {
            alert(this.message);
        }
    }
    ```

=== ".component.html"

    ```html
    <button
        type="button"
        [disabled]="canClick"
        (click)="sayMessage()">
        Trigger alert message
    </button>
    ```
