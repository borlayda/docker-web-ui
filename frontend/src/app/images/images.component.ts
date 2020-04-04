import { Component } from '@angular/core';
import { testData } from '../testData';

@Component({
  selector: 'images',
  templateUrl: './images.component.html',
  styleUrls: ['./images.component.css']
})
export class ImagesListComponent {
  images = testData.images;

  share() {
    window.alert('The product has been shared!');
  }
}
