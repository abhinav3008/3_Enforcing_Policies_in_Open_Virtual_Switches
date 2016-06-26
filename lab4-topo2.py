"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController   

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        h1 = self.addHost( 'h1', mac='00:00:00:00:00:01' )
        h2 = self.addHost( 'h2', mac='00:00:00:00:00:02' )
	h3 = self.addHost( 'h3', mac='00:00:00:00:00:03' )
	h4 = self.addHost( 'h4', mac='00:00:00:00:00:04' )
        s3 = self.addSwitch( 's3' )
        s2 = self.addSwitch( 's2' )
        s1 = self.addSwitch( 's1' )

        # Add links
        self.addLink(h1, s1)
        self.addLink(h3, s1)
        self.addLink(h2, s2)
        self.addLink(h4, s2)
        self.addLink(s1, s2)
        self.addLink(s1, s3)
	self.addLink(s2, s3)



topos = { 'mytopo': ( lambda: MyTopo() ) }
