from homeassistant.config_entries import ConfigEntry
from homeassistant.core import CoreState, HomeAssistant, Context
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers import discovery
from homeassistant.const import Platform
import logging

from .const import PLATFORMS
from .manifest import manifest
from .ha_tv import HaTV

_LOGGER = logging.getLogger(__name__)
CONFIG_SCHEMA = cv.deprecated(manifest.domain)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    # 初始化服务
    tv = hass.data.get(manifest.domain)
    if tv is None:
        tv = HaTV(hass)
        hass.data.setdefault(manifest.domain, tv)

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    entry.async_on_unload(entry.add_update_listener(update_listener))
    await discovery.async_load_platform(hass,
        Platform.NOTIFY,
        manifest.domain,
        {
            'name': manifest.domain,
            'entry_id': entry.entry_id
        },
        {},
    )
    return True

async def update_listener(hass, entry):
    await async_unload_entry(hass, entry)
    await async_setup_entry(hass, entry)

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)