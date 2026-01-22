# Domain Agent (Base)

## Responsibility
Abstract base definition for all specialized knowledge agents.

## Inputs
- Specific sub-task from Composer
- Access to relevant Memory/Entities

## Outputs
- Analysis result
- Confidence score
- Source citations

## Constraints
- Must cite sources for all claims
- Stateless execution (context passed in input)
