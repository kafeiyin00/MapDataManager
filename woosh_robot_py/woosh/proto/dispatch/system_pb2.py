# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: woosh/proto/dispatch/system.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from woosh.proto.util import common_pb2 as woosh_dot_proto_dot_util_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!woosh/proto/dispatch/system.proto\x12\x15woosh.dispatch.system\x1a\x1dwoosh/proto/util/common.proto\"\xd5\x01\n\x05Scene\x12\r\n\x05scene\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x12.\n\x04maps\x18\x03 \x03(\x0b\x32 .woosh.dispatch.system.Scene.Map\x1a|\n\x03Map\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nresolution\x18\n \x01(\x02\x12$\n\x06origin\x18\x0b \x01(\x0b\x32\x14.woosh.common.Pose2D\x12!\n\x03\x65nd\x18\x0c \x01(\x0b\x32\x14.woosh.common.Pose2D\"\xac\x02\n\x0e\x43hargeSettings\x12?\n\x08settings\x18\x01 \x03(\x0b\x32-.woosh.dispatch.system.ChargeSettings.Setting\x12:\n\x05order\x18\x0b \x01(\x0e\x32+.woosh.dispatch.system.ChargeSettings.Order\x1av\n\x07Setting\x12\r\n\x05level\x18\x01 \x01(\r\x12\x13\n\x0bguard_power\x18\x02 \x01(\r\x12\x11\n\tlow_power\x18\x03 \x01(\r\x12\x12\n\nwork_power\x18\x04 \x01(\r\x12\x12\n\nfull_power\x18\x05 \x01(\r\x12\x0c\n\x04time\x18\x0b \x01(\x05\"%\n\x05Order\x12\x08\n\x04kGet\x10\x00\x12\x08\n\x04kPut\x10\x01\x12\x08\n\x04kDel\x10\x02\"\x1b\n\x0bSwitchScene\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\rSceneSettings\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x85\x02\n\nPacAccount\x12\n\n\x02id\x18\x01 \x01(\r\x12\n\n\x02no\x18\x02 \x01(\t\x12\x34\n\x04type\x18\x05 \x01(\x0e\x32&.woosh.dispatch.system.PacAccount.Type\x12\x36\n\x05state\x18\x06 \x01(\x0e\x32\'.woosh.dispatch.system.PacAccount.State\x12\r\n\x05robot\x18\x0b \x01(\r\x12\x0f\n\x07tset_id\x18\x0c \x01(\x05\"\x1f\n\x04Type\x12\t\n\x05kPark\x10\x00\x12\x0c\n\x08kCharger\x10\x01\"0\n\x05State\x12\t\n\x05kIdle\x10\x00\x12\x0f\n\x0bkTransiting\x10\x01\x12\x0b\n\x07kOccupy\x10\x02\"E\n\x0ePacAccountList\x12\x33\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32!.woosh.dispatch.system.PacAccount\"\'\n\nGotoCharge\x12\r\n\x05robot\x18\x01 \x01(\r\x12\n\n\x02no\x18\x02 \x01(\t\"6\n\x06GetPos\x12\n\n\x02no\x18\x01 \x01(\t\x12 \n\x04pose\x18\x0b \x01(\x0b\x32\x12.woosh.common.Pose\"\x9e\x01\n\nPrintLevel\x12\x36\n\x05level\x18\x01 \x01(\x0e\x32\'.woosh.dispatch.system.PrintLevel.Level\"X\n\x05Level\x12\n\n\x06kTrace\x10\x00\x12\n\n\x06kDebug\x10\x01\x12\t\n\x05kInfo\x10\x02\x12\t\n\x05kWarn\x10\x03\x12\x08\n\x04kErr\x10\x04\x12\r\n\tkCritical\x10\x05\x12\x08\n\x04kOff\x10\x06\x42\x37\n\x1bwoosh.proto.dispatch.systemB\x13\x44ispatchSystemProtoP\x00\xf8\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'woosh.proto.dispatch.system_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033woosh.proto.dispatch.systemB\023DispatchSystemProtoP\000\370\001\001'
  _SCENE._serialized_start=92
  _SCENE._serialized_end=305
  _SCENE_MAP._serialized_start=181
  _SCENE_MAP._serialized_end=305
  _CHARGESETTINGS._serialized_start=308
  _CHARGESETTINGS._serialized_end=608
  _CHARGESETTINGS_SETTING._serialized_start=451
  _CHARGESETTINGS_SETTING._serialized_end=569
  _CHARGESETTINGS_ORDER._serialized_start=571
  _CHARGESETTINGS_ORDER._serialized_end=608
  _SWITCHSCENE._serialized_start=610
  _SWITCHSCENE._serialized_end=637
  _SCENESETTINGS._serialized_start=639
  _SCENESETTINGS._serialized_end=668
  _PACACCOUNT._serialized_start=671
  _PACACCOUNT._serialized_end=932
  _PACACCOUNT_TYPE._serialized_start=851
  _PACACCOUNT_TYPE._serialized_end=882
  _PACACCOUNT_STATE._serialized_start=884
  _PACACCOUNT_STATE._serialized_end=932
  _PACACCOUNTLIST._serialized_start=934
  _PACACCOUNTLIST._serialized_end=1003
  _GOTOCHARGE._serialized_start=1005
  _GOTOCHARGE._serialized_end=1044
  _GETPOS._serialized_start=1046
  _GETPOS._serialized_end=1100
  _PRINTLEVEL._serialized_start=1103
  _PRINTLEVEL._serialized_end=1261
  _PRINTLEVEL_LEVEL._serialized_start=1173
  _PRINTLEVEL_LEVEL._serialized_end=1261
# @@protoc_insertion_point(module_scope)
