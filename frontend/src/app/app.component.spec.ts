import { waitForAsync, ComponentFixture, TestBed } from '@angular/core/testing';

import { AppComponent } from './app.component';
import { CarsComponent } from './components/Car/cars.component';

describe('AppComponent', () => {
    let component: AppComponent;
    let fixture: ComponentFixture<AppComponent>;

    beforeEach(waitForAsync(() => {
        TestBed.configureTestingModule({
            declarations: [AppComponent]
        })
            .compileComponents();
    }));

    beforeEach(() => {
        fixture = TestBed.createComponent(AppComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });

    it('should have a title equal to "learningAngular"', () => {
        expect(component.title === "learningAngular").toBeTruthy();
    })
    
});