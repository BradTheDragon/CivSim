traits = {
    "Technology": 50,
    "Culture": 50,
    "Government": 50,
    "Economy": 50,
    "Military": 50,
    "Society": 50,
    "Environment": 50,
    "Philosophy": 50,
    "Diplomacy": 50,
    "Art": 50
}

influence = {
    "Technology":     { "Culture": +1, "Government": +2, "Economy": +4, "Military": +2, "Society": +2, "Environment": -2, "Philosophy": -1, "Diplomacy": +1, "Art": -1 },
    "Culture":        { "Government": -1, "Economy": +1, "Military": -1, "Society": +3, "Philosophy": +3, "Art": +4 },
    "Government":     { "Technology": +2, "Culture": -1, "Economy": +2, "Military": +3, "Society": -2, "Environment": -1, "Philosophy": -2, "Diplomacy": +4, "Art": -1 },
    "Economy":        { "Technology": +3, "Environment": -3, "Society": -1, "Art": -1 },
    "Military":       { "Society": -2, "Philosophy": -2, "Diplomacy": +2 },
    "Society":        { "Culture": +3, "Philosophy": +1, "Art": +2 },
    "Environment":    { "Philosophy": +1 },
    "Philosophy":     { "Government": -2, "Art": +2 },
    "Diplomacy":      { "Government": +3 },
    "Art":            {}
}