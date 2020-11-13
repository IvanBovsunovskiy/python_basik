class Warehouse:
    equipment_quantity = []  # '[{"printer": 10},{"scanner": 2}]'
    equipment_location = []  # '[{"printer": "10b"},{"scanner": "3c"}]'
    pass


class OfficeEquipment:
    mass = None
    quantity = None
    power_consumption = None


class Printer(OfficeEquipment):
    print_speed = None


class Scanner(OfficeEquipment):
    scanning_resolution = None
