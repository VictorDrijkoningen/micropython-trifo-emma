import time
import asyncio
import systemfunctions

def blink(pin):
    from machine import Pin
    led=Pin(pin,Pin.OUT)        #create LED object from pin2,Set Pin2 to output

    while True:
        led.value(1)            #Set led turn on
        time.sleep(0.5)
        led.value(0)            #Set led turn off
        time.sleep(0.5)

async def loop():
    done = False
    while not done:
        await asyncio.sleep(0.05)
        blink(2)


async def tasks():
    await asyncio.gather(loop())


if __name__ == "__main__":
    print("starting")
    systemfunctions.update()
    asyncio.run(tasks())