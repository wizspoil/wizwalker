from wizwalker.memory.memory_object import MemoryObject, DynamicMemoryObject


class CamView(MemoryObject):
    # TODO: Find real name (or more fitting)
    async def read_base_address(self) -> int:
        raise NotImplementedError()    

    async def view_matrix(self) -> list[float]:
        return list(await self.read_vector(80, 9))

    async def write_view_matrix(self, values: list[float]):
        await self.write_vector(80, tuple(values), 9)

    async def cull_near(self) -> float:
        return await self.read_value_from_offset(304, "float")
    
    async def write_cull_near(self, value: float):
        await self.write_value_to_offset(304, value, "float")

    async def cull_far(self) -> float:
        return await self.read_value_from_offset(308, "float")
    
    async def write_cull_far(self, value: float):
        await self.write_value_to_offset(308, value, "float")

    async def base_cull_near(self) -> float:
        return await self.read_value_from_offset(316, "float")
    
    async def write_base_cull_near(self, value: float):
        await self.write_value_to_offset(316, value, "float")

    async def base_cull_far(self) -> float:
        return await self.read_value_from_offset(320, "float")
    
    async def write_base_cull_far(self, value: float):
        await self.write_value_to_offset(320, value, "float")

    async def viewport_left(self) -> float:
        return await self.read_value_from_offset(288, "float")
    
    async def write_viewport_left(self, value: float):
        await self.write_value_to_offset(288, value, "float")

    async def viewport_right(self) -> float:
        return await self.read_value_from_offset(292, "float")
    
    async def write_viewport_right(self, value: float):
        await self.write_value_to_offset(292, value, "float")

    async def viewport_top(self) -> float:
        return await self.read_value_from_offset(296, "float")
    
    async def write_viewport_top(self, value: float):
        await self.write_value_to_offset(296, value, "float")

    async def viewport_bottom(self) -> float:
        return await self.read_value_from_offset(300, "float")
    
    async def write_viewport_bottom(self, value: float):
        await self.write_value_to_offset(300, value, "float")

    async def screenport_left(self) -> float:
        return await self.read_value_from_offset(324, "float")
    
    async def write_screenport_left(self, value: float):
        await self.write_value_to_offset(324, value, "float")

    async def screenport_right(self) -> float:
        return await self.read_value_from_offset(328, "float")
    
    async def write_screenport_right(self, value: float):
        await self.write_value_to_offset(328, value, "float")

    async def screenport_top(self) -> float:
        return await self.read_value_from_offset(332, "float")
    
    async def write_screenport_top(self, value: float):
        await self.write_value_to_offset(332, value, "float")

    async def screenport_bottom(self) -> float:
        return await self.read_value_from_offset(336, "float")
    
    async def write_screenport_bottom(self, value: float):
        await self.write_value_to_offset(336, value, "float")


class DynamicCamView(DynamicMemoryObject, CamView):
    pass
