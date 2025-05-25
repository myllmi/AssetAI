import {Component} from '@angular/core';
import {FormsModule} from '@angular/forms';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {LLMResponse} from '../../../model/objects';
import {marked} from 'marked';
import {DomSanitizer, SafeHtml} from '@angular/platform-browser';

@Component({
  selector: 'app-input-chat',
  imports: [
    FormsModule
  ],
  templateUrl: './input-chat.component.html',
  styleUrl: './input-chat.component.css'
})
export class InputChatComponent {

  constructor(
    private readonly httpClient: HttpClient,
    private readonly sanitizer: DomSanitizer) {
  }

  inputTerm: string = 'I need a service to get allocated drivers'
  htmlContent: SafeHtml = ''

  askLLM() {
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
          const responseLLM = marked(response.data.llm)
          this.htmlContent = this.sanitizer.bypassSecurityTrustHtml(responseLLM.toString())
          // console.log(response)
        }
      )
  }
}
