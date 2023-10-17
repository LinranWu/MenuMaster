import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-results',
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.css']
})
export class ResultsComponent  {
  searchQuery: string = '';

  constructor(private route: ActivatedRoute) { 
    this.route.queryParams.subscribe(params => {
      this.searchQuery = params['query'];
      // Now, this.searchQuery contains the search query passed from the search component
    });
    console.log('Search Query:', this.searchQuery);

  }
}
