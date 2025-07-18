# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: woosh/proto/task/task.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from woosh.proto.util import task_pb2 as woosh_dot_proto_dot_util_dot_task__pb2
from woosh.proto.util import robot_pb2 as woosh_dot_proto_dot_util_dot_robot__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bwoosh/proto/task/task.proto\x12\nwoosh.task\x1a\x1bwoosh/proto/util/task.proto\x1a\x1cwoosh/proto/util/robot.proto\"\xca\x01\n\x08TaskBase\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07mark_no\x18\x0b \x01(\t\x12\x1e\n\x04type\x18\x0c \x01(\x0e\x32\x10.woosh.task.Type\x12(\n\tdirection\x18\r \x01(\x0e\x32\x15.woosh.task.Direction\x12\x0f\n\x07type_no\x18\x0e \x01(\x05\x12\x11\n\twait_time\x18\x0f \x01(\x05\x12\x15\n\rcannot_cancel\x18\x15 \x01(\x08\x12\x0e\n\x06\x63ustom\x18\x1f \x01(\x0c\"D\n\x08TaskExec\x12 \n\x05state\x18\x01 \x01(\x0e\x32\x11.woosh.task.State\x12\x16\n\x0e\x61\x63tion_wait_id\x18\x02 \x01(\x05\"N\n\x04Task\x12\"\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x14.woosh.task.TaskBase\x12\"\n\x04\x65xec\x18\x02 \x01(\x0b\x32\x14.woosh.task.TaskExec\"\xb7\x01\n\x0bTaskSetBase\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\r\n\x05route\x18\x04 \x01(\t\x12\n\n\x02no\x18\x05 \x01(\t\x12\x0f\n\x07\x61\x64\x61pter\x18\x0b \x01(\t\x12\x10\n\x08\x61\x63tuator\x18\x0c \x01(\t\x12 \n\x05rtype\x18\x15 \x01(\x0e\x32\x11.woosh.robot.Type\x12\x10\n\x08priority\x18\x33 \x01(\x05\x12\x0e\n\x06robots\x18\x34 \x03(\r\"o\n\x0bTaskSetExec\x12\r\n\x05robot\x18\x01 \x01(\r\x12\'\n\x05state\x18\x0b \x01(\x0e\x32\x18.woosh.task.TaskSetState\x12\x13\n\x0b\x63ur_task_id\x18\x15 \x01(\x05\x12\x13\n\x0bpre_task_id\x18\x16 \x01(\x05\";\n\x0bTaskSetTime\x12\x10\n\x08generate\x18\x01 \x01(\x05\x12\r\n\x05start\x18\x02 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x03 \x01(\x05\"\x9f\x01\n\x07TaskSet\x12%\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x17.woosh.task.TaskSetBase\x12%\n\x04\x65xec\x18\x02 \x01(\x0b\x32\x17.woosh.task.TaskSetExec\x12%\n\x04time\x18\x03 \x01(\x0b\x32\x17.woosh.task.TaskSetTime\x12\x1f\n\x05tasks\x18\n \x03(\x0b\x32\x10.woosh.task.Task\">\n\x0bTaskSetList\x12\"\n\x05tsets\x18\x01 \x03(\x0b\x32\x13.woosh.task.TaskSet\x12\x0b\n\x03qty\x18\x0b \x01(\x03*\x82\x01\n\x05Order\x12\x13\n\x0fkOrderUndefined\x10\x00\x12\n\n\x06kPause\x10\x01\x12\r\n\tkContinue\x10\x02\x12\x0b\n\x07kCancel\x10\x03\x12\t\n\x05kNext\x10\x04\x12\t\n\x05kRedo\x10\x05\x12\r\n\tkComplete\x10\x06\x12\n\n\x06kReset\x10\x07\x12\x0b\n\x07kDelete\x10\x08*\x85\x01\n\x0cTaskSetState\x12\x1a\n\x16kTaskSetStateUndefined\x10\x00\x12\x12\n\x0ekSetUnassigned\x10\x01\x12\x11\n\rkSetExecuting\x10\x02\x12\x11\n\rkSetCompleted\x10\x03\x12\x0e\n\nkSetFailed\x10\x04\x12\x0f\n\x0bkSetDeleted\x10\x05\x42&\n\x10woosh.proto.taskB\rTaskBaseProtoP\x00\xf8\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'woosh.proto.task.task_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\020woosh.proto.taskB\rTaskBaseProtoP\000\370\001\001'
  _ORDER._serialized_start=1044
  _ORDER._serialized_end=1174
  _TASKSETSTATE._serialized_start=1177
  _TASKSETSTATE._serialized_end=1310
  _TASKBASE._serialized_start=103
  _TASKBASE._serialized_end=305
  _TASKEXEC._serialized_start=307
  _TASKEXEC._serialized_end=375
  _TASK._serialized_start=377
  _TASK._serialized_end=455
  _TASKSETBASE._serialized_start=458
  _TASKSETBASE._serialized_end=641
  _TASKSETEXEC._serialized_start=643
  _TASKSETEXEC._serialized_end=754
  _TASKSETTIME._serialized_start=756
  _TASKSETTIME._serialized_end=815
  _TASKSET._serialized_start=818
  _TASKSET._serialized_end=977
  _TASKSETLIST._serialized_start=979
  _TASKSETLIST._serialized_end=1041
# @@protoc_insertion_point(module_scope)
