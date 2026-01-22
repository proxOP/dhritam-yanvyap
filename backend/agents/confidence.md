# Confidence Agent

## Responsibility
Evaluates the reliability and certainty of the final synthesized answer.

## Inputs
- Individual agent outputs
- Source credibility scores
- Conflict markers between agents

## Outputs
- Global confidence score (0.0 - 1.0)
- Uncertainty drivers (list of factors reducing confidence)

## Constraints
- Score must strictly penalize missing data
- Cannot fabricate confidence; conservative scoring required
