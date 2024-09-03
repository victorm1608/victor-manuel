import flet as ft

def mostrar_nombre(text_field, page):
    
    nombre = text_field.value
    Dialog = ft.AlertDialog(
        title=ft.text("Mostrar Nombre"),
        content=ft.text(f"tu nombre es: {nombre} " + " Bienvenido a flet"),
        actions[
            ft.textbutton("Da click para salir", on_click=lambda e: close_dialog(page))
        ],
    )
    
    page.dialog = Dialog
    page.dialog.open = True
    page.update()
    
    def main(page: ft.page):
        page.title=("Mostrar nombre")
        page.dgcolor="#4bff33"
        text_field = ft.textField(label="Ingresa tu nombre")