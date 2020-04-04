import { Component } from '@angular/core';
import { testData } from '../testData';

@Component({
  selector: 'containers',
  templateUrl: './containers.component.html',
  styleUrls: ['./containers.component.css']
})
export class ContainersListComponent {
  containers = testData.containers;

  share() {
    window.alert('The product has been shared!');
  }
}
