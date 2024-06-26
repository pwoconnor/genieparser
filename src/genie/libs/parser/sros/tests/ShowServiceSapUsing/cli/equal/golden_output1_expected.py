expected_output = {
    "sap": {
        "2/1/6:10.*": {
            "service_id": 10,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "2/1/2:8.1": {
            "service_id": 181,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/2:3101.3101": {
            "service_id": 1121,
            "ingress_qos": 3501,
            "egress_qos": 3501,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/6:4000.1": {
            "service_id": 1121,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "2/1/6:3101.*": {
            "service_id": 1121,
            "ingress_qos": 4503,
            "egress_qos": 4503,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "2/1/6:4000.2": {
            "service_id": 1122,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "2/1/6:3999.1": {
            "service_id": 1221,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "2/1/6:101.2": {
            "service_id": 1230,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "2/1/6:4000.101": {
            "service_id": 2121,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "2/1/6:3999.101": {
            "service_id": 2221,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "1/2/1:391.*": {
            "service_id": 4092,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "1/2/1:4092.*": {
            "service_id": 4092,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "2/1/6:4092.*": {
            "service_id": 4092,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "2/2/1:1001": {
            "service_id": 5051,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/2/1:1002": {
            "service_id": 5051,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/7:2990": {
            "service_id": 10010,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/7:3990": {
            "service_id": 10010,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/8:980": {
            "service_id": 10010,
            "ingress_qos": 3511,
            "egress_qos": 3511,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/7:2991": {
            "service_id": 10011,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/7:3991": {
            "service_id": 10011,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/8:981": {
            "service_id": 10011,
            "ingress_qos": 3511,
            "egress_qos": 3511,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/7:2992": {
            "service_id": 10012,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/7:3992": {
            "service_id": 10012,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/8:982": {
            "service_id": 10012,
            "ingress_qos": 3511,
            "egress_qos": 3511,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/7:2993": {
            "service_id": 10013,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/7:3993": {
            "service_id": 10013,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/8:983": {
            "service_id": 10013,
            "ingress_qos": 3511,
            "egress_qos": 3511,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/7:2994": {
            "service_id": 10014,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/7:3994": {
            "service_id": 10014,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/8:984": {
            "service_id": 10014,
            "ingress_qos": 3511,
            "egress_qos": 3511,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/7:2995": {
            "service_id": 10015,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/7:3995": {
            "service_id": 10015,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/8:985": {
            "service_id": 10015,
            "ingress_qos": 3511,
            "egress_qos": 3511,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/7:2996": {
            "service_id": 10016,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/7:3996": {
            "service_id": 10016,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/8:986": {
            "service_id": 10016,
            "ingress_qos": 3511,
            "egress_qos": 3511,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/7:2997": {
            "service_id": 10017,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/7:3997": {
            "service_id": 10017,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/8:987": {
            "service_id": 10017,
            "ingress_qos": 3511,
            "egress_qos": 3511,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/7:2998": {
            "service_id": 10018,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/7:3998": {
            "service_id": 10018,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/8:988": {
            "service_id": 10018,
            "ingress_qos": 3511,
            "egress_qos": 3511,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/7:2999": {
            "service_id": 10019,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/7:3999": {
            "service_id": 10019,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/8:989": {
            "service_id": 10019,
            "ingress_qos": 3511,
            "egress_qos": 3511,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/7:2888": {
            "service_id": 10020,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/7:3888": {
            "service_id": 10020,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/8:888": {
            "service_id": 10020,
            "ingress_qos": 3511,
            "egress_qos": 3511,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/4:100": {
            "service_id": 30001,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "1/2/1:380.*": {
            "service_id": 40001,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "ip4",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "2/1/4:741": {
            "service_id": 40001,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "2/1/6:3000.100": {
            "service_id": 40001,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "2/1/6:3117.*": {
            "service_id": 40001,
            "ingress_qos": 3515,
            "egress_qos": 3515,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "3/1/5": {
            "service_id": 40001,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "1/1/1:100": {
            "service_id": 42001,
            "ingress_qos": 1,
            "egress_qos": 4201,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "2/1/8:4004": {
            "service_id": 42001,
            "ingress_qos": 1,
            "egress_qos": 3512,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/2/1:4006": {
            "service_id": 42001,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/8:4010": {
            "service_id": 52001,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "ip4",
            "egress_filter": "ip4",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/6:3331.1": {
            "service_id": 91009,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "2/1/6:3332.1": {
            "service_id": 91009,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "2/1/6:11.*": {
            "service_id": 100001,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/1:100.200": {
            "service_id": 100100,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "1/2/1:888.888": {
            "service_id": 100101,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/1:999.1": {
            "service_id": 100101,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/1:120.5": {
            "service_id": 100101,
            "ingress_qos": 1,
            "egress_qos": 3507,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/1:99.99": {
            "service_id": 100101,
            "ingress_qos": 10001,
            "egress_qos": 10001,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/1:100.100": {
            "service_id": 100101,
            "ingress_qos": 10001,
            "egress_qos": 10001,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/1:100.101": {
            "service_id": 100101,
            "ingress_qos": 10001,
            "egress_qos": 10001,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/1:100.199": {
            "service_id": 100101,
            "ingress_qos": 3504,
            "egress_qos": 3504,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "1/2/1:3993.1": {
            "service_id": 100201,
            "ingress_qos": 3501,
            "egress_qos": 3501,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "1/2/1:3994.1": {
            "service_id": 100201,
            "ingress_qos": 3501,
            "egress_qos": 3501,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "1/2/1:3995.1": {
            "service_id": 100201,
            "ingress_qos": 3501,
            "egress_qos": 3501,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "1/2/1:3996.1": {
            "service_id": 100201,
            "ingress_qos": 3501,
            "egress_qos": 3501,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "1/2/1:3997.1": {
            "service_id": 100201,
            "ingress_qos": 3501,
            "egress_qos": 3501,
            "ingress_filter": "ip4",
            "egress_filter": "ip4",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "1/2/1:3998.1": {
            "service_id": 100201,
            "ingress_qos": 3501,
            "egress_qos": 3501,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "1/2/1:3999.1": {
            "service_id": 100201,
            "ingress_qos": 3501,
            "egress_qos": 3501,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "1/2/1:4000.1": {
            "service_id": 100201,
            "ingress_qos": 3501,
            "egress_qos": 3501,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "2/1/8:995": {
            "service_id": 100201,
            "ingress_qos": 3511,
            "egress_qos": 3511,
            "ingress_filter": "ip4",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "1/2/1:3993.2": {
            "service_id": 100202,
            "ingress_qos": 3501,
            "egress_qos": 3501,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "1/2/1:3994.2": {
            "service_id": 100202,
            "ingress_qos": 3501,
            "egress_qos": 3501,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "1/2/1:3995.2": {
            "service_id": 100202,
            "ingress_qos": 3501,
            "egress_qos": 3501,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "1/2/1:3996.2": {
            "service_id": 100202,
            "ingress_qos": 3501,
            "egress_qos": 3501,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "1/2/1:3997.2": {
            "service_id": 100202,
            "ingress_qos": 3501,
            "egress_qos": 3501,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "1/2/1:3998.2": {
            "service_id": 100202,
            "ingress_qos": 3501,
            "egress_qos": 3501,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "1/2/1:3999.2": {
            "service_id": 100202,
            "ingress_qos": 3501,
            "egress_qos": 3501,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "1/2/1:4000.2": {
            "service_id": 100202,
            "ingress_qos": 3501,
            "egress_qos": 3501,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "2/1/8:994": {
            "service_id": 100202,
            "ingress_qos": 3511,
            "egress_qos": 3511,
            "ingress_filter": "ip4",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/2/1:802": {
            "service_id": 100202,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/8:999": {
            "service_id": 100204,
            "ingress_qos": 3511,
            "egress_qos": 3511,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/8:998": {
            "service_id": 100205,
            "ingress_qos": 3511,
            "egress_qos": 3511,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/8:997": {
            "service_id": 100401,
            "ingress_qos": 3511,
            "egress_qos": 3511,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/8:996": {
            "service_id": 100402,
            "ingress_qos": 3511,
            "egress_qos": 3511,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/2:3975.1": {
            "service_id": 100702,
            "ingress_qos": 3501,
            "egress_qos": 3501,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/2:1.2": {
            "service_id": 100702,
            "ingress_qos": 3501,
            "egress_qos": 3501,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "1/2/1:3000.1": {
            "service_id": 101199,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "2/1/2:9.1": {
            "service_id": 189901,
            "ingress_qos": 3501,
            "egress_qos": 3501,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/2:9.2": {
            "service_id": 189901,
            "ingress_qos": 3501,
            "egress_qos": 3501,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/2:9.3": {
            "service_id": 189901,
            "ingress_qos": 3501,
            "egress_qos": 3501,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/2:9.4": {
            "service_id": 189901,
            "ingress_qos": 3501,
            "egress_qos": 3501,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "1/2/1:3993.101": {
            "service_id": 200201,
            "ingress_qos": 3502,
            "egress_qos": 3502,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "1/2/1:3994.101": {
            "service_id": 200201,
            "ingress_qos": 3502,
            "egress_qos": 3502,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "1/2/1:3995.101": {
            "service_id": 200201,
            "ingress_qos": 3502,
            "egress_qos": 3502,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "1/2/1:3996.101": {
            "service_id": 200201,
            "ingress_qos": 3502,
            "egress_qos": 3502,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "1/2/1:3997.101": {
            "service_id": 200201,
            "ingress_qos": 3502,
            "egress_qos": 3502,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "1/2/1:3998.101": {
            "service_id": 200201,
            "ingress_qos": 3502,
            "egress_qos": 3502,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "1/2/1:3999.101": {
            "service_id": 200201,
            "ingress_qos": 3502,
            "egress_qos": 3502,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "1/2/1:4000.101": {
            "service_id": 200201,
            "ingress_qos": 3502,
            "egress_qos": 3502,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "2/1/2:100.100": {
            "service_id": 500100,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "3/1/4:4000.101": {
            "service_id": 4810101,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "3/1/4:4000.201": {
            "service_id": 4810102,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "2/1/6:151.1": {
            "service_id": 91034501,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Up",
        },
        "2/1/9:4002.1": {
            "service_id": 540020001,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/10:4002.1": {
            "service_id": 540020001,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/9:4002.2": {
            "service_id": 540020002,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
        "2/1/10:4002.2": {
            "service_id": 540020002,
            "ingress_qos": 1,
            "egress_qos": 1,
            "ingress_filter": "none",
            "egress_filter": "none",
            "admin_state": "Up",
            "oper_state": "Down",
        },
    },
    "total": 115,
}
