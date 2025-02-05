# FILE: /my-sungrow-hacs/my-sungrow-hacs/custom_components/sungrow/__init__.py
"""Initialize the Sungrow integration."""

from homeassistant import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers import discovery

DOMAIN = "sungrow"

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the Sungrow integration."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Sungrow from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    # Load sensors or other components here
    await discovery.async_load_platform(hass, "sensor", DOMAIN, {}, entry)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    await discovery.async_unload_platform(hass, "sensor", DOMAIN)
    return True