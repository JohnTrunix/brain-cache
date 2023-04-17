# Angular Directives

!!! note

    Classes that add additional behavior to an element

    - [Reference](https://angular.io/guide/built-in-directives)

## NgClass

!!! note

    Adds and removes CSS classes on an HTML element.

    - [Reference](https://angular.io/guide/built-in-directives#adding-and-removing-classes-with-ngclass)

=== ".component.ts"

    ```typescript
    ...
    export class ngClassComponent {
        this.isSpecial = true;
    }
    ```

=== ".component.html"

    ```html
    <div [ngClass]="isSpecial ? 'special' : ''">
    	This div is special
    </div>
    ```

## NgStyle

!!! note

    Adds and removes styles inline on an HTML element.

    - [Reference](https://angular.io/guide/built-in-directives#setting-inline-styles-with-ngstyle)

=== ".component.ts"

    ```typescript
    ...
    export class ngStyleComponent {
        this.currentSyles = {
                'font-style' : this.canSave   ? 'italic' : 'normal',
                'font-weight': this.isSpecial ? 'bold'   : 'normal'
        };
    }
    ```

=== ".component.html"

    ```html
    <div [ngStyle]="currentStyles">
        This div is special
    </div>
    ```

## NgModel

!!! note

    Displays and updates the properties of a data-bound object.

    - [Reference](https://angular.io/guide/built-in-directives#displaying-and-updating-properties-with-ngmodel)

=== "app.module.ts"

    ```typescript
    import { FormsModule } from '@angular/forms';
    ...
    imports: [
        BrowserModule,
        FormsModule // <--- import into the NgModule
    ],
    ...
    ```

=== ".component.html"

    ```html
    <label for="example-ngModel">
        [(ngModel)]:
    </label>
    <input
        [(ngModel)]="currentItem.name"
        (ngModelChange)="setUppercaseName($event)"
        id="example-ngModel"
    >
    ```

## Structural Directives

!!! note

    Shape and reshape the DOM's structure, by adding, removing, and manipulating elements.

    - [Reference](https://angular.io/guide/built-in-directives#built-in-structural-directives)

### NgIf

```html
<app-item-detail *ngIf="isActive" [item]="item"> </app-item-detail>

<div *ngIf="nullCustomer">Hello, <span>{{nullCustomer}}</span></div>
```

### NgFor

```html
<div *ngFor="let item of items">{{item.name}}</div>
<app-item-detail *ngFor="let item of items" [item]="item"></app-item-detail>

<!-- with index -->
<div *ngFor="let item of items; let i=index">{{i + 1}} - {{item.name}}</div>
```

### NgSwitch

```html
<div [ngSwitch]="currentItem.feature">
    <app-stout-item
        *ngSwitchCase="'stout'"
        [item]="currentItem"
    ></app-stout-item>
    <app-device-item
        *ngSwitchCase="'slim'"
        [item]="currentItem"
    ></app-device-item>
    <app-lost-item
        *ngSwitchCase="'vintage'"
        [item]="currentItem"
    ></app-lost-item>
</div>
```
