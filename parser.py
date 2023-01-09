import re

def parse(incoming_data):
    if not incoming_data:
        return {'Interval': None, 'Transfer': None, 'Bandwidth': None}

    interval = re.findall(r"\d+.\d+-\d+.\d+ sec", incoming_data)[0].replace(' sec', '')
    transfer = float(re.findall(r"\d+.\d+ MBytes", incoming_data)[0].replace(' MBytes', ''))
    bandwidth = float(re.findall(r"\d+.\d+ Mbits.sec", incoming_data)[0].replace(' Mbits/sec', ''))

    return {'Interval': interval, 'Transfer': transfer, 'Bandwidth': bandwidth}
