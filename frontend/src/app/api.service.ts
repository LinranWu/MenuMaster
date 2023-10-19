import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://127.0.0.1:5000'; // flask port

  constructor(private http: HttpClient) { }

  getSearchResult(searchQuery: string): Observable<any> {
    const url = `${this.apiUrl}?query=${searchQuery}`;
    return this.http.get(url);
  }
}