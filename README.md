# My Sungrow HACS Integration

This repository contains a custom integration for Home Assistant to support Sungrow solar inverters via Modbus communication.

## Features

- Monitors various parameters from Sungrow inverters.
- Supports multiple device types.
- Provides real-time updates on inverter status.

## Installation

1. **HACS Installation**:
   - Ensure you have [HACS](https://hacs.xyz/) installed in your Home Assistant instance.
   - Go to HACS in your Home Assistant UI.

2. **Add Custom Repository**:
   - Navigate to the "Integrations" tab.
   - Click on the "+" button to add a new integration.
   - Enter the repository URL: `https://github.com/yourusername/my-sungrow-hacs`.

3. **Install the Integration**:
   - Find "Sungrow" in the list and click "Install".

4. **Restart Home Assistant**:
   - After installation, restart your Home Assistant instance to load the new integration.

## Configuration

To configure the Sungrow integration, add the following to your `configuration.yaml`:

```yaml
sungrow:
  host: <IP_ADDRESS>
  port: <PORT>
```

Replace `<IP_ADDRESS>` and `<PORT>` with the appropriate values for your Sungrow inverter.

## Usage

Once configured, the integration will create sensor entities in Home Assistant that represent various metrics from your Sungrow inverter. You can view these sensors in the Home Assistant dashboard.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.