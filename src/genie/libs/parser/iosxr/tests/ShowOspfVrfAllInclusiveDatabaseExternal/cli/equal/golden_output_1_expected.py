

expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "1": {
                            "areas": {
                                "0.0.0.0": {
                                    "database": {
                                        "lsa_types": {
                                            5: {
                                                "lsa_type": 5,
                                                "lsas": {
                                                    "10.94.44.44 10.64.4.4": {
                                                        "adv_router": "10.64.4.4",
                                                        "lsa_id": "10.94.44.44",
                                                        "ospfv2": {
                                                            "body": {
                                                                "external": {
                                                                    "network_mask": "255.255.255.255",
                                                                    "topologies": {
                                                                        0: {
                                                                            "external_route_tag": 0,
                                                                            "flags": "E",
                                                                            "forwarding_address": "0.0.0.0",
                                                                            "metric": 20,
                                                                            "mt_id": 0,
                                                                            "tos": 0,
                                                                        }
                                                                    },
                                                                }
                                                            },
                                                            "header": {
                                                                "adv_router": "10.64.4.4",
                                                                "age": 608,
                                                                "checksum": "0x7d61",
                                                                "length": 36,
                                                                "lsa_id": "10.94.44.44",
                                                                "option": "None",
                                                                "option_desc": "No TOS-capability, DC",
                                                                "routing_bit_enable": True,
                                                                "seq_num": "80000002",
                                                                "type": 5,
                                                            },
                                                        },
                                                    }
                                                },
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
