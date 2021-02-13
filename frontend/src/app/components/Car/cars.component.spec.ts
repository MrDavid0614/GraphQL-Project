import { waitForAsync, ComponentFixture, TestBed } from '@angular/core/testing';

import { CarsComponent } from './cars.component';

describe('CarsComponent', () => {
    let component: CarsComponent;
    let fixture: ComponentFixture<CarsComponent>;

    beforeEach(waitForAsync(() => {
        TestBed.configureTestingModule({
            declarations: [CarsComponent]
        })
            .compileComponents();
    }));

    beforeEach(() => {
        fixture = TestBed.createComponent(CarsComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });
    
    it('should have an undefined list of cars', () => {
        expect(component.cars).toBeUndefined();
    })

    it('should have a h1 tag that contains "Cars Info:" text', () => {

        const title = document.querySelector('h1');
        expect(title.textContent).toEqual('Cars Info:');

    })

    it('should have an add car form with a h1 as him first child', ()=>{

        const form = document.querySelector('form:not(.edit-form)');
        expect(form.firstChild).toEqual(form.querySelector('h1'))
    })

});