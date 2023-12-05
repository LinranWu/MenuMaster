import { ActivatedRoute } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-results',
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.css']
})
export class ResultsComponent implements OnInit {
  searchQuery: string='';
  response:any;
  parsedResponse: any[] = [];
  constructor(private apiService: ApiService, private route: ActivatedRoute) { }

  ngOnInit() {
    // Retrieve the searchQuery parameter from the route
    this.route.params.subscribe(params => {
      this.searchQuery = params['searchQuery'];
      
      const requestObject = {
        inputText: this.searchQuery
      };

      // Call the API service with the searchQuery
      this.apiService.getSearchResult(requestObject).subscribe(
        data => {
          this.response = data;
          console.log('API Response:', data);
          this.parsedResponse = this.response.response;
        },
        error => {
          console.error(error);
        }
      );
      
    });
  }
}
