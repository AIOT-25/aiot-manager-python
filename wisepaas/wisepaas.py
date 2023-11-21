import datetime
import random
from wisepaasdatahubedgesdk.EdgeAgent import EdgeAgent
import wisepaasdatahubedgesdk.Common.Constants as constant
from wisepaasdatahubedgesdk.Model.Edge import EdgeAgentOptions, MQTTOptions, DCCSOptions, EdgeData, EdgeTag, EdgeStatus, EdgeDeviceStatus, EdgeConfig, NodeConfig, DeviceConfig, AnalogTagConfig, DiscreteTagConfig, TextTagConfig
from wisepaasdatahubedgesdk.Common.Utils import RepeatedTimer
import time

def get_edge_agent_options(config):
    print(config['nodeId'].strip())
    return EdgeAgentOptions(
        reconnectInterval=1,
        nodeId=config['nodeId'].strip(),
        type=constant.EdgeType['Gateway'],
        heartbeat=60,
        dataRecover = True,
        connectType = constant.ConnectType['DCCS'],
        DCCS = DCCSOptions(
            apiUrl = config['dccs']['apiUrl'].strip(),
            credentialKey = config['dccs']['credentialKey'].strip()
        ),
    )

class WisePaas:
    def __init__(self, config):
        if config == None:
            raise("Config can't be None")
        self.config = config
        self.options = get_edge_agent_options(self.config)
        self.edgeAgent = None

    def connect(self):
        edgeAgent = EdgeAgent(options=self.options)
        edgeAgent.on_connected = self.edgeAgent_on_connected
        edgeAgent.on_disconnected = self.edgeAgent_on_disconnected
        edgeAgent.on_message = self.edgeAgent_on_message
        edgeAgent.connect()
        self.edgeAgent = edgeAgent
        
    def disconnect(self):
        self.edgeAgent.disconnect()        

    def edgeAgent_on_connected(agent, isConnected):
        print('Connection success')

    def edgeAgent_on_disconnected(agent, isDisconnected):
        print('Disconnected')

    def edgeAgent_on_message(agent, messageReceivedEventArgs):
    # messageReceivedEventArgs format: Model.Event.MessageReceivedEventArgs
        type = messageReceivedEventArgs.type
        message = messageReceivedEventArgs.message
        if type == constant.MessageType['WriteValue']:
        # message format: Model.Edge.WriteValueCommand
            for device in message.deviceList:
                print('deviceId: {0}'.format(device.Id))
            for tag in device.tagList:
                print('tagName: {0}, Value: {1}'.format(tag.name, str(tag.value)))
        elif type == constant.MessageType['WriteConfig']:
            print('WriteConfig')
        elif type == constant.MessageType['TimeSync']:
        # message format: Model.Edge.TimeSyncCommand
            print(str(message.UTCTime))
        elif type == constant.MessageType['ConfigAck']:
        # message format: Model.Edge.ConfigAck
            print({'Upload Config Result: {0}'}.format(str(message.result)))

    def get_edge_list(self):
        list = []
        for i in range(1, self.config["edgeTag"]["count"] + 1):
            list.append(self.config["edgeTag"][f'tag{i}'])
        return list        

# edgeData = EdgeData()
# total = 0
# v = 12
# while True:
#     inter_flow = random.randint(1, 20)
#     total += inter_flow
#     if total > 200:
#         outer_flow = inter_flow * 1.2
#         energy = outer_flow * 15
#         current = energy / v
#     else:
#         outer_flow = inter_flow * 0.8
#         energy = outer_flow * 10
#         current = energy / v
#     total -= outer_flow
   
#     deviceId = '6lQguETNe7sT'
#     edgeData.tagList.append(EdgeTag(deviceId, 'a', inter_flow))
#     edgeData.tagList.append(EdgeTag(deviceId, 'b', outer_flow))
#     edgeData.tagList.append(EdgeTag(deviceId, 'c', v))
#     edgeData.tagList.append(EdgeTag(deviceId, 'd', energy))
#     edgeData.timestamp = datetime.datetime.now()
#     #edgeData.timestamp = datetime.datetime(2020,8,24,6,10,8)   # You can specify the time(local time) of data
#     result = edgeAgent.sendData(data = edgeData)
#     print(result)
#     time.sleep(1) 