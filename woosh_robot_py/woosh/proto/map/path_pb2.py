# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: woosh/proto/map/path.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from woosh.proto.util import common_pb2 as woosh_dot_proto_dot_util_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1awoosh/proto/map/path.proto\x12\x0ewoosh.map.path\x1a\x1dwoosh/proto/util/common.proto\"n\n\x08PathInfo\x12,\n\nmono_paths\x18\x01 \x03(\x0b\x32\x18.woosh.map.path.MonoPath\x12\x34\n\x0e\x62idirect_paths\x18\x02 \x03(\x0b\x32\x1c.woosh.map.path.BidirectPath\"Q\n\x08MonoPath\x12!\n\x04path\x18\x01 \x03(\x0b\x32\x13.woosh.common.Point\x12\r\n\x05width\x18\x02 \x01(\x02\x12\x13\n\x0b\x61llow_avoid\x18\x0b \x01(\x08\"U\n\x0c\x42idirectPath\x12!\n\x04path\x18\x01 \x03(\x0b\x32\x13.woosh.common.Point\x12\r\n\x05width\x18\x02 \x01(\x02\x12\x13\n\x0b\x61llow_avoid\x18\x0b \x01(\x08\x42*\n\x14woosh.proto.map.pathB\rPathInfoProtoP\x00\xf8\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'woosh.proto.map.path_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024woosh.proto.map.pathB\rPathInfoProtoP\000\370\001\001'
  _PATHINFO._serialized_start=77
  _PATHINFO._serialized_end=187
  _MONOPATH._serialized_start=189
  _MONOPATH._serialized_end=270
  _BIDIRECTPATH._serialized_start=272
  _BIDIRECTPATH._serialized_end=357
# @@protoc_insertion_point(module_scope)
