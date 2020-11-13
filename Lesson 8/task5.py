class OfficeEquipment:
    name = None
    mass = None
    quantity = None
    power_consumption = None


class Printer(OfficeEquipment):
    name = 'printer'
    print_speed = None


class Scanner(OfficeEquipment):
    name = 'scanner'
    scanning_resolution = None


class Warehouse:
    equipment_quantity = [{}, {}]  # [{"printer": 10,"scanner": 2}, {}] [{warehouse}, {accounting}, {office}]

    def to_warehouse(self, equipment: OfficeEquipment, from_division: str):  # equipment = {'scanner': 10}
        """use positive numbers(equipment.quantity) of office equipment to add to warehouse or negative
        to add to current division"""
        check = True
        if len(self.equipment_quantity):
            for item in self.equipment_quantity[0]:
                if equipment.name == item:
                    self.equipment_quantity[0].update({item: self.equipment_quantity[0](item) + equipment.quantity})
                    if from_division == 'accounting':
                        self.equipment_quantity[1].update({item: self.equipment_quantity[1](item) - equipment.quantity})
                    elif from_division == 'office':
                        self.equipment_quantity[2].update({item: self.equipment_quantity[2](item) - equipment.quantity})
                    check = False
        elif check:
            self.equipment_quantity[0].update({equipment.name: equipment.quantity})
