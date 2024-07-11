import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Analizador_lexico as lexical
import Analizador_sintactico as syntax
import Generador_log as genlog
import random as rd
import subprocess
import os
import threading

lexical_analysis = []

def run_code():
    # clean lists
    syntax.syntax_error.clear()
    syntax.semantic_error.clear()
    lexical_analysis.clear()
    # clean all fields
    clean_all()
    input_code = editor_text.get(1.0, tk.END)
    if input_code == '\n':
        messagebox.showerror("Error", "No hay código que analizar")
    else:
        # LEXICAL
        lexer = lexical.lexer
        lexer.input(input_code)
        checker_text_lexical.config(state=tk.NORMAL)
        checker_text_lexical.delete(1.0, tk.END)
        while True:
            tok = lexer.token()
            if not tok:
                break
            s = f"Token: {tok.type}, Valor: {tok.value}"
            lexical_analysis.append(s)
            checker_text_lexical.insert(tk.END, f"Token: {tok.type}, Valor: {tok.value}\n")
        # SYNTAX
        checker_text_syntax.config(state=tk.NORMAL)
        checker_text_syntax.delete(1.0, tk.END)
        parser = syntax.parser
        parser.parse(input_code)
        for i in syntax.syntax_error:
            checker_text_syntax.insert(tk.END, f"{i}\n")
        # SEMANTIC
        checker_text_semantic.config(state=tk.NORMAL)
        checker_text_semantic.delete(1.0, tk.END)
        for i in syntax.semantic_error:
            checker_text_semantic.insert(tk.END, f"{i}\n")
        # execute code
        # execute_php_code(input_code)
        # disable fields (avoid text editing)
        disable_fields()
        # generate log
        # genlog.create_log(lexical_analysis, syntax.syntax_error, syntax.semantic_error)

def clean_all():
    checker_text_lexical.config(state=tk.NORMAL)
    checker_text_lexical.delete(1.0, tk.END)
    checker_text_lexical.config(state="disabled")

    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.config(state="disabled")

    checker_text_syntax.config(state=tk.NORMAL)
    checker_text_syntax.delete(1.0, tk.END)
    checker_text_syntax.config(state="disabled")

    checker_text_semantic.config(state=tk.NORMAL)
    checker_text_semantic.delete(1.0, tk.END)
    checker_text_semantic.config(state="disabled")

def disable_fields():
    checker_text_lexical.config(state="disabled")
    checker_text_syntax.config(state="disabled")
    checker_text_semantic.config(state="disabled")

def generate_example_code():
    editor_text.delete(1.0, tk.END)
    genlog.get_random_algorithms()
    example_code = rd.choice(list(genlog.algorithms_3.values()))
    editor_text.insert(tk.END, example_code)

def execute_php_code(input_code, timeout=5):
    def php_code():
        with open('temp.php', 'w') as f:
            f.write(input_code)
        php_executable_path = 'C:\\tools\\php83\\php.exe'
        try:
            result = subprocess.run([php_executable_path, 'temp.php'], capture_output=True, text=True, timeout=timeout)
            output = [result.stderr, '\n' ,result.stdout]
        except subprocess.TimeoutExpired:
            output = "Error: Pasó el tiempo de ejecución."
        except Exception as e:
            output = f"Error inesperado: {e}"
        finally:
            os.remove('temp.php')

        output_text.config(state=tk.NORMAL)
        output_text.insert(tk.END, f"{output}")
        output_text.config(state="disabled")

    php_thread = threading.Thread(target=php_code)
    php_thread.start()

root = tk.Tk()
root.title("Editor de Código")
root.geometry("800x600")

main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky="NSEW")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=2)
main_frame.rowconfigure(2, weight=1)

# editor
editor_frame = ttk.LabelFrame(main_frame, text="Editor")
editor_frame.grid(row=0, column=0, columnspan=2, sticky="NSEW", padx=5, pady=5)
editor_text = tk.Text(editor_frame, height=20)
editor_text.pack(fill="both", expand=True)
editor_text.insert(tk.END, "<?php echo \"Hola Mundo\"; ?>")

# output
output_frame = ttk.LabelFrame(main_frame, text="Salida")
output_frame.grid(row=1, column=1, sticky="NSEW", padx=5, pady=5)
output_text = tk.Text(output_frame, height=20)
output_text.pack(fill="both", expand=True)

# checker
checker_frame = ttk.LabelFrame(main_frame, text="Verificador")
checker_frame.grid(row=1, column=0, sticky="NSEW", padx=5, pady=5)

# checker tabs
checker_tabs = ttk.Notebook(checker_frame)
checker_tabs.pack(fill="both", expand=True)

# create checker
tab_lexical = ttk.Frame(checker_tabs)
tab_syntax = ttk.Frame(checker_tabs)
tab_semantic = ttk.Frame(checker_tabs)

checker_tabs.add(tab_lexical, text="Léxico")
checker_tabs.add(tab_syntax, text="Sintáctico")
checker_tabs.add(tab_semantic, text="Semántico")

# add checker tabs
checker_text_lexical = tk.Text(tab_lexical, height=10)
checker_text_lexical.pack(fill="both", expand=True)

checker_text_syntax = tk.Text(tab_syntax, height=10)
checker_text_syntax.pack(fill="both", expand=True)

checker_text_semantic = tk.Text(tab_semantic, height=10)
checker_text_semantic.pack(fill="both", expand=True)

# buttons
buttons_frame = ttk.Frame(main_frame)
buttons_frame.grid(row=0, column=2, sticky="NSEW", padx=5, pady=5)

run_code_button = ttk.Button(buttons_frame, text="Ejecutar Código", command=run_code)
run_code_button.pack(fill="x", pady=10)

generate_example_code_button = ttk.Button(buttons_frame, text="Generar Código de Prueba", command=generate_example_code)
generate_example_code_button.pack(fill="x", pady=10)

root.mainloop()