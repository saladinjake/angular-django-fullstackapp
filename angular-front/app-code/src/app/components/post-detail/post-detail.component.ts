import { Component, OnInit } from '@angular/core';
import { PostService } from 'src/app/services/post-service.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-post-detail',
  templateUrl: './post-detail.component.html',
  styleUrls: ['./post-detail.component.css']
})
export class PostDetailComponent implements OnInit {

  currentPost = null;
  message = '';

  constructor(
    private postService: PostService,
    private route: ActivatedRoute,
    private router: Router) { }

  ngOnInit(): void {
    this.message = '';
    this.getPostById(this.route.snapshot.paramMap.get('id'));
  }

  getPostById(id): void {
    this.postService.getById(id)
      .subscribe(
        data => {
          this.currentPost = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

  updatePublished(status): void {
    const data = {
      title: this.currentPost.title,
      description: this.currentPost.description,
      published: status
    };

    this.postService.updatePost(this.currentPost.id, data)
      .subscribe(
        response => {
          this.currentTutorial.published = status;
          console.log(response);
        },
        error => {
          console.log(error);
        });
  }

  updatePost(): void {
    this.postService.updatePost(this.currentPost.id, this.currentPost)
      .subscribe(
        response => {
          console.log(response);
          this.message = 'This post was update was successful!';
        },
        error => {
          console.log(error);
        });
  }

  deletePost(): void {
    this.postService.deletePost(this.currentPost.id)
      .subscribe(
        response => {
          console.log(response);
          this.router.navigate(['/posts']);
        },
        error => {
          console.log(error);
        });
  }

}
