def has_enough_energy(energy_available, distance_one_way, meters_per_energy):

    energy_needed = (distance_one_way / meters_per_energy) * 2

    if (energy_needed <= energy_available):
        return True
    else:
        return False



