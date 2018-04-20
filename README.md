# Openprocurement data mapping in OCDS compatible format
---

## Purpose:
Repository contains mapping configuration which can be applied to produce OCDS data from Openprocurement API. 
Mainly used with [ galleon ](https://gitlab.quintagroup.com/yshalenyk/galleon) package

## `schemas` folder contains release schemas in jsonpatch format
1. `schemas/1.1-schema.json` 

    Contains pure schema for OCDS 1.1 data format
2. `schemas/1.1-extended-schema.json`

    Contains schema with applied Openprocurement extensions 

## `mapping` 
Folder contains mappings itself for 1.1 adn 1.1 extended format

## `extensions`
Folder contains Openprocurement extensions for OCDS 1.1 to fit all data available 

## OCDS 1.1 progress:
- [x] done

## OCDS 1.1 extended:

- [x] Bid
- [x] Auction
- [x] Lot
- [x] Complaints
- [ ] Complaint lotID
- [x] AdditionalContactPoints
- [x] ContractID
- [x] ContractNumber
- [x] ContractSuppliers
- [ ] Delivery
- [ ] Eligibility
- [x] Enquiries
- [x] Guarantee
- [x] LinkedDocuments
- [x] MEAT
- [x] Negotiation
- [ ] PendingCancellation
- [x] procurmentMethodDetails
- [x] Qualification
- [ ] Qualification Documents
- [ ] ShortlistedFirm
- [x] tenderID
- [ ] unitCode
- [ ] valueAddedTax

## Build dev environment:
```bash
pyenv virtualenv env
pyenv activate env
pip install -r requirements.txt
```

## Run transform on test data
``` bash
cat test-data/tender-simple.json | python ocds.py pure | jq
```
