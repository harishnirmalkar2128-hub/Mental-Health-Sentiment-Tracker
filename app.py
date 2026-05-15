import customtkinter as ctk
from textblob import TextBlob

# System Settings for Modern Look
ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class MentalHealthApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Mental Health Sentiment Tracker")
        self.geometry("600x550")

        # --- UI Layout ---
        self.label_title = ctk.CTkLabel(self, text="Mental Health Sentiment Tracker", font=ctk.CTkFont(size=28, weight="bold"))
        self.label_title.pack(pady=(30, 10))

        self.label_subtitle = ctk.CTkLabel(self, text="How are you feeling right now?", font=ctk.CTkFont(size=14))
        self.label_subtitle.pack(pady=(0, 20))

        # Modern Text Area (Rounded)
        self.textbox = ctk.CTkTextbox(self, width=450, height=150, corner_radius=15, border_width=2)
        self.textbox.pack(pady=10)

        # Polished Button
        self.analyze_btn = ctk.CTkButton(self, text="Analyze My Mood", command=self.analyze_mood, 
                                          corner_radius=20, font=ctk.CTkFont(size=15, weight="bold"),
                                          height=45, hover_color="#2980b9")
        self.analyze_btn.pack(pady=30)

        # Result Display Card
        self.result_frame = ctk.CTkFrame(self, width=450, height=100, corner_radius=15)
        self.result_frame.pack(pady=10)
        
        self.label_result = ctk.CTkLabel(self.result_frame, text="Analysis will appear here...", 
                                         font=ctk.CTkFont(size=15), wraplength=400)
        self.label_result.place(relx=0.5, rely=0.5, anchor="center")

    def analyze_mood(self):
        user_text = self.textbox.get("1.0", "end-1c")
        if not user_text.strip():
            self.label_result.configure(text="Please share your thoughts first!", text_color="orange")
            return

        analysis = TextBlob(user_text)
        score = analysis.sentiment.polarity

        # Polishing logic with colors
        if score < -0.2:
            msg = "Detection: High Stress Levels ⚠️\nSuggested Action: Practice 5-min meditation."
            color = "#ff7675" # Soft Red
        elif -0.2 <= score < 0.2:
            msg = "Detection: Stable / Neutral 😐\nSuggested Action: Stay hydrated and keep working!"
            color = "#fdcb6e" # Soft Yellow
        else:
            msg = "Detection: Positive & Vibrant! 😊\nSuggested Action: Excellent mindset, keep it up!"
            color = "#55efc4" # Soft Green
            
        self.label_result.configure(text=msg, text_color=color)

if __name__ == "__main__":
    app = MentalHealthApp()
    app.mainloop()