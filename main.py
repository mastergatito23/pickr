import random
import customtkinter

elements = []


def add_element():
    input_dialog = customtkinter.CTkInputDialog(
        text="Elemento:", title="Añadir elemento"
    )
    element = input_dialog.get_input()

    if element and element.strip():
        elements.append(element.strip())
        update_list_display()


def delete_element(index):
    elements.pop(index)
    result_label.configure(text="")
    update_list_display()


def update_list_display(selected_item=None):
    for child in scroll.winfo_children():
        child.destroy()

    for idx, item in enumerate(elements):
        is_selected = item == selected_item

        row_frame = customtkinter.CTkFrame(
            master=scroll, fg_color="transparent"
        )
        row_frame.pack(fill="x", padx=5, pady=3)

        item_label = customtkinter.CTkLabel(
            master=row_frame,
            text=f"★ {item}" if is_selected else item,
            font=("Arial", 14, "bold" if is_selected else "normal"),
            text_color="#1F6AA5" if is_selected else "white",
            anchor="w",
        )
        item_label.pack(side="left", fill="x", expand=True, padx=(5, 0))

        delete_btn = customtkinter.CTkButton(
            master=row_frame,
            text="✕",
            width=28,
            height=28,
            fg_color="#D32F2F",
            hover_color="#9A0007",
            # Pass the current index via default argument in lambda
            command=lambda i=idx: delete_element(i),
        )
        delete_btn.pack(side="right", padx=(5, 0))


def pick_random_element():
    if elements:
        picked = random.choice(elements)
        result_label.configure(
            text=f"Elemento seleccionado: {picked}", text_color="#1F6AA5"
        )
        update_list_display(selected_item=picked)
    else:
        result_label.configure(
            text="¡Añade por lo menos un elemento!", text_color="orange"
        )


app = customtkinter.CTk()
app.geometry("400x500")
app.title("Pickr")
customtkinter.set_default_color_theme("dark-blue")

title = customtkinter.CTkLabel(master=app, text="Pickr", font=("Arial", 32))
title.pack(padx=20, pady=10)

scroll = customtkinter.CTkScrollableFrame(master=app, width=320, height=200)
scroll.pack(padx=20, pady=10, fill="both", expand=True)

result_label = customtkinter.CTkLabel(
    master=app, text="", font=("Arial", 16, "bold")
)
result_label.pack(pady=5)

button_frame = customtkinter.CTkFrame(master=app, fg_color="transparent")
button_frame.pack(padx=20, pady=15)

button_add = customtkinter.CTkButton(
    button_frame, text="Añadir elemento", command=add_element
)
button_add.pack(side="left", padx=5)

button_pick = customtkinter.CTkButton(
    button_frame,
    text="Seleccionar elemento aleatorio",
    command=pick_random_element,
    fg_color="#2FA572",
    hover_color="#1E6B4A",
)
button_pick.pack(side="right", padx=5)

app.mainloop()