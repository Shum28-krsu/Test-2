import flet as ft
from db import main_db


def main(page: ft.Page):
    page.title = "Список покупок"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    list_view = ft.Column()
    filter_type = "all"
    counter_text = ft.Text()

    def load_items():
        list_view.controls.clear()
        items = main_db.get_items(filter_type)

        done_count = 0

        for item_id, name, count, done in items:
            if done:
                done_count += 1

            list_view.controls.append(
                create_item(item_id, name, count, done)
            )

        counter_text.value = f"Куплено: {done_count} / {len(items)}"
        page.update()

    def add_item(e):
        if name_input.value:
            main_db.add_item(name_input.value, int(count_value.value))
            name_input.value = ""
            count_value.value = "1"
            load_items()

    def set_filter(f):
        nonlocal filter_type
        filter_type = f
        load_items()

    def toggle(item_id, value):
        main_db.toggle_item(item_id, int(value))
        load_items()

    def delete(item_id):
        main_db.delete_item(item_id)
        load_items()

    def increase(e):
        count_value.value = str(int(count_value.value) + 1)
        page.update()

    def decrease(e):
        if int(count_value.value) > 1:
            count_value.value = str(int(count_value.value) - 1)
            page.update()

    count_value = ft.Text(value="1", width=30, text_align=ft.TextAlign.CENTER)

    counter_box = ft.Row(
        [
            ft.IconButton(ft.Icons.REMOVE, on_click=decrease),
            count_value,
            ft.IconButton(ft.Icons.ADD, on_click=increase),
        ]
    )

    def create_item(item_id, name, count, done):
        return ft.Row(
            [
                ft.Checkbox(
                    value=bool(done),
                    on_change=lambda e: toggle(item_id, e.control.value)
                ),
                ft.Text(f"{name} (x{count})", expand=True),
                ft.IconButton( icon=ft.Icons.DELETE,  on_click=lambda e: delete(item_id) )
            ]
        )

    name_input = ft.TextField( label="Товар", expand=True, on_submit=add_item )

    add_btn = ft.ElevatedButton("Добавить", on_click=add_item)

    input_row = ft.Row([name_input, counter_box, add_btn])

    filter_row = ft.Row(
        [
            ft.TextButton("Все", on_click=lambda e: set_filter("all")),
            ft.TextButton("Купленные", on_click=lambda e: set_filter("done")),
            ft.TextButton("Не купленные", on_click=lambda e: set_filter("not_done")),
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(
        ft.Column(
            [
                ft.Text("Список покупок", size=20),
                input_row,
                filter_row,
                counter_text,
                ft.Divider(),
                list_view
            ],
            width=400
        )
    )

    load_items()


if __name__ == "__main__":
    main_db.init_db()
    ft.run(main , view = ft.AppView.WEB_BROWSER)