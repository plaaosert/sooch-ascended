import time

import buildings

class Player:
    def __init__(self, discord_id, name, sooch, tsooch, csooch, last_claim, ascension_level, transcension_level, consolidation_level, total_eaten):
        # Regular constructor uses only static data.
        self.discord_id = discord_id
        self.name = name
        self.sooch = sooch
        self.tsooch = tsooch
        self.csooch = csooch
        self.last_claim = last_claim
        self.ascension_level = ascension_level
        self.transcension_level = transcension_level
        self.consolidation_level = consolidation_level

        self.total_eaten = total_eaten

        self.buildings = {}
        self.t_buildings = {}
        self.c_buildings = {}
        self.c_talents = {}

        self.inventory = {}
        self.effects = {}

        self.income = -1

        self.needs_recalculation = False

    def get_income(self):
        if self.needs_recalculation:
            print("Recalculated income")
            self.calculate_income()

        return self.income

    def calculate_income(self):
        base_income = sum(buildings.building_data[b[0]] * b[1] for b in self.buildings.values())

        # apply bonuses here...

        self.income = base_income

    def is_claimable(self):
        if time.time() - self.last_claim > 30:
            return True



    def add_building_info(self, buildings):
        self.buildings = buildings

    def add_tbuilding_info(self, t_buildings):
        self.t_buildings = t_buildings

    def add_cbuilding_info(self, c_buildings):
        self.c_buildings = c_buildings

    def add_inventory(self, inventory):
        self.inventory = inventory

    def add_effects(self, effects):
        self.effects = effects

    def add_ctalents(self, c_talents):
        self.c_talents = c_talents
