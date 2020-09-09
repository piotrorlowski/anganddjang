import { TodoListService } from "./todolist.service";
import { Component } from "@angular/core";

@Component({
  selector: 'todolist',
  template: '<h2 *ngFor="let element of toDoList">{{ element }}</h2>',
})

export class TodoListComponent {
  title = "TodoList";
  toDoList = [];

  constructor(service: TodoListService) {
    this.toDoList = service.getToDoList();
  }
}
