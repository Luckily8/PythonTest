import threading
import time
import zlib  # 导入zlib库用于CRC计算


# 模拟的 CAN 总线类
class CANBus:
    def __init__(self):
        self.bus_lock = threading.Lock()
        self.current_senders = []
        self.arbitration_in_progress = False

    def request_to_send(self, node_id, msg_id):
        with self.bus_lock:
            print(f" 节点 {node_id} 请求发送消息 ID: {msg_id}".center(80, "*"))
            self.current_senders.append((node_id, msg_id))

    def start_arbitration(self):
        with self.bus_lock:
            if not self.arbitration_in_progress and self.current_senders:
                self.arbitration_in_progress = True
                print("\n=== 开始仲裁过程 ===")
                # 按照消息 ID 从小到大排序，ID 越小优先级越高
                self.current_senders.sort(key=lambda x: x[1])
                print("参与仲裁的节点及其消息 ID:")
                for sender in self.current_senders:
                    print(f"  节点 {sender[0]} - 消息 ID: {sender[1]}")
                winner = self.current_senders[0]
                print(f"仲裁结果: 节点 {winner[0]} 胜出，准备发送消息 ID: {winner[1]}")
                # 通知其他节点仲裁结果
                losers = self.current_senders[1:]
                self.current_senders = []
                self.arbitration_in_progress = False
                return winner, losers
            else:
                return None, None

    def calculate_crc(self, msg_id):
        msg_bytes = msg_id.to_bytes(2, byteorder="big")
        crc = zlib.crc32(msg_bytes)
        return crc


# 预定义的消息 ID，节点 1 到 4 的优先级从高到低
NODE_IDS = {1: 0x100, 2: 0x110, 3: 0x120, 4: 0x130}

# 主程序
if __name__ == "__main__":
    bus = CANBus()

    while True:
        try:
            node_ids = input(
                "请输入多个节点 ID (1-4), 用逗号分隔，或输入 0 退出: "
            ).split(",")
            if "0" in node_ids:
                print("模拟结束。")
                break
            node_ids = [
                int(node_id.strip())
                for node_id in node_ids
                if node_id.strip().isdigit() and 1 <= int(node_id.strip()) <= 4
            ]
            if not node_ids:
                print("无效的节点 ID，请输入 1 到 4 之间的数字。")
                continue
            data_list = input("请输入对应的数据，用逗号分隔: ").split(",")
            if len(node_ids) != len(data_list):
                print("节点 ID 和数据的数量不匹配，请重新输入。")
                continue

            for node_id, data in zip(node_ids, data_list):
                msg_id = NODE_IDS[node_id]  # 使用预定义的消息 ID
                bus.request_to_send(node_id, msg_id)
            winner, losers = bus.start_arbitration()
            if winner:
                for node_id, data in zip(node_ids, data_list):
                    if winner[0] == node_id:
                        crc = bus.calculate_crc(NODE_IDS[node_id])
                        print(
                            f"节点 {node_id} 正在发送数据: {data}, 消息 ID: {NODE_IDS[node_id]}, CRC 校验码: {crc:#010x}"
                        )
                        time.sleep(0.2)
                        print(f"节点 {node_id} 完成数据: {data} 的发送\n")
                    elif any(loser[0] == node_id for loser in losers):
                        print(f"节点 {node_id} 仲裁失败，等待下一次发送")
            else:
                print("仲裁尚未开始或没有胜出")
        except ValueError:
            print("输入无效，请输入有效的数字。")
