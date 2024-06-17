""" Module categories 

    

    Created on 14/06/2024
    By Jean-Marc Le Peuvédic
    © CalCool Studios SAS 2021-2024
"""
# TODO List

# Import system libraries
from enum import Enum
from itertools import accumulate


# Import public libraries

# Import application modules

class Category:
    """ Impact categorization is useful, but there is no natural standard. This class offers in internal
        categorization scheme which can be translated into commonly used published category nomenclatures
        like BEGESv4, BEGESv5, GHG Protocol or ISO/TR 14067.
    """
    class GoodsOrService(Enum):
        """ Goods or service: 1 bit """
        GOODS = 0
        SERVICE = 1
    
    class FinancialControl(Enum):
        """ Type of financial control: 2 bits """
        OWNED = 0
        OPERATING_LEASE = 2
        FINANCE_CAPITAL_LEASE = 2
        SUBCONTRACTED_WORK = 3
        
    class LifecyclePhase(Enum):
        """ Life-cycle phase: 3 bits """
        RAW_MATERIAL_EXTRACTION = 0
        MATERIAL_PROCESSING_MANUFACTURE = 1
        DISTRIBUTION_TRANSPORTATION = 2
        COMMISSIONING = 3
        USE_SERVICE_PHASE = 4
        ASSET_USE_OPERATION = 5
        ASSET_END_OF_LIFE = 6
        CARBON_ABSORBING = 7
        
    class OperationScope(Enum):
        """ The operation aspect: upstream, own operations, downstream.
            Taking into account suppliers being paid to work on delivered products, or waste: 2 bits """
        OWN_OPERATIONS = 0
        SUPPLIER_RELATED = 1
        CUSTOMER_RELATED = 2
        SUPPLIER_DOWNSTREAM = 3
        
    class NatureOfOperation(Enum):
        """ Some categories are wide, others are narrow but they represent significant emissions: 4 bits """
        TRANSPORTATION_OPERATION = 0
        WASTE = 1
        HEATING = 2
        RESIDENTIAL_COOKING = 3
        SANITARY_HOT_WATER = 4
        STREET_LIGHTING = 5
        HOUSEHOLD_LIGHTING = 6
        COOLING = 7
        GENERIC_INDUSTRIAL_ACTIVITY = 8
        FIXED_INDUSTRIAL_HEAT_SOURCE = 9
        FIXED_THERMAL_ENGINE = 10
        CHEMICAL_SYNTHESIS = 11
        RESERVED_12 = 12
        RESERVED_13 = 13
        RESERVED_14 = 14
        RESERVED_15 = 15
        
    class Biomass(Enum):
        """ Degree of dependence on fossil sources: 2 bits. """
        FOSSIL_SOURCES = 0
        BIOMASS_RELATED_EMISSIONS = 1
        MIXED_SOURCE_FUEL = 2
        LOCAL_ELECTRIC_MIX = 3
    
    @staticmethod
    def _get_enum_value(packed_value, bit_position, num_bits):
        return (packed_value >> bit_position) & ((1 << num_bits) - 1)
        
    max_values = {
        'is_service'       : 1,  # 1 bit
        'financial_control': 3,  # 2 bits
        'life_cycle_phase' : 7,  # 3 bits
        'ownership'        : 3,  # 2 bits
        'operation_nature' : 15,  # 4 bits
        'process_emissions': 3,  # 2 bits
        'biomass_source'   : 3,  # 2 bits
    }
    
    _iterator = accumulate(max_values.items(), lambda a, v: (v[0], a[1]+v[1]), initial=("",0))
    bit_position = {field: position for field, position in _iterator}
    
    @staticmethod
    def pack_enums(is_service, financial_control, life_cycle_phase, ownership, operation_nature, process_emissions,
                   biomass_source):
        # Values packed into
        values = {
            'is_service'       : is_service,
            'financial_control': financial_control,
            'life_cycle_phase' : life_cycle_phase,
            'ownership'        : ownership,
            'operation_nature' : operation_nature,
            'process_emissions': process_emissions,
            'biomass_source'   : biomass_source,
        }
        
        # Validate each value does not exceed maximum
        for key, value in values.items():
            if value < 0 or value > Category.max_values[key]:
                raise ValueError(f"{key} value of {value} exceeds limit of {max_values[key]}")
        
        # Bitwise packing
        result = is_service
        result |= (financial_control << 1)
        result |= (life_cycle_phase << 3)
        result |= (ownership << 6)
        result |= (operation_nature << 8)
        result |= (process_emissions << 12)
        result |= (biomass_source << 14)
        
        return result


