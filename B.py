from pyp2p.net import *
servers=[
    {
        "addr": "104.199.192.71",
        "port": 8000
    }
]
#Setup Bob's p2p node.
bob = Net(passive_bind="192.168.8.108", passive_port=44445, node_type="passive", debug=1,wan_ip="180.217.173.79",servers=servers)
bob.start()
bob.bootstrap()
bob.advertise()

#Event loop.
while 1:
    for con in bob:
        con.send_line("test")

    time.sleep(1)
