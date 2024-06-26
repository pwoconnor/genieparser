expected_output = {
    "100.0.0.2/32": {
        "via": {
            "100.0.0.2": {
                "tunnel": {
                    "tunnel_name": "Tunnel100",
                    "created": "00:00:42",
                    "expire": "00:02:17",
                },
                "type": "dynamic",
                "flags": "router nhop rib",
                "nbma_address": "103.1.1.1",
                "preference": 255,
            }
        }
    },
    "100.0.0.100/32": {
        "via": {
            "100.0.0.100": {
                "tunnel": {
                    "tunnel_name": "Tunnel100",
                    "created": "10w2d",
                    "expire": "never expire",
                },
                "type": "static",
                "flags": "",
                "nbma_address": "101.1.1.1",
                "preference": 255,
            }
        }
    },
    "123.1.1.0/24": {
        "via": {
            "100.0.0.2": {
                "tunnel": {
                    "tunnel_name": "Tunnel100",
                    "created": "00:00:42",
                    "expire": "00:02:17",
                },
                "type": "dynamic",
                "flags": "router rib",
                "nbma_address": "103.1.1.1",
                "preference": 255,
            }
        }
    },
    "100.0.0.1/32": {
        "via": {
            "100.0.0.1": {
                "tunnel": {
                    "tunnel_name": "Tunnel100",
                    "created": "00:00:42",
                    "expire": "00:02:19",
                },
                "type": "dynamic",
                "flags": "router unique local",
                "nbma_address": "102.1.1.1",
                "preference": 255,
                "requester": "100.0.0.2",
                "request_id": "97",
            }
        }
    },
    "111.0.0.100/32": {
        "via": {
            "111.0.0.100": {
                "tunnel": {
                    "tunnel_name": "Tunnel111",
                    "created": "10w2d",
                    "expire": "never expire",
                },
                "type": "static",
                "flags": "",
                "nbma_address": "111.1.1.1",
                "preference": 255,
            }
        }
    },
}
