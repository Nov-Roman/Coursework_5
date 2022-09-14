from resourses.skills.base_skill import BaseSkill


class FerociousKick(BaseSkill):
    """Конкретный экземпляр навыка"""
    name: str = "Свирепый пинок"
    stamina_required: float = 6.0
    damage: float = 12.0

    def skill_effect(self) -> str:
        self.user.stamina_points_ -= self.stamina_required
        self.target.health_points_ -= self.damage
        return f"{self.user.name} применил умение {self.name} и нанес {self.damage} урона по {self.target.name}"
