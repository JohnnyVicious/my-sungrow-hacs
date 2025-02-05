from homeassistant.helpers.entity import Entity
from .const import DOMAIN, SENSOR_TYPES

class SungrowSensor(Entity):
    """Representation of a Sungrow sensor."""

    def __init__(self, sensor_type, name, device):
        """Initialize the sensor."""
        self._sensor_type = sensor_type
        self._name = name
        self._device = device
        self._state = None

    @property
    def unique_id(self):
        """Return a unique ID for this sensor."""
        return f"{self._device.unique_id}_{self._sensor_type}"

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def device_class(self):
        """Return the device class of the sensor."""
        return SENSOR_TYPES.get(self._sensor_type, None)

    async def async_update(self):
        """Fetch new state data for the sensor."""
        # Implement the logic to update the sensor state from the device
        self._state = await self._device.get_sensor_data(self._sensor_type)