import {Component} from '@angular/core';
import {MainContentComponent} from './infra/main-content/main-content.component';

@Component({
  selector: 'app-root',
  imports: [
    MainContentComponent
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'chat-fe';
}
