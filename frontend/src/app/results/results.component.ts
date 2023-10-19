import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-results',
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.css']
})
export class ResultsComponent  {
  searchQuery: string = '';
  restaurants: any[] = [];

  constructor(private route: ActivatedRoute, private apiService: ApiService) { 
    this.route.queryParams.subscribe(params => {
      this.searchQuery = params['query'];
      // Now, this.searchQuery contains the search query passed from the search component
    });
    console.log('Search Query:', this.searchQuery);

    this.apiService.getSearchResult(this.searchQuery).subscribe(
      data => {
        this.restaurants = data;
      },
      error => {
        console.error(error);
      }
    );

  }
}
