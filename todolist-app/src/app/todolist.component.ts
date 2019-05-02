import {TodolistService} from "./todolist.service";
import {Component} from "@angular/core";

@Component({
  selector: 'todolist',
  template: '<h1 *ngFor="let list of toDoList">{{ list }}</h1>',
})

export class TodolistComponent {
  title = "Todolist";
  toDoList;

  constructor() {
    let service = new TodolistService();
    this.toDoList = service.getToDoList();
  }
}
