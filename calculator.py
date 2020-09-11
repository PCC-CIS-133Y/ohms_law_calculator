import tkinter as tk
import tkinter.ttk as ttk

class SimpleApp:
    def __init__(self, parent):
        # build ui
        top_frame = ttk.Frame(parent, padding=10)
        top_frame.grid(column=0, row=0, sticky="nsew")

        header_label = ttk.Label(top_frame, font="{Arial} 16 {bold}", text="Ohm's Law Calculator")
        header_label.grid(column=0, row=0, pady=3)

        input_frame = ttk.Frame(top_frame, padding=10)
        input_frame.grid(column=0, row=1)

        volts_label = ttk.Label(input_frame, text="Volts:")
        volts_label.grid(column=0, row=0, pady=3, sticky="e")
        ohms_label = ttk.Label(input_frame, text="Ohms:")
        ohms_label.grid(column=0, row=1, pady=3, sticky="e")

        volts_entry = ttk.Entry(input_frame)
        volts_entry.grid(column=1, row=0, pady=3)
        ohms_entry = ttk.Entry(input_frame)
        ohms_entry.grid(column=1, row=1, pady=3)

        button_frame = ttk.Frame(top_frame)
        button_frame.grid(column=0, row=2, sticky="e")
        button_frame.rowconfigure(0, weight=1)
        button_frame.columnconfigure(0, weight=1)

        clear_button = ttk.Button(button_frame, text="Clear", command=self.clear)
        clear_button.grid(column=0, row=0)
        ok_button = ttk.Button(button_frame, text="OK", command=self.calculate)
        ok_button.grid(column=1, row=0)

        # store widgets we need to access later as properties
        self.mainwindow = top_frame
        self.volts_entry = volts_entry
        self.ohms_entry = ohms_entry

    def open_answer_frame(self, parent, text):
        answer_top_frame = ttk.Frame(parent, padding=10)
        answer_top_frame.grid(column=0, row=0, sticky="nsew")

        answer_header_label = ttk.Label(answer_top_frame, font="{Arial} 16 {bold}", text="The Answer")
        answer_header_label.grid(column=0, row=0, pady=3)
        answer_label = ttk.Label(answer_top_frame, text=text, justify=tk.CENTER)
        answer_label.grid(column=0, row=1, pady=5)

    def calculate(self):
        print("Calculating.")
        # self.mainwindow = self.builder.get_object('output_frame')
        # self.builder.connect_callbacks(self)
        try:
            volts = float(self.volts_entry.get())
            ohms = float(self.ohms_entry.get())
            amps = volts / ohms
            watts = volts * amps
        except:
            top2 = tk.Toplevel(self.mainwindow)
            self.open_answer_frame(top2, "There was an error processing your inputs.\n"
                                         + "Please make sure that volts and ohms are both numbers\n"
                                         + "and that ohms is greater than 0." )
            return

        result_text = (str(volts) + " volts running through " + str(ohms) + " Ohms would be:\n\n"
                             + "{:.2f} Amps\n".format(amps)
                             + "{:.2f} Watts".format(watts))
        top2 = tk.Toplevel(self.mainwindow)
        self.open_answer_frame(top2, result_text)

    def clear(self):
        self.volts_entry.delete(0, tk.END)
        self.ohms_entry.delete(0, tk.END)

    def run(self):
        self.mainwindow.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Ohm's Law Calculator")
    app = SimpleApp(root)
    app.run()

