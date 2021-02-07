import { Component, OnInit } from '@angular/core';
import {Apollo, gql} from 'apollo-angular';


@Component({
  selector: 'app-cars',
  templateUrl: './cars.component.html',
  styleUrls: ['./cars.component.css']
})
export class CarsComponent implements OnInit {

  public cars: [];
  public carsHeaders: String[];
  private apiUrl = "http://localhost:8000/graphql/";

  constructor() { }

  ngOnInit(): void {
    this.fetchCars();
  }

  fetchCars(): void {
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    const graphql = JSON.stringify({
      query: `query getCars{
          cars {
            id
            brand
            model
            color
            year
        }

      }`,
    })

    const requestOptions: RequestInit = {
      method: 'POST',
      headers: myHeaders,
      body: graphql,
      redirect: 'follow'
    };

    fetch(this.apiUrl, requestOptions)
      .then(response => response.json())
      .then(result => {
        
        const { cars } = result.data;
        
        this.cars = cars;
        this.carsHeaders = [...Object.keys(cars[0]), 'actions'];

      })
      .catch(error => console.log('error', error));

  }

  createCar(event): void {
    event.preventDefault();
    
    const brand = (<HTMLInputElement>document.querySelector('#add-brand'))
    const model = (<HTMLInputElement>document.querySelector('#add-model'))
    const color = (<HTMLInputElement>document.querySelector('#add-color'))
    const year = (<HTMLInputElement>document.querySelector('#add-year'))

    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    const graphql = JSON.stringify({
      query: `mutation createCar {
  
        createCar(input:{
          brand: "${brand.value}"
          model:"${model.value}"
          color:"${color.value}"
          year:"${year.value}"}) {
          
          ok
          car {
            id
            brand
            model
            color
            year
            
          }
          
        }
        
      }`,
    })
    const requestOptions: RequestInit = {
      method: 'POST',
      headers: myHeaders,
      body: graphql,
      redirect: 'follow'
    };

    fetch(this.apiUrl, requestOptions)
      .then(response => response.json())
      .then(result => {

        this.fetchCars()
        brand.value = "";
        model.value = "";
        color.value = "";
        year.value = "";

      })
      .catch(error => console.log('error', error));
    
  }

  updateCar(event): void {

    event.preventDefault();
    const id: HTMLTableCellElement = event.target.parentElement.id;
    const brand = (<HTMLInputElement>document.querySelector('#edit-brand')).value.trim()
    const model = (<HTMLInputElement>document.querySelector('#edit-model')).value.trim()
    const color = (<HTMLInputElement>document.querySelector('#edit-color')).value.trim()
    const year = (<HTMLInputElement>document.querySelector('#edit-year')).value.trim()

    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    const graphql = JSON.stringify({
      query: `mutation updateCar {updateCar(id: ${id}, input: {brand: "${brand}",model:"${model}",color: "${color}",year:"${year}"}){
                    ok
                    car {
                      id
                      brand
                      model
                      color
                      year
                    }
                  }
                }`
    })
    const requestOptions: RequestInit = {
      method: 'POST',
      headers: myHeaders,
      body: graphql,
      redirect: 'follow'
    };

    fetch(this.apiUrl, requestOptions)
      .then(response => response.json())
      .then(result => this.fetchCars())
      .catch(error => console.log('error', error));

    this.closeForm();

  }

  deleteCar(event): void {

    if(confirm('Are you sure you wanna delete this row?')) {

      const cell: HTMLTableCellElement = event.target.parentElement.parentElement.parentElement;
      const myHeaders = new Headers();
      myHeaders.append("Content-Type", "application/json");

      const graphql = JSON.stringify({
        query: `mutation deleteCar {
                      deleteCar(id: ${cell.id}) {
                        ok
                      }
                    }`,
      })
      const requestOptions: RequestInit = {
        method: 'POST',
        headers: myHeaders,
        body: graphql,
        redirect: 'follow'
      };

      fetch(this.apiUrl, requestOptions)
        .then(response => response.json())
        .then(result => this.fetchCars())
        .catch(error => console.log('error', error));
      
    }

  }

  openForm(event): void {
    
    const form = (<HTMLFormElement>document.querySelector('.edit-form'));
    const inputs = form.querySelectorAll('input');
    const row = event.target.parentElement.parentElement.parentElement.parentElement;
    const dataId = row.querySelector('td').textContent;
    const cells = Array.from(row.querySelectorAll('td')).slice(1, 5);
    const cellData = []

    form.id = dataId;

    cells.forEach((cell: HTMLTableCellElement) => {

      cellData.push(cell.textContent);

    })

    inputs.forEach((input: HTMLInputElement, index)=> {
      input.value = cellData[index].trim();
    })
    
    if(form.classList.contains('invisible'))
      form.classList.remove('invisible');

  }

  closeForm(): void {

    const form = (<HTMLFormElement>document.querySelector('.edit-form'));

    if(!form.classList.contains('invisible'))
      form.classList.add('invisible')

  }

}
