from typing import List, Optional

from wizwalker.memory.memory_object import DynamicMemoryObject, PropertyClass
from .enums import DelayOrder, SpellSourceType

from .spell_effect import DynamicSpellEffect, get_spell_effects
from .spell_rank import DynamicSpellRank


class SpellTemplate(PropertyClass):
    async def read_base_address(self) -> int:
        raise NotImplementedError()

    # async def behaviors(self) -> class BehaviorTemplate*:
    #     return await self.read_value_from_offset(72, "class BehaviorTemplate*")

    async def name(self) -> str:
        return await self.read_string_from_offset(96)

    async def write_name(self, name: str):
        await self.write_string_to_offset(96, name)

    async def description(self) -> str:
        return await self.read_string_from_offset(168)

    async def write_description(self, description: str):
        await self.write_string_to_offset(168, description)

    async def display_name(self) -> str:
        return await self.read_string_from_offset(136)

    async def write_display_name(self, display_name: str):
        await self.write_string_to_offset(136, display_name)

    async def spell_base(self) -> str:
        return await self.read_string_from_offset(248)

    async def write_spell_base(self, spell_base: str):
        await self.write_string_to_offset(248, spell_base)

    async def effects(self) -> List[DynamicSpellEffect]:
        return await get_spell_effects(self, 280)

    async def magic_school_name(self) -> str:
        return await self.read_string_from_offset(312)

    async def write_magic_school_name(self, magic_school_name: str):
        await self.write_string_to_offset(312, magic_school_name)

    async def type_name(self) -> str:
        return await self.read_string_from_offset(352)

    async def write_type_name(self, type_name: str):
        await self.write_string_to_offset(352, type_name)

    async def training_cost(self) -> int:
        return await self.read_value_from_offset(384, "int")

    async def write_training_cost(self, training_cost: int):
        await self.write_value_to_offset(384, training_cost, "int")

    async def accuracy(self) -> int:
        return await self.read_value_from_offset(388, "int")

    async def write_accuracy(self, accuracy: int):
        await self.write_value_to_offset(388, accuracy, "int")

    async def base_cost(self) -> int:
        return await self.read_value_from_offset(232, "int")

    async def write_base_cost(self, base_cost: int):
        await self.write_value_to_offset(232, base_cost, "int")

    async def credits_cost(self) -> int:
        return await self.read_value_from_offset(236, "int")

    async def write_credits_cost(self, credits_cost: int):
        await self.write_value_to_offset(236, credits_cost, "int")

    async def pvp_currency_cost(self) -> int:
        return await self.read_value_from_offset(240, "int")

    async def write_pvp_currency_cost(self, cost: int):
        await self.write_value_to_offset(240, cost, "int")

    async def booster_pack_icon(self) -> str:
        return await self.read_string_from_offset(496)

    async def write_booster_pack_icon(self, booster_pack_icon: str):
        await self.write_string_to_offset(496, booster_pack_icon)

    async def valid_target_spells(self) -> int:
        return await self.read_value_from_offset(392, "unsigned int")

    async def write_valid_target_spells(self, valid_target_spells: int):
        await self.write_value_to_offset(392, valid_target_spells, "unsigned int")

    async def pvp(self) -> bool:
        return await self.read_value_from_offset(408, "bool")

    async def write_pvp(self, pvp: bool):
        await self.write_value_to_offset(408, pvp, "bool")

    async def pve(self) -> bool:
        return await self.read_value_from_offset(409, "bool")

    async def write_pve(self, pve: bool):
        await self.write_value_to_offset(409, pve, "bool")

    async def no_pvp_enchant(self) -> bool:
        return await self.read_value_from_offset(410, "bool")

    async def write_no_pvp_enchant(self, no_pvp_enchant: bool):
        await self.write_value_to_offset(410, no_pvp_enchant, "bool")

    async def no_pve_enchant(self) -> bool:
        return await self.read_value_from_offset(411, "bool")

    async def write_no_pve_enchant(self, no_pve_enchant: bool):
        await self.write_value_to_offset(411, no_pve_enchant, "bool")

    async def battlegrounds_only(self) -> bool:
        return await self.read_value_from_offset(412, "bool")

    async def write_battlegrounds_only(self, battlegrounds_only: bool):
        await self.write_value_to_offset(412, battlegrounds_only, "bool")

    async def treasure(self) -> bool:
        return await self.read_value_from_offset(413, "bool")

    async def write_treasure(self, treasure: bool):
        await self.write_value_to_offset(413, treasure, "bool")

    async def no_discard(self) -> bool:
        return await self.read_value_from_offset(414, "bool")

    async def write_no_discard(self, no_discard: bool):
        await self.write_value_to_offset(414, no_discard, "bool")

    async def leaves_play_when_cast(self) -> bool:
        return await self.read_value_from_offset(532, "bool")

    async def write_leaves_play_when_cast(self, leaves_play_when_cast: bool):
        await self.write_value_to_offset(532, leaves_play_when_cast, "bool")

    async def image_index(self) -> int:
        return await self.read_value_from_offset(416, "int")

    async def write_image_index(self, image_index: int):
        await self.write_value_to_offset(416, image_index, "int")

    async def image_name(self) -> str:
        return await self.read_string_from_offset(424)

    async def write_image_name(self, image_name: str):
        await self.write_string_to_offset(424, image_name)

    async def cloaked(self) -> bool:
        return await self.read_value_from_offset(489, "bool")

    async def write_cloaked(self, cloaked: bool):
        await self.write_value_to_offset(489, cloaked, "bool")

    async def caster_invisible(self) -> bool:
        return await self.read_value_from_offset(490, "bool")

    async def write_caster_invisible(self, caster_invisible: bool):
        await self.write_value_to_offset(490, caster_invisible, "bool")

    async def adjectives(self) -> str:
        return await self.read_string_from_offset(576)

    async def write_adjectives(self, adjectives: str):
        await self.write_string_to_offset(576, adjectives)

    async def spell_source_type(self) -> SpellSourceType:
        return await self.read_enum(528, SpellSourceType)

    async def write_spell_source_type(self, spell_source_type: SpellSourceType):
        await self.write_enum(528, spell_source_type)

    async def cloaked_name(self) -> str:
        return await self.read_string_from_offset(536)

    async def write_cloaked_name(self, cloaked_name: str):
        await self.write_string_to_offset(536, cloaked_name)

    # async def purchase_requirements(self) -> class RequirementList*:
    #     return await self.read_value_from_offset(576, "class RequirementList*")

    async def description_trainer(self) -> str:
        return await self.read_string_from_offset(616)

    async def write_description_trainer(self, description_trainer: str):
        await self.write_string_to_offset(616, description_trainer)

    async def description_combat_hud(self) -> str:
        return await self.read_string_from_offset(648)

    async def write_description_combat_hud(self, description_combat_hud: str):
        await self.write_string_to_offset(648, description_combat_hud)

    async def display_index(self) -> int:
        return await self.read_value_from_offset(680, "int")

    async def write_display_index(self, display_index: int):
        await self.write_value_to_offset(680, display_index, "int")

    async def hidden_from_effects_window(self) -> bool:
        return await self.read_value_from_offset(684, "bool")

    async def write_hidden_from_effects_window(self, hidden_from_effects_window: bool):
        await self.write_value_to_offset(684, hidden_from_effects_window, "bool")

    async def ignore_charms(self) -> bool:
        return await self.read_value_from_offset(685, "bool")

    async def write_ignore_charms(self, ignore_charms: bool):
        await self.write_value_to_offset(685, ignore_charms, "bool")

    async def always_fizzle(self) -> bool:
        return await self.read_value_from_offset(686, "bool")

    async def write_always_fizzle(self, always_fizzle: bool):
        await self.write_value_to_offset(686, always_fizzle, "bool")

    async def spell_category(self) -> str:
        return await self.read_string_from_offset(688)

    async def write_spell_category(self, spell_category: str):
        await self.write_string_to_offset(688, spell_category)

    async def show_polymorphed_name(self) -> bool:
        return await self.read_value_from_offset(720, "bool")

    async def write_show_polymorphed_name(self, show_polymorphed_name: bool):
        await self.write_value_to_offset(720, show_polymorphed_name, "bool")

    async def skip_truncation(self) -> bool:
        return await self.read_value_from_offset(721, "bool")

    async def write_skip_truncation(self, skip_truncation: bool):
        await self.write_value_to_offset(721, skip_truncation, "bool")

    async def max_copies(self) -> int:
        return await self.read_value_from_offset(724, "unsigned int")

    async def write_max_copies(self, max_copies: int):
        await self.write_value_to_offset(724, max_copies, "unsigned int")

    async def level_restriction(self) -> int:
        return await self.read_value_from_offset(728, "int")

    async def write_level_restriction(self, level_restriction: int):
        await self.write_value_to_offset(728, level_restriction, "int")

    async def delay_enchantment(self) -> bool:
        return await self.read_value_from_offset(732, "bool")

    async def write_delay_enchantment(self, delay_enchantment: bool):
        await self.write_value_to_offset(732, delay_enchantment, "bool")

    async def delay_enchantment_order(self) -> DelayOrder:
        return await self.read_enum(736, DelayOrder)

    async def write_delay_enchantment_order(self, delay_enchantment_order: DelayOrder):
        await self.write_enum(736, delay_enchantment_order)

    async def previous_spell_name(self) -> str:
        return await self.read_string_from_offset(744)

    async def write_previous_spell_name(self, previous_spell_name: str):
        await self.write_string_to_offset(744, previous_spell_name)

    async def card_front(self) -> str:
        return await self.read_string_from_offset(456)

    async def write_card_front(self, card_front: str):
        await self.write_string_to_offset(456, card_front)

    async def use_gloss(self) -> bool:
        return await self.read_value_from_offset(488, "bool")

    async def write_use_gloss(self, use_gloss: bool):
        await self.write_value_to_offset(488, use_gloss, "bool")

    async def ignore_dispel(self) -> bool:
        return await self.read_value_from_offset(776, "bool")

    async def write_ignore_dispel(self, ignore_dispel: bool):
        await self.write_value_to_offset(776, ignore_dispel, "bool")

    async def backrow_friendly(self) -> bool:
        return await self.read_value_from_offset(777, "bool")

    async def write_backrow_friendly(self, backrow_friendly: bool):
        await self.write_value_to_offset(777, backrow_friendly, "bool")

    async def spell_rank(self) -> Optional[DynamicSpellRank]:
        addr = await self.read_value_from_offset(784, "long long")
        if addr == 0:
            return None

        return DynamicSpellRank(self.hook_handler, addr)

class DynamicSpellTemplate(DynamicMemoryObject, SpellTemplate):
    pass
