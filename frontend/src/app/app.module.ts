import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from "@angular/common";

import { AppComponent } from './app.component';
import { HeadBarComponent } from './headbar/headbar.component';

import { ContainersListComponent } from './containers/containers.component';
import { ImagesListComponent } from './images/images.component';
import { ProductListComponent } from './product-list/product-list.component';

@NgModule({
  imports: [
    BrowserModule,
    CommonModule,
    ReactiveFormsModule,
    RouterModule.forRoot([
      { path: '', component: ProductListComponent },
      { path: 'containers', component: ContainersListComponent },
      { path: 'images', component: ImagesListComponent }
    ])
  ],
  declarations: [
    AppComponent,
    HeadBarComponent,
    ContainersListComponent,
    ImagesListComponent,
    ProductListComponent
  ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
