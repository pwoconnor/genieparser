expected_output = {
    "pce_sr_policy_database":{
      "color":30,
      "end_point":"10.0.0.14",
      "name":"srte_c_30_ep_10.0.0.14",
      "status":{
         "admin":"up",
         "operational":{
            "state":"up",
            "time_for_state":"00:00:04",
            "since":"Oct  3 12:04:44.675)"
         }
      },
      "candidate_paths":{
         "preference":{
            100:{
               "Requested_bsid":"dynamic",
               "pcc_info":{
                  "symbolic_name":"cfg_srte_c_30_ep_10.0.0.14_discr_100",
                  "plsp_id":1
               },
               "constraints":{
                  "protection_type":"protected-preferred",
                  "maximum_dept":12
               },
               "path_type":{
                  "dynamic":{
                     "status":"valid",
                     "metric_type":"TE,",
                     "path_accumulated_metric":260,
                     "hops":{
                        1:{
                           "sid":24000,
                           "sid_type":"Adjacency-SID",
                           "local_address":"10.2.12.1",
                           "remote_address":"10.2.12.2"
                        },
                        2:{
                           "sid":24008,
                           "sid_type":"Adjacency-SID",
                           "local_address":"10.12.14.1",
                           "remote_address":"10.12.14.2"
                        }
                     }
                  }
               }
            }
         }
      },
      "attributes":{
         "binding_sid":"26628",
         "forward_class":"Not Configured",
         "steering_labeled_services_disabled":"no",
         "steering_bgp_disabled":"no",
         "ipv6_caps_enable":"yes",
         "invalidation_drop_enabled":"no",
         "max_install_standby_candidate_paths":0
      }
   }
}