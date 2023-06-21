"""Support to interact with a Music Player Daemon."""
from __future__ import annotations

from contextlib import suppress
from datetime import timedelta, datetime
import logging
from typing import Any
from urllib.parse import quote
import voluptuous as vol

from homeassistant.components.media_player import (
    BrowseMedia,
    MediaPlayerEntity,
    MediaPlayerEntityFeature,
    MediaPlayerDeviceClass,
)
from homeassistant.const import (
    STATE_OFF, 
    STATE_ON, 
    STATE_PLAYING, 
    STATE_PAUSED,
    STATE_UNAVAILABLE,
    CONF_NAME
)
from homeassistant.components.media_player.const import (
    SUPPORT_BROWSE_MEDIA,
    SUPPORT_TURN_OFF,
    SUPPORT_TURN_ON,
    SUPPORT_VOLUME_STEP,
    SUPPORT_VOLUME_SET,
    SUPPORT_VOLUME_MUTE,
    SUPPORT_SELECT_SOURCE,
    SUPPORT_SELECT_SOUND_MODE,
    SUPPORT_PLAY_MEDIA,
    SUPPORT_PLAY,
    SUPPORT_PAUSE,
    SUPPORT_SEEK,
    SUPPORT_CLEAR_PLAYLIST,
    SUPPORT_SHUFFLE_SET,
    SUPPORT_REPEAT_SET,
    SUPPORT_NEXT_TRACK,
    SUPPORT_PREVIOUS_TRACK,
    MEDIA_TYPE_MUSIC
)
from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.util import Throttle
import homeassistant.util.dt as dt_util

_LOGGER = logging.getLogger(__name__)

from .manifest import manifest, get_device_info

SUPPORT_FEATURES = SUPPORT_VOLUME_STEP | SUPPORT_VOLUME_MUTE | SUPPORT_VOLUME_SET | \
    SUPPORT_SELECT_SOURCE | SUPPORT_SELECT_SOUND_MODE | SUPPORT_TURN_ON | SUPPORT_TURN_OFF | \
    SUPPORT_PLAY_MEDIA | SUPPORT_PLAY | SUPPORT_PAUSE | SUPPORT_PREVIOUS_TRACK | SUPPORT_NEXT_TRACK | \
    SUPPORT_SEEK | SUPPORT_CLEAR_PLAYLIST | SUPPORT_SHUFFLE_SET | SUPPORT_REPEAT_SET

async def async_setup_entry(
    hass: HomeAssistant,
    entry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    # 播放器
    async_add_entities([ AndroidTVMediaPlayer(hass, entry) ], True)

class AndroidTVMediaPlayer(MediaPlayerEntity):

    def __init__(self, hass, entry):
        self.hass = hass
        self._attr_unique_id = entry.entry_id
        self._attr_name = "家庭助理TV应用"

        self._attr_media_image_remotely_accessible = True
        self._attr_device_class = MediaPlayerDeviceClass.TV.value
        self._attr_supported_features = SUPPORT_FEATURES
        self._attr_extra_state_attributes = { 'platform': 'tv' }

        # default attribute
        self._attr_source_list = []
        self._attr_sound_mode_list = []
        self._attr_state =  STATE_OFF
        self._attr_volume_level = 1
        self._attr_repeat = 'all'
        self._attr_shuffle = False

        self._attr_media_position_updated_at = datetime.now()

        self.tv = hass.data.get(manifest.domain)
        self.tv.on_event(self.tv_event)

    def tv_event(self, msg_type, msg_data):
        if msg_type == 'media_info':
            state = msg_data.get('state')
            if state == 'playing':
                state = STATE_PLAYING
            elif state == 'paused':
                state = STATE_PAUSED
            else:
                state = STATE_ON

            self._attr_state = state
            self._attr_media_position = msg_data.get('media_position', 0)
            self._attr_media_duration = msg_data.get('media_duration', 0)
            self._attr_volume_level = msg_data.get('volume')
            self._attr_repeat = msg_data.get('repeat')
            self._attr_shuffle = msg_data.get('shuffle')
            self._attr_is_volume_muted = msg_data.get('muted')
            self._attr_media_position_updated_at = datetime.now()

    @property
    def device_info(self):
        return get_device_info(self._attr_unique_id, self._attr_name)

    async def async_update(self) -> None:
        if (datetime.now() - self._attr_media_position_updated_at).total_seconds() > 120:
            self._attr_state = STATE_OFF

    async def async_set_volume_level(self, volume: float) -> None:
        self._attr_volume_level = volume
        self.tv.send_data('set_volume_level', volume)

    async def async_volume_up(self) -> None:
        volume_level = self._attr_volume_level + 0.1
        if volume_level > 1:
            volume_level = 1
        self._attr_volume_level = volume_level
        await self.async_set_volume_level(volume_level)

    async def async_volume_down(self) -> None:
        volume_level = self._attr_volume_level - 0.1
        if volume_level < 0.1:
            volume_level = 0.1
        self._attr_volume_level = volume_level
        await self.async_set_volume_level(volume_level)

    async def async_media_play(self) -> None:
        self._attr_state = STATE_PLAYING
        self.tv.send_data('media_play', '')

    async def async_media_pause(self) -> None:
        self._attr_state = STATE_PAUSED
        self.tv.send_data('media_pause', '')

    async def async_media_next_track(self) -> None:
        self._attr_state = STATE_PAUSED
        self.tv.send_data('media_next_track', '')

    async def async_media_previous_track(self) -> None:
        self._attr_state = STATE_PAUSED
        self.tv.send_data('media_previous_track', '')

    async def async_turn_off(self) -> None:
        pass

    async def async_turn_on(self) -> None:
        pass

    async def async_mute_volume(self, mute: bool) -> None:
        self._attr_is_volume_muted = mute
        self.tv.send_data('mute_volume', mute)

    async def async_set_repeat(self, repeat) -> None:
        self._attr_repeat = repeat
        self.tv.send_data('set_repeat', repeat)

    async def async_set_shuffle(self, shuffle: bool) -> None:
        self._attr_shuffle = shuffle
        self.tv.send_data('set_shuffle', shuffle)

    async def async_media_seek(self, position: float) -> None:
        self._attr_media_position = position
        self.tv.send_data('media_seek', position)

    async def async_play_media(self, media_type: str, media_id: str, **kwargs: Any) -> None:
        print(media_type, media_id)
        self.tv.send_data('play_media', { 'media_type': media_type, 'media_id': media_id })