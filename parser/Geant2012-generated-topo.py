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
from mininet.util import dumpNodeConnections

class GeneratedTopo( Topo ):
    "Internet Topology Zoo Specimen."

    def __init__( self, **opts ):
        "Create a topology."

        # Initialize Topology
        Topo.__init__( self, **opts )

        # add nodes, switches first...
        NL = self.addSwitch( 's0' )
        BE = self.addSwitch( 's1' )
        DK = self.addSwitch( 's2' )
        PL = self.addSwitch( 's3' )
        DE = self.addSwitch( 's4' )
        CZ = self.addSwitch( 's5' )
        LU = self.addSwitch( 's6' )
        FR = self.addSwitch( 's7' )
        CH = self.addSwitch( 's8' )
        IT = self.addSwitch( 's9' )
        UA = self.addSwitch( 's10' )
        MD = self.addSwitch( 's11' )
        BG = self.addSwitch( 's12' )
        RO = self.addSwitch( 's13' )
        TR = self.addSwitch( 's14' )
        GR = self.addSwitch( 's15' )
        CY = self.addSwitch( 's16' )
        IL = self.addSwitch( 's17' )
        MT = self.addSwitch( 's18' )
        BY = self.addSwitch( 's19' )
        MK = self.addSwitch( 's20' )
        ME = self.addSwitch( 's21' )
        HU = self.addSwitch( 's22' )
        SK = self.addSwitch( 's23' )
        PT = self.addSwitch( 's24' )
        ES = self.addSwitch( 's25' )
        RS = self.addSwitch( 's26' )
        HR = self.addSwitch( 's27' )
        SL = self.addSwitch( 's28' )
        AT = self.addSwitch( 's29' )
        LT = self.addSwitch( 's30' )
        RU = self.addSwitch( 's31' )
        IS = self.addSwitch( 's32' )
        IE = self.addSwitch( 's33' )
        UK = self.addSwitch( 's34' )
        NO = self.addSwitch( 's35' )
        SE = self.addSwitch( 's36' )
        FI = self.addSwitch( 's37' )
        EE = self.addSwitch( 's38' )
        LV = self.addSwitch( 's39' )

        # ... and now hosts
        NL_host = self.addHost( 'h0' )
        BE_host = self.addHost( 'h1' )
        DK_host = self.addHost( 'h2' )
        PL_host = self.addHost( 'h3' )
        DE_host = self.addHost( 'h4' )
        CZ_host = self.addHost( 'h5' )
        LU_host = self.addHost( 'h6' )
        FR_host = self.addHost( 'h7' )
        CH_host = self.addHost( 'h8' )
        IT_host = self.addHost( 'h9' )
        UA_host = self.addHost( 'h10' )
        MD_host = self.addHost( 'h11' )
        BG_host = self.addHost( 'h12' )
        RO_host = self.addHost( 'h13' )
        TR_host = self.addHost( 'h14' )
        GR_host = self.addHost( 'h15' )
        CY_host = self.addHost( 'h16' )
        IL_host = self.addHost( 'h17' )
        MT_host = self.addHost( 'h18' )
        BY_host = self.addHost( 'h19' )
        MK_host = self.addHost( 'h20' )
        ME_host = self.addHost( 'h21' )
        HU_host = self.addHost( 'h22' )
        SK_host = self.addHost( 'h23' )
        PT_host = self.addHost( 'h24' )
        ES_host = self.addHost( 'h25' )
        RS_host = self.addHost( 'h26' )
        HR_host = self.addHost( 'h27' )
        SL_host = self.addHost( 'h28' )
        AT_host = self.addHost( 'h29' )
        LT_host = self.addHost( 'h30' )
        RU_host = self.addHost( 'h31' )
        IS_host = self.addHost( 'h32' )
        IE_host = self.addHost( 'h33' )
        UK_host = self.addHost( 'h34' )
        NO_host = self.addHost( 'h35' )
        SE_host = self.addHost( 'h36' )
        FI_host = self.addHost( 'h37' )
        EE_host = self.addHost( 'h38' )
        LV_host = self.addHost( 'h39' )

        # add edges between switch and corresponding host
        self.addLink( NL , NL_host )
        self.addLink( BE , BE_host )
        self.addLink( DK , DK_host )
        self.addLink( PL , PL_host )
        self.addLink( DE , DE_host )
        self.addLink( CZ , CZ_host )
        self.addLink( LU , LU_host )
        self.addLink( FR , FR_host )
        self.addLink( CH , CH_host )
        self.addLink( IT , IT_host )
        self.addLink( UA , UA_host )
        self.addLink( MD , MD_host )
        self.addLink( BG , BG_host )
        self.addLink( RO , RO_host )
        self.addLink( TR , TR_host )
        self.addLink( GR , GR_host )
        self.addLink( CY , CY_host )
        self.addLink( IL , IL_host )
        self.addLink( MT , MT_host )
        self.addLink( BY , BY_host )
        self.addLink( MK , MK_host )
        self.addLink( ME , ME_host )
        self.addLink( HU , HU_host )
        self.addLink( SK , SK_host )
        self.addLink( PT , PT_host )
        self.addLink( ES , ES_host )
        self.addLink( RS , RS_host )
        self.addLink( HR , HR_host )
        self.addLink( SL , SL_host )
        self.addLink( AT , AT_host )
        self.addLink( LT , LT_host )
        self.addLink( RU , RU_host )
        self.addLink( IS , IS_host )
        self.addLink( IE , IE_host )
        self.addLink( UK , UK_host )
        self.addLink( NO , NO_host )
        self.addLink( SE , SE_host )
        self.addLink( FI , FI_host )
        self.addLink( EE , EE_host )
        self.addLink( LV , LV_host )

        # add edges between switches
        self.addLink( NL , BE, bw=10, delay='0.826375597084ms')
        self.addLink( NL , DK, bw=10, delay='1.33881763027ms')
        self.addLink( NL , DE, bw=10, delay='0.730024007865ms')
        self.addLink( NL , UK, bw=10, delay='0.396342917022ms')
        self.addLink( NL , LT, bw=10, delay='1.42786188323ms')
        self.addLink( BE , IE, bw=10, delay='0.689695636944ms')
        self.addLink( DK , IS, bw=10, delay='1.53067362474ms')
        self.addLink( DK , NO, bw=10, delay='0.771959520999ms')
        self.addLink( DK , DE, bw=10, delay='1.09302339436ms')
        self.addLink( DK , EE, bw=10, delay='1.3844019532ms')
        self.addLink( DK , SE, bw=10, delay='1.32151737845ms')
        self.addLink( DK , RU, bw=10, delay='0.0532948946864ms')
        self.addLink( PL , UA, bw=10, delay='0.335138620425ms')
        self.addLink( PL , BY, bw=10, delay='1.54000727166ms')
        self.addLink( PL , DE, bw=10, delay='0.83001190537ms')
        self.addLink( PL , CZ, bw=10, delay='0.71593289141ms')
        self.addLink( PL , LT, bw=10, delay='1.41137816688ms')
        self.addLink( DE , CZ, bw=10, delay='0.304613779335ms')
        self.addLink( DE , LU, bw=10, delay='1.22544550898ms')
        self.addLink( DE , CH, bw=10, delay='1.08723965413ms')
        self.addLink( DE , CY, bw=10, delay='1.28426625864ms')
        self.addLink( DE , IL, bw=10, delay='0.542429302293ms')
        self.addLink( DE , AT, bw=10, delay='0.85647793909ms')
        self.addLink( DE , RU, bw=10, delay='1.14581614036ms')
        self.addLink( CZ , SK, bw=10, delay='0.516764984797ms')
        self.addLink( LU , FR, bw=10, delay='0.591802591418ms')
        self.addLink( FR , CH, bw=10, delay='1.01952467188ms')
        self.addLink( FR , ES, bw=10, delay='1.21440856492ms')
        self.addLink( FR , UK, bw=10, delay='1.64821293722ms')
        self.addLink( CH , IT, bw=10, delay='0.780117284874ms')
        self.addLink( CH , ES, bw=10, delay='0.768056898874ms')
        self.addLink( IT , ES, bw=10, delay='0.695555126478ms')
        self.addLink( IT , MT, bw=10, delay='1.66749261576ms')
        self.addLink( IT , AT, bw=10, delay='1.52881686645ms')
        self.addLink( IT , GR, bw=10, delay='0.748787465971ms')
        self.addLink( MD , RO, bw=10, delay='0.652041478471ms')
        self.addLink( BG , TR, bw=10, delay='1.52715774179ms')
        self.addLink( BG , MK, bw=10, delay='0.234962097042ms')
        self.addLink( BG , RO, bw=10, delay='1.2912273047ms')
        self.addLink( BG , HU, bw=10, delay='0.617741544344ms')
        self.addLink( BG , GR, bw=10, delay='0.896035926899ms')
        self.addLink( RO , HU, bw=10, delay='1.36936004632ms')
        self.addLink( RO , TR, bw=10, delay='0.732064268229ms')
        self.addLink( GR , AT, bw=10, delay='1.16011323012ms')
        self.addLink( CY , UK, bw=10, delay='1.12870494627ms')
        self.addLink( IL , LT, bw=10, delay='0.928605204774ms')
        self.addLink( ME , HR, bw=10, delay='1.6109756694ms')
        self.addLink( HU , RS, bw=10, delay='1.09545760062ms')
        self.addLink( HU , HR, bw=10, delay='1.24616554301ms')
        self.addLink( HU , SK, bw=10, delay='0.807830696587ms')
        self.addLink( SK , AT, bw=10, delay='0.203998129737ms')
        self.addLink( PT , ES, bw=10, delay='0.867823186843ms')
        self.addLink( PT , UK, bw=10, delay='0.48711044856ms')
        self.addLink( HR , SL, bw=10, delay='0.301744591339ms')
        self.addLink( SL , AT, bw=10, delay='1.45311154254ms')
        self.addLink( LT , LV, bw=10, delay='1.15517813928ms')
        self.addLink( IS , UK, bw=10, delay='0.334073726607ms')
        self.addLink( IE , UK, bw=10, delay='1.03528464437ms')
        self.addLink( NO , SE, bw=10, delay='0.959408230968ms')
        self.addLink( SE , FI, bw=10, delay='1.23153497486ms')
        self.addLink( EE , LV, bw=10, delay='1.2618715879ms')

topos = { 'generated': ( lambda: GeneratedTopo() ) }

# HERE THE CODE DEFINITION OF THE TOPOLOGY ENDS

# the following code produces an executable script working with a remote controller
# and providing ssh access to the the mininet hosts from within the ubuntu vm
controller_ip = ''

def setupNetwork(controller_ip):
    "Create network and run simple performance test"
    # check if remote controller's ip was set
    # else set it to localhost
    topo = GeneratedTopo()
    if controller_ip == '':
        #controller_ip = '10.0.2.2';
        controller_ip = '127.0.0.1';
    net = Mininet(topo=topo, controller=lambda a: RemoteController( a, ip=controller_ip, port=6633 ), host=CPULimitedHost, link=TCLink)
    return net

def connectToRootNS( network, switch, ip, prefixLen, routes ):
    "Connect hosts to root namespace via switch. Starts network."
    "network: Mininet() network object"
    "switch: switch to connect to root namespace"
    "ip: IP address for root namespace node"
    "prefixLen: IP address prefix length (e.g. 8, 16, 24)"
    "routes: host networks to route to"
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
    routes = [ '10.0.0.0/8' ]  # host networks to route to
    connectToRootNS( network, switch, ip, 8, routes )
    for host in network.hosts:
        host.cmd( cmd + ' ' + opts + '&' )

    # DEBUGGING INFO
    print
    print "Dumping host connections"
    dumpNodeConnections(network.hosts)
    print
    print "*** Hosts are running sshd at the following addresses:"
    print
    for host in network.hosts:
        print host.name, host.IP()
    print
    print "*** Type 'exit' or control-D to shut down network"
    print
    print "*** For testing network connectivity among the hosts, wait a bit for the controller to create all the routes, then do 'pingall' on the mininet console."
    print

    CLI( network )
    for host in network.hosts:
        host.cmd( 'kill %' + cmd )
    network.stop()


if __name__ == '__main__':
    setLogLevel('info')
    #setLogLevel('debug')
    sshd( setupNetwork(controller_ip) )
