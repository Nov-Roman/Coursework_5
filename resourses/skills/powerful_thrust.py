from resourses.skills.base_skill import BaseSkill


class PowerfulThrust(BaseSkill):
    """Конкретный экземпляр навыка"""
    name: str = "Мощный укол"
    stamina_required: float = 5.0
    damage: float = 15.0

    def skill_effect(self) -> str:
        self.user.stamina_points_ -= self.stamina_required
        self.target.health_points_ -= self.damage
        return f"{self.user.name} применил умение {self.name} и нанес {self.damage} урона по {self.target.name}"
