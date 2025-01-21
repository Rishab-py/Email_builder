import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { provideHttpClient, withInterceptorsFromDi } from '@angular/common/http';

import { AppComponent } from './app.component';
import { EmailEditorComponent } from './email-editor/email-editor.component'; // Updated import path

@NgModule({
  declarations: [
    AppComponent,
    EmailEditorComponent // Declaring the component
  ],
  imports: [
    BrowserModule,
    FormsModule // Enables two-way data binding
  ],
  providers: [
    provideHttpClient(withInterceptorsFromDi()) // Configures HTTP client with interceptors
  ],
  bootstrap: [AppComponent] // Bootstrapping the main app component
})
export class AppModule {}
