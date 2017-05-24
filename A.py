from pyp2p.net import *
import time
servers=[
    {
        "addr": "104.199.219.56",
        "port": 8000
    }
]
#Setup Alice's p2p node.
alice = Net(passive_bind="192.168.123.5", passive_port=44444, node_type="passive", debug=1,wan_ip="111.250.97.185",servers=servers)
alice.start()
alice.bootstrap()
alice.advertise()

#Event loop.
while 1:
    for con in alice:
        for reply in con:
            print(reply)

    time.sleep(1)
