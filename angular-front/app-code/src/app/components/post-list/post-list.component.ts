import { Component, OnInit } from '@angular/core';
import { PostService } from '../../services/post-service.service';


@Component({
  selector: 'app-post-list',
  templateUrl: './post-list.component.html',
  styleUrls: ['./post-list.component.css']
})
export class PostListComponent implements OnInit {

  posts: any;
  currentPost = null;
  currentIndex = -1;
  title = '';

  constructor(private postService: PostService) { }

  ngOnInit(): void {
    this.getPosts();
  }

  getPosts(): void {
    this.postService.getAllPosts()
      .subscribe(
        data => {
          this.posts = data;

        },
        error => {
          console.log(error);
        });
  }

  refreshList(): void {
    this.getPosts();
    this.currentPost = null;
    this.currentIndex = -1;
  }

  setPostInView(tutorial, index): void {
    this.currentPost = tutorial;
    this.currentIndex = index;
  }

  removeAllPosts(): void {
    this.postService.deleteAll()
      .subscribe(
        response => {
          console.log(response);
          this.getPosts();
        },
        error => {
          console.log(error);
        });
  }

  searchTitle(): void {
    this.postService.findByTitle(this.title)
      .subscribe(
        data => {
          this.posts = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }


}
