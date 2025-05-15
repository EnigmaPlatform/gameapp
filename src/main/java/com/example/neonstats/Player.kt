data class Stat(
    val name: String,
    var value: Int,
    var progress: Int = 0
)

class Player {
    var experience: Int = 0
    var experienceToNextLevel: Int = 100
    var level: Int = 1
    var talentPoints: Int = 0
    
    val stats = listOf(
        Stat("Сила", 1),
        Stat("Ловкость", 1),
        Stat("Интеллект", 1),
        Stat("Харизма", 1),
        Stat("Выносливость", 1)
    )
    
    fun addExperience(amount: Int) {
        experience += amount
        if (experience >= experienceToNextLevel) {
            levelUp()
        }
    }
    
    private fun levelUp() {
        level++
        talentPoints++
        experience -= experienceToNextLevel
        experienceToNextLevel = (experienceToNextLevel * 1.2).toInt()
    }
    
    fun upgradeStat(statName: String) {
        if (talentPoints > 0) {
            stats.find { it.name == statName }?.let {
                it.value++
                talentPoints--
            }
        }
    }
}
