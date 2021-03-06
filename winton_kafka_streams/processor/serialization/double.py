from ._serde import extract_config_property
from ._deserializer import Deserializer
from ._serializer import Serializer
import struct


class DoubleSerializer(Serializer):
    def serialize(self, topic, data):
        return struct.pack('d', data)

    def configure(self, configs, is_key):
        pass

    def close(self):
        pass


class DoubleDeserializer(Deserializer):
    def deserialize(self, topic, data):
        return struct.unpack('d', data)[0]

    def configure(self, configs, is_key):
        pass

    def close(self):
        pass
