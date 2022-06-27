#!/usr/bin/env python3

#GraphML-Topo-to-Mininet-Network-Generator
#
# This file parses Network Topologies in GraphML format from the Internet Topology Zoo.
# A python file for creating Mininet Topologies will be created as Output.
# Files have to be in the same directory.
#
# Arguments:
#   -f              [filename of GraphML input file]
#   --file          [filename of GraphML input file]
#   -o              [filename of GraphML output file]
#   --output        [filename of GraphML output file]
#   -b              [number as integer for bandwidth in mbit]
#   --bw            [number as integer for bandwidth in mbit]
#   --bandwidth     [number as integer for bandwidth in mbit]
#   -c              [controller ip as string]
#   --controller    [controller ip as string]
#
# Without any input, program will terminate.
# Without specified output, outputfile will have the same name as the input file.
# This means, the argument for the outputfile can be omitted.
# Parameters for bandwith and controller ip have default values, if they are omitted, too.
#
#
# sjas
# Wed Jul 17 02:59:06 PDT 2013
#
#
# TODO's:
#   -   fix double name error of some topologies
#   -   fix topoparsing (choose by name, not element <d..>)
#           =    topos with duplicate labels
# UPDATE:
#   -   implemented argparse for script parameters @YM:06/27/2022
#   -   update the generated code for python3 mininet libraries @YM:06/27/2022
#################################################################################



import xml.etree.ElementTree as ET
import sys
import math
import re
import argparse
from sys import argv

input_file_name = ''
output_file_name = ''
bandwidth_argument = ''
controller_ip = ''

# first check commandline arguments


parser = argparse.ArgumentParser(description='Parser of .graphml file, generates a mininet network topology')
parser.add_argument('-f', '--file', type=str, help='filename of GraphML input file')
parser.add_argument('-o', '--output', type=str, help='filename of mininet topology *.py file')
parser.add_argument('-b', '-bw', '--bandwidth', type=str, help='numebr as integer for bandwidth in mbit')
parser.add_argument('-c', '--controller', type=str, help='controller ip as string')

args = parser.parse_args()

if args.file is not None:
    input_file_name = args.file
else:
    input_file_name = ''
# terminate when inputfile is missing
if input_file_name == '':
    sys.exit('No input file was specified as argument....EXITED!')

if args.output is not None:
    output_file_name = args.output
if args.bandwidth is not None:
    bandwidth_argument = args.bandwidth
if args.controller is not None:
    controller_ip = args.controller

# define string fragments for output later on
outputstring_1 = '''#!/usr/bin/python

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
'''

outputstring_2a='''
        # add nodes, switches first...
'''
outputstring_2b='''
        # ... and now hosts
'''

outputstring_3a='''
        # add edges between switch and corresponding host
'''

outputstring_3b='''
        # add edges between switches
'''

outputstring_4a='''
topos = { 'generated': ( lambda: GeneratedTopo() ) }

# HERE THE CODE DEFINITION OF THE TOPOLOGY ENDS

# the following code produces an executable script working with a remote controller
# and providing ssh access to the the mininet hosts from within the ubuntu vm
'''

outputstring_4b = '''
def setupNetwork(controller_ip):
    "Create network and run simple performance test"
    # check if remote controller's ip was set
    # else set it to localhost
    topo = GeneratedTopo()
    if controller_ip == '':
        #controller_ip = '10.0.2.2';
        controller_ip = '127.0.0.1'
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
    print()
    print("Dumping host connections")
    print()
    dumpNodeConnections(network.hosts)
    print()
    print("*** Hosts are running sshd at the following addresses:")
    print()
    for host in network.hosts:
        print(host.name, host.IP())
    print()
    print("*** Type 'exit' or control-D to shut down network")
    print()
    print()
    print("*** For testing network connectivity among the hosts, wait a bit for the controller to create all the routes, then do 'pingall' on the mininet console.")
    print()

    CLI( network )
    for host in network.hosts:
        host.cmd( 'kill %' + cmd )
    network.stop()


if __name__ == '__main__':
    setLogLevel('info')
    #setLogLevel('debug')
    sshd( setupNetwork(controller_ip) )
'''

#WHERE TO PUT RESULTS
outputstring_to_be_exported = ''
outputstring_to_be_exported += outputstring_1

#READ FILE AND DO ALL THE ACTUAL PARSING IN THE NEXT PARTS
xml_tree    = ET.parse(input_file_name)
namespace   = "{http://graphml.graphdrawing.org/xmlns}"
ns          = namespace # just doing shortcutting, namespace is needed often.

#GET ALL ELEMENTS THAT ARE PARENTS OF ELEMENTS NEEDED LATER ON
root_element    = xml_tree.getroot()
graph_element   = root_element.find(ns + 'graph')

# GET ALL ELEMENT SETS NEEDED LATER ON
index_values_set    = root_element.findall(ns + 'key')
node_set            = graph_element.findall(ns + 'node')
edge_set            = graph_element.findall(ns + 'edge')

# SET SOME VARIABLES TO SAVE FOUND DATA FIRST
# memomorize the values' ids to search for in current topology
node_label_name_in_graphml = ''
node_latitude_name_in_graphml = ''
node_longitude_name_in_graphml = ''
# for saving the current values
node_index_value     = ''
node_name_value      = ''
node_longitude_value = ''
node_latitude_value  = ''
# id:value dictionaries
id_node_name_dict   = {}     # to hold all 'id: node_name_value' pairs
id_longitude_dict   = {}     # to hold all 'id: node_longitude_value' pairs
id_latitude_dict    = {}     # to hold all 'id: node_latitude_value' pairs

# FIND OUT WHAT KEYS ARE TO BE USED, SINCE THIS DIFFERS IN DIFFERENT GRAPHML TOPOLOGIES
for i in index_values_set:

    if i.attrib['attr.name'] == 'label' and i.attrib['for'] == 'node':
        node_label_name_in_graphml = i.attrib['id']
    if i.attrib['attr.name'] == 'Longitude':
        node_longitude_name_in_graphml = i.attrib['id']
    if i.attrib['attr.name'] == 'Latitude':
        node_latitude_name_in_graphml = i.attrib['id']

# NOW PARSE ELEMENT SETS TO GET THE DATA FOR THE TOPO
# GET NODE_NAME DATA
# GET LONGITUDE DATK
# GET LATITUDE DATA
for n in node_set:

    node_index_value = n.attrib['id']

    #get all data elements residing under all node elements
    data_set = n.findall(ns + 'data')

    #finally get all needed values
    for d in data_set:

        #node name
        if d.attrib['key'] == node_label_name_in_graphml:
            #strip all whitespace from names so they can be used as id's
            node_name_value = re.sub(r'\s+', '', d.text)
        #longitude data
        if d.attrib['key'] == node_longitude_name_in_graphml:
            node_longitude_value = d.text
        #latitude data
        if d.attrib['key'] == node_latitude_name_in_graphml:
            node_latitude_value = d.text

        #save id:data couple
        id_node_name_dict[node_index_value] = node_name_value
        id_longitude_dict[node_index_value] = node_longitude_value
        id_latitude_dict[node_index_value]  = node_latitude_value


# STRING CREATION
# FIRST CREATE THE SWITCHES AND HOSTS
tempstring1 = ''
tempstring2 = ''
tempstring3 = ''

for i in range(0, len(id_node_name_dict)):

    #create switch
    temp1 =  '        '
    temp1 += id_node_name_dict[str(i)]
    temp1 += " = self.addSwitch( 's"
    temp1 += str(i)
    temp1 += "' )\n"

    #create corresponding host
    temp2 =  '        '
    temp2 += id_node_name_dict[str(i)]
    temp2 += "_host = self.addHost( 'h"
    temp2 += str(i)
    temp2 += "' )\n"
    tempstring1 += temp1
    tempstring2 += temp2

    # link each switch and its host...
    temp3 =  '        self.addLink( '
    temp3 += id_node_name_dict[str(i)]
    temp3 += ' , '
    temp3 += id_node_name_dict[str(i)]
    temp3 += "_host )"
    temp3 += '\n'
    tempstring3 += temp3

outputstring_to_be_exported += outputstring_2a
outputstring_to_be_exported += tempstring1
outputstring_to_be_exported += outputstring_2b
outputstring_to_be_exported += tempstring2
outputstring_to_be_exported += outputstring_3a
outputstring_to_be_exported += tempstring3
outputstring_to_be_exported += outputstring_3b


# SECOND CALCULATE DISTANCES BETWEEN SWITCHES,
#   set global bandwidth and create the edges between switches,
#   and link each single host to its corresponding switch

tempstring4 = ''
tempstring5 = ''
distance = 0.0
latency = 0.0

for e in edge_set:

    # GET IDS FOR EASIER HANDLING
    src_id = e.attrib['source']
    dst_id = e.attrib['target']

    # CALCULATE DELAYS

    #    CALCULATION EXPLANATION
    #
    #    formula: (for distance)
    #    dist(SP,EP) = arccos{ sin(La[EP]) * sin(La[SP]) + cos(La[EP]) * cos(La[SP]) * cos(Lo[EP] - Lo[SP])} * r
    #    r = 6378.137 km
    #
    #    formula: (speed of light, not within a vacuumed box)
    #     v = 1.97 * 10**8 m/s
    #
    #    formula: (latency being calculated from distance and light speed)
    #    t = distance / speed of light
    #    t (in ms) = ( distance in km * 1000 (for meters) ) / ( speed of light / 1000 (for ms))

    #    ACTUAL CALCULATION: implementing this was no fun.

    first_product               = math.sin(float(id_latitude_dict[dst_id])) * math.sin(float(id_latitude_dict[src_id]))
    second_product_first_part   = math.cos(float(id_latitude_dict[dst_id])) * math.cos(float(id_latitude_dict[src_id]))
    second_product_second_part  = math.cos((float(id_longitude_dict[dst_id])) - (float(id_longitude_dict[src_id])))

    distance = math.radians(math.acos(first_product + (second_product_first_part * second_product_second_part))) * 6378.137

    # t (in ms) = ( distance in km * 1000 (for meters) ) / ( speed of light / 1000 (for ms))
    # t         = ( distance       * 1000              ) / ( 1.97 * 10**8   / 1000         )
    latency = ( distance * 1000 ) / ( 197000 )

    # BANDWIDTH LIMITING
    #set bw to 10mbit if nothing was specified otherwise on startup
    if bandwidth_argument == '':
        bandwidth_argument = '10';

    # ... and link all corresponding switches with each other
    temp4 =  '        self.addLink( '
    temp4 += id_node_name_dict[src_id]
    temp4 += ' , '
    temp4 += id_node_name_dict[dst_id]
    temp4 += ", bw="
    temp4 += bandwidth_argument
    temp4 += ", delay='"
    temp4 += str(latency)
    temp4 += "ms')"
    temp4 += '\n'
    # next line so i dont have to look up other possible settings
    #temp += "ms', loss=0, max_queue_size=1000, use_htb=True)"
    tempstring4 += temp4

outputstring_to_be_exported += tempstring4
outputstring_to_be_exported += outputstring_4a

# this is kind of dirty, due to having to use mixed '' ""
temp5  = "controller_ip = '"
temp5 += controller_ip
temp5 += "'\n"
tempstring5 += temp5

outputstring_to_be_exported += tempstring5
outputstring_to_be_exported += outputstring_4b


# GENERATION FINISHED, WRITE STRING TO FILE
outputfile = ''
if output_file_name == '':
    output_file_name = input_file_name + '-generated-Mininet-Topo.py'

outputfile = open(output_file_name, 'w')
outputfile.write(outputstring_to_be_exported)
outputfile.close()

print("Topology generation SUCCESSFUL!")
