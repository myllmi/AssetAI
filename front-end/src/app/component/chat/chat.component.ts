import {Component, inject} from '@angular/core';
import {FormsModule} from '@angular/forms';
import {SseService} from '../../service/sse.service';
import {Subscription} from 'rxjs';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {LLMResponse} from '../../model/objects';
import {marked} from 'marked';
import {DomSanitizer, SafeHtml} from '@angular/platform-browser';
import {InputChatComponent} from '../input-chat/input-chat.component';

@Component({
  selector: 'app-chat',
  imports: [
    FormsModule,
    InputChatComponent
  ],
  templateUrl: './chat.component.html',
  styleUrl: './chat.component.css'
})
export class ChatComponent {

  sseService = inject(SseService)
  sanitizer = inject(DomSanitizer)

  private eventSub!: Subscription;
  content: string = ''
  htmlContent: SafeHtml = ''


  ngOnInit() {
    const url = 'http://localhost:5000/chat/listen?token=ABC123'; // Replace with your server endpoint

    this.eventSub = this.sseService.getServerSentEvent(url).subscribe({
      next: (event) => {
        console.log(event.data);
        const obj_data = JSON.parse(event.data)
        this.content += obj_data['v']
        const responseLLM = marked(this.content)
        const htmlContent = this.sanitizer.bypassSecurityTrustHtml(responseLLM.toString())
        const elementAssistant = document.getElementById("ABC123");
        elementAssistant!.innerHTML = responseLLM.toString();
      },
      error: (err) => {
        console.error('SSE error:', err);
      }
    });
  }

  ngOnDestroy() {
    this.eventSub?.unsubscribe();
  }

}
