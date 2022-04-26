class FormattedMoveData:
    def __init__(self, _input, move, damage, guard, invincibility, startup,
                 block, hit, active, recovery, counter, level, prorate):
        self.input = _input
        self.move = move
        self.damage = damage
        self.guard = guard
        self.invincibility = invincibility
        self.startup = startup
        self.block = block
        self.hit = hit
        self.active = active
        self.recovery = recovery
        self.counter = counter
        self.level = level
        self.prorate = prorate

    def __str__(self):
        return f"Input: {self.input} Name: {self.move}, Damage: {self.damage}, Guard: {self.guard}, " \
               f"Invincibility: {self.invincibility}, " \
               f"Start up: {self.startup}, On Block: {self.block}, On Hit: {self.hit}, Active frames: {self.active}, " \
               f"Recovery Frames: {self.recovery}, Counter Hit: {self.counter}, Attack Level: {self.level}, " \
               f"Proration: {self.prorate}"
