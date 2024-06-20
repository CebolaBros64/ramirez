import dearpygui.dearpygui as dpg
from LMS.Message.MSBT import MSBT, MSBP
from LMS.Stream.Reader import Reader

if __name__ == '__main__':
    # Create the MSBT object
    msbt = MSBT()
    msbp = MSBP()
    
    with open('msbt/pajama.msbp', 'rb+') as msbp_f:
        reader1 = Reader(msbp_f.read())
        msbp.read(reader1)
        with open('msbt/agb.msbt', 'rb+') as message:
            # Create the reader object 
            reader = Reader(message.read())
            # Read the MSBT
            msbt.read(reader, msbp)
        
    dpg.create_context()
    dpg.create_viewport(title="Ramirez", width=1000, height=500)

    with dpg.window(tag='primaryWindow'):
        dpg.add_text('Ramirez')

    with dpg.window(label="Entries", min_size=(225, 400), max_size=(225, 400), pos=(10, 20), no_close=True):
        def _selection(sender, app_data, user_data):
            print(f"User selected ${sender}")
            # dpg.set_value('originalMessage', msbt.TXT2.messages[int(sender.split('_')[1])])
            dpg.set_value('originalMessage', repr(msbt.TXT2.messages[int(sender.split('_')[1])])[1:-1])

            for _item in user_data:
                if _item != sender:
                    dpg.set_value(_item, False)
        
        items = []

        for index in msbt.LBL1.labels:
            items.append(dpg.add_selectable(label=msbt.LBL1.labels[index], tag=f"entry_{index}"))

        for item in items:
            dpg.configure_item(item, callback=_selection, user_data=items)
    
    with dpg.window(label="Original Message", min_size=(500, 200), max_size=(500, 200), pos=(250, 20), no_close=True):
        #dpg.add_input_text(tag='originalMessage', enabled=False, width=500, height=200)
        dpg.add_text(tag='originalMessage', wrap=485)

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window('primaryWindow', True)
    dpg.start_dearpygui()
    dpg.destroy_context()

