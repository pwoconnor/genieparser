expected_output =  {
     'list_of_neighbors': ['10.37.176.11'],
     'vrf': {
         'default': {
             'neighbor': {
                 '10.37.176.11': {
                     'address_family': {
                         'l2vpn evpn': {
                             'advertise_bit': 0,
                             'bgp_table_version': 320,
                             'community_attribute_sent': True,
                             'current_time': '0x4110577',
                             'dynamic_slow_peer_recovered': 'never',
                             'extended_community_attribute_sent': True,
                             'index': 1,
                             'last_detected_dynamic_slow_peer': 'never',
                             'last_received_refresh_end_of_rib': '18:53:19',
                             'last_received_refresh_start_of_rib': '18:53:19',
                             'last_sent_refresh_end_of_rib': '18:52:54',
                             'last_sent_refresh_start_of_rib': '18:53:19',
                             'local_policy_denied_prefixes_counters': {
                                 'inbound': {
                                     'af_permit_check': 'n/a',
                                     'refresh_end_of_rib': 1,
                                     'refresh_start_of_rib': 1,
                                     'total': 10,
                                 },
                                 'outbound': {
                                     'af_permit_check': 61,
                                     'refresh_end_of_rib': 1,
                                     'refresh_start_of_rib': 1,
                                     'total': 61,
                                 },
                             },
                             'max_nlri': 4,
                             'min_nlri': 0,
                             'neighbor_version': '320/0',
                             'output_queue_size': 0,
                             'prefix_activity_counters': {
                                 'received': {
                                     'explicit_withdraw': 58,
                                     'implicit_withdraw': 0,
                                     'prefixes_current': 57,
                                     'prefixes_total': 115,
                                     'used_as_bestpath': 24,
                                     'used_as_multipath': 0,
                                     'used_as_secondary': 0,
                                 },
                                 'sent': {
                                     'explicit_withdraw': 58,
                                     'implicit_withdraw': 14,
                                     'prefixes_current': 71,
                                     'prefixes_total': 143,
                                     'used_as_bestpath': 'n/a',
                                     'used_as_multipath': 'n/a',
                                     'used_as_secondary': 'n/a',
                                 },
                             },
                             'refresh_epoch': 2,
                             'refresh_in': 0,
                             'refresh_out': 25,
                             'slow_peer_detection': False,
                             'slow_peer_split_update_group_dynamic': False,
                             'update_group_member': 1,
                         },
                     },
                     'bgp_event_timer': {
                         'next': {
                             'ackhold': '0x0',
                             'deadwait': '0x0',
                             'giveup': '0x0',
                             'keepalive': '0x0',
                             'linger': '0x0',
                             'processq': '0x0',
                             'retrans': '0x0',
                             'sendwnd': '0x0',
                             'timewait': '0x0',
                         },
                         'starts': {
                             'ackhold': 1299,
                             'deadwait': 0,
                             'giveup': 0,
                             'keepalive': 0,
                             'linger': 0,
                             'processq': 0,
                             'retrans': 1310,
                             'sendwnd': 0,
                             'timewait': 0,
                         },
                         'wakeups': {
                             'ackhold': 1208,
                             'deadwait': 0,
                             'giveup': 0,
                             'keepalive': 0,
                             'linger': 0,
                             'processq': 0,
                             'retrans': 0,
                             'sendwnd': 0,
                             'timewait': 0,
                         },
                     },
                     'bgp_negotiated_capabilities': {
                         'enhanced_refresh': 'advertised and received',
                         'four_octets_asn': 'advertised and received',
                         'graceful_restart': 'received',
                         'l2vpn_evpn': 'advertised and received',
                         'remote_restart_timer': 120,
                         'route_refresh': 'advertised and received(new)',
                         'stateful_switchover': 'NO for session 1',
                     },
                     'bgp_negotiated_keepalive_timers': {
                         'hold_time': 180,
                         'keepalive_interval': 60,
                     },
                     'bgp_neighbor_counters': {
                         'messages': {
                             'in_queue_depth': 0,
                             'out_queue_depth': 0,
                             'received': {
                                 'keepalives': 1207,
                                 'notifications': 0,
                                 'opens': 1,
                                 'route_refresh': 0,
                                 'total': 1331,
                                 'updates': 121,
                             },
                             'sent': {
                                 'keepalives': 1216,
                                 'notifications': 0,
                                 'opens': 1,
                                 'route_refresh': 0,
                                 'total': 1344,
                                 'updates': 125,
                             },
                         },
                     },
                     'bgp_neighbor_session': {
                         'sessions': 1,
                     },
                     'bgp_session_transport': {
                         'ack_hold': 200,
                         'address_tracking_status': 'enabled',
                         'connection': {
                             'dropped': 0,
                             'established': 1,
                             'last_reset': 'never',
                         },
                         'connection_state': 'estab',
                         'connection_tableid': 0,
                         'datagram': {
                             'datagram_received': {
                                 'out_of_order': 0,
                                 'total_data': 38439,
                                 'value': 2599,
                                 'with_data': 1302,
                             },
                             'datagram_sent': {
                                 'fastretransmit': 0,
                                 'partialack': 0,
                                 'retransmit': 0,
                                 'second_congestion': 0,
                                 'total_data': 39383,
                                 'value': 2551,
                                 'with_data': 1312,
                             },
                         },
                         'delrcvwnd': 437,
                         'ecn_connection': 'disabled',
                         'enqueued_packets': {
                             'input_packet': 0,
                             'mis_ordered_packet': 0,
                             'retransmit_packet': 0,
                         },
                         'fast_lock_acquisition_failures': 0,
                         'graceful_restart': 'disabled',
                         'io_status': 1,
                         'ip_precedence_value': 6,
                         'irs': 3387932665,
                         'iss': 31738988,
                         'krtt': 0,
                         'lock_slow_path': 0,
                         'max_rtt': 1000,
                         'maximum_output_segment_queue_size': 50,
                         'maxrcvwnd': 16384,
                         'min_rtt': 0,
                         'min_time_between_advertisement_runs': 30,
                         'minimum_incoming_ttl': 0,
                         'option_flags': 'nagle, path mtu capable',
                         'outgoing_ttl': 4,
                         'packet_fast_path': 0,
                         'packet_fast_processed': 0,
                         'packet_slow_path': 0,
                         'rcv_scale': 0,
                         'rcvnxt': 3387971105,
                         'rcvwnd': 15947,
                         'receive_idletime': 34788,
                         'rib_route_ip': '10.37.176.11',
                         'rtto': 1003,
                         'rtv': 3,
                         'sent_idletime': 34588,
                         'snd_scale': 0,
                         'sndnxt': 31778372,
                         'snduna': 31778372,
                         'sndwnd': 16152,
                         'srtt': 1000,
                         'sso': False,
                         'status_flags': 'active open',
                         'tcp_path_mtu_discovery': 'enabled',
                         'tcp_semaphore': '0x7F30D2340458',
                         'tcp_semaphore_status': 'FREE',
                         'transport': {
                             'foreign_host': '10.37.176.11',
                             'foreign_port': '179',
                             'local_host': '10.37.176.10',
                             'local_port': '49807',
                             'mss': 1460,
                         },
                         'unread_input_bytes': 0,
                         'uptime': 67999934,
                     },
                     'bgp_version': 4,
                     'link': 'external',
                     'remote_as': 4200006053,
                     'router_id': '10.37.176.11',
                     'session_state': 'Established',
                     'shutdown': False,
                 },
             },
         },
     },
 }
 

