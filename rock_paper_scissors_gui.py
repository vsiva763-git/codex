"""
Rock Paper Scissors GUI Game using Tkinter
"""
import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player, computer):
    if player == computer:
        return 'tie'
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return 'player'
    else:
        return 'computer'

class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        self.player_score = 0
        self.computer_score = 0
        
        # Title Label
        title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)
        
        # Score Label
        self.score_label = tk.Label(root, text=f"Player: {self.player_score}  |  Computer: {self.computer_score}", 
                                     font=("Arial", 16))
        self.score_label.pack(pady=10)
        
        # Result Label
        self.result_label = tk.Label(root, text="Choose your move!", font=("Arial", 14))
        self.result_label.pack(pady=10)
        
        # Choice Label
        self.choice_label = tk.Label(root, text="", font=("Arial", 12))
        self.choice_label.pack(pady=5)
        
        # Button Frame
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)
        
        # Buttons
        rock_btn = tk.Button(button_frame, text="🪨 Rock", font=("Arial", 14), width=10, height=2,
                            command=lambda: self.play('rock'), bg="#e74c3c", fg="white")
        rock_btn.grid(row=0, column=0, padx=10)
        
        paper_btn = tk.Button(button_frame, text="📄 Paper", font=("Arial", 14), width=10, height=2,
                             command=lambda: self.play('paper'), bg="#3498db", fg="white")
        paper_btn.grid(row=0, column=1, padx=10)
        
        scissors_btn = tk.Button(button_frame, text="✂️ Scissors", font=("Arial", 14), width=10, height=2,
                                command=lambda: self.play('scissors'), bg="#2ecc71", fg="white")
        scissors_btn.grid(row=0, column=2, padx=10)
        
        # Reset Button
        reset_btn = tk.Button(root, text="Reset Game", font=("Arial", 12), command=self.reset_game,
                             bg="#95a5a6", fg="white")
        reset_btn.pack(pady=10)
        
    def play(self, player_choice):
        computer_choice = get_computer_choice()
        winner = determine_winner(player_choice, computer_choice)
        
        # Update choice display
        self.choice_label.config(text=f"You chose: {player_choice.upper()}  |  Computer chose: {computer_choice.upper()}")
        
        # Update result and scores
        if winner == 'player':
            self.player_score += 1
            self.result_label.config(text="🎉 You Win This Round!", fg="green")
        elif winner == 'computer':
            self.computer_score += 1
            self.result_label.config(text="💻 Computer Wins This Round!", fg="red")
        else:
            self.result_label.config(text="🤝 It's a Tie!", fg="orange")
        
        # Update score display
        self.score_label.config(text=f"Player: {self.player_score}  |  Computer: {self.computer_score}")
    
    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.score_label.config(text=f"Player: {self.player_score}  |  Computer: {self.computer_score}")
        self.result_label.config(text="Choose your move!", fg="black")
        self.choice_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGUI(root)
    root.mainloop()
