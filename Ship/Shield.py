class Shield:

    def __init__(self):
        self.is_raised = False
        self.SHIELD_LEVEL_MAX = 10000
        self.shield_level = 4000

    def is_up(self):
        return self.is_raised

    def be_raised(self):
        self.is_raised = True

    def check_level(self):
        return self.shield_level

    def receive_energy(self, requested_energy):
        if self.shield_level + requested_energy > self.SHIELD_LEVEL_MAX:
            self.shield_level = self.SHIELD_LEVEL_MAX
        else:
            self.shield_level += requested_energy
