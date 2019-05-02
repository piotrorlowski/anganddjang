import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {TodolistComponent} from "./todolist.component";
import {TodolistService} from "./todolist.service";

@NgModule({
  declarations: [
    AppComponent,
    TodolistComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [
    TodolistService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
