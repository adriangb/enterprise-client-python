# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/endpoint/v4alpha/load_report.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.core.v4alpha import address_pb2 as envoy_dot_config_dot_core_dot_v4alpha_dot_address__pb2
from envoy.config.core.v4alpha import base_pb2 as envoy_dot_config_dot_core_dot_v4alpha_dot_base__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/config/endpoint/v4alpha/load_report.proto',
  package='envoy.config.endpoint.v4alpha',
  syntax='proto3',
  serialized_options=b'\n+io.envoyproxy.envoy.config.endpoint.v4alphaB\017LoadReportProtoP\001\272\200\310\321\006\002\020\003',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n/envoy/config/endpoint/v4alpha/load_report.proto\x12\x1d\x65nvoy.config.endpoint.v4alpha\x1a\'envoy/config/core/v4alpha/address.proto\x1a$envoy/config/core/v4alpha/base.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"\xc5\x03\n\x15UpstreamLocalityStats\x12\x35\n\x08locality\x18\x01 \x01(\x0b\x32#.envoy.config.core.v4alpha.Locality\x12!\n\x19total_successful_requests\x18\x02 \x01(\x04\x12\"\n\x1atotal_requests_in_progress\x18\x03 \x01(\x04\x12\x1c\n\x14total_error_requests\x18\x04 \x01(\x04\x12\x1d\n\x15total_issued_requests\x18\x08 \x01(\x04\x12Q\n\x11load_metric_stats\x18\x05 \x03(\x0b\x32\x36.envoy.config.endpoint.v4alpha.EndpointLoadMetricStats\x12U\n\x17upstream_endpoint_stats\x18\x07 \x03(\x0b\x32\x34.envoy.config.endpoint.v4alpha.UpstreamEndpointStats\x12\x10\n\x08priority\x18\x06 \x01(\r:5\x9a\xc5\x88\x1e\x30\n.envoy.config.endpoint.v3.UpstreamLocalityStats\"\x85\x03\n\x15UpstreamEndpointStats\x12\x33\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\".envoy.config.core.v4alpha.Address\x12)\n\x08metadata\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12!\n\x19total_successful_requests\x18\x02 \x01(\x04\x12\"\n\x1atotal_requests_in_progress\x18\x03 \x01(\x04\x12\x1c\n\x14total_error_requests\x18\x04 \x01(\x04\x12\x1d\n\x15total_issued_requests\x18\x07 \x01(\x04\x12Q\n\x11load_metric_stats\x18\x05 \x03(\x0b\x32\x36.envoy.config.endpoint.v4alpha.EndpointLoadMetricStats:5\x9a\xc5\x88\x1e\x30\n.envoy.config.endpoint.v3.UpstreamEndpointStats\"\xae\x01\n\x17\x45ndpointLoadMetricStats\x12\x13\n\x0bmetric_name\x18\x01 \x01(\t\x12)\n!num_requests_finished_with_metric\x18\x02 \x01(\x04\x12\x1a\n\x12total_metric_value\x18\x03 \x01(\x01:7\x9a\xc5\x88\x1e\x32\n0envoy.config.endpoint.v3.EndpointLoadMetricStats\"\x8e\x04\n\x0c\x43lusterStats\x12\x1d\n\x0c\x63luster_name\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x1c\n\x14\x63luster_service_name\x18\x06 \x01(\t\x12_\n\x17upstream_locality_stats\x18\x02 \x03(\x0b\x32\x34.envoy.config.endpoint.v4alpha.UpstreamLocalityStatsB\x08\xfa\x42\x05\x92\x01\x02\x08\x01\x12\x1e\n\x16total_dropped_requests\x18\x03 \x01(\x04\x12U\n\x10\x64ropped_requests\x18\x05 \x03(\x0b\x32;.envoy.config.endpoint.v4alpha.ClusterStats.DroppedRequests\x12\x37\n\x14load_report_interval\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x1a\x81\x01\n\x0f\x44roppedRequests\x12\x19\n\x08\x63\x61tegory\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x15\n\rdropped_count\x18\x02 \x01(\x04:<\x9a\xc5\x88\x1e\x37\n5envoy.config.endpoint.v3.ClusterStats.DroppedRequests:,\x9a\xc5\x88\x1e\'\n%envoy.config.endpoint.v3.ClusterStatsBH\n+io.envoyproxy.envoy.config.endpoint.v4alphaB\x0fLoadReportProtoP\x01\xba\x80\xc8\xd1\x06\x02\x10\x03\x62\x06proto3'
  ,
  dependencies=[envoy_dot_config_dot_core_dot_v4alpha_dot_address__pb2.DESCRIPTOR,envoy_dot_config_dot_core_dot_v4alpha_dot_base__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,udpa_dot_annotations_dot_status__pb2.DESCRIPTOR,udpa_dot_annotations_dot_versioning__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])




_UPSTREAMLOCALITYSTATS = _descriptor.Descriptor(
  name='UpstreamLocalityStats',
  full_name='envoy.config.endpoint.v4alpha.UpstreamLocalityStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='locality', full_name='envoy.config.endpoint.v4alpha.UpstreamLocalityStats.locality', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_successful_requests', full_name='envoy.config.endpoint.v4alpha.UpstreamLocalityStats.total_successful_requests', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_requests_in_progress', full_name='envoy.config.endpoint.v4alpha.UpstreamLocalityStats.total_requests_in_progress', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_error_requests', full_name='envoy.config.endpoint.v4alpha.UpstreamLocalityStats.total_error_requests', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_issued_requests', full_name='envoy.config.endpoint.v4alpha.UpstreamLocalityStats.total_issued_requests', index=4,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='load_metric_stats', full_name='envoy.config.endpoint.v4alpha.UpstreamLocalityStats.load_metric_stats', index=5,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='upstream_endpoint_stats', full_name='envoy.config.endpoint.v4alpha.UpstreamLocalityStats.upstream_endpoint_stats', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='priority', full_name='envoy.config.endpoint.v4alpha.UpstreamLocalityStats.priority', index=7,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\0360\n.envoy.config.endpoint.v3.UpstreamLocalityStats',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=315,
  serialized_end=768,
)


_UPSTREAMENDPOINTSTATS = _descriptor.Descriptor(
  name='UpstreamEndpointStats',
  full_name='envoy.config.endpoint.v4alpha.UpstreamEndpointStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='envoy.config.endpoint.v4alpha.UpstreamEndpointStats.address', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='envoy.config.endpoint.v4alpha.UpstreamEndpointStats.metadata', index=1,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_successful_requests', full_name='envoy.config.endpoint.v4alpha.UpstreamEndpointStats.total_successful_requests', index=2,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_requests_in_progress', full_name='envoy.config.endpoint.v4alpha.UpstreamEndpointStats.total_requests_in_progress', index=3,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_error_requests', full_name='envoy.config.endpoint.v4alpha.UpstreamEndpointStats.total_error_requests', index=4,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_issued_requests', full_name='envoy.config.endpoint.v4alpha.UpstreamEndpointStats.total_issued_requests', index=5,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='load_metric_stats', full_name='envoy.config.endpoint.v4alpha.UpstreamEndpointStats.load_metric_stats', index=6,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\0360\n.envoy.config.endpoint.v3.UpstreamEndpointStats',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=771,
  serialized_end=1160,
)


_ENDPOINTLOADMETRICSTATS = _descriptor.Descriptor(
  name='EndpointLoadMetricStats',
  full_name='envoy.config.endpoint.v4alpha.EndpointLoadMetricStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metric_name', full_name='envoy.config.endpoint.v4alpha.EndpointLoadMetricStats.metric_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_requests_finished_with_metric', full_name='envoy.config.endpoint.v4alpha.EndpointLoadMetricStats.num_requests_finished_with_metric', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_metric_value', full_name='envoy.config.endpoint.v4alpha.EndpointLoadMetricStats.total_metric_value', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\0362\n0envoy.config.endpoint.v3.EndpointLoadMetricStats',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1163,
  serialized_end=1337,
)


_CLUSTERSTATS_DROPPEDREQUESTS = _descriptor.Descriptor(
  name='DroppedRequests',
  full_name='envoy.config.endpoint.v4alpha.ClusterStats.DroppedRequests',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='category', full_name='envoy.config.endpoint.v4alpha.ClusterStats.DroppedRequests.category', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\004r\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dropped_count', full_name='envoy.config.endpoint.v4alpha.ClusterStats.DroppedRequests.dropped_count', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\0367\n5envoy.config.endpoint.v3.ClusterStats.DroppedRequests',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1691,
  serialized_end=1820,
)

_CLUSTERSTATS = _descriptor.Descriptor(
  name='ClusterStats',
  full_name='envoy.config.endpoint.v4alpha.ClusterStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_name', full_name='envoy.config.endpoint.v4alpha.ClusterStats.cluster_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\004r\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cluster_service_name', full_name='envoy.config.endpoint.v4alpha.ClusterStats.cluster_service_name', index=1,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='upstream_locality_stats', full_name='envoy.config.endpoint.v4alpha.ClusterStats.upstream_locality_stats', index=2,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005\222\001\002\010\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_dropped_requests', full_name='envoy.config.endpoint.v4alpha.ClusterStats.total_dropped_requests', index=3,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dropped_requests', full_name='envoy.config.endpoint.v4alpha.ClusterStats.dropped_requests', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='load_report_interval', full_name='envoy.config.endpoint.v4alpha.ClusterStats.load_report_interval', index=5,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CLUSTERSTATS_DROPPEDREQUESTS, ],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036\'\n%envoy.config.endpoint.v3.ClusterStats',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1340,
  serialized_end=1866,
)

_UPSTREAMLOCALITYSTATS.fields_by_name['locality'].message_type = envoy_dot_config_dot_core_dot_v4alpha_dot_base__pb2._LOCALITY
_UPSTREAMLOCALITYSTATS.fields_by_name['load_metric_stats'].message_type = _ENDPOINTLOADMETRICSTATS
_UPSTREAMLOCALITYSTATS.fields_by_name['upstream_endpoint_stats'].message_type = _UPSTREAMENDPOINTSTATS
_UPSTREAMENDPOINTSTATS.fields_by_name['address'].message_type = envoy_dot_config_dot_core_dot_v4alpha_dot_address__pb2._ADDRESS
_UPSTREAMENDPOINTSTATS.fields_by_name['metadata'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_UPSTREAMENDPOINTSTATS.fields_by_name['load_metric_stats'].message_type = _ENDPOINTLOADMETRICSTATS
_CLUSTERSTATS_DROPPEDREQUESTS.containing_type = _CLUSTERSTATS
_CLUSTERSTATS.fields_by_name['upstream_locality_stats'].message_type = _UPSTREAMLOCALITYSTATS
_CLUSTERSTATS.fields_by_name['dropped_requests'].message_type = _CLUSTERSTATS_DROPPEDREQUESTS
_CLUSTERSTATS.fields_by_name['load_report_interval'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
DESCRIPTOR.message_types_by_name['UpstreamLocalityStats'] = _UPSTREAMLOCALITYSTATS
DESCRIPTOR.message_types_by_name['UpstreamEndpointStats'] = _UPSTREAMENDPOINTSTATS
DESCRIPTOR.message_types_by_name['EndpointLoadMetricStats'] = _ENDPOINTLOADMETRICSTATS
DESCRIPTOR.message_types_by_name['ClusterStats'] = _CLUSTERSTATS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpstreamLocalityStats = _reflection.GeneratedProtocolMessageType('UpstreamLocalityStats', (_message.Message,), {
  'DESCRIPTOR' : _UPSTREAMLOCALITYSTATS,
  '__module__' : 'envoy.config.endpoint.v4alpha.load_report_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.endpoint.v4alpha.UpstreamLocalityStats)
  })
_sym_db.RegisterMessage(UpstreamLocalityStats)

UpstreamEndpointStats = _reflection.GeneratedProtocolMessageType('UpstreamEndpointStats', (_message.Message,), {
  'DESCRIPTOR' : _UPSTREAMENDPOINTSTATS,
  '__module__' : 'envoy.config.endpoint.v4alpha.load_report_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.endpoint.v4alpha.UpstreamEndpointStats)
  })
_sym_db.RegisterMessage(UpstreamEndpointStats)

EndpointLoadMetricStats = _reflection.GeneratedProtocolMessageType('EndpointLoadMetricStats', (_message.Message,), {
  'DESCRIPTOR' : _ENDPOINTLOADMETRICSTATS,
  '__module__' : 'envoy.config.endpoint.v4alpha.load_report_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.endpoint.v4alpha.EndpointLoadMetricStats)
  })
_sym_db.RegisterMessage(EndpointLoadMetricStats)

ClusterStats = _reflection.GeneratedProtocolMessageType('ClusterStats', (_message.Message,), {

  'DroppedRequests' : _reflection.GeneratedProtocolMessageType('DroppedRequests', (_message.Message,), {
    'DESCRIPTOR' : _CLUSTERSTATS_DROPPEDREQUESTS,
    '__module__' : 'envoy.config.endpoint.v4alpha.load_report_pb2'
    # @@protoc_insertion_point(class_scope:envoy.config.endpoint.v4alpha.ClusterStats.DroppedRequests)
    })
  ,
  'DESCRIPTOR' : _CLUSTERSTATS,
  '__module__' : 'envoy.config.endpoint.v4alpha.load_report_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.endpoint.v4alpha.ClusterStats)
  })
_sym_db.RegisterMessage(ClusterStats)
_sym_db.RegisterMessage(ClusterStats.DroppedRequests)


DESCRIPTOR._options = None
_UPSTREAMLOCALITYSTATS._options = None
_UPSTREAMENDPOINTSTATS._options = None
_ENDPOINTLOADMETRICSTATS._options = None
_CLUSTERSTATS_DROPPEDREQUESTS.fields_by_name['category']._options = None
_CLUSTERSTATS_DROPPEDREQUESTS._options = None
_CLUSTERSTATS.fields_by_name['cluster_name']._options = None
_CLUSTERSTATS.fields_by_name['upstream_locality_stats']._options = None
_CLUSTERSTATS._options = None
# @@protoc_insertion_point(module_scope)
