import rclpy as rp
import sys
import time

from threading import Thread
from rclpy.node import Node
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from library.Constants import Service, Topic
from message.msg import DispenserStatus, ComponentStatus
from message.srv import RobotService, DispenseService
from GUI.config import NodeConfig, GUIConfig

from GUI.db_manager import DBManager


class RobotController(Node):
    def __init__(self):
        super().__init__(NodeConfig.node_name)
        self.robot_client = self.create_client(RobotService, Service.SERVICE_ROBOT)
        self.dispenser_client = self.create_client(DispenseService, Service.SERVICE_DISPENSER)
        self.robot_sub = self.create_subscription(DispenserStatus, Topic.ROBOT_STATUS, self.state_callback, 1)

        self.robot_state = None
        self.seq_no = None
        self.component_status = None

    def state_callback(self, msg = DispenserStatus):
        self.robot_state = msg.node_status
        self.seq_no = msg.seq_no
        self.component_status = msg.component


    def get_robot_state(self):
        return self.robot_state
    

    def robot_service_call(self, data, seq_no) -> RobotService.Response:
        try:
            req = RobotService.Request()
            req.cmd = data["cmd"]

            if data['par1'] == None and data["cmd"] != "reset":
                req = DispenseService.Request()
                req.command = data["cmd"]
                req.seq_no = str(seq_no)
                res = self.dispenser_client.call(request=req)
                return res
            
            elif data['par1'] == None:
                res = self.robot_client.call(request=req)
                return res
            
            req.par1 = data["par1"]
            req.par2 = data["par2"]
            req.par3 = data["par3"]
            req.par4 = data["par4"]
            req.par5 = data["par5"]

            res = self.robot_client.call(request=req)
            return res
        
        except:
            print("unable service call")
            print(data)
            return False


    def __del__(self):
        pass



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db_manager = DBManager()
        uic.loadUi(GUIConfig.main_ui_path, self)

        self.is_wait = False
        self.sequence_count = GUIConfig.sequence_cnt_reset

        self.node_thread = Thread(target=self.run_node)
        self.node_deamon = True
        self.node_thread.start()
        self.wait_thread = Thread(target=self.wait_drip)
        self.wait_deamon = True
        self.wait_thread.start()

        self.orderButton.clicked.connect(self.start_order)
        self.init_hide()



    def init_hide(self):
        self.order_label_1.hide()
        self.progressBar_1.hide()
        # self.timer_label.hide()

        
    def run_node(self):
        rp.init(args=None)
        node = RobotController()
        self.node = node
        old_state = self.node.robot_state
        while self.node_deamon:
            rp.spin_once(self.node)
            if self.node.robot_state != old_state:
                self.progress_label.setText("robot_state : " + str(self.node.robot_state))
            old_state = self.node.robot_state
        rp.shutdown()
        

    def start_order(self):
        max_id = self.db_manager.get_max_id()
        self.progressBar_1.setMaximum(max_id)
        self.progressBar_1.show()
        self.order_label_1.show()
        self.order_label_1.setText("커피를 준비중 입니다.")

        for i in range(self.sequence_count, max_id):
            is_drip = self.next_sequence()
            self.progressBar_1.setValue(i)
            time.sleep(0.3)
            if is_drip:
                return

        self.order_label_1.setText("커피가 준비되었어요")
        self.progressBar_1.setValue(max_id)
        self.sequence_count = GUIConfig.sequence_cnt_reset
        self.node.robot_service_call(NodeConfig.reset_data, None) # service call reset


    def next_sequence(self):
        data = self.db_manager.get_cammand(self.sequence_count)
        if not data:
            return
        res = self.node.robot_service_call(data, self.sequence_count)
        # print(res)
        if self.sequence_count == GUIConfig.drip_count:
            self.order_label_1.setText("커피를 내리고 있어요")
            self.is_wait = True
            self.sequence_count += 1
            return True

        self.sequence_count += 1
        return False

    def wait_drip(self):
        while self.wait_deamon:
            if self.is_wait :
                self.timer_label.show()
                start_time = time.time()
                current_time = time.time()

                while current_time - start_time <= GUIConfig.wait_drip_time:
                    self.timer_label.setText(str(int(GUIConfig.wait_drip_time - current_time + start_time) // 60) + " : " + str(int(GUIConfig.wait_drip_time - current_time + start_time) % 60))
                    current_time = time.time()
                    time.sleep(0.3)

                self.timer_label.hide()
                self.orderButton.click()
                self.is_wait = False
            else:
                time.sleep(0.3)
            
            
        

    def __del__(self):
        self.node_deamon = False
        self.node.destroy_node()
    
    

def main(args=None):
    app = QApplication(sys.argv)
    
    try:
        main_window = MainWindow()
        main_window.show()
        
    except KeyboardInterrupt:
        print('Keyboard Interrupt (SIGINT)')

    finally:
        print("RobotSystemNode System Deinit")
        sys.exit(app.exec_())

if __name__ == "__main__":
    main()