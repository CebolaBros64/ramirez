import dearpygui.dearpygui as dpg
from LMS.Message.MSBT import MSBT
from LMS.Stream.Reader import Reader

if __name__ == '__main__':
    # Create the MSBT object
    msbt = MSBT()

    with open('msbt/agb.msbt', 'rb+') as message:
        # Create the reader object 
        reader = Reader(message.read())
        # Read the MSBT
        msbt.read(reader)
    
    print(msbt)
        
    dpg.create_context()
    dpg.create_viewport(title="Ramirez", width=800, height=900)

    with dpg.window(tag='primaryWindow'):
        dpg.add_text('Ramirez')

    with dpg.window(label="Entries", min_size=(200, 400), max_size=(200, 400), pos=(10, 20), no_close=True):
        def _selection(sender, app_data, user_data):
            print(f"User selected ${sender}")

            for _item in user_data:
                if _item != sender:
                    dpg.set_value(_item, False)
        
        items = []

        for i in range(1, 50 + 1):
            items.append(dpg.add_selectable(label=f"Entry {i}", tag=f"entry_{i}"))

        for item in items:
            dpg.configure_item(item, callback=_selection, user_data=items)

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window('primaryWindow', True)
    dpg.start_dearpygui()
    dpg.destroy_context()

