import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verdana", 35)


class GUI(tk.Tk):

    # __init__ function for class GUI
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        #self.resizable(False, False)
        self.title('Smart City Visualisation')
        window_Width = self.winfo_screenwidth()
        window_Height = self.winfo_screenheight()
        app_Width = 1100
        app_Height = 700

        x = int((window_Width / 2) - (app_Width / 2))
        y = int((window_Height / 2) - (app_Height / 2))

        self.geometry("{}x{}+{}+{}".format(app_Width, app_Height, x, y))

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting of the different page layouts
        for F in (HomePage, Page1, Page2):
            frame = F(container, self)

            # initializing frame of that object from all the pages within the for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    # to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# HomePage window frame
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')

        # Create left and right frames
        left_frame = tk.Frame(self, width=225, height=694, bg='royalblue', highlightbackground="deepskyblue", highlightthickness=5)
        left_frame.grid(row=0, column=0, padx=2, pady=3)

        right_frame = tk.Frame(self, width=865, height=694, bg='deepskyblue', highlightbackground="royalblue", highlightthickness=5)
        right_frame.grid(row=0, column=1, padx=2, pady=3)

        label = tk.Label(right_frame, text="Home Page", width=23, font=('Raleway', 35, 'bold'), bg='deepskyblue')
        label.grid(row=0, column=0, padx=42, pady=15)

        right_inside_frame = tk.Frame(right_frame, width=755, height=584, bg='lightskyblue')
        right_inside_frame.grid(row=1, column=0, pady=5, padx=50)

        #label = tk.Label(right_inside_frame, text="HOME PAGE\n\n\n\n\n\n\n\n\n", width=23, font=LARGEFONT, bg='lightskyblue')
        #label.grid(row=0, column=0, padx=42, pady=6)



# second window frame page1
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 1", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="StartPage",
                             command=lambda: controller.show_frame(HomePage))

        # putting the button in its place
        # by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text="Page 2",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Page 1",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(HomePage))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    software = GUI()
    software.mainloop()
