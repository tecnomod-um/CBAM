from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

__NAMESPACE__ = "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1"


@dataclass
class AddressType:
    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 2,
            "max_length": 2,
        },
    )
    sub_division: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDivision",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    street: Optional[str] = field(
        default=None,
        metadata={
            "name": "Street",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 70,
        },
    )
    street_additional_line: Optional[str] = field(
        default=None,
        metadata={
            "name": "StreetAdditionalLine",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 70,
        },
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 35,
        },
    )
    postcode: Optional[str] = field(
        default=None,
        metadata={
            "name": "Postcode",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 17,
        },
    )
    pobox: Optional[str] = field(
        default=None,
        metadata={
            "name": "POBox",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class ApplicableMethodologyConfirmationType:
    other_applicable_reporting_methodology: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OtherApplicableReportingMethodology",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
        },
    )


@dataclass
class AttachmentType:
    filename: Optional[str] = field(
        default=None,
        metadata={
            "name": "Filename",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 2048,
        },
    )
    mime: Optional[str] = field(
        default=None,
        metadata={
            "name": "MIME",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 71,
        },
    )
    binary: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Binary",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "format": "base64",
        },
    )


@dataclass
class CommodityDetailsType:
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 512,
        },
    )


@dataclass
class ContactDetailsType:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    phone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 35,
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class DirectEmissionsType:
    determination_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeterminationType",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 5,
        },
    )
    determination_type_electricity: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeterminationTypeElectricity",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 5,
        },
    )
    applicable_reporting_type_methodology: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplicableReportingTypeMethodology",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        },
    )
    applicable_reporting_methodology: Optional[str] = field(
        default=None,
        metadata={
            "name": "ApplicableReportingMethodology",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 4000,
        },
    )
    specific_embedded_emissions: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SpecificEmbeddedEmissions",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "total_digits": 16,
            "fraction_digits": 7,
        },
    )
    other_source_indication: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherSourceIndication",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 4000,
        },
    )
    emission_factor_source_electricity: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmissionFactorSourceElectricity",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 5,
        },
    )
    emission_factor: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "EmissionFactor",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "total_digits": 16,
            "fraction_digits": 5,
        },
    )
    electricity_imported: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ElectricityImported",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
        },
    )
    total_embedded_electricity_imported: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TotalEmbeddedElectricityImported",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "total_digits": 16,
            "fraction_digits": 7,
        },
    )
    measurement_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "MeasurementUnit",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        },
    )
    emission_factor_source_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmissionFactorSourceValue",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 5000,
        },
    )
    conditionality_fulfillment: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConditionalityFulfillment",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 5000,
        },
    )


@dataclass
class ImportAreaType:
    import_area: Optional[str] = field(
        default=None,
        metadata={
            "name": "ImportArea",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        },
    )


@dataclass
class IndirectEmissionsType:
    determination_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeterminationType",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        },
    )
    emission_factor_source: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmissionFactorSource",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 5,
        },
    )
    emission_factor: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "EmissionFactor",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "total_digits": 16,
            "fraction_digits": 5,
        },
    )
    specific_embedded_emissions: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SpecificEmbeddedEmissions",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "total_digits": 16,
            "fraction_digits": 7,
        },
    )
    measurement_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "MeasurementUnit",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        },
    )
    electricity_consumed: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ElectricityConsumed",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "total_digits": 7,
            "fraction_digits": 2,
        },
    )
    electricity_source: Optional[str] = field(
        default=None,
        metadata={
            "name": "ElectricitySource",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        },
    )
    other_source_indication: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherSourceIndication",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 4000,
        },
    )
    emission_factor_source_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmissionFactorSourceValue",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 512,
        },
    )


@dataclass
class InstallationAddressType:
    establishment_country: Optional[str] = field(
        default=None,
        metadata={
            "name": "EstablishmentCountry",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 2,
            "max_length": 2,
        },
    )
    sub_division: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubDivision",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 35,
        },
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 35,
        },
    )
    street: Optional[str] = field(
        default=None,
        metadata={
            "name": "Street",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 70,
        },
    )
    street_additional_line: Optional[str] = field(
        default=None,
        metadata={
            "name": "StreetAdditionalLine",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 70,
        },
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 35,
        },
    )
    postcode: Optional[str] = field(
        default=None,
        metadata={
            "name": "Postcode",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 17,
        },
    )
    pobox: Optional[str] = field(
        default=None,
        metadata={
            "name": "POBox",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 70,
        },
    )
    plot_parcel_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlotParcelNumber",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 15,
        },
    )
    unlocode: Optional[str] = field(
        default=None,
        metadata={
            "name": "UNLOCODE",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 17,
        },
    )
    latitude: Optional[str] = field(
        default=None,
        metadata={
            "name": "Latitude",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 17,
        },
    )
    longitude: Optional[str] = field(
        default=None,
        metadata={
            "name": "Longitude",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 17,
        },
    )
    coordinates_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "CoordinatesType",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 5,
        },
    )


@dataclass
class InwardProcessingInfoType:
    member_state_auth: Optional[str] = field(
        default=None,
        metadata={
            "name": "MemberStateAuth",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 2,
            "max_length": 2,
        },
    )
    discharge_bill_waiver: Optional[int] = field(
        default=None,
        metadata={
            "name": "DischargeBillWaiver",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "total_digits": 1,
        },
    )
    authorisation: Optional[str] = field(
        default=None,
        metadata={
            "name": "Authorisation",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 512,
        },
    )
    start_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "total_digits": 8,
        },
    )
    end_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "total_digits": 8,
        },
    )
    deadline: Optional[int] = field(
        default=None,
        metadata={
            "name": "Deadline",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "total_digits": 8,
        },
    )


@dataclass
class MeasureProcedureType:
    indicator: Optional[int] = field(
        default=None,
        metadata={
            "name": "Indicator",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "total_digits": 1,
        },
    )
    net_mass: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NetMass",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "total_digits": 16,
            "fraction_digits": 6,
        },
    )
    supplementary_units: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SupplementaryUnits",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "total_digits": 16,
            "fraction_digits": 6,
        },
    )
    measurement_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "MeasurementUnit",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        },
    )


@dataclass
class MeasureType:
    net_mass: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NetMass",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "total_digits": 16,
            "fraction_digits": 6,
        },
    )
    supplementary_units: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SupplementaryUnits",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "total_digits": 16,
            "fraction_digits": 6,
        },
    )
    measurement_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "MeasurementUnit",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        },
    )


@dataclass
class OriginCountryType:
    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 2,
            "max_length": 2,
        },
    )


@dataclass
class QualifyingParametersType:
    sequence_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "pattern": r"\d{1,5}",
        },
    )
    parameter_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParameterId",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        },
    )
    parameter_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParameterName",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 256,
        },
    )
    parameter_value_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParameterValueType",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    parameter_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParameterValue",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    additional_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdditionalInformation",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 512,
        },
    )


@dataclass
class RemarksEmissionsType:
    sequence_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "pattern": r"\d{1,5}",
        },
    )
    additional_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdditionalInformation",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 512,
        },
    )


@dataclass
class RemarksType:
    additional_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdditionalInformation",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 9999,
        },
    )


@dataclass
class ReportConfirmationType:
    global_data_confirmation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GlobalDataConfirmation",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
        },
    )
    use_of_data_confirmation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseOfDataConfirmation",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
        },
    )
    signature_place: Optional[str] = field(
        default=None,
        metadata={
            "name": "SignaturePlace",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        },
    )
    signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        },
    )
    position_of_person_sending: Optional[str] = field(
        default=None,
        metadata={
            "name": "PositionOfPersonSending",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        },
    )


@dataclass
class SpecialReferencesType:
    additional_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdditionalInformation",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 512,
        },
    )


@dataclass
class CommodityCodeType:
    hs_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "HsCode",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 6,
            "max_length": 6,
        },
    )
    cn_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CnCode",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 8,
            "max_length": 8,
        },
    )
    commodity_details: Optional[CommodityDetailsType] = field(
        default=None,
        metadata={
            "name": "CommodityDetails",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
        },
    )


@dataclass
class DeclarantType:
    identification_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentificationNumber",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 17,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        },
    )
    actor_address: Optional[AddressType] = field(
        default=None,
        metadata={
            "name": "ActorAddress",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
        },
    )


@dataclass
class ImporterType:
    identification_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentificationNumber",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 17,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    importer_address: Optional[AddressType] = field(
        default=None,
        metadata={
            "name": "ImporterAddress",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
        },
    )


@dataclass
class InstallationOperatorType:
    operator_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatorId",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 17,
        },
    )
    operator_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatorName",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    operator_address: Optional[AddressType] = field(
        default=None,
        metadata={
            "name": "OperatorAddress",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
        },
    )
    contact_details: List[ContactDetailsType] = field(
        default_factory=list,
        metadata={
            "name": "ContactDetails",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_occurs": 1,
            "max_occurs": 9,
        },
    )


@dataclass
class InstallationType:
    installation_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstallationId",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 17,
        },
    )
    installation_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstallationName",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    economic_activity: Optional[str] = field(
        default=None,
        metadata={
            "name": "EconomicActivity",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 256,
        },
    )
    address: Optional[InstallationAddressType] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
        },
    )


@dataclass
class ProcedureType:
    requested_proc: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestedProc",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 2,
            "max_length": 2,
        },
    )
    previous_proc: Optional[str] = field(
        default=None,
        metadata={
            "name": "PreviousProc",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 2,
            "max_length": 2,
        },
    )
    inward_processing_info: List[InwardProcessingInfoType] = field(
        default_factory=list,
        metadata={
            "name": "InwardProcessingInfo",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "max_occurs": 999,
        },
    )


@dataclass
class ProdMethodQualifyingParamsType:
    sequence_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "pattern": r"\d{1,5}",
        },
    )
    method_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "MethodId",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        },
    )
    method_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "MethodName",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 256,
        },
    )
    steel_mill_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SteelMillNumber",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 256,
        },
    )
    additional_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdditionalInformation",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 512,
        },
    )
    direct_qualifying_parameters: List[QualifyingParametersType] = field(
        default_factory=list,
        metadata={
            "name": "DirectQualifyingParameters",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "max_occurs": 99,
        },
    )
    indirect_qualifying_parameters: List[QualifyingParametersType] = field(
        default_factory=list,
        metadata={
            "name": "IndirectQualifyingParameters",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "max_occurs": 99,
        },
    )


@dataclass
class ProductsCoveredType:
    sequence_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "pattern": r"\d{1,5}",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        },
    )
    cn: Optional[str] = field(
        default=None,
        metadata={
            "name": "CN",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 8,
        },
    )
    quantity_covered: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "QuantityCovered",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "total_digits": 16,
            "fraction_digits": 5,
        },
    )
    quantity_covered_free_aloc: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "QuantityCoveredFreeAloc",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "total_digits": 16,
            "fraction_digits": 5,
        },
    )
    supplementary_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplementaryInformation",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 256,
        },
    )
    additional_information: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdditionalInformation",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 512,
        },
    )
    measure: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "Measure",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
        },
    )


@dataclass
class RepresentativeType:
    identification_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentificationNumber",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 17,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    representative_address: Optional[AddressType] = field(
        default=None,
        metadata={
            "name": "RepresentativeAddress",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
        },
    )


@dataclass
class SignaturesType:
    report_confirmation: Optional[ReportConfirmationType] = field(
        default=None,
        metadata={
            "name": "ReportConfirmation",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
        },
    )
    applicable_methodology_confirmation: Optional[
        ApplicableMethodologyConfirmationType
    ] = field(
        default=None,
        metadata={
            "name": "ApplicableMethodologyConfirmation",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
        },
    )


@dataclass
class SupportingDocumentsType:
    sequence_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "pattern": r"\d{1,5}",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 4,
            "max_length": 4,
        },
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 2,
            "max_length": 2,
        },
    )
    reference_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferenceNumber",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 70,
        },
    )
    line_item_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineItemNumber",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "pattern": r"\d{1,5}",
        },
    )
    issuing_auth_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "IssuingAuthName",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 70,
        },
    )
    validity_start_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidityStartDate",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "pattern": r"\d{4}-\d\d-\d\d",
        },
    )
    validity_end_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidityEndDate",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "pattern": r"\d{4}-\d\d-\d\d",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 256,
        },
    )
    attachment: Optional[AttachmentType] = field(
        default=None,
        metadata={
            "name": "Attachment",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
        },
    )


@dataclass
class CarbonPriceDueType:
    sequence_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "pattern": r"\d{1,5}",
        },
    )
    instrument_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrumentType",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        },
    )
    legal_act_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegalActDescription",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 1,
            "max_length": 512,
        },
    )
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
        },
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 3,
            "max_length": 3,
        },
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 2,
            "max_length": 2,
        },
    )
    products_covered: List[ProductsCoveredType] = field(
        default_factory=list,
        metadata={
            "name": "ProductsCovered",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "max_occurs": 9,
        },
    )


@dataclass
class ImportedQuantityType:
    sequence_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "pattern": r"\d{1,5}",
        },
    )
    procedure: Optional[ProcedureType] = field(
        default=None,
        metadata={
            "name": "Procedure",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
        },
    )
    import_area: Optional[ImportAreaType] = field(
        default=None,
        metadata={
            "name": "ImportArea",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
        },
    )
    measure_procedure_imported: List[MeasureProcedureType] = field(
        default_factory=list,
        metadata={
            "name": "MeasureProcedureImported",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
    special_references: Optional[SpecialReferencesType] = field(
        default=None,
        metadata={
            "name": "SpecialReferences",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
        },
    )


@dataclass
class GoodsEmissionsType:
    sequence_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "pattern": r"\d{1,5}",
        },
    )
    production_country: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProductionCountry",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 2,
            "max_length": 2,
        },
    )
    installation_operator: Optional[InstallationOperatorType] = field(
        default=None,
        metadata={
            "name": "InstallationOperator",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
        },
    )
    installation: Optional[InstallationType] = field(
        default=None,
        metadata={
            "name": "Installation",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
        },
    )
    produced_measure: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "ProducedMeasure",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
        },
    )
    direct_emissions: Optional[DirectEmissionsType] = field(
        default=None,
        metadata={
            "name": "DirectEmissions",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
        },
    )
    indirect_emissions: Optional[IndirectEmissionsType] = field(
        default=None,
        metadata={
            "name": "IndirectEmissions",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
        },
    )
    prod_method_qualifying_params: List[ProdMethodQualifyingParamsType] = (
        field(
            default_factory=list,
            metadata={
                "name": "ProdMethodQualifyingParams",
                "type": "Element",
                "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
                "min_occurs": 1,
                "max_occurs": 99,
            },
        )
    )
    supporting_documents: List[SupportingDocumentsType] = field(
        default_factory=list,
        metadata={
            "name": "SupportingDocuments",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "max_occurs": 99,
        },
    )
    carbon_price_due: List[CarbonPriceDueType] = field(
        default_factory=list,
        metadata={
            "name": "CarbonPriceDue",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "max_occurs": 99,
        },
    )
    remarks_emissions: List[RemarksEmissionsType] = field(
        default_factory=list,
        metadata={
            "name": "RemarksEmissions",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "max_occurs": 9,
        },
    )


@dataclass
class ImportedGoodType:
    item_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemNumber",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "pattern": r"\d{1,5}",
        },
    )
    representative: Optional[RepresentativeType] = field(
        default=None,
        metadata={
            "name": "Representative",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
        },
    )
    importer: Optional[ImporterType] = field(
        default=None,
        metadata={
            "name": "Importer",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
        },
    )
    commodity_code: Optional[CommodityCodeType] = field(
        default=None,
        metadata={
            "name": "CommodityCode",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
        },
    )
    origin_country: Optional[OriginCountryType] = field(
        default=None,
        metadata={
            "name": "OriginCountry",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
        },
    )
    imported_quantity: List[ImportedQuantityType] = field(
        default_factory=list,
        metadata={
            "name": "ImportedQuantity",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_occurs": 1,
            "max_occurs": 9,
        },
    )
    measure_imported: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "MeasureImported",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
        },
    )
    supporting_documents: List[SupportingDocumentsType] = field(
        default_factory=list,
        metadata={
            "name": "SupportingDocuments",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "max_occurs": 99,
        },
    )
    remarks: Optional[RemarksType] = field(
        default=None,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
        },
    )
    goods_emissions: List[GoodsEmissionsType] = field(
        default_factory=list,
        metadata={
            "name": "GoodsEmissions",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )


@dataclass
class QreportType:
    class Meta:
        name = "QReportType"

    submission_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubmissionDate",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ",
        },
    )
    report_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReportId",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_length": 1,
            "max_length": 22,
        },
    )
    reporting_period: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReportingPeriod",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "min_length": 2,
            "max_length": 2,
        },
    )
    year: Optional[int] = field(
        default=None,
        metadata={
            "name": "Year",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
            "total_digits": 4,
        },
    )
    declarant: Optional[DeclarantType] = field(
        default=None,
        metadata={
            "name": "Declarant",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
        },
    )
    representative: Optional[RepresentativeType] = field(
        default=None,
        metadata={
            "name": "Representative",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
        },
    )
    importer: Optional[ImporterType] = field(
        default=None,
        metadata={
            "name": "Importer",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
        },
    )
    signatures: Optional[SignaturesType] = field(
        default=None,
        metadata={
            "name": "Signatures",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "required": True,
        },
    )
    remarks: Optional[RemarksType] = field(
        default=None,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
        },
    )
    imported_good: List[ImportedGoodType] = field(
        default_factory=list,
        metadata={
            "name": "ImportedGood",
            "type": "Element",
            "namespace": "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1",
            "min_occurs": 1,
            "max_occurs": 99999,
        },
    )


@dataclass
class Qreport(QreportType):
    class Meta:
        name = "QReport"
        namespace = "http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1"
