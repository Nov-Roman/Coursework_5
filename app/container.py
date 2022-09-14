from resourses.arena.arena import Arena
from resourses.equipment.equipment import Equipment
from resourses.skills.ferocious_kick import FerociousKick
from resourses.skills.powerful_thrust import PowerfulThrust
from resourses.unit_class import UnitClass


"""Создание экземпляров"""
arena = Arena()
equipment = Equipment()

heroes = {
    "player": None,
    "enemy": None
}

"""Создание экземпляра двух героев"""
WarriorClass = UnitClass(
    name="Воин",
    max_health=30.0,
    max_stamina=30.0,
    damage_modifier=1.1,
    stamina_modifier=1.1,
    armor_modifier=1.1,
    skill=FerociousKick()
)

ThiefClass = UnitClass(
    name="Вор",
    max_health=30.0,
    max_stamina=30.0,
    damage_modifier=0.9,
    stamina_modifier=1.1,
    armor_modifier=1.2,
    skill=PowerfulThrust()
)

unit_classes = {
    WarriorClass.name: WarriorClass,
    ThiefClass.name: ThiefClass
}
