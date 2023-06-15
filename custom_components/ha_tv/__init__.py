from homeassistant.config_entries import ConfigEntry
from homeassistant.core import CoreState, HomeAssistant, Context
import homeassistant.helpers.config_validation as cv

import logging

from .manifest import manifest

_LOGGER = logging.getLogger(__name__)
CONFIG_SCHEMA = cv.deprecated(manifest.domain)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    config = entry.data
    entry.async_on_unload(entry.add_update_listener(update_listener))
    await update_listener(hass, entry)

    async def async_location(call):
        data = call.data
        event_data = {
            "type": "location",
            "data": data.get("url")
        }
        hass.bus.async_fire("ha_tv", event_data)

    async def async_notify(call):
        data = call.data
        event_data = {
            "type": "notify",
            "data": {
                "title": data.get("title"),
                "message": data.get("message")
            }
        }
        hass.bus.async_fire("ha_tv", event_data)

    hass.services.async_register(manifest.domain, 'location', async_location)
    hass.services.async_register(manifest.domain, 'notify', async_notify)
    return True

async def update_listener(hass, entry):
    options = entry.options

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    config = entry.data
    return True