import tkinter as tk

def main():
    root = tk.Tk()

    account_section = tk.Frame(root)
    account_section.grid(row=0, column=0)

    target_section = tk.Frame(root)
    target_section.grid(row=1, column=0)
    
    user_name_label = tk.Label(account_section, text="User Name:")
    user_name_label.grid(row=0, column=0)
    user_name_entry = tk.Entry(account_section)
    user_name_entry.grid(row=0, column=1)

    pass_word_label = tk.Label(account_section, text="Password:")
    pass_word_label.grid(row=1, column=0)
    pass_word_entry = tk.Entry(account_section)
    pass_word_entry.grid(row=1, column=1)

    otp_label = tk.Label(account_section, text="OTP:")
    otp_label.grid(row=2, column=0)
    otp_entry = tk.Entry(account_section)
    otp_entry.grid(row=2, column=1)

    login_button = tk.Button(account_section, text="Login")
    login_button.grid(row=3, column=1)

    target_link_label = tk.Label(target_section, text="Target Link:")
    target_link_label.grid(row=0, column=0)
    target_link_entry = tk.Entry(target_section)
    target_link_entry.grid(row=0, column=1)

    download_button = tk.Button(target_section, text="Download")
    download_button.grid(row=1, column=1)

    def popup_message(message):
        popup = tk.Toplevel()
        popup.title("Popup Window")
        label = tk.Label(popup, text=message)
        label.pack(side="top", fill="x", pady=10)
        ok_button = tk.Button(popup, text="OK", command=popup.destroy)
        ok_button.pack()

    download_button.config(command=lambda: popup_message("Download started"))
        

    


    root.mainloop()

if __name__ == "__main__":
    main()