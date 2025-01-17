import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime, timedelta
import sys
from pathlib import Path
import calendar
from tkcalendar import Calendar
import random


class SATTopics:
    MATH_TOPICS = {
        "Heart of Algebra": {
            "Linear Equations": {
                "subtopics": [
                    "Single-variable equations",
                    "Systems of linear equations",
                    "Linear inequalities",
                    "Graphing linear equations"
                ],
                "key_concepts": [
                    "Solving for variables",
                    "Understanding slope and y-intercept",
                    "Interpreting graphs",
                    "Word problems with linear relationships"
                ],
                "importance": "High - 25-30% of Math section"
            },
            "Linear Functions": {
                "subtopics": [
                    "Function notation",
                    "Domain and range",
                    "Function graphs",
                    "Linear modeling"
                ],
                "key_concepts": [
                    "Understanding f(x) notation",
                    "Identifying functions",
                    "Real-world applications",
                    "Rate of change"
                ],
                "importance": "High - Part of algebra foundation"
            }
        },
        "Problem Solving and Data Analysis": {
            "Statistics": {
                "subtopics": [
                    "Mean, median, mode",
                    "Standard deviation",
                    "Interquartile range",
                    "Data interpretation"
                ],
                "key_concepts": [
                    "Calculating central tendency",
                    "Understanding spread",
                    "Reading charts and graphs",
                    "Statistical significance"
                ],
                "importance": "Medium - 15-20% of Math section"
            },
            "Ratios and Proportions": {
                "subtopics": [
                    "Unit rates",
                    "Proportional relationships",
                    "Percentage problems",
                    "Scale factors"
                ],
                "key_concepts": [
                    "Setting up proportions",
                    "Cross multiplication",
                    "Unit conversion",
                    "Real-world applications"
                ],
                "importance": "High - Frequently tested"
            }
        },
        "Passport to Advanced Math": {
            "Quadratic Equations": {
                "subtopics": [
                    "Factoring",
                    "Completing the square",
                    "Quadratic formula",
                    "Graphing parabolas"
                ],
                "key_concepts": [
                    "Finding roots",
                    "Vertex form",
                    "Maximum/minimum values",
                    "Word problems"
                ],
                "importance": "High - 15-20% of Math section"
            },
            "Polynomial Functions": {
                "subtopics": [
                    "Operations with polynomials",
                    "Polynomial factors",
                    "Polynomial graphs",
                    "Complex numbers"
                ],
                "key_concepts": [
                    "Factor theorem",
                    "Polynomial division",
                    "End behavior",
                    "Zeros of polynomials"
                ],
                "importance": "Medium - Advanced topic"
            }
        }
    }

    READING_TOPICS = {
        "Command of Evidence": {
            "Finding Evidence": {
                "subtopics": [
                    "Text citations",
                    "Data interpretation",
                    "Supporting claims",
                    "Multiple sources"
                ],
                "key_concepts": [
                    "Identifying relevant evidence",
                    "Connecting ideas across passages",
                    "Evaluating support",
                    "Drawing conclusions"
                ],
                "importance": "High - Core reading skill"
            }
        },
        "Words in Context": {
            "Vocabulary": {
                "subtopics": [
                    "Context clues",
                    "Multiple meanings",
                    "Tone and connotation",
                    "Academic vocabulary"
                ],
                "key_concepts": [
                    "Using context",
                    "Word families",
                    "Denotation vs connotation",
                    "Root words"
                ],
                "importance": "High - Throughout reading section"
            }
        }
    }

    @classmethod
    def add_new_topic(cls, subject, topic_name):
        if subject == "Math":
            cls.MATH_TOPICS[topic_name] = {}
        else:
            cls.READING_TOPICS[topic_name] = {}

    @classmethod
    def add_new_subtopic(cls, subject, topic_name, subtopic_name):
        new_subtopic = {
            "subtopics": [],
            "key_concepts": [],
            "importance": "Not specified"
        }
        
        if subject == "Math":
            if topic_name in cls.MATH_TOPICS:
                cls.MATH_TOPICS[topic_name][subtopic_name] = new_subtopic
        else:
            if topic_name in cls.READING_TOPICS:
                cls.READING_TOPICS[topic_name][subtopic_name] = new_subtopic


class ModernTheme:
    BACKGROUND = "#2a0a4a"  # Dark Purple
    DARKER_BG = "#1a0636"   # Darker Purple
    LIGHTER_BG = "#3d1466"  # Lighter Purple
    TEXT = "#00ff9d"        # Dark Green
    ACCENT = "#5f7d95"      # Grayish Blue
    SECONDARY_ACCENT = "#4a6276"  # Darker Grayish Blue
    
    @classmethod
    def apply_theme(cls):
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure(".",
            background=cls.BACKGROUND,
            foreground=cls.TEXT,
            fieldbackground=cls.LIGHTER_BG,
            troughcolor=cls.DARKER_BG,
            selectbackground=cls.ACCENT,
            selectforeground=cls.DARKER_BG)
        
        style.configure("Custom.TFrame", background=cls.BACKGROUND)
        style.configure("Topic.TFrame", background=cls.LIGHTER_BG)
        
        style.configure("Custom.TLabel",
            background=cls.BACKGROUND,
            foreground=cls.TEXT,
            padding=5,
            font=('Helvetica', 10))
        
        style.configure("Header.TLabel",
            background=cls.BACKGROUND,
            foreground=cls.ACCENT,
            font=('Helvetica', 12, 'bold'))
        
        style.configure("Custom.TButton",
            background=cls.ACCENT,
            foreground=cls.DARKER_BG,
            padding=[5, 2])
        
        style.configure("TNotebook",
            background=cls.BACKGROUND,
            tabmargins=[2, 5, 2, 0])
        
        style.configure("TNotebook.Tab",
            background=cls.LIGHTER_BG,
            foreground=cls.TEXT,
            padding=[10, 2],
            font=('Helvetica', 9))
        
        style.configure("Treeview",
            background=cls.LIGHTER_BG,
            foreground=cls.TEXT,
            fieldbackground=cls.LIGHTER_BG)
        
        style.configure("Treeview.Heading",
            background=cls.DARKER_BG,
            foreground=cls.TEXT)
        
        style.map("Treeview",
            background=[('selected', cls.ACCENT)],
            foreground=[('selected', cls.DARKER_BG)])
        
        style.map("TNotebook.Tab",
            background=[("selected", cls.ACCENT)],
            foreground=[("selected", cls.DARKER_BG)])


class ModernSATStudyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SAT Study Planner Pro")
        self.root.geometry("1400x800")
        self.root.configure(bg=ModernTheme.BACKGROUND)
        
        ModernTheme.apply_theme()
        
        self.topics_data = SATTopics()
        self.current_ratings = {}
        self.topic_notes = {}
        self.selected_topic = None
        
        self.load_data()
        
        # Create fullscreen button
        self.is_fullscreen = False
        self.fullscreen_btn = ttk.Button(self.root, text="⛶", 
                                       command=self.toggle_fullscreen,
                                       style="Custom.TButton")
        self.fullscreen_btn.place(relx=0.95, rely=0.02)
        
        # Create close button
        self.close_btn = ttk.Button(self.root, text="✕",
                                   command=self.confirm_close,
                                   style="Custom.TButton")
        self.close_btn.place(relx=0.98, rely=0.02)
        
        self.main_frame = ttk.Frame(self.root, style="Custom.TFrame")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.left_panel = ttk.Frame(self.main_frame, style="Custom.TFrame")
        self.left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        self.right_panel = ttk.Frame(self.main_frame, style="Custom.TFrame")
        self.right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        self.create_topic_controls()
        self.create_topic_tree()
        self.create_rating_section()
        self.create_notes_section()
        
        self.root.protocol("WM_DELETE_WINDOW", self.confirm_close)
        
        # Bind F11 to toggle fullscreen
        self.root.bind("<F11>", lambda event: self.toggle_fullscreen())
        self.root.bind("<Escape>", lambda event: self.exit_fullscreen())

    def toggle_fullscreen(self):
        self.is_fullscreen = not self.is_fullscreen
        self.root.attributes("-fullscreen", self.is_fullscreen)
        
    def exit_fullscreen(self):
        self.is_fullscreen = False
        self.root.attributes("-fullscreen", False)

    def confirm_close(self):
        if messagebox.askokcancel("Confirm Exit", "Are you sure you want to exit?"):
            self.on_closing()

    def create_topic_controls(self):
        control_frame = ttk.Frame(self.left_panel, style="Custom.TFrame")
        control_frame.pack(fill=tk.X, pady=(0, 5))

        self.folder_btn = ttk.Button(control_frame, text="📁 New Topic",
                                   command=self.add_new_topic,
                                   style="Custom.TButton")
        self.folder_btn.pack(side=tk.LEFT, padx=5)

        self.file_btn = ttk.Button(control_frame, text="📄 New Subtopic",
                                  command=self.add_new_subtopic,
                                  style="Custom.TButton")
        self.file_btn.pack(side=tk.LEFT, padx=5)

    def add_new_topic(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Add New Topic")
        dialog.geometry("400x250")  # Increased size
        dialog.configure(bg=ModernTheme.BACKGROUND)
        dialog.resizable(False, False)
        
        ttk.Label(dialog, text="Select Subject:", style="Custom.TLabel").pack(pady=10)
        subject_var = tk.StringVar(value="Math")
        subject_combo = ttk.Combobox(dialog, textvariable=subject_var, values=["Math", "Reading"])
        subject_combo.pack(pady=10)
        
        ttk.Label(dialog, text="Topic Name:", style="Custom.TLabel").pack(pady=10)
        topic_entry = ttk.Entry(dialog)
        topic_entry.pack(pady=10)
        
        def save_topic():
            subject = subject_var.get()
            topic_name = topic_entry.get().strip()
            if topic_name:
                SATTopics.add_new_topic(subject, topic_name)
                self.refresh_topic_tree()
                dialog.destroy()
            else:
                messagebox.showerror("Error", "Please enter a topic name")
        
        ttk.Button(dialog, text="Save", command=save_topic, style="Custom.TButton").pack(pady=20)

    def add_new_subtopic(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Add New Subtopic")
        dialog.geometry("400x300")  # Increased size
        dialog.configure(bg=ModernTheme.BACKGROUND)
        dialog.resizable(False, False)
        
        ttk.Label(dialog, text="Select Subject:", style="Custom.TLabel").pack(pady=10)
        subject_var = tk.StringVar(value="Math")
        subject_combo = ttk.Combobox(dialog, textvariable=subject_var, values=["Math", "Reading"])
        subject_combo.pack(pady=10)
        
        ttk.Label(dialog, text="Select Topic:", style="Custom.TLabel").pack(pady=10)
        topic_var = tk.StringVar()
        topic_combo = ttk.Combobox(dialog, textvariable=topic_var)
        topic_combo.pack(pady=10)
        
        def update_topics(*args):
            topics = list(SATTopics.MATH_TOPICS.keys()) if subject_var.get() == "Math" else list(SATTopics.READING_TOPICS.keys())
            topic_combo['values'] = topics
            if topics:
                topic_combo.set(topics[0])
        
        subject_var.trace('w', update_topics)
        update_topics()
        
        ttk.Label(dialog, text="Subtopic Name:", style="Custom.TLabel").pack(pady=10)
        subtopic_entry = ttk.Entry(dialog)
        subtopic_entry.pack(pady=10)
        
        def save_subtopic():
            subject = subject_var.get()
            topic_name = topic_var.get()
            subtopic_name = subtopic_entry.get().strip()
            if topic_name and subtopic_name:
                SATTopics.add_new_subtopic(subject, topic_name, subtopic_name)
                self.refresh_topic_tree()
                dialog.destroy()
            else:
                messagebox.showerror("Error", "Please fill in all fields")
        
        ttk.Button(dialog, text="Save", command=save_subtopic, style="Custom.TButton").pack(pady=20)

    def refresh_topic_tree(self):
        self.topics_notebook.destroy()
        self.create_topic_tree()

    def create_topic_tree(self):
        self.topics_notebook = ttk.Notebook(self.left_panel)
        self.topics_notebook.pack(fill=tk.BOTH, expand=True)
        
        math_frame = ttk.Frame(self.topics_notebook, style="Custom.TFrame")
        self.math_tree = self.create_subject_tree(math_frame, self.topics_data.MATH_TOPICS, "Math")
        self.topics_notebook.add(math_frame, text="Mathematics")
        
        reading_frame = ttk.Frame(self.topics_notebook, style="Custom.TFrame")
        self.reading_tree = self.create_subject_tree(reading_frame, self.topics_data.READING_TOPICS, "Reading")
        self.topics_notebook.add(reading_frame, text="Reading")

    def create_subject_tree(self, parent, topics_dict, subject):
        tree = ttk.Treeview(parent, style="Treeview", show="tree headings")
        tree.pack(fill=tk.BOTH, expand=True)
        
        tree["columns"] = ("rating",)
        tree.column("rating", width=100, anchor="center")
        tree.heading("rating", text="Rating")
        
        for main_topic, subtopics in topics_dict.items():
            main_id = tree.insert("", "end", text=main_topic, values=(self.get_rating(f"{subject} - {main_topic}"),))
            
            for subtopic, details in subtopics.items():
                sub_id = tree.insert(main_id, "end", text=subtopic, 
                                   values=(self.get_rating(f"{subject} - {main_topic} - {subtopic}"),))
                
                if "subtopics" in details:
                    for sub in details["subtopics"]:
                        tree.insert(sub_id, "end", text=sub,
                                  values=(self.get_rating(f"{subject} - {main_topic} - {subtopic} - {sub}"),))
        
        tree.bind("<<TreeviewSelect>>", self.on_topic_select)
        return tree

    def create_rating_section(self):
        self.rating_frame = ttk.LabelFrame(self.right_panel, text="Topic Rating", style="Custom.TFrame")
        self.rating_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.rating_var = tk.DoubleVar(value=1)
        self.rating_scale = ttk.Scale(self.rating_frame, from_=1, to=10,
                                    variable=self.rating_var,
                                    command=self.update_rating)
        self.rating_scale.pack(fill=tk.X, padx=10, pady=5)
        
        self.rating_label = ttk.Label(self.rating_frame, 
                                    text="Current Rating: 1",
                                    style="Custom.TLabel")
        self.rating_label.pack(pady=5)

    def create_notes_section(self):
        self.notes_frame = ttk.LabelFrame(self.right_panel, text="Topic Notes", style="Custom.TFrame")
        self.notes_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Updated text widget with larger font and bold
        self.notes_text = tk.Text(self.notes_frame, wrap=tk.WORD,
                                bg=ModernTheme.LIGHTER_BG,
                                fg=ModernTheme.TEXT,
                                insertbackground=ModernTheme.TEXT,
                                font=('Helvetica', 12, 'bold'))  # Increased font size and made bold
        self.notes_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.save_button = ttk.Button(self.notes_frame, text="Save Notes",
                                    command=self.save_notes,
                                    style="Custom.TButton")
        self.save_button.pack(pady=5)

    def get_rating(self, topic_path):
        rating = self.current_ratings.get(topic_path, "Not Rated")
        return rating if rating != "Not Rated" else "-"

    def on_topic_select(self, event):
        tree = event.widget
        selection = tree.selection()
        if selection:
            item = selection[0]
            topic_path = self.get_topic_path(tree, item)
            self.selected_topic = topic_path
            
            current_rating = self.current_ratings.get(topic_path, 1)
            self.rating_var.set(current_rating)
            self.rating_label.config(text=f"Current Rating: {current_rating}")
            
            self.notes_text.delete("1.0", tk.END)
            if topic_path in self.topic_notes:
                self.notes_text.insert("1.0", self.topic_notes[topic_path])

    def get_topic_path(self, tree, item):
        path_parts = []
        while item:
            path_parts.insert(0, tree.item(item)["text"])
            item = tree.parent(item)
        
        if tree == self.math_tree:
            return "Math - " + " - ".join(path_parts)
        else:
            return "Reading - " + " - ".join(path_parts)

    def update_rating(self, value):
        if self.selected_topic:
            try:
                rating = float(value)
                self.current_ratings[self.selected_topic] = rating
                self.rating_label.config(text=f"Current Rating: {rating:.1f}")
                
                tree = self.math_tree if self.selected_topic.startswith("Math") else self.reading_tree
                for item in tree.selection():
                    tree.set(item, "rating", f"{rating:.1f}")
                
                self.save_data()
            except ValueError:
                pass

    def save_notes(self):
        if self.selected_topic:
            notes_text = self.notes_text.get("1.0", "end-1c")
            if notes_text.strip():
                self.topic_notes[self.selected_topic] = notes_text
                self.save_data()
                messagebox.showinfo("Success", "Notes saved successfully!")

    def save_data(self):
        data = {
            "ratings": self.current_ratings,
            "notes": self.topic_notes,
            "custom_topics": {
                "math": self.topics_data.MATH_TOPICS,
                "reading": self.topics_data.READING_TOPICS
            }
        }
        try:
            with open("sat_study_data.json", "w") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"Error saving data: {str(e)}")

    def load_data(self):
        try:
            if os.path.exists("sat_study_data.json"):
                with open("sat_study_data.json", "r") as f:
                    data = json.load(f)
                    self.current_ratings = data.get("ratings", {})
                    self.topic_notes = data.get("notes", {})
                    if "custom_topics" in data:
                        custom_topics = data["custom_topics"]
                        self.topics_data.MATH_TOPICS.update(custom_topics.get("math", {}))
                        self.topics_data.READING_TOPICS.update(custom_topics.get("reading", {}))
        except Exception as e:
            messagebox.showerror("Error", f"Error loading data: {str(e)}")
            self.current_ratings = {}
            self.topic_notes = {}

    def on_closing(self):
        if self.selected_topic:
            notes_text = self.notes_text.get("1.0", "end-1c")
            if notes_text.strip():
                self.topic_notes[self.selected_topic] = notes_text
        
        self.save_data()
        self.root.destroy()


def main():
    root = tk.Tk()
    app = ModernSATStudyApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()