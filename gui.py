__author__ = 'james benitez'

from tkinter import *
from tkinter import ttk, messagebox
from svm_handler import SVMHandler
from mail import sendemail
import threading


def run_gui():
    root = Tk()
    root.title("SVM GUI")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # SVM HANDLER
    svm_handler = SVMHandler()

    def activate_train():
        def training():
            train_bar.start()
            svm_handler.training()
            train_bar.stop()
            train_btn['state'] = "normal"
            test_btn['state'] = "normal"

        train_btn['state'] = "disabled"
        threading.Thread(target=training).start()

    def activate_test():
        def testing():
            test_bar.start()
            svm_handler.testing()
            test_bar.stop()
            test_btn['state'] = "normal"
            send_email_btn['state'] = "normal"

        test_btn['state'] = "disabled"
        threading.Thread(target=testing).start()

    def send_mail():
        def sending_email():
            msg = f"I Got an error rate of {round(svm_handler.error_rate, 2)}%"
            sendemail(msg)
            send_email_btn['state'] = "normal"
            messagebox.showinfo('Success', 'Mail sent successfully!!!')

        threading.Thread(target=sending_email).start()

    # BUTTONS
    train_btn = ttk.Button(mainframe, text="TRAIN", command=activate_train)
    test_btn = ttk.Button(mainframe, text="TEST", state="disabled", command=activate_test)
    send_email_btn = ttk.Button(mainframe, text="SEND RESULT", state="disabled", command=send_mail)

    train_btn.grid(column=0, row=1, sticky=W)
    test_btn.grid(column=0, row=2, sticky=W)
    send_email_btn.grid(column=1, row=3, sticky=W)

    # PROGRESS BARS
    train_bar = ttk.Progressbar(mainframe, length=100, style='black.Horizontal.TProgressbar', mode="indeterminate")
    test_bar = ttk.Progressbar(mainframe, length=100, style='black.Horizontal.TProgressbar', mode="indeterminate")
    train_bar.grid(column=1, row=1)
    test_bar.grid(column=1, row=2)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()


if __name__ == "__main__":
    run_gui()
