expected_output = {
    'http_secure_server': {
        'active_session_modules': 'ALL',
        'capability': 'Present',
        'ciphersuite': ['rsa-aes-cbc-sha2', 'rsa-aes-gcm-sha2', 'dhe-aes-cbc-sha2', 'dhe-aes-gcm-sha2', 'ecdhe-rsa-aes-cbc-sha2', 'ecdhe-rsa-aes-gcm-sha2', 'ecdhe-ecdsa-aes-gcm-sha2', 'tls13-aes128-gcm-sha256', 'tls13-aes256-gcm-sha384', 'tls13-chacha20-poly1305-sha256'],
        'client_authentication': 'Disabled',
        'ecdhe_curve': 'secp256r1',
        'piv_authentication': 'Disabled',
        'piv_authorization': 'Disabled',
        'port': 443,
        'status': 'Enabled',
        'tls_version': ['TLSv1.3', 'TLSv1.2'],
        'trustpoint': 'TP-self-signed-3059606619',
    },
    'http_server': {
        'access_class': '0',
        'active_session_modules': 'ALL',
        'application_session_modules': {
            'banner_page': {
                'description': 'HTTP Banner Page Server',
                'handle': 5,
                'secure_status': 'Active',
                'status': 'Active',
            },
            'gsi7635a35535a0_web': {
                'description': 'wsma infra',
                'handle': 8,
                'secure_status': 'Active',
                'status': 'Active',
            },
            'gsi7635a732c8c0_web': {
                'description': 'wsma infra',
                'handle': 7,
                'secure_status': 'Active',
                'status': 'Active',
            },
            'home_page': {
                'description': 'IOS Homepage Server',
                'handle': 4,
                'secure_status': 'Active',
                'status': 'Active',
            },
            'http_ifs': {
                'description': 'HTTP based IOS File Server',
                'handle': 1,
                'secure_status': 'Active',
                'status': 'Active',
            },
            'ng_webui': {
                'description': 'Web GUI',
                'handle': 9,
                'secure_status': 'Active',
                'status': 'Active',
            },
            'openresty_pki': {
                'description': 'IOS OpenResty PKI Server',
                'handle': 3,
                'secure_status': 'Active',
                'status': 'Active',
            },
            'sl_http': {
                'description': 'HTTP REST IOS-XE Smart License Server',
                'handle': 2,
                'secure_status': 'Active',
                'status': 'Active',
            },
            'web_exec': {
                'description': 'HTTP based IOS EXEC Server',
                'handle': 6,
                'secure_status': 'Active',
                'status': 'Active',
            },
        },
        'auth_retry': 0,
        'authentication_method': 'enable',
        'conn_history_current_pos': 2,
        'current_connections': {
            '127.0.0.1:21111': {
                'in_bytes': 0,
                'out_bytes': 0,
                'remote_ipaddress_port': '127.0.0.1:39278',
            },
        },
        'digest_algorithm': 'md5',
        'file_upload_status': 'Disabled',
        'history': {
            'index': {
                '0': {
                    'end_time': '12:52:11 15/05',
                    'in_bytes': 0,
                    'local_ip_address_port': '127.0.0.1:21111',
                    'out_bytes': 404,
                    'remote_ip_address_port': '127.0.0.1:39278',
                },
                '1': {
                    'end_time': '12:52:13 15/05',
                    'in_bytes': 0,
                    'local_ip_address_port': '127.0.0.1:21111',
                    'out_bytes': 277,
                    'remote_ip_address_port': '127.0.0.1:39290',
                },
            },
        },
        'idle_timeout': 180,
        'ipv4_access_class': 'None',
        'ipv6_access_class': 'None',
        'life_timeout': 180,
        'linger_timeout': 60,
        'max_connections_allowed': 300,
        'max_requests_allowed': 25,
        'max_secondary_connections': 50,
        'nginx_internal_counters': {
            'active_connection': 1,
            'maximum_connection_hit': 0,
            'pool': 915,
            'pool_available': 904,
        },
        'port': 80,
        'session_idle_timeout': 600,
        'statistics': {
            'accepted_connections': 1,
            'reading': 0,
            'server_accepts_handled_requests': '2 2 2',
            'waiting': 0,
            'writing': 1,
        },
        'status': 'Disabled',
        'supplementary_listener_ports': 21111,
        'time_window': 0,
    },
}