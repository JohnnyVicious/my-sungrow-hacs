# FILE: /my-sungrow-hacs/my-sungrow-hacs/custom_components/sungrow/const.py
"""Constants for the Sungrow integration."""

DOMAIN = "sungrow"

# Sensor types
SENSOR_TYPE_POWER = "power"
SENSOR_TYPE_ENERGY = "energy"
SENSOR_TYPE_VOLTAGE = "voltage"
SENSOR_TYPE_CURRENT = "current"
SENSOR_TYPE_TEMPERATURE = "temperature"

# Units of measurement
UNIT_WATT = "W"
UNIT_WATT_HOUR = "Wh"
UNIT_VOLT = "V"
UNIT_AMPERE = "A"
UNIT_CELSIUS = "°C"

# Configuration keys
CONF_DEVICE_TYPE = "device_type"
CONF_MODBUS_ADDRESS = "modbus_address"
CONF_UPDATE_INTERVAL = "update_interval"

# Default values
DEFAULT_UPDATE_INTERVAL = 60  # seconds

# Error messages
ERROR_CONNECTION = "Failed to connect to the Sungrow inverter."
ERROR_INVALID_RESPONSE = "Received invalid response from the Sungrow inverter."