import os



class NodeConfig():
    node_name = "robot_controller"
    reset_data = {"cmd" : 'reset', "par1" : None,  "par2" : None,  "par3" : None,  "par4" : None,  "par5" : None}

class GUIConfig():
    gui_name = "Main_ui"
    current_file_path   = os.path.abspath(__file__)
    current_directory   = os.path.dirname(current_file_path)
    parent_directory    = os.path.dirname(current_directory)
    main_ui_path        = "/home/rds/baris_edu/ui/main_window.ui"
    wait_drip_time      = 150
    drip_count          = 16
    sequence_cnt_reset  = 1


class DBConfig():
    db_path = "/home/rds/baris_edu/test.db"
    
    base_data = [{"cmd" : "HOME_NORMAL",     "par1" : "0",   "par2" : "0",   "par3" : "0",   "par4" : "0",   "par5" : "0"},
                {"cmd" : "GRIPPER_INIT",    "par1" : "0",   "par2" : "0",   "par3" : "0",   "par4" : "0",   "par5" : "0"},
                {"cmd" : "PICKUP",          "par1" : "DSP", "par2" : "2",   "par3" : "0",   "par4" : "0",   "par5" : "0"},
                {"cmd" : "HOLD",            "par1" : "COF", "par2" : "0",   "par3" : "0",   "par4" : "0",   "par5" : "0"},
                {"cmd" : "COFFEE_ON",       "par1" : None,  "par2" : None,  "par3" : None,  "par4" : None,  "par5" : None},
                {"cmd" : "UNHOLD",          "par1" : "COF", "par2" : "0",   "par3" : "0",   "par4" : "0",   "par5" : "0"},
                {"cmd" : "HOME_NORMAL",     "par1" : "0",   "par2" : "0",   "par3" : "0",   "par4" : "0",   "par5" : "0"},
                {"cmd" : "FLATTENING",      "par1" : "ZON", "par2" : "1",   "par3" : "0",   "par4" : "0",   "par5" : "0"},
                {"cmd" : "PLACE_DRIP",      "par1" : "ZON", "par2" : "1",   "par3" : "0",   "par4" : "0",   "par5" : "0"},
                {"cmd" : "PICKUP",          "par1" : "DSP", "par2" : "1",   "par3" : "0",   "par4" : "0",   "par5" : "0"},
                {"cmd" : "PLACE_CUP",       "par1" : "ZON", "par2" : "1",   "par3" : "0",   "par4" : "0",   "par5" : "0"},
                {"cmd" : "PICKUP",          "par1" : "KET", "par2" : "0",   "par3" : "0",   "par4" : "0",   "par5" : "0"},
                {"cmd" : "WATER_TOGGLE",    "par1" : None,  "par2" : None,  "par3" : None,  "par4" : None,  "par5" : None},
                {"cmd" : "DRAIN_FIT",       "par1" : "HOT", "par2" : "1",   "par3" : "DPO", "par4" : "0",   "par5" : "0"},
                {"cmd" : "HOME_KETTLE",     "par1" : "0",   "par2" : "0",   "par3" : "0",   "par4" : "0",   "par5" : "0"},
                {"cmd" : "DRIP",            "par1" : "DPO", "par2" : "SOL", "par3" : "HOT", "par4" : "1",   "par5" : "1"},
                {"cmd" : "HOME_KETTLE",     "par1" : "0",   "par2" : "0",   "par3" : "0",   "par4" : "0",   "par5" : "0"},
                {"cmd" : "DRAIN_ALL",       "par1" : "0",   "par2" : "0",   "par3" : "0",   "par4" : "0",   "par5" : "0"},
                {"cmd" : "PLACE",           "par1" : "KET", "par2" : "0",   "par3" : "0",   "par4" : "0",   "par5" : "0"},
                {"cmd" : "HOME_NORMAL",     "par1" : "0",   "par2" : "0",   "par3" : "0",   "par4" : "0",   "par5" : "0"},
                {"cmd" : "PICKUP_CUP",      "par1" : "ZON", "par2" : "1",   "par3" : "0",   "par4" : "0",   "par5" : "0"},
                {"cmd" : "PLACE",           "par1" : "PIC", "par2" : "1",   "par3" : "0",   "par4" : "0",   "par5" : "0"},
                {"cmd" : "PICKUP_DRIP",     "par1" : "ZON", "par2" : "1",   "par3" : "0",   "par4" : "0",   "par5" : "0"},
                {"cmd" : "PLACE",           "par1" : "BIN", "par2" : "0",   "par3" : "0",   "par4" : "0",   "par5" : "0"},
                {"cmd" : "GESTURE",         "par1" : "ETC", "par2" : "2",   "par3" : "0",   "par4" : "0",   "par5" : "0"}]
    
    create_table_query  = """CREATE TABLE robot_command_list (id INTEGER PRIMARY KEY AUTOINCREMENT, cmd TEXT, par1 TEXT     par2 TEXT   par3 TEXT   par4 TEXT   par5 TEXT);"""
    all_data_query      = """SELECT * FROM robot_command_list;"""
    max_id_query        = """SELECT MAX(id) FROM robot_command_list"""
    