#    Copyright 2015 Rackspace
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
from octavia_lib.common import constants as lib_constants
from openstack.network.v2.floating_ip import FloatingIP
from openstack.network.v2.network import Network
from openstack.network.v2.network_ip_availability import NetworkIPAvailability
from openstack.network.v2.port import Port
from openstack.network.v2.security_group import SecurityGroup
from openstack.network.v2.subnet import Subnet

from octavia.common import constants


class MockNovaInterface:
    net_id = None
    port_id = None
    fixed_ips = []


MOCK_NETWORK_ID = 'mock-network-1'
MOCK_NETWORK_ID2 = 'mock-network-2'
MOCK_NETWORK_NAME = 'TestNet1'
MOCK_SUBNET_ID = 'mock-subnet-1'
MOCK_SUBNET_ID2 = 'mock-subnet-2'
MOCK_SUBNET_ID3 = 'mock-subnet-3'
MOCK_SUBNET_NAME = 'TestSubnet1'
MOCK_PORT_ID = 'mock-port-1'
MOCK_PORT_ID2 = 'mock-port-2'
MOCK_PORT_NAME = 'TestPort1'
MOCK_PORT_NAME2 = 'TestPort2'
MOCK_COMPUTE_ID = 'mock-compute-1'
MOCK_IP_ADDRESS = '10.0.0.1'
MOCK_IP_ADDRESS2 = '10.0.0.2'
MOCK_GATEWAY_IP = '10.0.0.3'
MOCK_IP_VERSION = 4
MOCK_CIDR = '10.0.0.0/24'
MOCK_MAC_ADDR = 'fe:16:3e:00:95:5c'
MOCK_MAC_ADDR2 = 'fe:16:3e:00:95:5d'
MOCK_PROJECT_ID = 'mock-project-1'
MOCK_HOST_ROUTES = []
MOCK_SUBNET = Subnet(**{'id': MOCK_SUBNET_ID,
                        'network_id': MOCK_NETWORK_ID,
                        'name': MOCK_SUBNET_NAME,
                        'tenant_id': MOCK_PROJECT_ID,
                        'gateway_ip': MOCK_GATEWAY_IP,
                        'cidr': MOCK_CIDR,
                        'ip_version': MOCK_IP_VERSION,
                        'host_routes': MOCK_HOST_ROUTES})
MOCK_SUBNET2 = Subnet(**{'id': MOCK_SUBNET_ID2,
                         'network_id': MOCK_NETWORK_ID2})
MOCK_HOST_ROUTES = []

MOCK_NOVA_INTERFACE = MockNovaInterface()
MOCK_NOVA_INTERFACE.net_id = MOCK_NETWORK_ID
MOCK_NOVA_INTERFACE.port_id = MOCK_PORT_ID
MOCK_NOVA_INTERFACE.fixed_ips = [{'ip_address': MOCK_IP_ADDRESS}]
MOCK_NOVA_INTERFACE2 = MockNovaInterface()
MOCK_NOVA_INTERFACE2.net_id = MOCK_NETWORK_ID2
MOCK_NOVA_INTERFACE2.port_id = MOCK_PORT_ID2
MOCK_NOVA_INTERFACE2.fixed_ips = [{'ip_address': MOCK_IP_ADDRESS2}]
MOCK_DEVICE_OWNER = 'Moctavia'
MOCK_DEVICE_ID = 'Moctavia123'
MOCK_DEVICE_ID2 = 'Moctavia124'
MOCK_SECURITY_GROUP_ID = 'security-group-1'
MOCK_SECURITY_GROUP_NAME = 'SecurityGroup1'

MOCK_SECURITY_GROUP = SecurityGroup(**{
    "id": MOCK_SECURITY_GROUP_ID,
    "name": MOCK_SECURITY_GROUP_NAME,
    "tenant_id": MOCK_PROJECT_ID,
    "description": "",
    "security_group_rules": [{
        "id": "85f1c72b-cdd4-484f-a9c8-b3205f4e6f53",
        "tenant_id": MOCK_PROJECT_ID,
        "security_group_id": MOCK_SECURITY_GROUP_ID,
        "ethertype": "IPv4",
        "direction": "ingress",
        "protocol": "tcp",
        "port_range_min": 80,
        "port_range_max": 80,
        "remote_ip_prefix": None,
        "remote_group_id": None,
        "description": "",
        "tags": [],
        "created_at": "2020-03-12T20:44:48Z",
        "updated_at": "2020-03-12T20:44:48Z",
        "revision_number": 0,
        "project_id": MOCK_PROJECT_ID
    }, {
        "id": "aa16ae5f-eac2-40b5-994b-5169a06228a4",
        "tenant_id": MOCK_PROJECT_ID,
        "security_group_id": "6530d536-3083-4d5c-a4a9-272ac7b8f3de",
        "ethertype": "IPv4",
        "direction": "egress",
        "protocol": None,
        "port_range_min": None,
        "port_range_max": None,
        "remote_ip_prefix": None,
        "remote_group_id": None,
        "description": None,
        "tags": [],
        "created_at": "2020-03-12T20:43:31Z",
        "updated_at": "2020-03-12T20:43:31Z",
        "revision_number": 0,
        "project_id": MOCK_PROJECT_ID,
    }],
    "tags": [],
    "created_at": "2020-03-12T20:43:31Z",
    "updated_at": "2020-03-12T20:44:48Z",
    "revision_number": 3,
    "project_id": MOCK_PROJECT_ID})

MOCK_ADMIN_STATE_UP = True
MOCK_STATUS = 'ACTIVE'
MOCK_MTU = 1500
MOCK_NETWORK_TYPE = 'flat'
MOCK_SEGMENTATION_ID = 1
MOCK_ROUTER_EXTERNAL = False

MOCK_NEUTRON_PORT = Port(**{'network_id': MOCK_NETWORK_ID,
                            'device_id': MOCK_DEVICE_ID,
                            'device_owner': MOCK_DEVICE_OWNER,
                            'id': MOCK_PORT_ID,
                            'name': MOCK_PORT_NAME,
                            'tenant_id': MOCK_PROJECT_ID,
                            'admin_state_up': MOCK_ADMIN_STATE_UP,
                            'status': MOCK_STATUS,
                            'mac_address': MOCK_MAC_ADDR,
                            'fixed_ips': [{'ip_address': MOCK_IP_ADDRESS,
                                           'subnet_id': MOCK_SUBNET_ID}],
                            'security_groups': [MOCK_SECURITY_GROUP_ID],
                            'binding_vnic_type': constants.VNIC_TYPE_NORMAL})
MOCK_NEUTRON_QOS_POLICY_ID = 'mock-qos-id'
MOCK_QOS_POLICY_ID1 = 'qos1-id'
MOCK_QOS_POLICY_ID2 = 'qos2-id'

MOCK_NEUTRON_PORT2 = Port(**{'network_id': MOCK_NETWORK_ID2,
                             'device_id': MOCK_DEVICE_ID2,
                             'device_owner': MOCK_DEVICE_OWNER,
                             'id': MOCK_PORT_ID2,
                             'name': MOCK_PORT_NAME2,
                             'tenant_id': MOCK_PROJECT_ID,
                             'admin_state_up': MOCK_ADMIN_STATE_UP,
                             'status': MOCK_STATUS,
                             'mac_address': MOCK_MAC_ADDR2,
                             'fixed_ips': [{'ip_address': MOCK_IP_ADDRESS2,
                                            'subnet_id': MOCK_SUBNET_ID2}]})

MOCK_NETWORK = Network(**{'id': MOCK_NETWORK_ID,
                          'name': MOCK_NETWORK_NAME,
                          'project_id': MOCK_PROJECT_ID,
                          'admin_state_up': MOCK_ADMIN_STATE_UP,
                          'subnet_ids': [MOCK_SUBNET_ID],
                          'mtu': MOCK_MTU,
                          'provider_network_type': 'flat',
                          'provider_physical_network': MOCK_NETWORK_NAME,
                          'provider_segmentation_id': MOCK_SEGMENTATION_ID,
                          'router_external': MOCK_ROUTER_EXTERNAL,
                          'port_security_enabled': False})
MOCK_FIXED_IP = {'subnet_id': MOCK_SUBNET_ID,
                 'ip_address': MOCK_IP_ADDRESS}
MOCK_FLOATING_IP_ID = 'floating-ip-1'
MOCK_FLOATING_IP_DESC = 'TestFloatingIP1'
MOCK_ROUTER_ID = 'mock-router-1'
MOCK_FLOATING_IP = FloatingIP(**{'id': MOCK_FLOATING_IP_ID,
                                 'description': MOCK_FLOATING_IP_DESC,
                                 'tenant_id': MOCK_PROJECT_ID,
                                 'status': MOCK_STATUS,
                                 'port_id': MOCK_PORT_ID,
                                 'router_id': MOCK_ROUTER_ID,
                                 'floating_network_id': MOCK_NETWORK_ID,
                                 'floating_ip_address': MOCK_IP_ADDRESS,
                                 'fixed_ip_address': MOCK_IP_ADDRESS2,
                                 'fixed_port_id': MOCK_PORT_ID2})

MOCK_AMP_ID1 = 'amp1-id'
MOCK_AMP_ID2 = 'amp2-id'
MOCK_AMP_ID3 = 'amp3-id'
MOCK_AMP_COMPUTE_ID1 = 'amp1-compute-id'
MOCK_AMP_COMPUTE_ID2 = 'amp2-compute-id'
MOCK_AMP_COMPUTE_ID3 = 'amp3-compute-id'

MOCK_MANAGEMENT_SUBNET_ID = 'mgmt-subnet-1'
MOCK_MANAGEMENT_NET_ID = 'mgmt-net-1'
MOCK_MANAGEMENT_PORT_ID1 = 'mgmt-port-1'
MOCK_MANAGEMENT_PORT_ID2 = 'mgmt-port-2'
# These IPs become lb_network_ip
MOCK_MANAGEMENT_IP1 = '99.99.99.1'
MOCK_MANAGEMENT_IP2 = '99.99.99.2'

MOCK_MANAGEMENT_FIXED_IPS1 = [{'ip_address': MOCK_MANAGEMENT_IP1,
                               'subnet_id': MOCK_MANAGEMENT_SUBNET_ID}]
MOCK_MANAGEMENT_FIXED_IPS2 = [{'ip_address': MOCK_MANAGEMENT_IP2,
                               'subnet_id': MOCK_MANAGEMENT_SUBNET_ID}]

MOCK_MANAGEMENT_INTERFACE1 = MockNovaInterface()
MOCK_MANAGEMENT_INTERFACE1.net_id = MOCK_MANAGEMENT_NET_ID
MOCK_MANAGEMENT_INTERFACE1.port_id = MOCK_MANAGEMENT_PORT_ID1
MOCK_MANAGEMENT_INTERFACE1.fixed_ips = MOCK_MANAGEMENT_FIXED_IPS1
MOCK_MANAGEMENT_INTERFACE2 = MockNovaInterface()
MOCK_MANAGEMENT_INTERFACE2.net_id = MOCK_MANAGEMENT_NET_ID
MOCK_MANAGEMENT_INTERFACE2.port_id = MOCK_MANAGEMENT_PORT_ID2
MOCK_MANAGEMENT_INTERFACE2.fixed_ips = MOCK_MANAGEMENT_FIXED_IPS2

MOCK_MANAGEMENT_PORT1 = Port(**{'network_id': MOCK_MANAGEMENT_NET_ID,
                                'device_id': MOCK_AMP_COMPUTE_ID1,
                                'device_owner': MOCK_DEVICE_OWNER,
                                'id': MOCK_MANAGEMENT_PORT_ID1,
                                'fixed_ips': MOCK_MANAGEMENT_FIXED_IPS1})

MOCK_MANAGEMENT_PORT2 = Port(**{'network_id': MOCK_MANAGEMENT_NET_ID,
                                'device_id': MOCK_AMP_COMPUTE_ID2,
                                'device_owner': MOCK_DEVICE_OWNER,
                                'id': MOCK_MANAGEMENT_PORT_ID2,
                                'fixed_ips': MOCK_MANAGEMENT_FIXED_IPS2})

MOCK_VIP_SUBNET_ID = 'vip-subnet-1'
MOCK_VIP_SUBNET_ID2 = 'vip-subnet-2'
MOCK_VIP_NET_ID = 'vip-net-1'
MOCK_VRRP_PORT_ID1 = 'vrrp-port-1'
MOCK_VRRP_PORT_ID2 = 'vrrp-port-2'
MOCK_VRRP_PORT_ID3 = 'vrrp-port-3'
# These IPs become vrrp_ip
MOCK_VRRP_IP1 = '55.55.55.1'
MOCK_VRRP_IP2 = '55.55.55.2'
MOCK_VRRP_IP3 = '55.55.55.3'

MOCK_VRRP_FIXED_IPS1 = [{'ip_address': MOCK_VRRP_IP1,
                         'subnet_id': MOCK_VIP_SUBNET_ID}]
MOCK_VRRP_FIXED_IPS2 = [{'ip_address': MOCK_VRRP_IP2,
                         'subnet_id': MOCK_VIP_SUBNET_ID}]

MOCK_VRRP_INTERFACE1 = MockNovaInterface()
MOCK_VRRP_INTERFACE1.net_id = MOCK_VIP_NET_ID
MOCK_VRRP_INTERFACE1.port_id = MOCK_VRRP_PORT_ID1
MOCK_VRRP_INTERFACE1.fixed_ips = MOCK_VRRP_FIXED_IPS1
MOCK_VRRP_INTERFACE2 = MockNovaInterface()
MOCK_VRRP_INTERFACE2.net_id = MOCK_VIP_NET_ID
MOCK_VRRP_INTERFACE2.port_id = MOCK_VRRP_PORT_ID2
MOCK_VRRP_INTERFACE2.fixed_ips = MOCK_VRRP_FIXED_IPS2

MOCK_VRRP_PORT1 = Port(**{'network_id': MOCK_VIP_NET_ID,
                          'device_id': MOCK_AMP_COMPUTE_ID1,
                          'device_owner': MOCK_DEVICE_OWNER,
                          'id': MOCK_VRRP_PORT_ID1,
                          'fixed_ips': MOCK_VRRP_FIXED_IPS1})

MOCK_VRRP_PORT2 = Port(**{'network_id': MOCK_VIP_NET_ID,
                          'device_id': MOCK_AMP_COMPUTE_ID2,
                          'device_owner': MOCK_DEVICE_OWNER,
                          'id': MOCK_VRRP_PORT_ID2,
                          'fixed_ips': MOCK_VRRP_FIXED_IPS2})

MOCK_NETWORK_TOTAL_IPS = 254
MOCK_NETWORK_USED_IPS = 0
MOCK_SUBNET_TOTAL_IPS = 254
MOCK_SUBNET_USED_IPS = 0
MOCK_SUBNET_IP_AVAILABILITY = [{'used_ips': MOCK_SUBNET_USED_IPS,
                                'subnet_id': MOCK_SUBNET_ID,
                                'total_ips': MOCK_SUBNET_TOTAL_IPS}]

MOCK_NETWORK_IP_AVAILABILITY = NetworkIPAvailability(
    **{'network_id': MOCK_NETWORK_ID,
       'tenant_id': MOCK_PROJECT_ID,
       'network_name': MOCK_NETWORK_NAME,
       'total_ips': MOCK_NETWORK_TOTAL_IPS,
       'used_ips': MOCK_NETWORK_USED_IPS,
       'subnet_ip_availability': MOCK_SUBNET_IP_AVAILABILITY})

INVALID_LISTENER_POOL_PROTOCOL_MAP = {
    constants.PROTOCOL_HTTP: [constants.PROTOCOL_HTTPS,
                              constants.PROTOCOL_TCP,
                              constants.PROTOCOL_TERMINATED_HTTPS,
                              constants.PROTOCOL_UDP],
    constants.PROTOCOL_HTTPS: [constants.PROTOCOL_HTTP,
                               constants.PROTOCOL_TERMINATED_HTTPS,
                               constants.PROTOCOL_UDP],
    constants.PROTOCOL_TCP: [constants.PROTOCOL_TERMINATED_HTTPS,
                             constants.PROTOCOL_UDP],
    constants.PROTOCOL_TERMINATED_HTTPS: [constants.PROTOCOL_HTTPS,
                                          constants.PROTOCOL_TCP,
                                          constants.PROTOCOL_UDP],
    constants.PROTOCOL_UDP: [constants.PROTOCOL_TCP,
                             constants.PROTOCOL_HTTP,
                             constants.PROTOCOL_HTTPS,
                             constants.PROTOCOL_TERMINATED_HTTPS,
                             constants.PROTOCOL_PROXY,
                             lib_constants.PROTOCOL_PROXYV2]}
