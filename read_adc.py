import smbus
import time

bus = smbus.SMBus(1)
ADDR = 0x48

CONFIG_REG = 0x01
CONVERT_REG = 0x00

def read_adc(channel=0):
    
    mux = 0x4000 + (channel << 12)

    config = (
        0x8000 |  # start conversion
        mux   |   # channel select
        0x0200 |  # 4.096V range
        0x0100 |  # single-shot
        0x0080 |  # 128 SPS
        0x0003    # disable comparator
    )

    bus.write_i2c_block_data(ADDR, CONFIG_REG,
                             [(config >> 8) & 0xFF, config & 0xFF])

    time.sleep(0.01)

    data = bus.read_i2c_block_data(ADDR, CONVERT_REG, 2)

    value = (data[0] << 8) | data[1]

    if value > 32767:
        value -= 65536

    return value

if __name__=="__main__" :
	print(read_adc(0))