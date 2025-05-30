import {Component, inject} from '@angular/core';
import {FormsModule} from '@angular/forms';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {LLMResponse} from '../../model/objects';
import {marked} from 'marked';
import {DomSanitizer, SafeHtml} from '@angular/platform-browser';
import { v4 as uuidv4 } from 'uuid';

@Component({
  selector: 'app-input-chat',
  imports: [
    FormsModule
  ],
  templateUrl: './input-chat.component.html',
  styleUrl: './input-chat.component.css'
})
export class InputChatComponent {

  httpClient = inject(HttpClient)
  sanitizer = inject(DomSanitizer)

  inputTerm: string = ''
  htmlContent: SafeHtml = ''

  askLLM() {
    const idTag = uuidv4()
    this.messageUser()
    this.messageAssistant(idTag)
    const headers = new HttpHeaders({
      'Content-Type': 'application/json; charset=utf-8',
      'Accept': 'application/json'
    });
    const requestOptions = {headers: headers};
    const bodyRequest = {
      _question: this.inputTerm,
      _tag: idTag
    }
    this.httpClient.post<LLMResponse>('http://localhost:5000/chat/q', bodyRequest, requestOptions)
      .subscribe(response => {
          const responseLLM = marked(response.data.llm)
          this.htmlContent = this.sanitizer.bypassSecurityTrustHtml(responseLLM.toString())
        }
      )
  }

  messageUser() {
    const tagText = document.createTextNode(this.inputTerm);
    const tagDivText = document.createElement("div");
    tagDivText.setAttribute("class", "text");
    const tagDivAvatar = document.createElement("div");
    tagDivAvatar.setAttribute("class", "avatar");
    const tagAvatar = document.createTextNode("👤");
    const tagDivMessage = document.createElement("div");
    tagDivMessage.setAttribute("class", "message user");
    tagDivText.appendChild(tagText);
    tagDivAvatar.appendChild(tagAvatar);
    tagDivMessage.appendChild(tagDivAvatar);
    tagDivMessage.appendChild(tagDivText);
    const elementChat = document.getElementById("messageContainer");
    elementChat!.appendChild(tagDivMessage);
  }

  messageAssistant(idDiv: string) {
    const tagDivText = document.createElement("div");
    tagDivText.setAttribute("class", "text");
    tagDivText.setAttribute("id", idDiv);
    const tagDivAvatar = document.createElement("div");
    tagDivAvatar.setAttribute("class", "avatar");
    const tagAvatar = document.createTextNode("🤖");
    const tagDivMessage = document.createElement("div");
    tagDivMessage.setAttribute("class", "message assistant");
    tagDivAvatar.appendChild(tagAvatar);
    tagDivMessage.appendChild(tagDivAvatar);
    tagDivMessage.appendChild(tagDivText);
    const elementChat = document.getElementById("messageContainer");
    elementChat!.appendChild(tagDivMessage);
  }

}
