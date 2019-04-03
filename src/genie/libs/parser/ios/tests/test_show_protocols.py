# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

from genie.libs.parser.ios.show_protocols import ShowIpProtocols, \
                                                 ShowIpProtocolsSectionRip

from genie.libs.parser.iosxe.tests.test_show_protocols import test_show_ip_protocols as \
                                                              test_show_ip_protocols_iosxe, \
                                                              test_show_ip_protocols_section_rip as \
                                                              test_show_ip_protocols_section_rip_iosxe

from genie.libs.parser.utils.common import format_output                                                        
# =================================
# Unit test for 'show ip protocols'
# =================================
class test_show_ip_protocols(test_show_ip_protocols_iosxe):

    def test_show_ip_protocols_full1(self):
        super().test_show_ip_protocols_full1()
        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        
        obj = ShowIpProtocols(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_protocols_full2(self):
        super().test_show_ip_protocols_full2()
        
        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        
        obj = ShowIpProtocols(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_ip_protocols_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpProtocols(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

class test_show_ip_protocols_section_rip(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_output = {'execute.return_value': '''
    Routing Protocol is "bgp 100"
      Sending updates every 60 seconds, next due in 0 sec
      Outgoing update filter list for all interfaces is 
      Incoming update filter list for all interfaces is 
      IGP synchronization is disabled
      Automatic route summarization is disabled
      Redistributing:connected, static
      Routing for Networks:
      Routing Information Sources:
        Gateway         Distance      Last Update
        10.13.13.13          200      02:20:54
        10.18.18.18          200      03:26:15
      Distance:external 20 internal 200 local 200
    '''
    }
    golden_parsed_output = {
        'protocols': {
            'bgp': {
                'instance': {
                    'default': {
                        'bgp_id': 100,
                        'vrf': {
                            'default': {
                                'address_family': {
                                    'ipv4': {
                                        'igp_sync': False,
                                        'automatic_route_summarization': False,
                                        'neighbor': {
                                            '10.13.13.13': {
                                                'neighbor_id': '10.13.13.13',
                                                'distance': 200,
                                                'last_update': '02:20:54',
                                                },
                                            '10.18.18.18': {
                                                'neighbor_id': '10.18.18.18',
                                                'distance': 200,
                                                'last_update': '03:26:15',
                                                },
                                            },
                                        'timers': {
                                            'update_interval': 60,
                                            'next_update': 0,
                                        },
                                        'redistribute': {
                                            'connected': {},
                                            'static': {},
                                        },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
    }
    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpProtocolsSectionRip(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_vrf_default(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpProtocolsSectionRip(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)
if __name__ == '__main__':
    unittest.main()
