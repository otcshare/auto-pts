#
# auto-pts - The Bluetooth PTS Automation Framework
#
# Copyright (c) 2017, Intel Corporation.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms and conditions of the GNU General Public License,
# version 2, as published by the Free Software Foundation.
#
# This program is distributed in the hope it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#

# Generated by h2py.py (CPython 2.7.10) from
# zephyr/tests/bluetooth/tester/src/bttester.h
BTP_MTU = 1024
BTP_INDEX_NONE = 0xff
BTP_SERVICE_ID_CORE = 0
BTP_SERVICE_ID_GAP = 1
BTP_SERVICE_ID_GATT = 2
BTP_SERVICE_ID_L2CAP = 3
BTP_SERVICE_ID_MESH = 4
BTP_SERVICE_ID_MMDL = 5
BTP_SERVICE_ID_GATTC = 6
BTP_SERVICE_ID_VCS = 8
BTP_SERVICE_ID_IAS = 9
BTP_SERVICE_ID_AICS = 10
BTP_SERVICE_ID_VOCS = 11
BTP_SERVICE_ID_PACS = 12
BTP_SERVICE_ID_ASCS = 13
BTP_SERVICE_ID_BAP = 14
BTP_SERVICE_ID_HAS = 15
BTP_SERVICE_ID_MICP = 16
BTP_SERVICE_ID_CSIS = 17
BTP_SERVICE_ID_MICS = 18

BTP_STATUS_SUCCESS = 0x00
BTP_STATUS_FAILED = 0x01
BTP_STATUS_UNKNOWN_CMD = 0x02
BTP_STATUS_NOT_READY = 0x03
BTP_STATUS = 0x00
CORE_READ_SUPPORTED_COMMANDS = 0x01
CORE_READ_SUPPORTED_SERVICES = 0x02
CORE_REGISTER_SERVICE = 0x03
CORE_UNREGISTER_SERVICE = 0x04
CORE_LOG_MESSAGE = 0x05
CORE_EV_IUT_READY = 0x80
GAP_READ_SUPPORTED_COMMANDS = 0x01
GAP_READ_CONTROLLER_INDEX_LIST = 0x02
GAP_SETTINGS_POWERED = 0
GAP_SETTINGS_CONNECTABLE = 1
GAP_SETTINGS_FAST_CONNECTABLE = 2
GAP_SETTINGS_DISCOVERABLE = 3
GAP_SETTINGS_BONDABLE = 4
GAP_SETTINGS_LINK_SEC_3 = 5
GAP_SETTINGS_SSP = 6
GAP_SETTINGS_BREDR = 7
GAP_SETTINGS_HS = 8
GAP_SETTINGS_LE = 9
GAP_SETTINGS_ADVERTISING = 10
GAP_SETTINGS_SC = 11
GAP_SETTINGS_DEBUG_KEYS = 12
GAP_SETTINGS_PRIVACY = 13
GAP_SETTINGS_CONTROLLER_CONFIG = 14
GAP_SETTINGS_STATIC_ADDRESS = 15
GAP_SETTINGS_SC_ONLY = 16
GAP_SETTINGS_EXTENDED_ADVERTISING = 17
GAP_READ_CONTROLLER_INFO = 0x03
GAP_RESET = 0x04
GAP_SET_POWERED = 0x05
GAP_SET_CONNECTABLE = 0x06
GAP_SET_FAST_CONNECTABLE = 0x07
GAP_NON_DISCOVERABLE = 0x00
GAP_GENERAL_DISCOVERABLE = 0x01
GAP_LIMITED_DISCOVERABLE = 0x02
GAP_SET_DISCOVERABLE = 0x08
GAP_SET_BONDABLE = 0x09
GAP_START_ADVERTISING = 0x0a
GAP_STOP_ADVERTISING = 0x0b
GAP_DISCOVERY_FLAG_LE = 0x01
GAP_DISCOVERY_FLAG_BREDR = 0x02
GAP_DISCOVERY_FLAG_LIMITED = 0x04
GAP_DISCOVERY_FLAG_LE_ACTIVE_SCAN = 0x08
GAP_DISCOVERY_FLAG_LE_OBSERVE = 0x10
GAP_START_DISCOVERY = 0x0c
GAP_STOP_DISCOVERY = 0x0d
GAP_CONNECT = 0x0e
GAP_DISCONNECT = 0x0f
GAP_IO_CAP_DISPLAY_ONLY = 0
GAP_IO_CAP_DISPLAY_YESNO = 1
GAP_IO_CAP_KEYBOARD_ONLY = 2
GAP_IO_CAP_NO_INPUT_OUTPUT = 3
GAP_IO_CAP_KEYBOARD_DISPLAY = 4
GAP_SET_IO_CAP = 0x10
GAP_PAIR = 0x11
GAP_UNPAIR = 0x12
GAP_PASSKEY_ENTRY = 0x13
GAP_PASSKEY_CONFIRM = 0x14
GAP_START_DIRECT_ADV_HD = 0x0001
GAP_START_DIRECT_ADV_OWN_ID = 0x0002
GAP_START_DIRECT_ADV_PEER_RPA = 0x0004
GAP_START_DIRECT_ADV = 0x15
GAP_CONN_PARAM_UPDATE = 0x16
GAP_PAIRING_CONSENT_RSP = 0x17
GAP_OOB_LEGACY_SET_DATA = 0x18
GAP_OOB_SC_GET_LOCAL_DATA = 0x19
GAP_OOB_SC_SET_REMOTE_DATA = 0x1a
GAP_SET_MITM = 0x1b
GAP_SET_FILTER_ACCEPT_LIST = 0x1c
GAP_SET_PRIVACY = 0x1d
GAP_SET_SC_ONLY = 0x1e
GAP_SET_SC = 0x1f
GAP_SET_MIN_ENC_KEY_SIZE = 0x20
GAP_SET_EXTENDED_ADVERTISING = 0x21
GAP_PADV_CONFIGURE = 0x22
GAP_PADV_START = 0x23
GAP_PADV_STOP = 0x24
GAP_PADV_SET_DATA = 0x25
GAP_PADV_CREATE_SYNC = 0x26
GAP_PADV_SYNC_TRANSFER_SET_INFO = 0x27
GAP_PADV_SYNC_TRANSFER_START = 0x28
GAP_PADV_SYNC_TRANSFER_RECV = 0x29
GAP_EV_NEW_SETTINGS = 0x80
GAP_DEVICE_FOUND_FLAG_RSSI = 0x01
GAP_DEVICE_FOUND_FLAG_AD = 0x02
GAP_DEVICE_FOUND_FLAG_SD = 0x04
GAP_EV_DEVICE_FOUND = 0x81
GAP_EV_DEVICE_CONNECTED = 0x82
GAP_EV_DEVICE_DISCONNECTED = 0x83
GAP_EV_PASSKEY_DISPLAY = 0x84
GAP_EV_PASSKEY_ENTRY_REQ = 0x85
GAP_EV_PASSKEY_CONFIRM_REQ = 0x86
GAP_EV_IDENTITY_RESOLVED = 0x87
GAP_EV_CONN_PARAM_UPDATE = 0x88
GAP_EV_SEC_LEVEL_CHANGED = 0x89
GAP_EV_PAIRING_CONSENT_REQ = 0x8a
GAP_EV_BOND_LOST = 0x8b
GAP_EV_PAIRING_FAILED = 0x8c
GAP_EV_PERIODIC_SYNC_ESTABLISHED = 0x8d
GAP_EV_PERIODIC_SYNC_LOST = 0x8e
GAP_EV_PERIODIC_REPORT = 0x8f
GAP_EV_PERIODIC_TRANSFER_RECEIVED = 0x90
GATT_READ_SUPPORTED_COMMANDS = 0x01
GATT_SERVICE_PRIMARY = 0x00
GATT_SERVICE_SECONDARY = 0x01
GATT_ADD_SERVICE = 0x02
GATT_ADD_CHARACTERISTIC = 0x03
GATT_ADD_DESCRIPTOR = 0x04
GATT_ADD_INCLUDED_SERVICE = 0x05
GATT_SET_VALUE = 0x06
GATT_START_SERVER = 0x07
GATT_SET_ENC_KEY_SIZE = 0x09
GATT_EXCHANGE_MTU = 0x0a
GATT_DISC_ALL_PRIM = 0x0b
GATT_DISC_PRIM_UUID = 0x0c
GATT_FIND_INCLUDED = 0x0d
GATT_DISC_ALL_CHRC = 0x0e
GATT_DISC_CHRC_UUID = 0x0f
GATT_DISC_ALL_DESC = 0x10
GATT_READ = 0x11
GATT_READ_UUID = 0x12
GATT_READ_LONG = 0x13
GATT_READ_MULTIPLE = 0x14
GATT_READ_MULTIPLE_VAR = 0x20
GATT_WRITE_WITHOUT_RSP = 0x15
GATT_SIGNED_WRITE_WITHOUT_RSP = 0x16
GATT_WRITE = 0x17
GATT_WRITE_LONG = 0x18
GATT_WRITE_RELIABLE = 0x19
GATT_CFG_NOTIFY = 0x1a
GATT_CFG_INDICATE = 0x1b
GATT_GET_ATTRIBUTES = 0x1c
GATT_GET_ATTRIBUTE_VALUE = 0x1d
GATT_CHANGE_DATABASE = 0x1e
GATT_EATT_CONNECT = 0x1f
GATT_NOTIFY_MULTIPLE = 0x21
GATT_EV_NOTIFICATION = 0x80
GATT_EV_ATTR_VALUE_CHANGED = 0x81
GATTC_READ_SUPPORTED_COMMANDS = 0x01
GATTC_EXCHANGE_MTU = 0x02
GATTC_DISC_ALL_PRIM = 0x03
GATTC_DISC_PRIM_UUID = 0x04
GATTC_FIND_INCLUDED = 0x05
GATTC_DISC_ALL_CHRC = 0x06
GATTC_DISC_CHRC_UUID = 0x07
GATTC_DISC_ALL_DESC = 0x08
GATTC_READ = 0x09
GATTC_READ_UUID = 0x0a
GATTC_READ_LONG = 0x0b
GATTC_READ_MULTIPLE = 0x0c
GATTC_WRITE_WITHOUT_RSP = 0x0d
GATTC_SIGNED_WRITE_WITHOUT_RSP = 0x0e
GATTC_WRITE = 0x0f
GATTC_WRITE_LONG = 0x10
GATTC_WRITE_RELIABLE = 0x11
GATTC_CFG_NOTIFY = 0x12
GATTC_CFG_INDICATE = 0x13
GATTC_READ_MULTIPLE_VAR = 0x14
GATTC_EV_MTU_EXCHANGED = 0x80
GATTC_DISC_ALL_PRIM_RP = 0x81
GATTC_DISC_PRIM_UUID_RP = 0x82
GATTC_FIND_INCLUDED_RP = 0x83
GATTC_DISC_ALL_CHRC_RP = 0x84
GATTC_DISC_CHRC_UUID_RP = 0x85
GATTC_DISC_ALL_DESC_RP = 0x86
GATTC_READ_RP = 0x87
GATTC_READ_UUID_RP = 0x88
GATTC_READ_LONG_RP = 0x89
GATTC_READ_MULTIPLE_RP = 0x8a
GATTC_WRITE_RP = 0x8b
GATTC_WRITE_LONG_RP = 0x8c
GATTC_RELIABLE_WRITE_RP = 0x8d
GATTC_RELIABLE_WRITE_RP = 0x8d
GATTC_CFG_NOTIFY_RP = 0x8e
GATTC_CFG_INDICATE_RP = 0x8f
GATTC_EV_NOTIFICATION_RXED = 0x90
GATTC_READ_MULTIPLE_VAR_RP = 0x91
L2CAP_READ_SUPPORTED_COMMANDS = 0x01
L2CAP_CONNECT = 0x02
L2CAP_CONNECT_OPT_ECFC = 0x01
L2CAP_CONNECT_OPT_HOLD_CREDIT = 0x02
L2CAP_DISCONNECT = 0x03
L2CAP_SEND_DATA = 0x04
L2CAP_TRANSPORT_BREDR = 0x00
L2CAP_TRANSPORT_LE = 0x01
L2CAP_LISTEN = 0x05
L2CAP_ACCEPT_CONNECTION = 0x06
L2CAP_RECONFIGURE = 0x07
L2CAP_CREDITS = 0x08
L2CAP_DISCONNECT_EATT_CHANS = 0x09
L2CAP_EV_CONNECTION_REQ = 0x80
L2CAP_EV_CONNECTED = 0x81
L2CAP_EV_DISCONNECTED = 0x82
L2CAP_EV_DATA_RECEIVED = 0x83
L2CAP_EV_RECONFIGURED = 0x84
MESH_READ_SUPPORTED_COMMANDS = 0x01
MESH_STATIC_OOB = 0x01
MESH_OUTPUT_OOB = 0x02
MESH_INPUT_OOB = 0x03
MESH_OUT_BLINK = 0x01
MESH_OUT_BEEP = 0x02
MESH_OUT_VIBRATE = 0x04
MESH_OUT_DISPLAY_NUMBER = 0x08
MESH_OUT_DISPLAY_STRING = 0x10
MESH_IN_PUSH = 0x01
MESH_IN_TWIST = 0x02
MESH_IN_ENTER_NUMBER = 0x04
MESH_IN_ENTER_STRING = 0x08
MESH_CONFIG_PROVISIONING = 0x02
MESH_PROVISION_NODE = 0x03
MESH_INIT = 0x04
MESH_RESET = 0x05
MESH_INPUT_NUMBER = 0x06
MESH_INPUT_STRING = 0x07
MESH_IV_UPDATE_TEST_MODE = 0x08
MESH_IV_UPDATE_TOGGLE = 0x09
MESH_NET_SEND = 0x0a
MESH_HEALTH_ADD_FAULTS = 0x0b
MESH_HEALTH_CLEAR_FAULTS = 0x0c
MESH_LPN_SET = 0x0d
MESH_LPN_POLL = 0x0e
MESH_MODEL_SEND = 0x0f
MESH_LPN_SUBSCRIBE = 0x10
MESH_LPN_UNSUBSCRIBE = 0x11
MESH_RPL_CLEAR = 0x12
MESH_PROXY_IDENTITY = 0x13
MESH_COMP_DATA_GET = 0x14
MESH_CFG_BEACON_GET = 0x15
MESH_CFG_BEACON_SET = 0x16
MESH_CFG_DATA_SET = 0x17
MESH_CFG_DEFAULT_TTL_GET = 0x18
MESH_CFG_DEFAULT_TTL_SET = 0x19
MESH_CFG_GATT_PROXY_GET = 0x1a
MESH_CFG_GATT_PROXY_SET = 0x1b
MESH_CFG_FRIEND_GET = 0x1c
MESH_CFG_FRIEND_SET = 0x1d
MESH_CFG_RELAY_GET = 0x1e
MESH_CFG_RELAY_SET = 0x1f
MESH_CFG_MODEL_PUB_GET = 0x20
MESH_CFG_MODEL_PUB_SET = 0x21
MESH_CFG_MODEL_SUB_ADD = 0x22
MESH_CFG_MODEL_SUB_DEL = 0x23
MESH_CFG_NETKEY_ADD = 0x24
MESH_CFG_NETKEY_GET = 0x25
MESH_CFG_NETKEY_DEL = 0x26
MESH_CFG_APPKEY_ADD = 0x27
MESH_CFG_APPKEY_DEL = 0x28
MESH_CFG_APPKEY_GET = 0x29
MESH_CFG_MODEL_APP_BIND = 0x2A
MESH_CFG_MODEL_APP_UNBIND = 0x2B
MESH_CFG_MODEL_APP_GET = 0x2C
MESH_CFG_MODEL_APP_VND_GET = 0x2D
MESH_CFG_HEARTBEAT_PUB_SET = 0x2E
MESH_CFG_HEARTBEAT_PUB_GET = 0x2F
MESH_CFG_HEARTBEAT_SUB_SET = 0x30
MESH_CFG_HEARTBEAT_SUB_GET = 0x31
MESH_CFG_NET_TRANSMIT_GET = 0x32
MESH_CFG_NET_TRANSMIT_SET = 0x33
MESH_CFG_MODEL_SUB_OVW = 0x34
MESH_CFG_MODEL_SUB_DEL_ALL = 0x35
MESH_CFG_MODEL_SUB_GET = 0x36
MESH_CFG_MODEL_SUB_VND_GET = 0x37
MESH_CFG_MODEL_SUB_VA_ADD = 0x38
MESH_CFG_MODEL_SUB_VA_DEL = 0x39
MESH_CFG_MODEL_SUB_VA_OVW = 0x3A
MESH_CFG_NETKEY_UPDATE = 0x3B
MESH_CFG_APPKEY_UPDATE = 0x3C
MESH_CFG_NODE_IDT_SET = 0x3D
MESH_CFG_NODE_IDT_GET = 0x3E
MESH_CFG_NODE_RESET = 0x3F
MESH_CFG_LPN_POLLTIMEOUT_GET = 0x40
MESH_CFG_MODEL_PUB_VA_SET = 0x41
MESH_CFG_MODEL_APP_BIND_VND = 0x42
MESH_HEALTH_FAULT_GET = 0x43
MESH_HEALTH_FAULT_CLEAR = 0x44
MESH_HEALTH_FAULT_TEST = 0x45
MESH_HEALTH_PERIOD_GET = 0x46
MESH_HEALTH_PERIOD_SET = 0x47
MESH_HEALTH_ATTENTION_GET = 0x48
MESH_HEALTH_ATTENTION_SET = 0x49
MESH_PROVISION_ADV = 0x4A
MESH_CFG_KRP_GET = 0x4B
MESH_CFG_KRP_SET = 0x4C
MESH_VA_ADD = 0x4D
MESH_VA_DEL = 0x4E
MESH_SAR_TRANSMITTER_GET = 0x4F
MESH_SAR_TRANSMITTER_SET = 0x50
MESH_SAR_RECEIVER_GET = 0x51
MESH_SAR_RECEIVER_SET = 0x52
MESH_LARGE_COMP_DATA_GET = 0x53
MESH_MODELS_METADATA_GET = 0x54
MESH_OPCODES_AGGREGATOR_INIT = 0x55
MESH_OPCODES_AGGREGATOR_SEND = 0x56
MESH_COMP_CHANGE_PREPARE = 0x57
MESH_COMP_SET_ALT = 0x58
MESH_RPR_SCAN_START = 0x59
MESH_RPR_EXT_SCAN_START = 0x5a
MESH_RPR_SCAN_CAPS_GET = 0x5b
MESH_RPR_SCAN_GET = 0x5c
MESH_RPR_SCAN_STOP = 0x5d
MESH_RPR_LINK_GET = 0x5e
MESH_RPR_LINK_CLOSE = 0x5f
MESH_RPR_PROV_REMOTE = 0x60
MESH_RPR_REPROV_REMOTE = 0x61

MESH_PRIV_BEACON_GET = 0x6c
MESH_PRIV_BEACON_SET = 0x6d
MESH_PRIV_GATT_PROXY_GET = 0x6e
MESH_PRIV_GATT_PROXY_SET = 0x6f
MESH_PRIV_NODE_ID_GET = 0x70
MESH_PRIV_NODE_ID_SET = 0x71
MESH_PROXY_PRIVATE_IDENTITY = 0x72
MESH_PROXY_CONNECT = 0x77
MESH_EV_OUT_NUMBER_ACTION = 0x80
MESH_EV_OUT_STRING_ACTION = 0x81
MESH_EV_IN_ACTION = 0x82
MESH_EV_PROVISIONED = 0x83
MESH_PROV_BEARER_PB_ADV = 0x00
MESH_PROV_BEARER_PB_GATT = 0x01
MESH_EV_PROV_LINK_OPEN = 0x84
MESH_EV_PROV_LINK_CLOSED = 0x85
MESH_EV_NET_RECV = 0x86
MESH_EV_INVALID_BEARER = 0x87
MESH_EV_INCOMP_TIMER_EXP = 0x88
MESH_EV_FRND_ESTABLISHED = 0x89
MESH_EV_FRND_TERMINATED = 0x8a
MESH_EV_LPN_ESTABLISHED = 0x8b
MESH_EV_LPN_TERMINATED = 0x8c
MESH_EV_LPN_POLLED = 0x8d
MESH_EV_PROV_NODE_ADDED = 0x8e
MESH_EV_MODEL_RECV = 0x8f
MESH_EV_BLOB_LOST_TARGET = 0x90
MMDL_READ_SUPPORTED_COMMANDS = 0x01
MMDL_GEN_ONOFF_GET = 0x02
MMDL_GEN_ONOFF_SET = 0x03
MMDL_GEN_LVL_GET = 0x04
MMDL_GEN_LVL_SET = 0x05
MMDL_GEN_LVL_DELTA_SET = 0x06
MMDL_GEN_LVL_MOVE_SET = 0x07
MMDL_GEN_DTT_GET = 0x08
MMDL_GEN_DTT_SET = 0x09
MMDL_GEN_PONOFF_GET = 0x0a
MMDL_GEN_PONOFF_SET = 0x0b
MMDL_GEN_PLVL_GET = 0x0c
MMDL_GEN_PLVL_SET = 0x0d
MMDL_GEN_PLVL_LAST_GET = 0x0e
MMDL_GEN_PLVL_DFLT_GET = 0x0f
MMDL_GEN_PLVL_DFLT_SET = 0x10
MMDL_GEN_PLVL_RANGE_GET = 0x11
MMDL_GEN_PLVL_RANGE_SET = 0x12
MMDL_GEN_BATTERY_GET = 0x13
MMDL_GEN_LOC_GLOBAL_GET = 0x14
MMDL_GEN_LOC_LOCAL_GET = 0x15
MMDL_GEN_LOC_GLOBAL_SET = 0x16
MMDL_GEN_LOC_LOCAL_SET = 0x17
MMDL_GEN_PROPS_GET = 0x18
MMDL_GEN_PROP_GET = 0x19
MMDL_GEN_PROP_SET = 0x1a
MMDL_SENSOR_DESC_GET = 0x1b
MMDL_SENSOR_GET = 0x1c
MMDL_SENSOR_COLUMN_GET = 0x1d
MMDL_SENSOR_SERIES_GET = 0x1e
MMDL_SENSOR_CADENCE_GET = 0x1f
MMDL_SENSOR_CADENCE_SET = 0x20
MMDL_SENSOR_SETTINGS_GET = 0x21
MMDL_SENSOR_SETTING_GET = 0x22
MMDL_SENSOR_SETTING_SET = 0x23
MMDL_TIME_GET = 0x24
MMDL_TIME_SET = 0x25
MMDL_TIME_ROLE_GET = 0x26
MMDL_TIME_ROLE_SET = 0x27
MMDL_TIME_ZONE_GET = 0x28
MMDL_TIME_ZONE_SET = 0x29
MMDL_TIME_TAI_UTC_DELTA_GET = 0x2a
MMDL_TIME_TAI_UTC_DELTA_SET = 0x2b
MMDL_LIGHT_LIGHTNESS_GET = 0x2c
MMDL_LIGHT_LIGHTNESS_SET = 0x2d
MMDL_LIGHT_LIGHTNESS_LINEAR_GET = 0x2e
MMDL_LIGHT_LIGHTNESS_LINEAR_SET = 0x2f
MMDL_LIGHT_LIGHTNESS_LAST_GET = 0x30
MMDL_LIGHT_LIGHTNESS_DEFAULT_GET = 0x31
MMDL_LIGHT_LIGHTNESS_DEFAULT_SET = 0x32
MMDL_LIGHT_LIGHTNESS_RANGE_GET = 0x33
MMDL_LIGHT_LIGHTNESS_RANGE_SET = 0x34
MMDL_LIGHT_LC_MODE_GET = 0x35
MMDL_LIGHT_LC_MODE_SET = 0x36
MMDL_LIGHT_LC_OCCUPANCY_MODE_GET = 0x37
MMDL_LIGHT_LC_OCCUPANCY_MODE_SET = 0x38
MMDL_LIGHT_LC_LIGHT_ONOFF_MODE_GET = 0x39
MMDL_LIGHT_LC_LIGHT_ONOFF_MODE_SET = 0x3a
MMDL_LIGHT_LC_PROPERTY_GET = 0x3b
MMDL_LIGHT_LC_PROPERTY_SET = 0x3c
MMDL_SENSOR_DATA_SET = 0x3d
MMDL_LIGHT_CTL_STATES_GET = 0x3e
MMDL_LIGHT_CTL_STATES_SET = 0x3f
MMDL_LIGHT_CTL_TEMPERATURE_GET = 0x40
MMDL_LIGHT_CTL_TEMPERATURE_SET = 0x41
MMDL_LIGHT_CTL_DEFAULT_GET = 0x42
MMDL_LIGHT_CTL_DEFAULT_SET = 0x43
MMDL_LIGHT_CTL_TEMPERATURE_RANGE_GET = 0x44
MMDL_LIGHT_CTL_TEMPERATURE_RANGE_SET = 0x45
MMDL_SCENE_STATE_GET = 0x46
MMDL_SCENE_REGISTER_GET = 0x47
MMDL_SCENE_STORE_PROCEDURE = 0x48
MMDL_SCENE_RECALL = 0x49
MMDL_LIGHT_XYL_GET = 0x4a
MMDL_LIGHT_XYL_SET = 0x4b
MMDL_LIGHT_XYL_TARGET_GET = 0x4c
MMDL_LIGHT_XYL_DEFAULT_GET = 0x4d
MMDL_LIGHT_XYL_DEFAULT_SET = 0x4e
MMDL_LIGHT_XYL_RANGE_GET = 0x4f
MMDL_LIGHT_XYL_RANGE_SET = 0x50
MMDL_LIGHT_HSL_GET = 0x51
MMDL_LIGHT_HSL_SET = 0x52
MMDL_LIGHT_HSL_TARGET_GET = 0x53
MMDL_LIGHT_HSL_DEFAULT_GET = 0x54
MMDL_LIGHT_HSL_DEFAULT_SET = 0x55
MMDL_LIGHT_HSL_RANGE_GET = 0x56
MMDL_LIGHT_HSL_RANGE_SET = 0x57
MMDL_LIGHT_HSL_HUE_GET = 0x58
MMDL_LIGHT_HSL_HUE_SET = 0x59
MMDL_LIGHT_HSL_SATURATION_GET = 0x5a
MMDL_LIGHT_HSL_SATURATION_SET = 0x5b
MMDL_SCHEDULER_GET = 0x5c
MMDL_SCHEDULER_ACTION_GET = 0x5d
MMDL_SCHEDULER_ACTION_SET = 0x5e
MMDL_DFU_INF_GET = 0x5f
MMDL_BLOB_INFO_GET = 0x60
MMDL_DFU_UPDATE_FIRMWARE_CHECK = 0x61
MMDL_DFU_UPDATE_FIRMWARE_GET = 0x62
MMDL_DFU_UPDATE_FIRMWARE_CANCEL = 0x63
MMDL_DFU_UPDATE_FIRMWARE_START = 0x64
MMDL_BLOB_SRV_RECV = 0x65
MMDL_BLOB_TRANSFER_START = 0x66
MMDL_BLOB_TRANSFER_CANCEL = 0x67
MMDL_BLOB_TRANSFER_GET = 0x68
MMDL_BLOB_SRV_CANCEL = 0x69
MMDL_DFU_UPDATE_FIRMWARE_APPLY = 0x6A
MMDL_DFU_SRV_APPLY = 0x6B

VCS_READ_SUPPORTED_COMMANDS = 0x01
VCS_SET_VOL = 0x02
VCS_VOL_UP = 0x03
VCS_VOL_DOWN = 0x04
VCS_MUTE = 0x05
VCS_UNMUTE = 0x06

IAS_EV_OUT_ALERT_ACTION = 0x80

AICS_READ_SUPPORTED_COMMANDS = 0x01
AICS_SET_GAIN = 0x02
AICS_MUTE = 0x03
AICS_UNMUTE = 0x04
AICS_MAN_GAIN_SET = 0x05
AICS_AUTO_GAIN_SET = 0x06
AICS_SET_MAN_GAIN_ONLY = 0x07
AICS_SET_AUTO_GAIN_ONLY = 0x08
AICS_AUDIO_DESC_SET = 0x09
AICS_MUTE_DISABLE = 0x0a
AICS_GAIN_SETTING_PROP_GET = 0x0b
AICS_TYPE_GET = 0x0c
AICS_STATUS_GET = 0x0d
AICS_STATE_GET = 0x0e
AICS_DESCRIPTION_GET = 0x0f
AICS_STATE_EV = 0x80
AICS_GAIN_SETTING_PROP_EV = 0x81
AICS_INPUT_TYPE_EV = 0x82
AICS_STATUS_EV = 0x83
AICS_DESCRIPTION_EV = 0x84

VOCS_READ_SUPPORTED_COMMANDS = 0x01
VOCS_UPDATE_AUDIO_LOC = 0x02
VOCS_UPDATE_OUT_DESC = 0x03

PACS_READ_SUPPORTED_COMMANDS = 0x01
PACS_UPDATE_CHARACTERISTIC = 0x02

PACS_CHARACTERISTIC_SINK_PAC = 0x01
PACS_CHARACTERISTIC_SOURCE_PAC = 0x02
PACS_CHARACTERISTIC_SINK_AUDIO_LOCATIONS = 0x03
PACS_CHARACTERISTIC_SOURCE_AUDIO_LOCATIONS = 0x04
PACS_CHARACTERISTIC_AVAILABLE_AUDIO_CONTEXTS = 0x05
PACS_CHARACTERISTIC_SUPPORTED_AUDIO_CONTEXTS = 0x06
PACS_EV_CHARACTERISTIC_SUBSCRIBED = 0x80

ASCS_READ_SUPPORTED_COMMANDS = 0x01
ASCS_CONFIGURE_CODEC = 0x02
ASCS_CONFIGURE_QOS = 0x03
ASCS_ENABLE = 0x04
ASCS_RECEIVER_START_READY = 0x05
ASCS_RECEIVER_STOP_READY = 0x06
ASCS_DISABLE = 0x07
ASCS_RELEASE = 0x08
ASCS_UPDATE_METADATA = 0x09
ASCS_ADD_ASE_TO_CIS = 0x0a
ASCS_EV_OPERATION_COMPLETED = 0x80
ASCS_EV_CHARACTERISTIC_SUBSCRIBED = 0x81
ASCS_EV_ASE_STATE_CHANGED = 0x82

BAP_READ_SUPPORTED_COMMANDS = 0x01
BAP_DISCOVER = 0x02
BAP_SEND = 0x03
BAP_EV_DISCOVERY_COMPLETED = 0x80
BAP_EV_CODEC_CAP_FOUND = 0x81
BAP_EV_ASE_FOUND = 0x82
BAP_EV_STREAM_RECEIVED = 0x83

HAS_READ_SUPPORTED_COMMANDS = 0x01
HAS_SET_ACTIVE_INDEX = 0x02
HAS_SET_PRESET_NAME = 0x03
HAS_REMOVE_PRESET = 0x04
HAS_ADD_PRESET = 0x05
HAS_SET_PROPERTIES = 0x06

CSIS_READ_SUPPORTED_COMMANDS = 0x01
CSIS_SET_MEMBER_LOCK = 0x02
CSIS_GET_MEMBER_RSI = 0x03

MICP_READ_SUPPORTED_COMMANDS = 0x01
MICP_DISCOVERY = 0x02
MICP_MUTE_STATE = 0x03
MICP_MUTE = 0x04
MICP_DISCOVERED_EV = 0x80
MICP_MUTE_STATE_EV = 0x81

MICS_READ_SUPPORTED_COMMANDS = 0x01
MICS_MUTE_DISABLE = 0x02
MICS_MUTE_READ = 0x03
MICS_MUTE = 0x04
MICS_UNMUTE = 0x05
MICS_MUTE_STATE_EV = 0x80

