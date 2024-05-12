import tkinter as tk

def calculate_scores():
    try:
        # Convert input to float and calculate total scores
        player1_round1 = float(round1_1_entry.get())
        player1_round2 = float(round2_1_entry.get())
        player1_round3 = float(round3_1_entry.get())
        player1_round4 = float(round4_1_entry.get())

        player2_round1 = float(round1_2_entry.get())
        player2_round2 = float(round2_2_entry.get())
        player2_round3 = float(round3_2_entry.get())
        player2_round4 = float(round4_2_entry.get())

        total_score_player1 = player1_round1 + player1_round2 + player1_round3 + player1_round4
        total_score_player2 = player2_round1 + player2_round2 + player2_round3 + player2_round4

        # Get player names
        player_name1 = player_name1_entry.get()
        player_name2 = player_name2_entry.get()

        # Determine winner
        winner = ""
        if total_score_player1 > total_score_player2:
            winner = player_name1
        elif total_score_player1 < total_score_player2:
            winner = player_name2
        else:
            winner = "It's a tie!"

        # Update result label
        result_label.config(text=f"Final Results:\n\n"
                   f"{player_name1}'s Total Score: {total_score_player1}\n"
                   f"{player_name2}'s Total Score: {total_score_player2}\n\n"
                   f"Winner: {winner}")



    except ValueError:
        result_label.config(text="Error: Please enter valid numeric scores.", fg="red")
    

def clear_entries():
    # Clear all entry fields
    player_name1_entry.delete(0, tk.END)
    player_name2_entry.delete(0, tk.END)
    for i in range(1, 5):
        globals()[f"round{i}_1_entry"].delete(0, tk.END)
        globals()[f"round{i}_2_entry"].delete(0, tk.END)
    result_label.config(text="")

# GUI
root = tk.Tk()
root.title("Player Score Calculator")
root.geometry("500x480")

# Styling
root.configure(bg="#f1f1f1")

# Player 1 Form
player1_frame = tk.Frame(root, bg="#f0f0f0", bd=2, relief=tk.GROOVE, padx=10, pady=10)
player1_frame.grid(row=0, column=0, padx=10, pady=10)

tk.Label(player1_frame, text="Player 1", bg="#f0f0f0", font=("Helvetica", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=5)
tk.Label(player1_frame, text="Player Name:", bg="#f0f0f0").grid(row=1, column=0, pady=5)
player_name1_entry = tk.Entry(player1_frame)
player_name1_entry.grid(row=1, column=1, pady=5)

for i, label_text in enumerate(["Round 1:", "Round 2:", "Round 3:", "Round 4:"]):
    tk.Label(player1_frame, text=label_text, bg="#f0f0f0").grid(row=i+2, column=0, pady=5)
    entry = tk.Entry(player1_frame)
    entry.grid(row=i+2, column=1, pady=5)
    globals()[f"round{i+1}_1_entry"] = entry

# Player 2 Form
player2_frame = tk.Frame(root, bg="#f0f0f0", bd=2, relief=tk.GROOVE, padx=10, pady=10)
player2_frame.grid(row=0, column=1, padx=10, pady=10)

tk.Label(player2_frame, text="Player 2", bg="#f0f0f0", font=("Helvetica", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=5)
tk.Label(player2_frame, text="Player Name:", bg="#f0f0f0").grid(row=1, column=0, pady=5)
player_name2_entry = tk.Entry(player2_frame)
player_name2_entry.grid(row=1, column=1, pady=5)

for i, label_text in enumerate(["Round 1:", "Round 2:", "Round 3:", "Round 4:"]):
    tk.Label(player2_frame, text=label_text, bg="#f0f0f0").grid(row=i+2, column=0, pady=5)
    entry = tk.Entry(player2_frame)
    entry.grid(row=i+2, column=1, pady=5)
    globals()[f"round{i+1}_2_entry"] = entry

# Calculate Button
calculate_button = tk.Button(root, text="Calculate Final Results", command=calculate_scores, bg="#373db4", fg="white", font=("Helvetica", 12))
calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Clear Button
clear_button = tk.Button(root, text="Clear", command=clear_entries, bg="#ff0000", fg="white", font=("Helvetica", 12))
clear_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(root, text="", bg="#f0f0f0", font=("Helvetica", 12))
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
