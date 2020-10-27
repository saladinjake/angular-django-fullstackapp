import { Component, OnInit } from '@angular/core';
import { PostService } from 'src/app/services/post-service.service';

@Component({
  selector: 'app-add-post',
  templateUrl: './add-post.component.html',
  styleUrls: ['./add-post.component.css']
})
export class AddPostComponent implements OnInit {

  post = {
    title: '',
    description: '',
    published: false
  };
  submitted = false;

  constructor(private postService: PostService) { }

  ngOnInit(): void {
  }

  savePost(): void {
    const data = {
      title: this.post.title,
      description: this.post.description
    };

    this.postService.createPost(data)
      .subscribe(
        response => {

          this.submitted = true;
        },
        error => {
          console.log(error);
        });
  }

  newPostReset(): void {
    this.submitted = false;
    this.post = {
      title: '',
      description: '',
      published: false
    };
  }

  ngOnInit(): void {
  }

}
