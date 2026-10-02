declare namespace foaf = "http://xmlns.com/foaf/0.1/";
declare namespace rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#";
declare namespace rdfs = "http://www.w3.org/2000/01/rdf-schema#";
declare namespace sch = "http://schema.org/";
declare namespace geonames = "https://www.geonames.org/ontology#";
declare namespace ontology-se-cbam-emissionsqualifyingparameters = "https://purl.org/cbam/emissionsqualifyingparameters/";
declare namespace ontology-se-cbam-cn = "https://purl.org/cbam/CN/";
declare namespace ontology-se-cbam-cbamreport = "https://purl.org/cbam/cbamreport/";
declare namespace ontology-se-cbam-electricity_determination = "https://purl.org/cbam/Electricity_Determination/";
declare namespace ontology-se-cbam-instrument = "https://purl.org/cbam/Instrument/";
declare namespace ontology-se-cbam-country = "https://purl.org/cbam/CountryPlus/";
declare namespace ontology-se-cbam-currency = "https://purl.org/cbam/currency/";
declare namespace ontology-se-cbam-production-method = "https://purl.org/cbam/Production_Method/";
declare namespace ontology-se-cbam-cbam-goods = "https://purl.org/cbam/cbam_goods/";
declare namespace se-cbam-emissionsqualifyingparameters = "https://data.com/cbam/emissionsqualifyingparameters#";
declare namespace se-cbam-cn = "https://data.com/cbam/CN#";
declare namespace se-cbam-cbamreport = "https://data.com/cbam/cbamreport#";
declare namespace se-cbam-electricity_determination = "https://data.com/cbam/Electricity_Determination#";
declare namespace se-cbam-instrument = "https://data.com/cbam/Instrument#";
declare namespace se-cbam-country = "https://data.com/cbam/CountryPlus#";
declare namespace se-cbam-currency = "https://data.com/cbam/currency#";
declare namespace se-cbam-production-method = "https://data.com/cbam/Production_Method#";
declare namespace se-cbam-cbam-goods = "https://data.com/cbam/cbam_goods#";


<v1:QReport xmlns:v1="http://xmlns.ec.eu/BusinessObjects/CBAM/Types/V1">
    <v1:SubmissionDate>{'1970-01-01T00:00:00Z'}</v1:SubmissionDate>
    <v1:ReportingPeriod>{'Qx'}</v1:ReportingPeriod>
    <v1:Year>{'1970'}</v1:Year>
    <v1:Declarant>
          <v1:IdentificationNumber>{'ES12345678901234'}</v1:IdentificationNumber>
          <v1:Name>{'Test Declarant SL'}</v1:Name>
          <v1:Role>{'IM'}</v1:Role>
          <v1:ActorAddress>
              <v1:Country>{'ES'}</v1:Country>
              <v1:City>{'Madrid'}</v1:City>
              <v1:Street>{'Calle Falsa'}</v1:Street>
              <v1:Number>{'123'}</v1:Number>
              <v1:Postcode>{'28001'}</v1:Postcode>
          </v1:ActorAddress>
      </v1:Declarant>
      <v1:Signatures>
          <v1:ReportConfirmation>
              <v1:GlobalDataConfirmation>{'true'}</v1:GlobalDataConfirmation>
              <v1:UseOfDataConfirmation>{'true'}</v1:UseOfDataConfirmation>
              <v1:SignaturePlace>{'Madrid'}</v1:SignaturePlace>
              <v1:Signature>{'Test Declarant'}</v1:Signature>
              <v1:PositionOfPersonSending>{'Sample post'}</v1:PositionOfPersonSending>
          </v1:ReportConfirmation>
      </v1:Signatures>
{ for $product $itemNumber from <${inputFile}>
	where {
		$product a ontology-se-cbam-cbamreport:Good .
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
            { for $originCountryCode from <${inputFile}>
                where {
                    $product ontology-se-cbam-cbamreport:isManufacturedAt $installation .
                    $installation ontology-se-cbam-cbamreport:hasAddress $installationAddress .
                    $installationAddress ontology-se-cbam-cbamreport:hasCountry $installationAddressCountry .
                    $installationAddressCountry geonames:countryCode $originCountryCode .
                }
                return <v1:OriginCountry>
                        <v1:Country>{$originCountryCode}</v1:Country>
                       </v1:OriginCountry>
            }
            <v1:ImportedQuantity>
                <v1:SequenceNumber>{'1'}</v1:SequenceNumber>
                <v1:Procedure>
                    <v1:RequestedProc>{'40'}</v1:RequestedProc>
                </v1:Procedure>
                <v1:ImportArea>
                    <v1:ImportArea>{'ES002'}</v1:ImportArea>
                </v1:ImportArea>
                <v1:MeasureProcedureImported>
                    <v1:Indicator>{'1'}</v1:Indicator>
                    <v1:NetMass>{'1000.0'}</v1:NetMass>
                    <v1:MeasurementUnit>{'KGM'}</v1:MeasurementUnit>
                </v1:MeasureProcedureImported>
            </v1:ImportedQuantity>
            <v1:MeasureImported>
                <v1:NetMass>{'1000.0'}</v1:NetMass>
                <v1:MeasurementUnit>{'KGM'}</v1:MeasurementUnit>
            </v1:MeasureImported>
            <v1:GoodsEmissions>
            { for $contactName $contactPhone $contactMail from <${inputFile}>
                where {
                    $product ontology-se-cbam-cbamreport:isManufacturedAt $installation .
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
                                <v1:Country>{'XX'}</v1:Country>
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
                    $product ontology-se-cbam-cbamreport:isManufacturedAt $installation .
                    $installation a ontology-se-cbam-cbamreport:Installation .
                    $installation geonames:lat $installationLatitude .
                    $installation geonames:long $installationLongitude .
                    $installation foaf:name $installationName .
                    $installation ontology-se-cbam-cbamreport:hasEconomicActivity $installationEconomicActivityInstance .
                    $installationEconomicActivityInstance foaf:name $installationEconomicActivity .
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
            <v1:ProducedMeasure>
                <v1:NetMass>{'1000.0'}</v1:NetMass>
                <v1:MeasurementUnit>{'t'}</v1:MeasurementUnit>
            </v1:ProducedMeasure>
            { for $directEmission $unitOfMeasure from <${inputFile}>
                where {
                    $product ontology-se-cbam-cbamreport:hasGreenHouseGasEmissions $greenHouseGasEmissions .
                    $greenHouseGasEmissions ontology-se-cbam-cbamreport:DirectEmbeddedEmissions $directEmission .
                    $greenHouseGasEmissions ontology-se-cbam-cbamreport:typeOfMeasurementUnitForEmissions $unitOfMeasure .
                }
                return <v1:DirectEmissions>
                            <v1:ApplicableReportingTypeMethodology>{'todo'}</v1:ApplicableReportingTypeMethodology>
                            <v1:SpecificEmbeddedEmissions>{$directEmission}</v1:SpecificEmbeddedEmissions>
                            <v1:MeasurementUnit>{$unitOfMeasure}</v1:MeasurementUnit>
                        </v1:DirectEmissions>
            }
            { for $indirectEmission $unitOfMeasure from <${inputFile}>
                where {
                    $product ontology-se-cbam-cbamreport:hasGreenHouseGasEmissions $greenHouseGasEmissions .
                    $greenHouseGasEmissions ontology-se-cbam-cbamreport:IndirectEmbeddedEmissions $indirectEmission .
                    $greenHouseGasEmissions ontology-se-cbam-cbamreport:typeOfMeasurementUnitForEmissions $unitOfMeasure .
                }
                return <v1:IndirectEmissions>
                            <v1:DeterminationType>{'todo'}</v1:DeterminationType>
                            <v1:SpecificEmbeddedEmissions>{$indirectEmission}</v1:SpecificEmbeddedEmissions>
                            <v1:MeasurementUnit>{$unitOfMeasure}</v1:MeasurementUnit>
                            <v1:ElectricitySource>{'todo'}</v1:ElectricitySource>
                        </v1:IndirectEmissions>
            }
            { for $methodName from <${inputFile}>
                where {
                    $product ontology-se-cbam-cbamreport:hasProductionMethod $productionMethod .
                    $productionMethod rdfs:label $methodName .
                }
                return  <v1:ProdMethodQualifyingParams>
                            <v1:SequenceNumber>{1}</v1:SequenceNumber>
                            <v1:MethodId>{'todo'}</v1:MethodId>
                            <v1:MethodName>{$methodName}</v1:MethodName>
                            { for $steelMillIdNumber from <${inputFile}>
                                where {
                                    $product ontology-se-cbam-cbamreport:isProducedAt $steelMill .
                                    $steelMill ontology-se-cbam-cbamreport:identificationnumberOfTheSpecificSteelMill $steelMillIdNumber .
                                }
                                return <v1:SteelMillNumber>{$steelMillIdNumber}</v1:SteelMillNumber>
                            }
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
                { for $amount from <${inputFile}>
                where {
                    $product ontology-se-cbam-cbamreport:hasEmissionsCovered $emissionsCovered .
                    $emissionsCovered ontology-se-cbam-cbamreport:amountOfCarbonPriceDue $amount .
                }
                return <v1:CarbonPriceDue>
                            <v1:SequenceNumber>{'1'}</v1:SequenceNumber>
                            <v1:InstrumentType>{'todo'}</v1:InstrumentType>
                            <v1:LegalActDescription>{'todo'}</v1:LegalActDescription>
                            <v1:Amount>{$amount}</v1:Amount>
                            { for $currency from <${inputFile}>
                                where {
                                    $product ontology-se-cbam-cbamreport:hasEmissionsCovered $emissionsCovered .
                                    $emissionsCovered ontology-se-cbam-currency:currencyCode $currency .
                                }
                                return <v1:Currency>{$currency}</v1:Currency>
                            }
                            { for $installationCountry from <${inputFile}>
                                where {
                                    $product ontology-se-cbam-cbamreport:isManufacturedAt $installation .
                                    $installation ontology-se-cbam-cbamreport:hasAddress $installationAddress .
                                    $installationAddress ontology-se-cbam-cbamreport:hasCountry $installationAddressCountry .
                                    $installationAddressCountry geonames:countryCode $installationCountry .
                                }
                                return <v1:Country>{$installationCountry}</v1:Country>
                            }

                            { for $quantityCovered from <${inputFile}>
                                where {
                                    $product ontology-se-cbam-cbamreport:isCoveredRebate $rebate .
                                    $rebate ontology-se-cbam-cbamreport:quantityCoveredByRebate $quantityCovered .
                                }
                                return <v1:ProductsCovered>
                                            <v1:SequenceNumber>{'1'}</v1:SequenceNumber>
                                            <v1:Type>{'todo'}</v1:Type>
                                            { for $cnCode from <${inputFile}>
                                                where {
                                                    $product ontology-se-cbam-cbamreport:isCoveredRebate $rebate .
                                                    $product ontology-se-cbam-cbamreport:hasCNCode $cnCodeIri .
                                                    $cnCodeIri ontology-se-cbam-cn:cn_code $cnCode .
                                                }
                                                return <v1:CN>{$cnCode}</v1:CN>
                                            }
                                            <v1:QuantityCovered>{$quantityCovered}</v1:QuantityCovered>
                                            <v1:QuantityCoveredFreeAloc>{'0.0'}</v1:QuantityCoveredFreeAloc>
                                            <v1:Measure>
                                                <v1:NetMass>{$quantityCovered}</v1:NetMass>
                                                <v1:MeasurementUnit>{'KGM'}</v1:MeasurementUnit>
                                            </v1:Measure>
                                        </v1:ProductsCovered>
                            }
                </v1:CarbonPriceDue>
                }
            </v1:GoodsEmissions>
		</v1:ImportedGood>
}
</v1:QReport>
