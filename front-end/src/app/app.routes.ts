import {Routes} from '@angular/router';
import {ChatComponent} from './component/chat/chat.component';

export const routes: Routes = [
  { path: 'chat', component: ChatComponent },
  { path: '**', component: ChatComponent },
];
