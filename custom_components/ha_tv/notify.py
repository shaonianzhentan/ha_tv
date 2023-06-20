"""Notify.Events platform for notify component."""
from __future__ import annotations

import logging

from homeassistant.components.notify import (
    ATTR_DATA,
    ATTR_TITLE,
    BaseNotificationService,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from .manifest import manifest

_LOGGER = logging.getLogger(__name__)

def get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None):
    return AndroidTVNotificationService(hass, discovery_info)

class AndroidTVNotificationService(BaseNotificationService):

    def __init__(self, hass, config):
        self.hass = hass        

    def send_message(self, message, **kwargs):
        """Send a message."""
        data = kwargs.get(ATTR_DATA) or {}

        tv = self.hass.data.get(manifest.domain)
        tv.send_data('notify', {
                "title": kwargs.get(ATTR_TITLE),
                "message": message,
                'url': data.get('url')
            })