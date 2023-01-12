// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: ConnectGazeboToRosTopic.proto

#define INTERNAL_SUPPRESS_PROTOBUF_FIELD_DEPRECATION
#include "ConnectGazeboToRosTopic.pb.h"

#include <algorithm>

#include <google/protobuf/stubs/common.h>
#include <google/protobuf/stubs/port.h>
#include <google/protobuf/stubs/once.h>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/wire_format_lite_inl.h>
#include <google/protobuf/descriptor.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/reflection_ops.h>
#include <google/protobuf/wire_format.h>
// @@protoc_insertion_point(includes)

namespace gz_std_msgs {

namespace {

const ::google::protobuf::Descriptor* ConnectGazeboToRosTopic_descriptor_ = NULL;
const ::google::protobuf::internal::GeneratedMessageReflection*
  ConnectGazeboToRosTopic_reflection_ = NULL;
const ::google::protobuf::EnumDescriptor* ConnectGazeboToRosTopic_MsgType_descriptor_ = NULL;

}  // namespace


void protobuf_AssignDesc_ConnectGazeboToRosTopic_2eproto() GOOGLE_ATTRIBUTE_COLD;
void protobuf_AssignDesc_ConnectGazeboToRosTopic_2eproto() {
  protobuf_AddDesc_ConnectGazeboToRosTopic_2eproto();
  const ::google::protobuf::FileDescriptor* file =
    ::google::protobuf::DescriptorPool::generated_pool()->FindFileByName(
      "ConnectGazeboToRosTopic.proto");
  GOOGLE_CHECK(file != NULL);
  ConnectGazeboToRosTopic_descriptor_ = file->message_type(0);
  static const int ConnectGazeboToRosTopic_offsets_[3] = {
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(ConnectGazeboToRosTopic, gazebo_topic_),
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(ConnectGazeboToRosTopic, ros_topic_),
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(ConnectGazeboToRosTopic, msgtype_),
  };
  ConnectGazeboToRosTopic_reflection_ =
    ::google::protobuf::internal::GeneratedMessageReflection::NewGeneratedMessageReflection(
      ConnectGazeboToRosTopic_descriptor_,
      ConnectGazeboToRosTopic::default_instance_,
      ConnectGazeboToRosTopic_offsets_,
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(ConnectGazeboToRosTopic, _has_bits_[0]),
      -1,
      -1,
      sizeof(ConnectGazeboToRosTopic),
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(ConnectGazeboToRosTopic, _internal_metadata_),
      -1);
  ConnectGazeboToRosTopic_MsgType_descriptor_ = ConnectGazeboToRosTopic_descriptor_->enum_type(0);
}

namespace {

GOOGLE_PROTOBUF_DECLARE_ONCE(protobuf_AssignDescriptors_once_);
inline void protobuf_AssignDescriptorsOnce() {
  ::google::protobuf::GoogleOnceInit(&protobuf_AssignDescriptors_once_,
                 &protobuf_AssignDesc_ConnectGazeboToRosTopic_2eproto);
}

void protobuf_RegisterTypes(const ::std::string&) GOOGLE_ATTRIBUTE_COLD;
void protobuf_RegisterTypes(const ::std::string&) {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedMessage(
      ConnectGazeboToRosTopic_descriptor_, &ConnectGazeboToRosTopic::default_instance());
}

}  // namespace

void protobuf_ShutdownFile_ConnectGazeboToRosTopic_2eproto() {
  delete ConnectGazeboToRosTopic::default_instance_;
  delete ConnectGazeboToRosTopic_reflection_;
}

void protobuf_AddDesc_ConnectGazeboToRosTopic_2eproto() GOOGLE_ATTRIBUTE_COLD;
void protobuf_AddDesc_ConnectGazeboToRosTopic_2eproto() {
  static bool already_here = false;
  if (already_here) return;
  already_here = true;
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  ::google::protobuf::DescriptorPool::InternalAddGeneratedFile(
    "\n\035ConnectGazeboToRosTopic.proto\022\013gz_std_"
    "msgs\"\234\003\n\027ConnectGazeboToRosTopic\022\024\n\014gaze"
    "bo_topic\030\002 \002(\t\022\021\n\tros_topic\030\003 \002(\t\022=\n\007msg"
    "Type\030\004 \002(\0162,.gz_std_msgs.ConnectGazeboTo"
    "RosTopic.MsgType\"\230\002\n\007MsgType\022\r\n\tACTUATOR"
    "S\020\000\022\014\n\010FLOAT_32\020\001\022\022\n\016FLUID_PRESSURE\020\002\022\007\n"
    "\003IMU\020\003\022\017\n\013JOINT_STATE\020\004\022\022\n\016MAGNETIC_FIEL"
    "D\020\005\022\017\n\013NAV_SAT_FIX\020\006\022\014\n\010ODOMETRY\020\007\022\010\n\004PO"
    "SE\020\010\022 \n\034POSE_WITH_COVARIANCE_STAMPED\020\t\022\025"
    "\n\021TRANSFORM_STAMPED\020\n\022\021\n\rTWIST_STAMPED\020\013"
    "\022\025\n\021VECTOR_3D_STAMPED\020\014\022\016\n\nWIND_SPEED\020\r\022"
    "\022\n\016WRENCH_STAMPED\020\016", 459);
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedFile(
    "ConnectGazeboToRosTopic.proto", &protobuf_RegisterTypes);
  ConnectGazeboToRosTopic::default_instance_ = new ConnectGazeboToRosTopic();
  ConnectGazeboToRosTopic::default_instance_->InitAsDefaultInstance();
  ::google::protobuf::internal::OnShutdown(&protobuf_ShutdownFile_ConnectGazeboToRosTopic_2eproto);
}

// Force AddDescriptors() to be called at static initialization time.
struct StaticDescriptorInitializer_ConnectGazeboToRosTopic_2eproto {
  StaticDescriptorInitializer_ConnectGazeboToRosTopic_2eproto() {
    protobuf_AddDesc_ConnectGazeboToRosTopic_2eproto();
  }
} static_descriptor_initializer_ConnectGazeboToRosTopic_2eproto_;

// ===================================================================

const ::google::protobuf::EnumDescriptor* ConnectGazeboToRosTopic_MsgType_descriptor() {
  protobuf_AssignDescriptorsOnce();
  return ConnectGazeboToRosTopic_MsgType_descriptor_;
}
bool ConnectGazeboToRosTopic_MsgType_IsValid(int value) {
  switch(value) {
    case 0:
    case 1:
    case 2:
    case 3:
    case 4:
    case 5:
    case 6:
    case 7:
    case 8:
    case 9:
    case 10:
    case 11:
    case 12:
    case 13:
    case 14:
      return true;
    default:
      return false;
  }
}

#if !defined(_MSC_VER) || _MSC_VER >= 1900
const ConnectGazeboToRosTopic_MsgType ConnectGazeboToRosTopic::ACTUATORS;
const ConnectGazeboToRosTopic_MsgType ConnectGazeboToRosTopic::FLOAT_32;
const ConnectGazeboToRosTopic_MsgType ConnectGazeboToRosTopic::FLUID_PRESSURE;
const ConnectGazeboToRosTopic_MsgType ConnectGazeboToRosTopic::IMU;
const ConnectGazeboToRosTopic_MsgType ConnectGazeboToRosTopic::JOINT_STATE;
const ConnectGazeboToRosTopic_MsgType ConnectGazeboToRosTopic::MAGNETIC_FIELD;
const ConnectGazeboToRosTopic_MsgType ConnectGazeboToRosTopic::NAV_SAT_FIX;
const ConnectGazeboToRosTopic_MsgType ConnectGazeboToRosTopic::ODOMETRY;
const ConnectGazeboToRosTopic_MsgType ConnectGazeboToRosTopic::POSE;
const ConnectGazeboToRosTopic_MsgType ConnectGazeboToRosTopic::POSE_WITH_COVARIANCE_STAMPED;
const ConnectGazeboToRosTopic_MsgType ConnectGazeboToRosTopic::TRANSFORM_STAMPED;
const ConnectGazeboToRosTopic_MsgType ConnectGazeboToRosTopic::TWIST_STAMPED;
const ConnectGazeboToRosTopic_MsgType ConnectGazeboToRosTopic::VECTOR_3D_STAMPED;
const ConnectGazeboToRosTopic_MsgType ConnectGazeboToRosTopic::WIND_SPEED;
const ConnectGazeboToRosTopic_MsgType ConnectGazeboToRosTopic::WRENCH_STAMPED;
const ConnectGazeboToRosTopic_MsgType ConnectGazeboToRosTopic::MsgType_MIN;
const ConnectGazeboToRosTopic_MsgType ConnectGazeboToRosTopic::MsgType_MAX;
const int ConnectGazeboToRosTopic::MsgType_ARRAYSIZE;
#endif  // !defined(_MSC_VER) || _MSC_VER >= 1900
#if !defined(_MSC_VER) || _MSC_VER >= 1900
const int ConnectGazeboToRosTopic::kGazeboTopicFieldNumber;
const int ConnectGazeboToRosTopic::kRosTopicFieldNumber;
const int ConnectGazeboToRosTopic::kMsgTypeFieldNumber;
#endif  // !defined(_MSC_VER) || _MSC_VER >= 1900

ConnectGazeboToRosTopic::ConnectGazeboToRosTopic()
  : ::google::protobuf::Message(), _internal_metadata_(NULL) {
  SharedCtor();
  // @@protoc_insertion_point(constructor:gz_std_msgs.ConnectGazeboToRosTopic)
}

void ConnectGazeboToRosTopic::InitAsDefaultInstance() {
}

ConnectGazeboToRosTopic::ConnectGazeboToRosTopic(const ConnectGazeboToRosTopic& from)
  : ::google::protobuf::Message(),
    _internal_metadata_(NULL) {
  SharedCtor();
  MergeFrom(from);
  // @@protoc_insertion_point(copy_constructor:gz_std_msgs.ConnectGazeboToRosTopic)
}

void ConnectGazeboToRosTopic::SharedCtor() {
  ::google::protobuf::internal::GetEmptyString();
  _cached_size_ = 0;
  gazebo_topic_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  ros_topic_.UnsafeSetDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  msgtype_ = 0;
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
}

ConnectGazeboToRosTopic::~ConnectGazeboToRosTopic() {
  // @@protoc_insertion_point(destructor:gz_std_msgs.ConnectGazeboToRosTopic)
  SharedDtor();
}

void ConnectGazeboToRosTopic::SharedDtor() {
  gazebo_topic_.DestroyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  ros_topic_.DestroyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  if (this != default_instance_) {
  }
}

void ConnectGazeboToRosTopic::SetCachedSize(int size) const {
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
}
const ::google::protobuf::Descriptor* ConnectGazeboToRosTopic::descriptor() {
  protobuf_AssignDescriptorsOnce();
  return ConnectGazeboToRosTopic_descriptor_;
}

const ConnectGazeboToRosTopic& ConnectGazeboToRosTopic::default_instance() {
  if (default_instance_ == NULL) protobuf_AddDesc_ConnectGazeboToRosTopic_2eproto();
  return *default_instance_;
}

ConnectGazeboToRosTopic* ConnectGazeboToRosTopic::default_instance_ = NULL;

ConnectGazeboToRosTopic* ConnectGazeboToRosTopic::New(::google::protobuf::Arena* arena) const {
  ConnectGazeboToRosTopic* n = new ConnectGazeboToRosTopic;
  if (arena != NULL) {
    arena->Own(n);
  }
  return n;
}

void ConnectGazeboToRosTopic::Clear() {
// @@protoc_insertion_point(message_clear_start:gz_std_msgs.ConnectGazeboToRosTopic)
  if (_has_bits_[0 / 32] & 7u) {
    if (has_gazebo_topic()) {
      gazebo_topic_.ClearToEmptyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
    }
    if (has_ros_topic()) {
      ros_topic_.ClearToEmptyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
    }
    msgtype_ = 0;
  }
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
  if (_internal_metadata_.have_unknown_fields()) {
    mutable_unknown_fields()->Clear();
  }
}

bool ConnectGazeboToRosTopic::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!GOOGLE_PREDICT_TRUE(EXPRESSION)) goto failure
  ::google::protobuf::uint32 tag;
  // @@protoc_insertion_point(parse_start:gz_std_msgs.ConnectGazeboToRosTopic)
  for (;;) {
    ::std::pair< ::google::protobuf::uint32, bool> p = input->ReadTagWithCutoff(127);
    tag = p.first;
    if (!p.second) goto handle_unusual;
    switch (::google::protobuf::internal::WireFormatLite::GetTagFieldNumber(tag)) {
      // required string gazebo_topic = 2;
      case 2: {
        if (tag == 18) {
          DO_(::google::protobuf::internal::WireFormatLite::ReadString(
                input, this->mutable_gazebo_topic()));
          ::google::protobuf::internal::WireFormat::VerifyUTF8StringNamedField(
            this->gazebo_topic().data(), this->gazebo_topic().length(),
            ::google::protobuf::internal::WireFormat::PARSE,
            "gz_std_msgs.ConnectGazeboToRosTopic.gazebo_topic");
        } else {
          goto handle_unusual;
        }
        if (input->ExpectTag(26)) goto parse_ros_topic;
        break;
      }

      // required string ros_topic = 3;
      case 3: {
        if (tag == 26) {
         parse_ros_topic:
          DO_(::google::protobuf::internal::WireFormatLite::ReadString(
                input, this->mutable_ros_topic()));
          ::google::protobuf::internal::WireFormat::VerifyUTF8StringNamedField(
            this->ros_topic().data(), this->ros_topic().length(),
            ::google::protobuf::internal::WireFormat::PARSE,
            "gz_std_msgs.ConnectGazeboToRosTopic.ros_topic");
        } else {
          goto handle_unusual;
        }
        if (input->ExpectTag(32)) goto parse_msgType;
        break;
      }

      // required .gz_std_msgs.ConnectGazeboToRosTopic.MsgType msgType = 4;
      case 4: {
        if (tag == 32) {
         parse_msgType:
          int value;
          DO_((::google::protobuf::internal::WireFormatLite::ReadPrimitive<
                   int, ::google::protobuf::internal::WireFormatLite::TYPE_ENUM>(
                 input, &value)));
          if (::gz_std_msgs::ConnectGazeboToRosTopic_MsgType_IsValid(value)) {
            set_msgtype(static_cast< ::gz_std_msgs::ConnectGazeboToRosTopic_MsgType >(value));
          } else {
            mutable_unknown_fields()->AddVarint(4, value);
          }
        } else {
          goto handle_unusual;
        }
        if (input->ExpectAtEnd()) goto success;
        break;
      }

      default: {
      handle_unusual:
        if (tag == 0 ||
            ::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
            ::google::protobuf::internal::WireFormatLite::WIRETYPE_END_GROUP) {
          goto success;
        }
        DO_(::google::protobuf::internal::WireFormat::SkipField(
              input, tag, mutable_unknown_fields()));
        break;
      }
    }
  }
success:
  // @@protoc_insertion_point(parse_success:gz_std_msgs.ConnectGazeboToRosTopic)
  return true;
failure:
  // @@protoc_insertion_point(parse_failure:gz_std_msgs.ConnectGazeboToRosTopic)
  return false;
#undef DO_
}

void ConnectGazeboToRosTopic::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // @@protoc_insertion_point(serialize_start:gz_std_msgs.ConnectGazeboToRosTopic)
  // required string gazebo_topic = 2;
  if (has_gazebo_topic()) {
    ::google::protobuf::internal::WireFormat::VerifyUTF8StringNamedField(
      this->gazebo_topic().data(), this->gazebo_topic().length(),
      ::google::protobuf::internal::WireFormat::SERIALIZE,
      "gz_std_msgs.ConnectGazeboToRosTopic.gazebo_topic");
    ::google::protobuf::internal::WireFormatLite::WriteStringMaybeAliased(
      2, this->gazebo_topic(), output);
  }

  // required string ros_topic = 3;
  if (has_ros_topic()) {
    ::google::protobuf::internal::WireFormat::VerifyUTF8StringNamedField(
      this->ros_topic().data(), this->ros_topic().length(),
      ::google::protobuf::internal::WireFormat::SERIALIZE,
      "gz_std_msgs.ConnectGazeboToRosTopic.ros_topic");
    ::google::protobuf::internal::WireFormatLite::WriteStringMaybeAliased(
      3, this->ros_topic(), output);
  }

  // required .gz_std_msgs.ConnectGazeboToRosTopic.MsgType msgType = 4;
  if (has_msgtype()) {
    ::google::protobuf::internal::WireFormatLite::WriteEnum(
      4, this->msgtype(), output);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        unknown_fields(), output);
  }
  // @@protoc_insertion_point(serialize_end:gz_std_msgs.ConnectGazeboToRosTopic)
}

::google::protobuf::uint8* ConnectGazeboToRosTopic::InternalSerializeWithCachedSizesToArray(
    bool deterministic, ::google::protobuf::uint8* target) const {
  // @@protoc_insertion_point(serialize_to_array_start:gz_std_msgs.ConnectGazeboToRosTopic)
  // required string gazebo_topic = 2;
  if (has_gazebo_topic()) {
    ::google::protobuf::internal::WireFormat::VerifyUTF8StringNamedField(
      this->gazebo_topic().data(), this->gazebo_topic().length(),
      ::google::protobuf::internal::WireFormat::SERIALIZE,
      "gz_std_msgs.ConnectGazeboToRosTopic.gazebo_topic");
    target =
      ::google::protobuf::internal::WireFormatLite::WriteStringToArray(
        2, this->gazebo_topic(), target);
  }

  // required string ros_topic = 3;
  if (has_ros_topic()) {
    ::google::protobuf::internal::WireFormat::VerifyUTF8StringNamedField(
      this->ros_topic().data(), this->ros_topic().length(),
      ::google::protobuf::internal::WireFormat::SERIALIZE,
      "gz_std_msgs.ConnectGazeboToRosTopic.ros_topic");
    target =
      ::google::protobuf::internal::WireFormatLite::WriteStringToArray(
        3, this->ros_topic(), target);
  }

  // required .gz_std_msgs.ConnectGazeboToRosTopic.MsgType msgType = 4;
  if (has_msgtype()) {
    target = ::google::protobuf::internal::WireFormatLite::WriteEnumToArray(
      4, this->msgtype(), target);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        unknown_fields(), target);
  }
  // @@protoc_insertion_point(serialize_to_array_end:gz_std_msgs.ConnectGazeboToRosTopic)
  return target;
}

int ConnectGazeboToRosTopic::RequiredFieldsByteSizeFallback() const {
// @@protoc_insertion_point(required_fields_byte_size_fallback_start:gz_std_msgs.ConnectGazeboToRosTopic)
  int total_size = 0;

  if (has_gazebo_topic()) {
    // required string gazebo_topic = 2;
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::StringSize(
        this->gazebo_topic());
  }

  if (has_ros_topic()) {
    // required string ros_topic = 3;
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::StringSize(
        this->ros_topic());
  }

  if (has_msgtype()) {
    // required .gz_std_msgs.ConnectGazeboToRosTopic.MsgType msgType = 4;
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::EnumSize(this->msgtype());
  }

  return total_size;
}
int ConnectGazeboToRosTopic::ByteSize() const {
// @@protoc_insertion_point(message_byte_size_start:gz_std_msgs.ConnectGazeboToRosTopic)
  int total_size = 0;

  if (((_has_bits_[0] & 0x00000007) ^ 0x00000007) == 0) {  // All required fields are present.
    // required string gazebo_topic = 2;
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::StringSize(
        this->gazebo_topic());

    // required string ros_topic = 3;
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::StringSize(
        this->ros_topic());

    // required .gz_std_msgs.ConnectGazeboToRosTopic.MsgType msgType = 4;
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::EnumSize(this->msgtype());

  } else {
    total_size += RequiredFieldsByteSizeFallback();
  }
  if (_internal_metadata_.have_unknown_fields()) {
    total_size +=
      ::google::protobuf::internal::WireFormat::ComputeUnknownFieldsSize(
        unknown_fields());
  }
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = total_size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
  return total_size;
}

void ConnectGazeboToRosTopic::MergeFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:gz_std_msgs.ConnectGazeboToRosTopic)
  if (GOOGLE_PREDICT_FALSE(&from == this)) {
    ::google::protobuf::internal::MergeFromFail(__FILE__, __LINE__);
  }
  const ConnectGazeboToRosTopic* source = 
      ::google::protobuf::internal::DynamicCastToGenerated<const ConnectGazeboToRosTopic>(
          &from);
  if (source == NULL) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:gz_std_msgs.ConnectGazeboToRosTopic)
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:gz_std_msgs.ConnectGazeboToRosTopic)
    MergeFrom(*source);
  }
}

void ConnectGazeboToRosTopic::MergeFrom(const ConnectGazeboToRosTopic& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:gz_std_msgs.ConnectGazeboToRosTopic)
  if (GOOGLE_PREDICT_FALSE(&from == this)) {
    ::google::protobuf::internal::MergeFromFail(__FILE__, __LINE__);
  }
  if (from._has_bits_[0 / 32] & (0xffu << (0 % 32))) {
    if (from.has_gazebo_topic()) {
      set_has_gazebo_topic();
      gazebo_topic_.AssignWithDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), from.gazebo_topic_);
    }
    if (from.has_ros_topic()) {
      set_has_ros_topic();
      ros_topic_.AssignWithDefault(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), from.ros_topic_);
    }
    if (from.has_msgtype()) {
      set_msgtype(from.msgtype());
    }
  }
  if (from._internal_metadata_.have_unknown_fields()) {
    mutable_unknown_fields()->MergeFrom(from.unknown_fields());
  }
}

void ConnectGazeboToRosTopic::CopyFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:gz_std_msgs.ConnectGazeboToRosTopic)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void ConnectGazeboToRosTopic::CopyFrom(const ConnectGazeboToRosTopic& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:gz_std_msgs.ConnectGazeboToRosTopic)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool ConnectGazeboToRosTopic::IsInitialized() const {
  if ((_has_bits_[0] & 0x00000007) != 0x00000007) return false;

  return true;
}

void ConnectGazeboToRosTopic::Swap(ConnectGazeboToRosTopic* other) {
  if (other == this) return;
  InternalSwap(other);
}
void ConnectGazeboToRosTopic::InternalSwap(ConnectGazeboToRosTopic* other) {
  gazebo_topic_.Swap(&other->gazebo_topic_);
  ros_topic_.Swap(&other->ros_topic_);
  std::swap(msgtype_, other->msgtype_);
  std::swap(_has_bits_[0], other->_has_bits_[0]);
  _internal_metadata_.Swap(&other->_internal_metadata_);
  std::swap(_cached_size_, other->_cached_size_);
}

::google::protobuf::Metadata ConnectGazeboToRosTopic::GetMetadata() const {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::Metadata metadata;
  metadata.descriptor = ConnectGazeboToRosTopic_descriptor_;
  metadata.reflection = ConnectGazeboToRosTopic_reflection_;
  return metadata;
}

#if PROTOBUF_INLINE_NOT_IN_HEADERS
// ConnectGazeboToRosTopic

// required string gazebo_topic = 2;
bool ConnectGazeboToRosTopic::has_gazebo_topic() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
void ConnectGazeboToRosTopic::set_has_gazebo_topic() {
  _has_bits_[0] |= 0x00000001u;
}
void ConnectGazeboToRosTopic::clear_has_gazebo_topic() {
  _has_bits_[0] &= ~0x00000001u;
}
void ConnectGazeboToRosTopic::clear_gazebo_topic() {
  gazebo_topic_.ClearToEmptyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  clear_has_gazebo_topic();
}
 const ::std::string& ConnectGazeboToRosTopic::gazebo_topic() const {
  // @@protoc_insertion_point(field_get:gz_std_msgs.ConnectGazeboToRosTopic.gazebo_topic)
  return gazebo_topic_.GetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
 void ConnectGazeboToRosTopic::set_gazebo_topic(const ::std::string& value) {
  set_has_gazebo_topic();
  gazebo_topic_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), value);
  // @@protoc_insertion_point(field_set:gz_std_msgs.ConnectGazeboToRosTopic.gazebo_topic)
}
 void ConnectGazeboToRosTopic::set_gazebo_topic(const char* value) {
  set_has_gazebo_topic();
  gazebo_topic_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::string(value));
  // @@protoc_insertion_point(field_set_char:gz_std_msgs.ConnectGazeboToRosTopic.gazebo_topic)
}
 void ConnectGazeboToRosTopic::set_gazebo_topic(const char* value, size_t size) {
  set_has_gazebo_topic();
  gazebo_topic_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(),
      ::std::string(reinterpret_cast<const char*>(value), size));
  // @@protoc_insertion_point(field_set_pointer:gz_std_msgs.ConnectGazeboToRosTopic.gazebo_topic)
}
 ::std::string* ConnectGazeboToRosTopic::mutable_gazebo_topic() {
  set_has_gazebo_topic();
  // @@protoc_insertion_point(field_mutable:gz_std_msgs.ConnectGazeboToRosTopic.gazebo_topic)
  return gazebo_topic_.MutableNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
 ::std::string* ConnectGazeboToRosTopic::release_gazebo_topic() {
  // @@protoc_insertion_point(field_release:gz_std_msgs.ConnectGazeboToRosTopic.gazebo_topic)
  clear_has_gazebo_topic();
  return gazebo_topic_.ReleaseNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
 void ConnectGazeboToRosTopic::set_allocated_gazebo_topic(::std::string* gazebo_topic) {
  if (gazebo_topic != NULL) {
    set_has_gazebo_topic();
  } else {
    clear_has_gazebo_topic();
  }
  gazebo_topic_.SetAllocatedNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), gazebo_topic);
  // @@protoc_insertion_point(field_set_allocated:gz_std_msgs.ConnectGazeboToRosTopic.gazebo_topic)
}

// required string ros_topic = 3;
bool ConnectGazeboToRosTopic::has_ros_topic() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
void ConnectGazeboToRosTopic::set_has_ros_topic() {
  _has_bits_[0] |= 0x00000002u;
}
void ConnectGazeboToRosTopic::clear_has_ros_topic() {
  _has_bits_[0] &= ~0x00000002u;
}
void ConnectGazeboToRosTopic::clear_ros_topic() {
  ros_topic_.ClearToEmptyNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
  clear_has_ros_topic();
}
 const ::std::string& ConnectGazeboToRosTopic::ros_topic() const {
  // @@protoc_insertion_point(field_get:gz_std_msgs.ConnectGazeboToRosTopic.ros_topic)
  return ros_topic_.GetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
 void ConnectGazeboToRosTopic::set_ros_topic(const ::std::string& value) {
  set_has_ros_topic();
  ros_topic_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), value);
  // @@protoc_insertion_point(field_set:gz_std_msgs.ConnectGazeboToRosTopic.ros_topic)
}
 void ConnectGazeboToRosTopic::set_ros_topic(const char* value) {
  set_has_ros_topic();
  ros_topic_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), ::std::string(value));
  // @@protoc_insertion_point(field_set_char:gz_std_msgs.ConnectGazeboToRosTopic.ros_topic)
}
 void ConnectGazeboToRosTopic::set_ros_topic(const char* value, size_t size) {
  set_has_ros_topic();
  ros_topic_.SetNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(),
      ::std::string(reinterpret_cast<const char*>(value), size));
  // @@protoc_insertion_point(field_set_pointer:gz_std_msgs.ConnectGazeboToRosTopic.ros_topic)
}
 ::std::string* ConnectGazeboToRosTopic::mutable_ros_topic() {
  set_has_ros_topic();
  // @@protoc_insertion_point(field_mutable:gz_std_msgs.ConnectGazeboToRosTopic.ros_topic)
  return ros_topic_.MutableNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
 ::std::string* ConnectGazeboToRosTopic::release_ros_topic() {
  // @@protoc_insertion_point(field_release:gz_std_msgs.ConnectGazeboToRosTopic.ros_topic)
  clear_has_ros_topic();
  return ros_topic_.ReleaseNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited());
}
 void ConnectGazeboToRosTopic::set_allocated_ros_topic(::std::string* ros_topic) {
  if (ros_topic != NULL) {
    set_has_ros_topic();
  } else {
    clear_has_ros_topic();
  }
  ros_topic_.SetAllocatedNoArena(&::google::protobuf::internal::GetEmptyStringAlreadyInited(), ros_topic);
  // @@protoc_insertion_point(field_set_allocated:gz_std_msgs.ConnectGazeboToRosTopic.ros_topic)
}

// required .gz_std_msgs.ConnectGazeboToRosTopic.MsgType msgType = 4;
bool ConnectGazeboToRosTopic::has_msgtype() const {
  return (_has_bits_[0] & 0x00000004u) != 0;
}
void ConnectGazeboToRosTopic::set_has_msgtype() {
  _has_bits_[0] |= 0x00000004u;
}
void ConnectGazeboToRosTopic::clear_has_msgtype() {
  _has_bits_[0] &= ~0x00000004u;
}
void ConnectGazeboToRosTopic::clear_msgtype() {
  msgtype_ = 0;
  clear_has_msgtype();
}
 ::gz_std_msgs::ConnectGazeboToRosTopic_MsgType ConnectGazeboToRosTopic::msgtype() const {
  // @@protoc_insertion_point(field_get:gz_std_msgs.ConnectGazeboToRosTopic.msgType)
  return static_cast< ::gz_std_msgs::ConnectGazeboToRosTopic_MsgType >(msgtype_);
}
 void ConnectGazeboToRosTopic::set_msgtype(::gz_std_msgs::ConnectGazeboToRosTopic_MsgType value) {
  assert(::gz_std_msgs::ConnectGazeboToRosTopic_MsgType_IsValid(value));
  set_has_msgtype();
  msgtype_ = value;
  // @@protoc_insertion_point(field_set:gz_std_msgs.ConnectGazeboToRosTopic.msgType)
}

#endif  // PROTOBUF_INLINE_NOT_IN_HEADERS

// @@protoc_insertion_point(namespace_scope)

}  // namespace gz_std_msgs

// @@protoc_insertion_point(global_scope)
