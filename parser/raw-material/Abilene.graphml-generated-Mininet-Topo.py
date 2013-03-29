#!/usr/bin/python

"""
Custom topology for Mininet, generated by GraphML-Topo-to-Mininet-Network-Generator.
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.node import Node
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

class GeneratedTopo( Topo ):
    "Internet Topology Zoo Specimen."

    def __init__( self, **opts ):
        "Create a topology."

        # Initialize Topology
        Topo.__init__( self, **opts )

        # add nodes
        # switches first
        NewYork = self.addSwitch( 's0' )
        NewYork_host = self.addHost( 'h0' )
        Chicago = self.addSwitch( 's1' )
        Chicago_host = self.addHost( 'h1' )
        WashingtonDC = self.addSwitch( 's2' )
        WashingtonDC_host = self.addHost( 'h2' )
        Seattle = self.addSwitch( 's3' )
        Seattle_host = self.addHost( 'h3' )
        Sunnyvale = self.addSwitch( 's4' )
        Sunnyvale_host = self.addHost( 'h4' )
        LosAngeles = self.addSwitch( 's5' )
        LosAngeles_host = self.addHost( 'h5' )
        Denver = self.addSwitch( 's6' )
        Denver_host = self.addHost( 'h6' )
        KansasCity = self.addSwitch( 's7' )
        KansasCity_host = self.addHost( 'h7' )
        Houston = self.addSwitch( 's8' )
        Houston_host = self.addHost( 'h8' )
        Atlanta = self.addSwitch( 's9' )
        Atlanta_host = self.addHost( 'h9' )
        Indianapolis = self.addSwitch( 's10' )
        Indianapolis_host = self.addHost( 'h10' )

        # hosts (put here if needed)
        # dont forget to add edges afterwards!

        #FIXME host and links section needs adjusting to your topology needs!!!
        # this are just exemplarical entries,
        # fitting my topology and needs.
        # I left this here as an sample entry.

        #FIXME this was needed before a host per switch was generated and linked

        #node1 = self.addHost( 'h1' )
        #node2 = self.addHost( 'h2' )

        # next tree lines never put to use so far
        #node3 = self.addHost( 'rcv1' )
        #node4 = self.addHost( 'rcv2' )
        #node5 = self.addHost( 'logserv' )

        #self.addLink( HAM , node1 )
        #self.addLink( GAR , node2 )

        # add edges
        self.addLink( NewYork , Chicago, bw=50, delay='0.690677696537ms')
        self.addLink( NewYork , NewYork_host )
        self.addLink( NewYork , WashingtonDC, bw=50, delay='0.518903303662ms')
        self.addLink( NewYork , NewYork_host )
        self.addLink( Chicago , Indianapolis, bw=50, delay='1.15170240387ms')
        self.addLink( Chicago , Chicago_host )
        self.addLink( WashingtonDC , Atlanta, bw=50, delay='0.477628158502ms')
        self.addLink( WashingtonDC , WashingtonDC_host )
        self.addLink( Seattle , Sunnyvale, bw=50, delay='1.10351797289ms')
        self.addLink( Seattle , Seattle_host )
        self.addLink( Seattle , Denver, bw=50, delay='0.952189623151ms')
        self.addLink( Seattle , Seattle_host )
        self.addLink( Sunnyvale , LosAngeles, bw=50, delay='0.506044716762ms')
        self.addLink( Sunnyvale , Sunnyvale_host )
        self.addLink( Sunnyvale , Denver, bw=50, delay='0.85423284091ms')
        self.addLink( Sunnyvale , Sunnyvale_host )
        self.addLink( LosAngeles , Houston, bw=50, delay='1.02920365882ms')
        self.addLink( LosAngeles , LosAngeles_host )
        self.addLink( Denver , KansasCity, bw=50, delay='0.191285963954ms')
        self.addLink( Denver , Denver_host )
        self.addLink( KansasCity , Houston, bw=50, delay='1.46743666378ms')
        self.addLink( KansasCity , KansasCity_host )
        self.addLink( KansasCity , Indianapolis, bw=50, delay='0.206336052247ms')
        self.addLink( KansasCity , KansasCity_host )
        self.addLink( Houston , Atlanta, bw=50, delay='1.15068985002ms')
        self.addLink( Houston , Houston_host )
        self.addLink( Atlanta , Indianapolis, bw=50, delay='0.466772343871ms')
        self.addLink( Atlanta , Atlanta_host )


topos = { 'generated': ( lambda: GeneratedTopo() ) }

# here the code defining the topology ends
# the following code produces an executable script working with a remote controller
# and ssh access to the the mininet hosts from within the ubuntu vm
def setupNetwork():
    "Create network and run simple performance test"
    topo = GeneratedTopo()
    #net = Mininet(topo=topo, controller=lambda c1: RemoteController( c1, ip='10.0.2.2', port=6633 ), host=CPULimitedHost, link=TCLink)
    net = Mininet(topo=topo, controller=lambda a: RemoteController( a, ip='10.0.2.2', port=6633 ), host=CPULimitedHost, link=TCLink)
    #print "Dumping host connections"
    #dumpNodeConnections(net.hosts)
    #print "Testing network connectivity"
    #net.pingAll()
    #print "Testing bandwidth between h1 and h2"
    #h1, h2 = net.getNodeByName('h1', 'h2')
    #net.iperf((h1, h2))
    return net

def connectToRootNS( network, switch, ip, prefixLen, routes ):
    """Connect hosts to root namespace via switch. Starts network.
      network: Mininet() network object
      switch: switch to connect to root namespace
      ip: IP address for root namespace node
      prefixLen: IP address prefix length (e.g. 8, 16, 24)
      routes: host networks to route to"""
    # Create a node in root namespace and link to switch 0
    root = Node( 'root', inNamespace=False )
    intf = TCLink( root, switch ).intf1
    root.setIP( ip, prefixLen, intf )
    # Start network that now includes link to root namespace
    network.start()
    # Add routes from root ns to hosts
    for route in routes:
        root.cmd( 'route add -net ' + route + ' dev ' + str( intf ) )

def sshd( network, cmd='/usr/sbin/sshd', opts='-D' ):
    "Start a network, connect it to root ns, and run sshd on all hosts."
    switch = network.switches[ 0 ]  # switch to use
    ip = '10.123.123.1'  # our IP address on host network
    #routes = [ '10.0.0.0/8' ]  # host networks to route to
    routes = [ '10.0.0.0/24' ]  # host networks to route to
    connectToRootNS( network, switch, ip, 24, routes )
    for host in network.hosts:
        host.cmd( cmd + ' ' + opts + '&' )
    print
    print "*** Hosts are running sshd at the following addresses:"
    print
    for host in network.hosts:
        print host.name, host.IP()
    print
    print "*** Type 'exit' or control-D to shut down network"
    CLI( network )
    for host in network.hosts:
        host.cmd( 'kill %' + cmd )
    network.stop()

if __name__ == '__main__':
    setLogLevel('info')
    sshd( setupNetwork() )
