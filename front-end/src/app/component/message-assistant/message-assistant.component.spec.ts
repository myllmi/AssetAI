import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MessageAssistantComponent } from './message-assistant.component';

describe('MessageAssistantComponent', () => {
  let component: MessageAssistantComponent;
  let fixture: ComponentFixture<MessageAssistantComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MessageAssistantComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MessageAssistantComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
