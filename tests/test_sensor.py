import unittest
from custom_components.sungrow.sensor import SungrowSensor

class TestSungrowSensor(unittest.TestCase):
    def setUp(self):
        self.sensor = SungrowSensor()

    def test_initial_state(self):
        self.assertEqual(self.sensor.state, None)

    def test_update_state(self):
        self.sensor.update_state(100)
        self.assertEqual(self.sensor.state, 100)

    def test_invalid_update(self):
        with self.assertRaises(ValueError):
            self.sensor.update_state("invalid")

    def test_sensor_attributes(self):
        self.sensor.update_state(200)
        self.assertEqual(self.sensor.name, "Sungrow Sensor")
        self.assertEqual(self.sensor.unit_of_measurement, "W")

if __name__ == '__main__':
    unittest.main()