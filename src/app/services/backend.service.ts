import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BackendService {
  private backendUrl = 'http://localhost:3000/email-content';

  constructor(private http: HttpClient) {}

  getEmailContent(): Observable<any> {
    return this.http.get(this.backendUrl);
  }

  saveEmailContent(content: any): Observable<any> {
    return this.http.post(this.backendUrl, content);
  }
}
