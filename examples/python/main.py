import os
import navigator

print(f"Imports available: {print(navigator.__all__)}")

if os.environ.get("CI") == "true":
    print("Running in CI")
    print("Not possible to test navigator sensors yet.")

else:
    print("Initializin navigator module.")
    navigator.init()

    print("Setting leds on!")
    navigator.set_led_on()

    print(f"Temperature: {navigator.read_temp()}")

    print(f"Pressure: {navigator.read_pressure()}")

    Data = navigator.read_adc()
    print(
        f"Data ADC Channels: 1 = {Data.first}, 2 = {Data.second}, 3 = {Data.third}, 4 = {Data.fourth}"
    )

    Data = navigator.read_mag()
    print(f"Magnetic field: X = {Data.x}, Y = {Data.y}, Z = {Data.z}")

    Data = navigator.read_accel()
    print(f"Acceleration: X = {Data.x}, Y = {Data.y}, Z = {Data.z}")

    Data = navigator.read_gyro()
    print(f"Gyroscope: X = {Data.x}, Y = {Data.y}, Z = {Data.z}")

    print("Setting leds off!")
    navigator.set_led_off()
