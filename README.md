# Prozorro data mapping in OCDS compatible format
---

## Purpose:
Repository contains mapping configuration which can be applied to produce OCDS data from Prozorro API. 
Mainly used with [ galleon ](https://gitlab.quintagroup.com/yshalenyk/galleon) package

## `schemas` folder contains release schemas in jsonpatch format
1. `schemas/1.1-schema.json` 

    Contains pure schema for OCDS 1.1 data format
2. `schemas/1.1-extended-schema.json`

    Contains schema with applied Prozorro extensions 

## `mapping` 
Folder contains mappings itself for 1.1 adn 1.1 extended format

## `extensions`
Folder contains Prozorro extensions for OCDS 1.1 to fit all data available 

## OCDS 1.1 progress:
 - all done

## OCDS 1.1 extended:

- [x] Bid
- [x] Auction
- [ ] Lot
- [ ] Complaints
- [ ] AdditionalContactPoints
- [ ] Complaints
- [ ] ContractID
- [ ] ContractNumber
- [ ] ContractSuppliers
- [ ] Delivery
- [ ] Eligibility
- [ ] Enquiries
- [ ] Guarantee
- [ ] LinkedDocuments
- [ ] MEAT
- [ ] Negotiation
- [ ] PendingCancellation
- [ ] procurmentMethodType
- [ ] Qualification
- [ ] ShortlistedFirm
- [ ] tenderID
- [ ] unitCode
- [ ] valueAddedTax