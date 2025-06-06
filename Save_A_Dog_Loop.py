"""
🐾 Dog Rescue Donation Dialog
👤 Author: PJ (@pjprogrammers)
📄 License: MIT
🔗 GitHub Profile: https://github.com/pjprogrammers
🔗 GitHub Repo: https://github.com/pjprogrammers/python

📝 Description:
A simple interactive dialog using tkinter message boxes that prompts the user
to decide about saving a starving dog by donating $5. The dialog loops logically
until the user makes a conclusive choice.

⚙️ How It Works:
- The user is asked if they want to save a starving dog.
- If yes, asked if they want to donate $5.
- If no, they're asked multiple follow-ups about their choice with warnings.
- Uses loops to ensure the conversation continues until a clear decision is reached.

🎯 Purpose:
To demonstrate GUI dialog handling and control flow with loops in Python using tkinter,
while practicing good user interaction design.

"""

from tkinter import Tk, messagebox as mg

def dog_rescue_dialog():
    """
    Controls the full dialog loop for dog rescue donation interaction.
    """
    root = Tk()
    root.withdraw()  # Hide the main Tk window
    
    while True:
        # Step 1: Ask if user wants to save the dog
        save = mg.askquestion(title="Notice!", message="There is a dog about to die of starvation.\nWould you like to save it?", icon='info')
        
        if save == 'yes':
            # Step 2: Ask if user wants to donate $5
            donate = mg.askquestion(title="Donation", message="Would you like to donate $5 to feed it?")
            
            if donate == 'yes':
                mg.showinfo(title="Thank You", message="Thank you for your donation! 🐶❤️")
                break  # End conversation positively
            
            else:
                # Step 3: If user refuses to donate
                want_die = mg.askquestion(title="Notice!", message="Do you want the dog to die?")
                
                if want_die == 'yes':
                    confirm = mg.askokcancel(title="Warning", message="Your actions might take someone's life.")
                    if confirm:
                        mg.showinfo(title="Information", message="The dog has died. 🐾💔")
                        mg.askquestion(title="", message="Do you feel happy now?")
                        mg.showwarning(title="", message="You are evil.")
                        mg.showerror(title="Notice", message="You have obtained rewards for KILLING a dog.")
                        mg.showinfo(title="Rewards", message="You have successfully obtained a seat in hell.")
                        break  # End conversation negatively
                    else:
                        # User changed mind at last moment
                        continue  # Loop again to restart
                else:
                    # User wants to save the dog after refusing donation
                    continue  # Loop again to restart

        else:
            # User does not want to save dog initially
            want_die = mg.askquestion(title="Notice!", message="Do you want the dog to die?")
            
            if want_die == 'yes':
                confirm = mg.askokcancel(title="Warning", message="Your actions might take someone's life.")
                if confirm:
                    mg.showinfo(title="Information", message="The dog has died. 🐾💔")
                    mg.askquestion(title="", message="Do you feel happy now?")
                    mg.showwarning(title="", message="You are evil.")
                    mg.showerror(title="Notice", message="You have obtained rewards for KILLING a dog.")
                    mg.showinfo(title="Rewards", message="You have successfully obtained a seat in hell.")
                    break  # End conversation negatively
                else:
                    continue  # Loop again to restart
            else:
                # User doesn't want dog to die and didn't want to save initially
                # Ask about donating $5 anyway
                donate_anyway = mg.askquestion(title="Notice", message="Then do you want to donate $5 to save it?")
                if donate_anyway == 'yes':
                    mg.showinfo(title="Thank You", message="Thank you for your donation! 🐶❤️")
                    break
                else:
                    continue  # Loop again to restart

    root.destroy()  # Close the hidden root window

if __name__ == "__main__":
    dog_rescue_dialog()
