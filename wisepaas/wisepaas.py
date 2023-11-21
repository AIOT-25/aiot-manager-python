import datetime
import random
from wisepaasdatahubedgesdk.EdgeAgent import EdgeAgent
import wisepaasdatahubedgesdk.Common.Constants as constant
from wisepaasdatahubedgesdk.Model.Edge import EdgeAgentOptions, MQTTOptions, DCCSOptions, EdgeData, EdgeTag, EdgeStatus, EdgeDeviceStatus, EdgeConfig, NodeConfig, DeviceConfig, AnalogTagConfig, DiscreteTagConfig, TextTagConfig
from wisepaasdatahubedgesdk.Common.Utils import RepeatedTimer
import time

def get_edge_agent_options(config):
    return EdgeAgentOptions(
        reconnectInterval=0.01,
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

class WisePaasClient:
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

    def is_connected(self):
        return not self.edgeAgent == None and self.edgeAgent.isConnected()

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

    def save_edge_data(self, datas, retry=300):
        if not self.is_connected():
            return False
        edgeData = EdgeData()
        edgeList = self.get_edge_list()
        deviceId = self.config["deviceId"]
        for i in range(self.config["edgeTag"]["count"]):
            edgeData.tagList.append(EdgeTag(deviceId, edgeList[i], datas[i]))
        edgeData.timestamp = datetime.datetime.now()
        for i in range(retry):
            self.edgeAgent.sendData(data = edgeData)