import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  title = 'angular-starter';
  items: any;

  constructor(private http: HttpClient) {
    this.getItems();
  }

  onGet() {
    this.getItems();
  }

  getItems() {
    this.http.get('http://localhost:5201/movies')
      .subscribe(
        data => {
          this.items = data;
        }
      );
  }

}

