declare namespace foaf = "http://xmlns.com/foaf/0.1/";
declare namespace rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#";
declare namespace rdfs = "http://www.w3.org/2000/01/rdf-schema#";
declare namespace sch = "http://schema.org/";
declare namespace geonames = "https://www.geonames.org/ontology#";
declare namespace ontology-se-cbam = "https://siemens-energy.com/cbam/";
declare namespace ontology-se-cbam-emissionsqualifyingparameters = "https://ontology.siemens-energy.com/cbam/emissionsqualifyingparameters/";
declare namespace ontology-se-cbam-cn = "https://ontology.siemens-energy.com/cbam/CN/";
declare namespace ontology-se-cbam-cbamreport = "https://ontology.siemens-energy.com/cbam/cbamreport/";
declare namespace ontology-se-cbam-electricity_determination = "https://ontology.siemens-energy.com/cbam/Electricity_Determination/";
declare namespace ontology-se-cbam-instrument = "https://ontology.siemens-energy.com/cbam/Instrument/";
declare namespace ontology-se-cbam-country = "https://ontology.siemens-energy.com/cbam/CountryPlus/";
declare namespace ontology-se-cbam-currency = "https://ontology.siemens-energy.com/cbam/currency/";
declare namespace ontology-se-cbam-production-method = "https://ontology.siemens-energy.com/cbam/Production_Method/";
declare namespace ontology-se-cbam-cbam-goods = "https://ontology.siemens-energy.com/cbam/cbam_goods/";
declare namespace se-cbam = "https://data.siemens-energy.com/cbam#";
declare namespace se-cbam-emissionsqualifyingparameters = "https://data.siemens-energy.com/cbam/emissionsqualifyingparameters#";
declare namespace se-cbam-cn = "https://data.siemens-energy.com/cbam/CN#";
declare namespace se-cbam-cbamreport = "https://data.siemens-energy.com/cbam/cbamreport#";
declare namespace se-cbam-electricity_determination = "https://data.siemens-energy.com/cbam/Electricity_Determination#";
declare namespace se-cbam-instrument = "https://data.siemens-energy.com/cbam/Instrument#";
declare namespace se-cbam-country = "https://data.siemens-energy.com/cbam/CountryPlus#";
declare namespace se-cbam-currency = "https://data.siemens-energy.com/cbam/currency#";
declare namespace se-cbam-production-method = "https://data.siemens-energy.com/cbam/Production_Method#";
declare namespace se-cbam-cbam-goods = "https://data.siemens-energy.com/cbam/cbam_goods#";


<v1:QReport xmlns:v1="http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1">
{ for $product $itemNumber from <${inputFile}>
	where {
		$product a sch:Product .
		$product ontology-se-cbam-cbamreport:itemNumber $itemNumber .
	} order by $itemNumber
	return <v1:ImportedGood>
			<v1:ItemNumber>{$itemNumber}</v1:ItemNumber>
            { for $hsCode $cnCode $cnDescription from <${inputFile}>
                where {
                    $product ontology-se-cbam-cbamreport:hasCNCode $cnCodeIri .
                    $cnCodeIri rdfs:label $cnDescription .
                    $cnCodeIri ontology-se-cbam-cn:cn_code $cnCode .
                    $cnCodeIri ontology-se-cbam-cn:hs6_code $hsCode .
                }
                return <v1:CommodityCode>
                        <v1:HsCode>{$hsCode}</v1:HsCode>
                        <v1:CnCode>{$cnCode}</v1:CnCode>
                        <v1:CommodityDetails>
                            <v1:Description>{$cnDescription}</v1:Description>
                        </v1:CommodityDetails>
                    </v1:CommodityCode>
            }
            <v1:GoodsEmissions>
            { for $contactName $contactPhone $contactMail from <${inputFile}>
                where {
                    $product ontology-se-cbam-cbamreport:isManufacturedIn $installation .
                    $installation a ontology-se-cbam-cbamreport:Installation .
                    $installation ontology-se-cbam-cbamreport:hasRepresentative $representative .
                    $representative foaf:name $contactName .
                    $representative foaf:phone $contactPhone .
                    $representative foaf:mbox $contactMail .
                }
                return  <v1:InstallationOperator>
                            <v1:OperatorId>{'todo'}</v1:OperatorId>
                            <v1:OperatorName>{'todo'}</v1:OperatorName>
                            <v1:OperatorAddress>
                                <v1:Country>{'todo'}</v1:EstablishmentCountry>
                                <v1:City>{'todo'}</v1:City>
                                <v1:Street>{'todo'}</v1:Street>
                                <v1:Number>{'todo'}</v1:Number>
                                <v1:Postcode>{'todo'}</v1:Postcode>
                                <v1:POBox>{'todo'}</v1:POBox>
                            </v1:OperatorAddress>
                            <v1:ContactDetails>
                                <v1:Name>{$contactName}</v1:Name>
                                <v1:Phone>{$contactPhone}</v1:Phone>
                                <v1:Email>{$contactMail}</v1:Email>
                            </v1:ContactDetails>
                        </v1:InstallationOperator>
            }
            { for $installationLatitude $installationLongitude $installationName $installationEconomicActivity $installationUnlocode $installationAddressCity $installationAddressCountryCode $installationAddressStreet $installationAddressNumber $installationAddressPostCode $installationAddressPoBox from <${inputFile}>
                where {
                    $product ontology-se-cbam-cbamreport:isManufacturedIn $installation .
                    $installation a ontology-se-cbam-cbamreport:Installation .
                    $installation geonames:lat $installationLatitude .
                    $installation geonames:long $installationLongitude .
                    $installation foaf:name $installationName .
                    $installation ontology-se-cbam-cbamreport:hasEconomicActivity $installationEconomicActivity .
                    $installation ontology-se-cbam-cbamreport:hasUNLOCODE $installationUnlocode .
                    $installation ontology-se-cbam-cbamreport:hasAddress $installationAddress .
                    $installationAddress  ontology-se-cbam-cbamreport:hasCity $installationAddressCity .
                    $installationAddress ontology-se-cbam-cbamreport:hasCountry $installationAddressCountry .
                    $installationAddressCountry geonames:countryCode $installationAddressCountryCode .
                    $installationAddress ontology-se-cbam-cbamreport:hasStreet $installationAddressStreet .
                    $installationAddress ontology-se-cbam-cbamreport:hasNumber $installationAddressNumber .
                    $installationAddress ontology-se-cbam-cbamreport:hasPostCode $installationAddressPostCode .
                    $installationAddress ontology-se-cbam-cbamreport:hasPoBox $installationAddressPoBox .
                }
                return  <v1:Installation>
                            <v1:InstallationId>{$installationUnlocode}</v1:InstallationId>
                            <v1:InstallationName>{$installationName}</v1:InstallationName>
                            <v1:EconomicActivity>{$installationEconomicActivity}</v1:EconomicActivity>
                            <v1:Address>
                                <v1:EstablishmentCountry>{$installationAddressCountryCode}</v1:EstablishmentCountry>
                                <v1:Street>{$installationAddressStreet}</v1:Street>
                                <v1:City>{$installationAddressCity}</v1:City>
                                <v1:Number>{$installationAddressNumber}</v1:Number>
                                <v1:Postcode>{$installationAddressPostCode}</v1:Postcode>
                                <v1:POBox>{$installationAddressPoBox}</v1:POBox>
                                <v1:UNLOCODE>{$installationUnlocode}</v1:UNLOCODE>
                                <v1:Latitude>{$installationLatitude}</v1:Latitude>
                                <v1:Longitude>{$installationLongitude}</v1:Longitude>
                            </v1:Address>
                        </v1:Installation>
            }
            { for $directEmission $unitOfMeasure from <${inputFile}>
                where {
                    $product ontology-se-cbam-cbamreport:generate $greenHouseGasEmissions .
                    $greenHouseGasEmissions ontology-se-cbam-cbamreport:DirectEmbeddedEmissions $directEmission .
                    $greenHouseGasEmissions ontology-se-cbam-cbamreport:typeOfMeasurementUnitForEmissions $unitOfMeasure .
                }
                return <v1:DirectEmissions>
                            <v1:SpecificEmbeddedEmissions>{$directEmission}</v1:SpecificEmbeddedEmissions>
                            <v1:MeasurementUnit>{$unitOfMeasure}</v1:MeasurementUnit>
                        </v1:DirectEmissions>
            }
            { for $indirectEmission $unitOfMeasure from <${inputFile}>
                where {
                    $product ontology-se-cbam-cbamreport:generate $greenHouseGasEmissions .
                    $greenHouseGasEmissions ontology-se-cbam-cbamreport:IndirectEmbeddedEmissions $indirectEmission .
                    $greenHouseGasEmissions ontology-se-cbam-cbamreport:typeOfMeasurementUnitForEmissions $unitOfMeasure .
                }
                return <v1:IndirectEmissions>
                            <v1:SpecificEmbeddedEmissions>{$indirectEmission}</v1:SpecificEmbeddedEmissions>
                            <v1:MeasurementUnit>{$unitOfMeasure}</v1:MeasurementUnit>
                        </v1:IndirectEmissions>
            }
            { for $methodName $steelMillIdNumber from <${inputFile}>
                where {
                    $product ontology-se-cbam-cbamreport:isExecutedBy $productionMethod .
                    $productionMethod rdfs:label $methodName .
                    $product ontology-se-cbam-cbamreport:isProducedIn $steelMill .
                    $steelMill ontology-se-cbam-cbamreport:identificationnumberOfTheSpecificSteelMill $steelMillIdNumber .
                }
                return  <v1:ProdMethodQualifyingParams>
                            <v1:SequenceNumber>{1}</v1:SequenceNumber>
                            <v1:MethodId>{'todo'}</v1:MethodId>
                            <v1:MethodName>{$methodName}</v1:MethodName>
                            <v1:SteelMillNumber>{$steelMillIdNumber}</v1:SteelMillNumber>
                            { for $parameterCode $parameterValue $parameterDescription $parameterName $parameterValueType from <${inputFile}>
                                where {
                                    $product ontology-se-cbam-cbamreport:hasEmissionQualifyingParameter $parameter .
                                    $parameter ontology-se-cbam-emissionsqualifyingparameters:typeOfEmissionValue "DIRECT" .
                                    $parameter ontology-se-cbam-emissionsqualifyingparameters:code $parameterCode .
	                                $parameter rdfs:label $parameterName .
                                    $parameter ontology-se-cbam-emissionsqualifyingparameters:description $parameterDescription .
                                    $parameter ontology-se-cbam-emissionsqualifyingparameters:parameterValueNumeric|ontology-se-cbam-emissionsqualifyingparameters:parameterValuePercentage|ontology-se-cbam-emissionsqualifyingparameters:parameterValueText $parameterValue .
                                    $parameter ontology-se-cbam-emissionsqualifyingparameters:typeOfParameterValue $parameterValueType .
                                } order by $parameterCode
                                return  <v1:DirectQualifyingParameters>
                                            <v1:SequenceNumber>{1}</v1:SequenceNumber>
                                            <v1:ParameterId>{$parameterCode}</v1:ParameterId>
                                            <v1:ParameterName>{$parameterName}</v1:ParameterName>
                                            <v1:Description>{$parameterDescription}</v1:Description>
                                            <v1:ParameterValueType>{$parameterValueType}</v1:ParameterValueType>
                                            <v1:ParameterValue>{$parameterValue}</v1:ParameterValue>
                                            <v1:AdditionalInformation>Additional information</v1:AdditionalInformation>
                                        </v1:DirectQualifyingParameters>
                            }
                            { for $parameterCode $parameterValue $parameterDescription $parameterName $parameterValueType from <${inputFile}>
                                where {
                                    $product ontology-se-cbam-cbamreport:hasEmissionQualifyingParameter $parameter .
                                    $parameter ontology-se-cbam-emissionsqualifyingparameters:typeOfEmissionValue "INDIRECT" .
                                    $parameter ontology-se-cbam-emissionsqualifyingparameters:code $parameterCode .
	                                $parameter rdfs:label $parameterName .
                                    $parameter ontology-se-cbam-emissionsqualifyingparameters:description $parameterDescription .
                                    $parameter ontology-se-cbam-emissionsqualifyingparameters:parameterValueNumeric|ontology-se-cbam-emissionsqualifyingparameters:parameterValuePercentage|ontology-se-cbam-emissionsqualifyingparameters:parameterValueText $parameterValue .
                                    $parameter ontology-se-cbam-emissionsqualifyingparameters:typeOfParameterValue $parameterValueType .
                                } order by $parameterCode
                                return  <v1:IndirectQualifyingParameters>
                                            <v1:SequenceNumber>{1}</v1:SequenceNumber>
                                            <v1:ParameterId>{$parameterCode}</v1:ParameterId>
                                            <v1:ParameterName>{$parameterName}</v1:ParameterName>
                                            <v1:Description>{$parameterDescription}</v1:Description>
                                            <v1:ParameterValueType>{$parameterValueType}</v1:ParameterValueType>
                                            <v1:ParameterValue>{$parameterValue}</v1:ParameterValue>
                                            <v1:AdditionalInformation>Additional information</v1:AdditionalInformation>
                                        </v1:IndirectQualifyingParameters>
                            }
                        </v1:ProdMethodQualifyingParams>
            }
                <v1:CarbonPriceDue>
                    <v1:SequenceNumber>{1}</v1:SequenceNumber>
                    <v1:InstrumentType>{"todo"}</v1:InstrumentType>
                    { for $amount from <${inputFile}>
                        where {
                            $product ontology-se-cbam-cbamreport:hasEmissionsCovered $emissionsCovered .
                            $emissionsCovered ontology-se-cbam-cbamreport:amountOfCarbonPriceDue $amount .
                        }
                        return <v1:Amount>{$amount}</v1:Amount>
                    }
                    { for $currency from <${inputFile}>
                        where {
                            $product ontology-se-cbam-cbamreport:hasEmissionsCovered $emissionsCovered .
                            $emissionsCovered ontology-se-cbam-currency:currencyCode $currency .
                        }
                        return <v1:Currency>{$currency}</v1:Currency>
                    }
                    { for $installationCountry from <${inputFile}>
                        where {
                            $product ontology-se-cbam-cbamreport:isManufacturedIn $installation .
                            $installation ontology-se-cbam-cbamreport:hasAddress $installationAddress .
                            $installationAddress ontology-se-cbam-cbamreport:hasCountry $installationAddressCountry .
                            $installationAddressCountry geonames:countryCode $installationCountry .
                        }
                        return <v1:Country>{$installationCountry}</v1:Country>
                    }

                    <v1:ProductsCovered>
                        <v1:SequenceNumber>{1}</v1:SequenceNumber>
                        <v1:Type>{"todo"}</v1:Type>
                        { for $cnCode from <${inputFile}>
                            where {
                                $product ontology-se-cbam-cbamreport:isCoveredRebate $rebate .
                                $product ontology-se-cbam-cbamreport:hasCNCode $cnCodeIri .
                                $cnCodeIri ontology-se-cbam-cn:cn_code $cnCode .
                            }
                            return <v1:CN>{$cnCode}</v1:CN>
                        }
                        { for $quantityCovered from <${inputFile}>
                            where {
                                $product ontology-se-cbam-cbamreport:isCoveredRebate $rebate .
                                $rebate ontology-se-cbam-cbamreport:quantityCoveredByRebate $quantityCovered .
                            }
                            return <v1:QuantityCovered>{$quantityCovered}</v1:QuantityCovered>
                        }
                        { for $quantityCoveredFreeAloc from <${inputFile}>
                            where {
                                $product ontology-se-cbam-cbamreport:isCoveredRebate $rebate .
                                $rebate ontology-se-cbam-cbamreport:quantityCoveredByRebate $quantityCovered .
                            }
                            return <v1:QuantityCoveredFreeAloc>{$quantityCoveredFreeAloc}</v1:QuantityCoveredFreeAloc>
                        }
                    </v1:ProductsCovered>
                </v1:CarbonPriceDue>
            </v1:GoodsEmissions>
		</v1:ImportedGood>
}
</v1:QReport>
