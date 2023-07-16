import tkinter as tk
import random

class MathApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Math Learning App")
        self.geometry("400x400")

        self.difficulty_frame = tk.Frame(self)
        self.exercise_frame = tk.Frame(self)

        self.difficulty_frame.pack(fill=tk.BOTH, expand=True)
        self.exercise_frame.pack(fill=tk.BOTH, expand=True)

        self.difficulty_label = tk.Label(self.difficulty_frame, text="Selecciona el nivel de dificultad:",
                                          font=("Helvetica", 14))
        self.difficulty_label.pack(pady=20)

        self.difficulty_frame_buttons = tk.Frame(self.difficulty_frame)
        self.difficulty_frame_buttons.pack()

        self.easy_button = tk.Button(self.difficulty_frame_buttons, text="Fácil", command=lambda: self.start_quiz("Fácil"), bg="green", fg="white")
        self.easy_button.pack(side=tk.LEFT, padx=5)

        self.medium_button = tk.Button(self.difficulty_frame_buttons, text="Medio", command=lambda: self.start_quiz("Medio"), bg="yellow", fg="black")
        self.medium_button.pack(side=tk.LEFT, padx=5)

        self.hard_button = tk.Button(self.difficulty_frame_buttons, text="Difícil", command=lambda: self.start_quiz("Difícil"), bg="orange", fg="black")
        self.hard_button.pack(side=tk.LEFT, padx=5)

        self.question_label = tk.Label(self.exercise_frame, text="", font=("Helvetica", 16))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(self.exercise_frame, font=("Helvetica", 14))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self.exercise_frame, text="Enviar", command=self.check_answer)
        self.submit_button.pack(pady=5)

        self.result_label = tk.Label(self.exercise_frame, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.exercise_frame, text="Puntuación: 0", font=("Helvetica", 14))
        self.score_label.pack()

        self.back_button = tk.Button(self.exercise_frame, text="Volver atrás", command=self.go_back)
        self.back_button.pack(pady=20)

        self.score = 0
        self.question_count = 0
        self.correct_answer = None
        self.current_difficulty = None

        # Ocultar la pestaña de ejercicios al inicio
        self.exercise_frame.pack_forget()

    def start_quiz(self, difficulty):
        self.current_difficulty = difficulty
        self.score = 0
        self.question_count = 0
        self.score_label.config(text="Puntuación: 0")
        self.result_label.config(text="")
        self.next_question()
        self.difficulty_frame.pack_forget()
        self.exercise_frame.pack()

    def next_question(self):
        if self.current_difficulty == "Fácil":
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
        elif self.current_difficulty == "Medio":
            num1 = random.randint(10, 50)
            num2 = random.randint(10, 50)
        else:
            num1 = random.randint(50, 100)
            num2 = random.randint(50, 100)

        operations = ["+", "-", "*", "/"]
        operation = random.choice(operations)

        if operation == "+":
            answer = num1 + num2
        elif operation == "-":
            answer = num1 - num2
        elif operation == "*":
            answer = num1 * num2
        else:
            answer = round(num1 / num2, 2)

        question_text = f"{num1} {operation} {num2} = "
        self.question_label.config(text=question_text)
        self.correct_answer = answer

    def check_answer(self):
        user_answer = self.answer_entry.get()

        if user_answer:
            try:
                user_answer = float(user_answer)

                if user_answer == self.correct_answer:
                    self.result_label.config(text="¡Correcto!", foreground="green")
                    self.score += 1
                else:
                    self.result_label.config(text="Incorrecto", foreground="red")

                self.question_count += 1
                self.score_label.config(text=f"Puntuación: {self.score}/{self.question_count}")
                self.answer_entry.delete(0, tk.END)
                self.next_question()

            except ValueError:
                self.result_label.config(text="Ingrese un número válido", foreground="red")
        else:
            self.result_label.config(text="Ingrese una respuesta", foreground="red")

    def go_back(self):
        self.difficulty_frame.pack()
        self.exercise_frame.pack_forget()
        self.result_label.config(text="")
        self.score_label.config(text="Puntuación: 0")
        self.current_difficulty = None


if __name__ == "__main__":
    app = MathApp()
    app.mainloop()
