import struct
from enum import Enum
from typing import Any, List, Type

from .memory_reader import MemoryReader
from .handler import HookHandler
from wizwalker.utils import XYZ
from wizwalker.errors import ReadingEnumFailed


# # TODO: figure out what other 8 bytes are
# class SharedPointer:
#     def __init__(self, entry_bytes: bytes):
#         self.pointed_address: int = struct.unpack("<q", entry_bytes[:8])[0]


class MemoryObject(MemoryReader):
    """
    Class for any represented classes from memory
    """

    def __init__(self, hook_handler: HookHandler):
        super().__init__(hook_handler.process)
        self.hook_handler = hook_handler

    async def read_base_address(self) -> int:
        raise NotImplementedError()

    async def read_value_from_offset(self, offset: int, data_type: str) -> Any:
        base_address = await self.read_base_address()
        return await self.read_typed(base_address + offset, data_type)

    async def write_value_to_offset(self, offset: int, value: Any, data_type: str):
        base_address = await self.read_base_address()
        await self.write_typed(base_address + offset, value, data_type)

    async def read_xyz(self, offset: int) -> XYZ:
        base_address = await self.read_base_address()
        position_bytes = await self.read_bytes(base_address + offset, 12)
        x, y, z = struct.unpack("<fff", position_bytes)
        return XYZ(x, y, z)

    async def write_xyz(self, offset: int, xyz: XYZ):
        base_address = await self.read_base_address()
        packed_position = struct.pack("<fff", *xyz)
        await self.write_bytes(base_address + offset, packed_position)

    async def read_enum(self, offset, enum: Type[Enum]):
        value = await self.read_value_from_offset(offset, "int")
        try:
            res = enum(value)
        except ValueError:
            raise ReadingEnumFailed(enum, value)
        else:
            return res

    async def write_enum(self, offset, value: Enum):
        await self.write_value_to_offset(offset, value.value, "int")


class DynamicMemoryObject(MemoryObject):
    def __init__(self, hook_handler: HookHandler, base_address: int):
        super().__init__(hook_handler)
        self.base_address = base_address

    async def read_base_address(self) -> int:
        return self.base_address