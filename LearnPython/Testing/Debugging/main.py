def take_magic_damage(health, resist, amp, spell_power):

    max_damage = spell_power * amp
    damage_after_resist = max_damage - resist
    new_health = health - damage_after_resist

    return new_health
