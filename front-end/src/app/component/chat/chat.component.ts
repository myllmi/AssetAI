import {Component, inject} from '@angular/core';
import {FormsModule} from '@angular/forms';
import {SseService} from '../../service/sse.service';
import {Subscription} from 'rxjs';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {LLMResponse} from '../../model/objects';
import {marked} from 'marked';
import {DomSanitizer, SafeHtml} from '@angular/platform-browser';

@Component({
  selector: 'app-chat',
  imports: [
    FormsModule
  ],
  templateUrl: './chat.component.html',
  styleUrl: './chat.component.css'
})
export class ChatComponent {

  sseService = inject(SseService)
  httpClient = inject(HttpClient)
  sanitizer = inject(DomSanitizer)

  inputTerm: string = 'I need a service to get allocated drivers'
  private eventSub!: Subscription;
  content: string = ''
  htmlContent: SafeHtml = ''


  ngOnInit() {
    const url = 'http://localhost:5000/chat/listen'; // Replace with your server endpoint
    this.eventSub = this.sseService.getServerSentEvent(url).subscribe({
      next: (event) => {
        console.log(event.data);
        const obj_data = JSON.parse(event.data)
        this.content += obj_data['v']
        const responseLLM = marked(this.content)
        this.htmlContent = this.sanitizer.bypassSecurityTrustHtml(responseLLM.toString())
        console.log(this.content)
      },
      error: (err) => {
        console.error('SSE error:', err);
      }
    });
  }

  ngOnDestroy() {
    this.eventSub?.unsubscribe();
  }

  askLLM() {
    this.content = ''
    const headers = new HttpHeaders({
      'Content-Type': 'application/json; charset=utf-8',
      'Accept': 'application/json'
    });
    const requestOptions = {headers: headers};
    const bodyRequest = {
      _question: this.inputTerm
    }
    this.httpClient.post<LLMResponse>('http://localhost:5000/chat/q', bodyRequest, requestOptions)
      .subscribe(response => {
        console.log(response)
        }
      )
  }
}
