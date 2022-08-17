#!/opt/monitor/venv/bin/python
import sys
import time
import logging
from pathlib import Path
import json
import serial
import os

logging.basicConfig(stream=sys.stdout, format="%(asctime)s %(levelname)-8s %(message)s", level=logging.DEBUG)

SLOWDIR = '/opt/monitor'

DEVS=[
  {
      'sn': '20061518',
      'model': 'UA10',
      'dev': '/dev/serial/by-id/usb-Dekist_Co.__Ltd._UA_SERIES__20061518-if00',
  },
]

def read(devinfo):
    datapoint = {}
    with serial.Serial(devinfo['dev'], 19200, timeout=5) as ser:
        ser.write(b'ATCD\r\n')
        line = ser.readline()   # read a '\n' terminated line
    line = line.decode('utf-8').strip()
    logging.debug(f'RESPONSE: {line}')
    cmd, result = line.split(' ')
    if devinfo['model'] == 'UA10':
        temp, hum = result.split(',')
        datapoint = {
            'measurement': 'temphum',
            'sn': devinfo['sn'],
            'model': devinfo['model'],
            'time': int(time.time()),
            'temp': float(temp),
            'hum': float(hum),
        }
    return datapoint

def main():
    while True:
        data = []
        for devinfo in DEVS:
            try:
                datapoint = read(devinfo)
                data.append(datapoint)
            except:
                logging.exception('Exception: ')
        logging.debug(data)
        try:
            p = Path(SLOWDIR) / 'data' / 'UA10.log'
            with p.open('w') as f:
                for d in data:
                    f.write(json.dumps(d)+'\n')

            cmd = f'scp {p} ymmon:/monitor/raw/'
            os.popen(cmd)

            time.sleep(60)
        except KeyboardInterrupt:
            logging.info('Good bye!')
            break
        except:
            logging.exception('Exception: ')
            time.sleep(60)

if __name__ == '__main__':
    main()
