class BaseBuilding:
    def __init__(self, name, cost, costamp):
        self.name = name
        self.cost = cost
        self.costamp = costamp


class Building(BaseBuilding):
    def __init__(self, name, cost, income):
        super().__init__(name, cost, 1.2)

        self.income = income


class TransBuilding(BaseBuilding):
    def __init__(self, name, cost, function, costamp):
        super().__init__(name, cost, costamp)

        self.function = function


class ConsBuilding(BaseBuilding):
    def __init__(self, name, cost, function, costamp):
        super().__init__(name, cost, costamp)

        self.function = function


building_data = [
    Building("Farm",           1.00e+01,  6.00e+02),
    Building("BigFarm",        1.00e+02,  9.50e+02),
    Building("BiggerFarm",     2.50e+02,  1.75e+03),
    Building("HyperFarm",      1.00e+03,  5.60e+03),
    Building("TerraceFarm",    2.50e+03,  9.00e+03),
    Building("CubicFarm",      1.00e+04,  2.00e+04),
    Building("VerticalFarm",   6.00e+04,  7.00e+04),
    Building("HuntingLodge",   2.20e+05,  2.40e+05),
    Building("Bank",           1.00e+06,  1.00e+06),
    Building("BigBank",        5.00e+06,  5.50e+06),
    Building("InvestmentBank", 2.20e+07,  2.70e+07),
    Building("GlobalBank",     9.00e+07,  8.50e+07),
    Building("Village",        5.00e+08,  6.25e+08),
    Building("City",           5.00e+09,  5.00e+09),
    Building("Metropolis",     5.00e+10,  4.50e+10),
    Building("Mine",           1.00e+12,  8.00e+11),
    Building("MegaMine",       1.00e+13,  7.00e+12),
    Building("GigaMine",       1.00e+14,  6.00e+13),
    Building("ZettaMine",      1.00e+15,  4.50e+14),
    Building("CoreMine",       1.00e+16,  2.50e+15),
    Building("Workhouse",      1.00e+19,  1.90e+17),
    Building("Factory",        1.00e+21,  1.00e+19),
    Building("WorkForce",      1.00e+22,  9.00e+19),
    Building("FactoryState",   1.00e+24,  9.50e+21),
    Building("Nation",         1.00e+28,  4.50e+24),
    Building("Empire",         1.00e+31,  5.00e+27),
    Building("Dominion",       1.00e+34,  3.00e+30),
    Building("Control",        1.00e+37,  2.50e+33),
    Building("Aspect",         1.50e+40,  2.00e+37),
    Building("Divinity",       1.75e+43,  1.40e+39),
    Building("God",            2.00e+46,  1.20e+42),
    Building("Beyond",         2.50e+49,  7.00e+44),
    Building("Further",        2.75e+52,  3.00e+47),
    Building("Absolution",     3.00e+55,  1.50e+50),
    Building("TheEnd",         3.50e+58,  1.00e+53),
    Building("Dream",          3.75e+61,  7.50e+55),
    Building("DreamFarm",      6.50e+64,  5.50e+59),
    Building("DreamMine",      9.50e+67,  3.00e+62),
    Building("Hallucination",  2.95e+69,  1.70e+68),
    Building("FalseFarm",      2.45e+71,  1.50e+71),
    Building("FalseVillage",   2.25e+75,  1.30e+76),
    Building("FalseFactory",   1.50e+85,  1.10e+82),
    Building("Temple",         1.25e+100, 9.00e+93),
    Building("Monastery",      1.00e+110, 8.00e+102),
    Building("Altar",          9.20e+120, 7.00e+112),
    Building("FalseGod",       8.50e+130, 6.50e+120),
    Building("DreamGod",       7.25e+140, 5.50e+128),
    Building("Idolator",       6.50e+150, 3.50e+136),
    Building("HolyBook",       2.95e+160, 2.00e+141),
    Building("TrueGod",        1.25e+175, 1.00e+147),
    Building("FinalTruth",     1.00e+200, 1.00e+152)
]
