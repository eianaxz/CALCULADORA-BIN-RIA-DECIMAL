import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font as tkfont
import os


class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Binária ↔️ Decimal")
        self.root.geometry("500x650")
        self.root.configure(bg="#03273f")
        self.root.resizable(False, False)

        try:
            caminho_arquivo = os.path.join(
                os.path.dirname(__file__), "calculadoraicone.ico")
            self.root.iconbitmap(caminho_arquivo)
        except:
            pass

        # Custum Font
        self.custom_font = tkfont.Font(family='Delon', size=12)
        self.title_font = tkfont.Font(
            family='Delon', size=18, weight='bold')

        # Variável para controlar qual campo está ativo
        self.active_entry = None

        # Frame principal com gradiente
        self.main_frame = tk.Frame(root, bg="#0a192f")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Título com efeito
        self.title_label = tk.Label(
            self.main_frame,
            text="Calculadora Binária↔Decimal",
            font=self.title_font,
            bg="#0a192f",
            fg="#489ad0",
            pady=10
        )
        self.title_label.pack()

        # Subtítulo
        self.subtitle_label = tk.Label(
            self.main_frame,
            text="Conversor Binário ↔ Decimal",
            font=('Helvetica', 10),
            bg="#0a192f",
            fg="#ffffff"
        )
        self.subtitle_label.pack(pady=(0, 20))

        # Container dos campos
        self.entry_frame = tk.Frame(self.main_frame, bg='#0a192f')
        self.entry_frame.pack(fill=tk.X, pady=10)

        # Campo Decimal
        self.decimal_frame = tk.Frame(self.entry_frame, bg='#0a192f')
        self.decimal_frame.pack(fill=tk.X, pady=8)

        self.decimal_label = tk.Label(
            self.decimal_frame,
            text="Decimal:",
            font=self.custom_font,
            bg='#0a192f',
            fg='#ccd6f6'
        )
        self.decimal_label.pack(side=tk.LEFT, padx=5)

        self.decimal_entry = tk.Entry(
            self.decimal_frame,
            font=self.custom_font,
            bd=0,
            relief=tk.FLAT,
            bg='#172a45',
            fg='#e6f1ff',
            insertbackground='#64ffda',
            highlightthickness=1,
            highlightbackground='#1e3a8a',
            highlightcolor='#64ffda',
            selectbackground='#1e3a8a',
            selectforeground='#ffffff'
        )
        self.decimal_entry.pack(side=tk.LEFT, fill=tk.X,
                                expand=True, padx=5, ipady=8)
        self.decimal_entry.bind(
            '<FocusIn>', lambda e: self.set_active_entry(self.decimal_entry))

        # Campo Binário
        self.binary_frame = tk.Frame(self.entry_frame, bg='#0a192f')
        self.binary_frame.pack(fill=tk.X, pady=8)

        self.binary_label = tk.Label(
            self.binary_frame,
            text="Binário:",
            font=self.custom_font,
            bg='#0a192f',
            fg='#ccd6f6'
        )
        self.binary_label.pack(side=tk.LEFT, padx=5)

        self.binary_entry = tk.Entry(
            self.binary_frame,
            font=self.custom_font,
            bd=0,
            relief=tk.FLAT,
            bg='#172a45',
            fg='#e6f1ff',
            insertbackground='#64ffda',
            highlightthickness=1,
            highlightbackground='#1e3a8a',
            highlightcolor='#64ffda',
            selectbackground='#1e3a8a',
            selectforeground='#ffffff'
        )
        self.binary_entry.pack(side=tk.LEFT, fill=tk.X,
                               expand=True, padx=5, ipady=8)
        self.binary_entry.bind(
            '<FocusIn>', lambda e: self.set_active_entry(self.binary_entry))

        # Botões de conversão
        self.convert_frame = tk.Frame(self.main_frame, bg='#0a192f')
        self.convert_frame.pack(pady=15)

        self.to_binary_btn = tk.Button(
            self.convert_frame,
            text="→ Binário",
            command=self.decimal_to_binary,
            bd=0,
            relief=tk.FLAT,
            bg='#1e3a8a',
            fg='#e6f1ff',
            activebackground='#172a45',
            activeforeground='#64ffda',
            font=self.custom_font,
            padx=20,
            pady=5,
            cursor="hand2"
        )
        self.to_binary_btn.pack(side=tk.LEFT, padx=10, ipadx=5, ipady=3)

        self.to_decimal_btn = tk.Button(
            self.convert_frame,
            text="→ Decimal",
            command=self.binary_to_decimal,
            bd=0,
            relief=tk.FLAT,
            bg='#1e3a8a',
            fg='#e6f1ff',
            activebackground='#172a45',
            activeforeground='#64ffda',
            font=self.custom_font,
            padx=20,
            pady=5,
            cursor="hand2"
        )
        self.to_decimal_btn.pack(side=tk.LEFT, padx=10, ipadx=5, ipady=3)

        # Teclado numérico
        self.keypad_frame = tk.Frame(self.main_frame, bg='#0a192f')
        self.keypad_frame.pack(pady=20)

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
            ('0', 3, 0), ('⌫', 3, 1), ('C', 3, 2)
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(
                self.keypad_frame,
                text=text,
                width=6,
                bd=0,
                relief=tk.FLAT,
                bg='#172a45',
                fg='#e6f1ff',
                activebackground='#1e3a8a',
                activeforeground='#64ffda',
                font=self.custom_font,
                command=lambda t=text: self.on_button_click(t),
                cursor="hand2",
                padx=10,
                pady=10
            )
            btn.grid(row=row, column=col, padx=5, pady=5, ipady=5)
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg='#1e3a8a'))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg='#172a45'))

        # Efeitos especiais para botões de conversão
        self.to_binary_btn.bind(
            "<Enter>", lambda e: self.to_binary_btn.config(bg='#172a45', fg='#64ffda'))
        self.to_binary_btn.bind(
            "<Leave>", lambda e: self.to_binary_btn.config(bg='#1e3a8a', fg='#e6f1ff'))
        self.to_decimal_btn.bind(
            "<Enter>", lambda e: self.to_decimal_btn.config(bg='#172a45', fg='#64ffda'))
        self.to_decimal_btn.bind(
            "<Leave>", lambda e: self.to_decimal_btn.config(bg='#1e3a8a', fg='#e6f1ff'))

        # Barra de status
        self.status_bar = tk.Label(
            self.main_frame,
            text="Ready",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W,
            bg='#0a192f',
            fg='#64ffda',
            font=('Helvetica', 9)
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X, pady=(10, 0))

        # Definir campo ativo inicial
        self.set_active_entry(self.decimal_entry)

        # Configurar o tema
        self.setup_theme()

    def setup_theme(self):
        """Configura o tema visual"""
        style = ttk.Style()
        style.theme_use('clam')

        # Configurar estilo para os botões
        style.configure('TButton',
                        font=self.custom_font,
                        background='#1e3a8a',
                        foreground='#e6f1ff',
                        bordercolor='#0a192f',
                        lightcolor='#0a192f',
                        darkcolor='#0a192f',
                        padding=5,
                        relief='flat')

        style.map('TButton',
                  background=[('active', '#172a45')],
                  foreground=[('active', '#64ffda')])

    def set_active_entry(self, entry):
        """Define qual campo de entrada está ativo"""
        self.active_entry = entry
        if entry == self.decimal_entry:
            self.binary_entry.config(
                bg='#172a45', highlightbackground='#1e3a8a')
            self.decimal_entry.config(
                bg='#1e3a8a', highlightbackground='#64ffda')
            self.status_bar.config(text="Entrada Decimal ativa")
        else:
            self.decimal_entry.config(
                bg='#172a45', highlightbackground='#1e3a8a')
            self.binary_entry.config(
                bg='#1e3a8a', highlightbackground='#64ffda')
            self.status_bar.config(text="Entrada Binária ativa")

    def on_button_click(self, button):
        """Manipula cliques nos botões do teclado"""
        if self.active_entry is None:
            return

        if button == "⌫":
            current = self.active_entry.get()
            self.active_entry.delete(0, tk.END)
            self.active_entry.insert(0, current[:-1])
            self.status_bar.config(text="Último caractere removido")
        elif button == "C":  # Limpar
            self.active_entry.delete(0, tk.END)
            self.status_bar.config(text="Entrada vazia")
        else:
            if self.active_entry == self.binary_entry and button not in ('0', '1'):
                messagebox.showerror(
                    "Error", "Números binários só podem conter 0 e 1!")
                self.status_bar.config(
                    text="Erro: Número binário só pode ser 0 ou 1")
                return
            self.active_entry.insert(tk.END, button)
            self.status_bar.config(text=f"Added {button} to input")

    def decimal_to_binary(self):
        """Converte decimal para binário"""
        try:
            decimal_num = self.decimal_entry.get()
            if not decimal_num:
                messagebox.showerror(
                    "Error", "Por favor, insira um número decimal!")
                self.status_bar.config(
                    text="Erro: Nenhum número decimal inserido.")
                return

            num = int(decimal_num)
            binary_num = bin(num)[2:]
            self.binary_entry.delete(0, tk.END)
            self.binary_entry.insert(0, binary_num)
            self.status_bar.config(
                text=f"Convertido {num} para binário: {binary_num}")
        except ValueError:
            messagebox.showerror(
                "Error", "Por favor, insira um número decimal válido!")
            self.status_bar.config(text="Erro: Número decimal inválido.")

    def binary_to_decimal(self):
        """Converte binário para decimal"""
        try:
            binary_num = self.binary_entry.get()
            if not binary_num:
                messagebox.showerror(
                    "Error", "Por favor, insira um número binário válido!")
                self.status_bar.config(
                    text="Erro: Nenhum número binário inserido.")
                return

            # Verifica se é um número binário válido
            for digit in binary_num:
                if digit not in ('0', '1'):
                    raise ValueError

            decimal_num = int(binary_num, 2)
            self.decimal_entry.delete(0, tk.END)
            self.decimal_entry.insert(0, str(decimal_num))
            self.status_bar.config(
                text=f"Convertido {binary_num} para decimal: {decimal_num}")
        except ValueError:
            messagebox.showerror(
                "Error", "Por favor, insira um número binário válido (somente 0 e 1)!")
            self.status_bar.config(text="Erro: Número binário inválido.")


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)

    root.mainloop()
