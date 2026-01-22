# Entities Memory

## Purpose
Graph database definitions for entity & supply-chain relationships.

## Node Types
- Company
- Commodity
- GeoLocation
- Regulation

## Edge Types
- `SUPPLIES_TO`
- `SUBSIDIARY_OF`
- `AFFECTED_BY` (e.g. Commodity -> Regulation)

## Indexing
- Vector index on Entity Description for fuzzy lookup.
