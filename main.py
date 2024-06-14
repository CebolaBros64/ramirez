import dearpygui.dearpygui as dpg

if __name__ == '__main__':
    dpg.create_context()

    dpg.create_viewport(title="Ramirez", width=800, height=900)

    with dpg.window(tag='primaryWindow'):
        dpg.add_text('Ramirez')

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window('primaryWindow', True)
    dpg.start_dearpygui()
    dpg.destroy_context()

