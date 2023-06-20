import voluptuous as vol
from homeassistant.components import websocket_api
from homeassistant.config_entries import ConfigEntry
from datetime import timedelta, datetime
from urllib.parse import quote
from homeassistant.helpers import template

from .const import HA_TV_SERVER
from .manifest import manifest

SCHEMA_WEBSOCKET = websocket_api.BASE_COMMAND_MESSAGE_SCHEMA.extend(
    {
        "type": HA_TV_SERVER,
        vol.Optional("data"): dict,
    }
)

class HaTV():

    def __init__(self, hass):
        self.hass = hass
        self.connection = None
        # 事件
        self.events = []
        # 全部设备
        self.device = {}
        hass.components.websocket_api.async_register_command(
            HA_TV_SERVER,
            self.receive_data,
            SCHEMA_WEBSOCKET
        )

    # 模板解析
    def template(self, _message):
        tpl = template.Template(_message, self.hass)
        _message = tpl.async_render(None)
        return _message

    # 发送数据
    def send_data(self, type, data):
        self.hass.bus.fire(manifest.domain, { 'type': type, 'data': data })

    # 消息接收
    def receive_data(self, hass, connection, msg):
        self.connection = connection
        data = msg['data']
        msg_type = data.get('type')
        msg_data = data.get('data', {})
        for func in self.events:
            func(msg_type, msg_data)

    def on_event(self, func):
        if func not in self.events:
            self.events.append(func)