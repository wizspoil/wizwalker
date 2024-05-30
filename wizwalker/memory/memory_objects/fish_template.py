from wizwalker.memory.memory_object import DynamicMemoryObject


class FishTemplate(DynamicMemoryObject):
    async def school_name(self) -> str:
        return await self.read_string_from_offset(0x80)

    async def rank(self) -> int:
        return await self.read_value_from_offset(0xA0, "int")

    async def size_min(self) -> float:
        return await self.read_value_from_offset(0xC8, "float")

    async def size_max(self) -> float:
        return await self.read_value_from_offset(0xCC, "float")

    async def is_sentinel(self) -> bool:
        return await self.read_value_from_offset(0xD0, "bool")

    async def bobber_submerge_ease(self) -> float:
        return await self.read_value_from_offset(0x108, "float")

    async def write_bobber_submerge_ease(self, val: float):
        ## At 1.0 the bobber is guaranteed to go down
        await self.write_value_to_offset(0x108, val, "float")
