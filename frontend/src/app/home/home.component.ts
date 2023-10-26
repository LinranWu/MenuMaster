import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  searchQuery: string = '';
  constructor(private router: Router) {}

  navigateToResults() {
    console.log('Search Query:', this.searchQuery);
    this.router.navigate(['/results', this.searchQuery ]); // Navigate to the results page
  }
}
