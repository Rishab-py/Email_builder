import { Component } from '@angular/core';
import { BackendService } from '../services/backend.service';

@Component({
  selector: 'app-email-editor',
  templateUrl: './email-editor.component.html',
  styleUrls: ['./email-editor.component.css']
})
export class EmailEditorComponent {
  emailContent = {
    title: '',
    content: '',
    imageUrl: ''
  };

  constructor(private backendService: BackendService) {}

  uploadImage(event: Event): void {
    const file = (event.target as HTMLInputElement).files?.[0];
    if (file) {
      // Simulate image upload; you can use a real backend service here
      const reader = new FileReader();
      reader.onload = () => {
        this.emailContent.imageUrl = reader.result as string;
      };
      reader.readAsDataURL(file);
    }
  }

  saveContent(): void {
    console.log('Content to save:', this.emailContent);
    this.backendService.saveEmailContent(this.emailContent).subscribe((response) => {
      console.log('Response from backend:', response);
    });
  }
}
