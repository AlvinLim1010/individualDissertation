import tkinter as tk


class HomePageWidget:

    def inner_homepage_widget(self, frame):
        intro_text = "• Welcome to the Visualisation and Prediction on Air Quality, VPAQ\n" \
                     "Software. There are a total of five pages, Home, Historical Vis, Live Vis," \
                     "\nAI Prediction, and AI Model Vis."
        introduction_text = tk.Label(frame, text=intro_text, width=58, height=22,
                                     font=('Raleway', 15, 'bold'), bg='lightskyblue', anchor='nw')
        introduction_text.grid(row=0, column=0, padx=(33, 32), pady=(24, 25), sticky='w')