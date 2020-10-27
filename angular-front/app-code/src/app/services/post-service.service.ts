import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

const baseUrl = 'http://localhost:8080/api/posts';

@Injectable({
  providedIn: 'root'
})
export class TutorialService {

  constructor(private http: HttpClient) { }

  getAllPosts(): Observable<any> {
    return this.http.get(baseUrl);
  }

  getById(id): Observable<any> {
    return this.http.get(`${baseUrl}/${id}`);
  }

  createPost(data): Observable<any> {
    return this.http.post(baseUrl, data);
  }

  updatePost(id, data): Observable<any> {
    return this.http.put(`${baseUrl}/${id}`, data);
  }

  deletePost(id): Observable<any> {
    return this.http.delete(`${baseUrl}/${id}`);
  }

  deleteAll(): Observable<any> {
    return this.http.delete(baseUrl);
  }

  findByTitle(title): Observable<any> {
    return this.http.get(`${baseUrl}?title=${title}`);
  }
}
