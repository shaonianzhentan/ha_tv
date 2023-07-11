from __future__ import annotations

from typing import Any
import voluptuous as vol

from homeassistant.config_entries import ConfigFlow, OptionsFlow, ConfigEntry
from homeassistant.data_entry_flow import FlowResult
from homeassistant.core import callback

from .manifest import manifest

DATA_SCHEMA = vol.Schema({
    vol.Required('ip'): str,
    vol.Required('url'): str,
    vol.Required('token'): str
})

DOMAIN = manifest.domain

class SimpleConfigFlow(ConfigFlow, domain=DOMAIN):

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:

        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        errors = {}
        if user_input is not None:
            ip = user_input.get('ip')
            url = user_input.get('url')
            token = user_input.get('token')
            
            return self.async_create_entry(title=manifest.name, data={})

        return self.async_show_form(step_id="user", data_schema=DATA_SCHEMA, errors=errors)

    @staticmethod
    @callback
    def async_get_options_flow(entry: ConfigEntry):
        return OptionsFlowHandler(entry)


class OptionsFlowHandler(OptionsFlow):
    def __init__(self, config_entry: ConfigEntry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        return await self.async_step_user(user_input)

    async def async_step_user(self, user_input=None):
        options = self.config_entry.options
        errors = {}
        DATA_SCHEMA = vol.Schema({})
        return self.async_show_form(step_id="user", data_schema=DATA_SCHEMA, errors=errors)