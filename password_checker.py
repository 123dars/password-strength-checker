import tkinter as tk
from tkinter import ttk
import re

# ==== Password Strength Logic ====

def assess_password_strength(password):
    strength_points = 0
    feedback = []

    if len(password) >= 8:
        strength_points += 1
    else:
        feedback.append("❌ At least 8 characters")

    if re.search(r"[A-Z]", password):
        strength_points += 1
    else:
        feedback.append("❌ Add uppercase letters")

    if re.search(r"[a-z]", password):
        strength_points += 1
    else:
        feedback.append("❌ Add lowercase letters")

    if re.search(r"[0-9]", password):
        strength_points += 1
    else:
        feedback.append("❌ Add numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_points += 1
    else:
        feedback.append("❌ Add special characters")

    if strength_points <= 2:
        strength_label = "Weak ❗"
        color = "red"
    elif strength_points in [3, 4]:
        strength_label = "Moderate ⚠️"
        color = "orange"
    else:
        strength_label = "Strong ✅"
        color = "green"

    return strength_points, strength_label, color, feedback

# ==== GUI Setup ====

def update_strength(*args):
    password = password_var.get()
    strength, label, color, feedback = assess_password_strength(password)

    progress_bar['value'] = strength * 20
    label_result.config(text=f"Strength: {label}", fg=color)
    label_feedback.config(text="\n".join(feedback), fg="black")

def toggle_password():
    if entry.cget('show') == '':
        entry.config(show='*')
        toggle_btn.config(text="👁 Show")
    else:
        entry.config(show='')
        toggle_btn.config(text="🙈 Hide")

# ==== GUI ====

root = tk.Tk()
root.title("🔐 Advanced Password Strength Checker")
root.geometry("420x350")
root.resizable(False, False)

# Password Entry
tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
password_var = tk.StringVar()
password_var.trace_add('write', update_strength)
entry_frame = tk.Frame(root)
entry_frame.pack(pady=5)

entry = tk.Entry(entry_frame, textvariable=password_var, width=30, show='*', font=("Arial", 12))
entry.pack(side=tk.LEFT, padx=(0, 10))

toggle_btn = tk.Button(entry_frame, text="👁 Show", command=toggle_password)
toggle_btn.pack(side=tk.RIGHT)

# Strength Bar
progress_bar = ttk.Progressbar(root, length=300, mode='determinate', maximum=100)
progress_bar.pack(pady=10)

# Strength Result
label_result = tk.Label(root, text="", font=("Arial", 14, "bold"))
label_result.pack(pady=5)

# Feedback
label_feedback = tk.Label(root, text="", font=("Arial", 10), justify="left")
label_feedback.pack(pady=5)

# Footer
tk.Label(root, text="🔐 Created by Darshan B", font=("Arial", 8), fg="gray").pack(side="bottom", pady=10)

root.mainloop()
