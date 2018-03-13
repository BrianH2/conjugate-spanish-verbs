#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, sys

verbs = [x.strip() for x in sys.argv[1].split(',')]
print(verbs)

count = 0
conjugatedVerbs = []
print("\nStarting to process " + str(len(verbs)) + " \n")

for verb in verbs:
	count = count + 1
	infinitive = verb
	pastparticiple = ""

	if infinitive[-2:] == "ir":
		verbType = "IR"
	elif infinitive[-2:] == "er":
		verbType = "ER"
	elif infinitive[-2:] == "ar":
		verbType = "AR"
	else:
		verbType = "Unknown"
		continue

	infinitiveNoEnding = infinitive[:len(infinitive)-2]
	haber = {"gerund": "habiendo","pastparticiple": "habido","fulltenses": {"indicative conditional": {"mood": "indicative","tense": "conditional","1s": "habría","2s": "habrías","3s": "habría","1p": "habríamos","2p": "habríais","3p": "habrían"},"indicative future": {"mood": "indicative","tense": "future","1s": "habré","2s": "habrás","3s": "habrá","1p": "habremos","2p": "habréis","3p": "habrán"},"indicative imperfect": {"mood": "indicative","tense": "imperfect","1s": "había","2s": "habías","3s": "había","1p": "habíamos","2p": "habíais","3p": "habían"},"indicative present": {"mood": "indicative","tense": "present","1s": "he","2s": "has","3s": "ha","1p": "hemos","2p": "habéis","3p": "han"},"indicative preterite": {"mood": "indicative","tense": "preterite","1s": "hube","2s": "hubiste","3s": "hubo","1p": "hubimos","2p": "hubisteis","3p": "hubieron"},"subjunctive future": {"mood": "subjunctive","tense": "future","1s": "hubiere","2s": "hubieres","3s": "hubiere","1p": "hubiéremos","2p": "hubiereis","3p": "hubieren"},"subjunctive imperfect": {"mood": "subjunctive","tense": "imperfect","1s": "hubiera","2s": "hubieras","3s": "hubiera","1p": "hubiéramos","2p": "hubierais","3p": "hubieran"},"subjunctive present": {"mood": "subjunctive","tense": "present","1s": "haya","2s": "hayas","3s": "haya","1p": "hayamos","2p": "hayáis","3p": "hayan"}}}

	if verbType == "IR":
		pastparticiple = infinitiveNoEnding + "ido"
		conjugation = {
			"gerund": infinitiveNoEnding + "iendo",
			"pastparticiple": pastparticiple,
			"fulltenses": {
			"imperative affirmative present": {
				"mood": "imperative",
				"tense": "affirmative present",
				"1s": "-",
				"2s": infinitiveNoEnding + "e",
				"3s": infinitiveNoEnding + "a",
				"1p": "-",
				"2p": infinitiveNoEnding + "id",
				"3p": infinitiveNoEnding + "an"
			},
			"imperative negative present": {
				"mood": "imperative",
				"tense": "negative present",
				"1s": "-",
				"2s": infinitiveNoEnding + "as",
				"3s": infinitiveNoEnding + "a",
				"1p": "-",
				"2p": infinitiveNoEnding + "áis",
				"3p": infinitiveNoEnding + "an"
			},
			"indicative conditional": {
				"mood": "indicative",
				"tense": "conditional",
				"1s": infinitiveNoEnding + "iría",
				"2s": infinitiveNoEnding + "irías",
				"3s": infinitiveNoEnding + "iría",
				"1p": infinitiveNoEnding + "iríamos",
				"2p": infinitiveNoEnding + "iríais",
				"3p": infinitiveNoEnding + "irían"
			},
			"indicative conditional perfect": {
				"mood": "indicative",
				"tense": "conditional perfect",
				"1s": haber["fulltenses"]["indicative conditional"]["1s"] + " " + pastparticiple,
				"2s": haber["fulltenses"]["indicative conditional"]["2s"] + " " + pastparticiple,
				"3s": haber["fulltenses"]["indicative conditional"]["3s"] + " " + pastparticiple,
				"1p": haber["fulltenses"]["indicative conditional"]["1p"] + " " + pastparticiple,
				"2p": haber["fulltenses"]["indicative conditional"]["2p"] + " " + pastparticiple,
				"3p": haber["fulltenses"]["indicative conditional"]["3p"] + " " + pastparticiple
			},
			"indicative future": {
				"mood": "indicative",
				"tense": "future",
				"1s": infinitiveNoEnding + "iré",
				"2s": infinitiveNoEnding + "irás",
				"3s": infinitiveNoEnding + "irá",
				"1p": infinitiveNoEnding + "iremos",
				"2p": infinitiveNoEnding + "iréis",
				"3p": infinitiveNoEnding + "irán"
			},
			"indicative future perfect": {
				"mood": "indicative",
				"tense": "future perfect",
				"1s": haber["fulltenses"]["indicative future"]["1s"] + " " + pastparticiple,
				"2s": haber["fulltenses"]["indicative future"]["2s"] + " " + pastparticiple,
				"3s": haber["fulltenses"]["indicative future"]["3s"] + " " + pastparticiple,
				"1p": haber["fulltenses"]["indicative future"]["1p"] + " " + pastparticiple,
				"2p": haber["fulltenses"]["indicative future"]["2p"] + " " + pastparticiple,
				"3p": haber["fulltenses"]["indicative future"]["3p"] + " " + pastparticiple
			},
			"indicative imperfect": {
				"mood": "indicative",
				"tense": "imperfect",
				"1s": infinitiveNoEnding + "ía",
				"2s": infinitiveNoEnding + "ías",
				"3s": infinitiveNoEnding + "ía",
				"1p": infinitiveNoEnding + "íamos",
				"2p": infinitiveNoEnding + "íais",
				"3p": infinitiveNoEnding + "ían"
			},
			"indicative past perfect": {
				"mood": "indicative",
				"tense": "past perfect",
				"1s": haber["fulltenses"]["indicative imperfect"]["1s"] + " " + pastparticiple,
				"2s": haber["fulltenses"]["indicative imperfect"]["2s"] + " " + pastparticiple,
				"3s": haber["fulltenses"]["indicative imperfect"]["3s"] + " " + pastparticiple,
				"1p": haber["fulltenses"]["indicative imperfect"]["1p"] + " " + pastparticiple,
				"2p": haber["fulltenses"]["indicative imperfect"]["2p"] + " " + pastparticiple,
				"3p": haber["fulltenses"]["indicative imperfect"]["3p"] + " " + pastparticiple
			},
			"indicative present": {
				"mood": "indicative",
				"tense": "present",
				"1s": infinitiveNoEnding + "o",
				"2s": infinitiveNoEnding + "es",
				"3s": infinitiveNoEnding + "e",
				"1p": infinitiveNoEnding + "imos",
				"2p": infinitiveNoEnding + "ís",
				"3p": infinitiveNoEnding + "en"
			},
			"indicative present perfect": {
				"mood": "indicative",
				"tense": "present perfect",
				"1s": haber["fulltenses"]["indicative present"]["1s"] + " " + pastparticiple,
				"2s": haber["fulltenses"]["indicative present"]["2s"] + " " + pastparticiple,
				"3s": haber["fulltenses"]["indicative present"]["3s"] + " " + pastparticiple,
				"1p": haber["fulltenses"]["indicative present"]["1p"] + " " + pastparticiple,
				"2p": haber["fulltenses"]["indicative present"]["2p"] + " " + pastparticiple,
				"3p": haber["fulltenses"]["indicative present"]["3p"] + " " + pastparticiple
			},
			"indicative preterite": {
				"mood": "indicative",
				"tense": "preterite",
				"1s": infinitiveNoEnding + "í",
				"2s": infinitiveNoEnding + "iste",
				"3s": infinitiveNoEnding + "ió",
				"1p": infinitiveNoEnding + "imos",
				"2p": infinitiveNoEnding + "isteis",
				"3p": infinitiveNoEnding + "ieron"
			},
			"indicative preterite archaic": {
				"mood": "indicative",
				"tense": "preterite archaic",
				"1s": haber["fulltenses"]["indicative preterite"]["1s"] + " " + pastparticiple,
				"2s": haber["fulltenses"]["indicative preterite"]["2s"] + " " + pastparticiple,
				"3s": haber["fulltenses"]["indicative preterite"]["3s"] + " " + pastparticiple,
				"1p": haber["fulltenses"]["indicative preterite"]["1p"] + " " + pastparticiple,
				"2p": haber["fulltenses"]["indicative preterite"]["2p"] + " " + pastparticiple,
				"3p": haber["fulltenses"]["indicative preterite"]["3p"] + " " + pastparticiple
			},
			"subjunctive future": {
				"mood": "subjunctive",
				"tense": "future",
				"1s": infinitiveNoEnding + "iere",
				"2s": infinitiveNoEnding + "ieres",
				"3s": infinitiveNoEnding + "iere",
				"1p": infinitiveNoEnding + "iéremos",
				"2p": infinitiveNoEnding + "iereis",
				"3p": infinitiveNoEnding + "ieren"
			},
			"subjunctive future perfect": {
				"mood": "subjunctive",
				"tense": "future perfect",
				"1s": haber["fulltenses"]["subjunctive future"]["1s"] + " " + pastparticiple,
				"2s": haber["fulltenses"]["subjunctive future"]["2s"] + " " + pastparticiple,
				"3s": haber["fulltenses"]["subjunctive future"]["3s"] + " " + pastparticiple,
				"1p": haber["fulltenses"]["subjunctive future"]["1p"] + " " + pastparticiple,
				"2p": haber["fulltenses"]["subjunctive future"]["2p"] + " " + pastparticiple,
				"3p": haber["fulltenses"]["subjunctive future"]["3p"] + " " + pastparticiple
			},
			"subjunctive imperfect": {
				"mood": "subjunctive",
				"tense": "imperfect",
				"1s": infinitiveNoEnding + "iera",
				"2s": infinitiveNoEnding + "ieras",
				"3s": infinitiveNoEnding + "iera",
				"1p": infinitiveNoEnding + "iéramos",
				"2p": infinitiveNoEnding + "ierais",
				"3p": infinitiveNoEnding + "ieran"
			},
			"subjunctive past perfect": {
				"mood": "subjunctive",
				"tense": "past perfect",
				"1s": haber["fulltenses"]["subjunctive imperfect"]["1s"] + " " + pastparticiple,
				"2s": haber["fulltenses"]["subjunctive imperfect"]["2s"] + " " + pastparticiple,
				"3s": haber["fulltenses"]["subjunctive imperfect"]["3s"] + " " + pastparticiple,
				"1p": haber["fulltenses"]["subjunctive imperfect"]["1p"] + " " + pastparticiple,
				"2p": haber["fulltenses"]["subjunctive imperfect"]["2p"] + " " + pastparticiple,
				"3p": haber["fulltenses"]["subjunctive imperfect"]["3p"] + " " + pastparticiple
			},
			"subjunctive present": {
				"mood": "subjunctive",
				"tense": "present",
				"1s": infinitiveNoEnding + "a",
				"2s": infinitiveNoEnding + "as",
				"3s": infinitiveNoEnding + "a",
				"1p": infinitiveNoEnding + "amos",
				"2p": infinitiveNoEnding + "áis",
				"3p": infinitiveNoEnding + "an"
			},
			"subjunctive present perfect": {
				"mood": "subjunctive",
				"tense": "present perfect",
				"1s": haber["fulltenses"]["subjunctive present"]["1s"] + " " + pastparticiple,
				"2s": haber["fulltenses"]["subjunctive present"]["2s"] + " " + pastparticiple,
				"3s": haber["fulltenses"]["subjunctive present"]["3s"] + " " + pastparticiple,
				"1p": haber["fulltenses"]["subjunctive present"]["1p"] + " " + pastparticiple,
				"2p": haber["fulltenses"]["subjunctive present"]["2p"] + " " + pastparticiple,
				"3p": haber["fulltenses"]["subjunctive present"]["3p"] + " " + pastparticiple
			}
			}
		}
	elif verbType == "ER":
		pastparticiple = infinitiveNoEnding + "ido"
		conjugation = {
			"gerund": infinitiveNoEnding + "iendo",
			"pastparticiple": pastparticiple,
			"fulltenses": {
			"imperative affirmative present": {
				"mood": "imperative",
				"tense": "affirmative present",
				"1s": "-",
				"2s": infinitiveNoEnding + "e",
				"3s": infinitiveNoEnding + "a",
				"1p": "-",
				"2p": infinitiveNoEnding + "ed",
				"3p": infinitiveNoEnding + "an"
			},
			"imperative negative present": {
				"mood": "imperative",
				"tense": "negative present",
				"1s": "-",
				"2s": infinitiveNoEnding + "as",
				"3s": infinitiveNoEnding + "a",
				"1p": "-",
				"2p": infinitiveNoEnding + "áis",
				"3p": infinitiveNoEnding + "an"
			},
			"indicative conditional": {
				"mood": "indicative",
				"tense": "conditional",
				"1s": infinitiveNoEnding + "ería",
				"2s": infinitiveNoEnding + "erías",
				"3s": infinitiveNoEnding + "ería",
				"1p": infinitiveNoEnding + "eríamos",
				"2p": infinitiveNoEnding + "eríais",
				"3p": infinitiveNoEnding + "erían"
			},
			"indicative conditional perfect": {
				"mood": "indicative",
				"tense": "conditional perfect",
				"1s": haber["fulltenses"]["indicative conditional"]["1s"] + " " + pastparticiple,
				"2s": haber["fulltenses"]["indicative conditional"]["2s"] + " " + pastparticiple,
				"3s": haber["fulltenses"]["indicative conditional"]["3s"] + " " + pastparticiple,
				"1p": haber["fulltenses"]["indicative conditional"]["1p"] + " " + pastparticiple,
				"2p": haber["fulltenses"]["indicative conditional"]["2p"] + " " + pastparticiple,
				"3p": haber["fulltenses"]["indicative conditional"]["3p"] + " " + pastparticiple
			},
			"indicative future": {
				"mood": "indicative",
				"tense": "future",
				"1s": infinitiveNoEnding + "eré",
				"2s": infinitiveNoEnding + "erás",
				"3s": infinitiveNoEnding + "erá",
				"1p": infinitiveNoEnding + "eremos",
				"2p": infinitiveNoEnding + "eréis",
				"3p": infinitiveNoEnding + "erán"
			},
			"indicative future perfect": {
				"mood": "indicative",
				"tense": "future perfect",
				"1s": haber["fulltenses"]["indicative future"]["1s"] + " " + pastparticiple,
				"2s": haber["fulltenses"]["indicative future"]["2s"] + " " + pastparticiple,
				"3s": haber["fulltenses"]["indicative future"]["3s"] + " " + pastparticiple,
				"1p": haber["fulltenses"]["indicative future"]["1p"] + " " + pastparticiple,
				"2p": haber["fulltenses"]["indicative future"]["2p"] + " " + pastparticiple,
				"3p": haber["fulltenses"]["indicative future"]["3p"] + " " + pastparticiple
			},
			"indicative imperfect": {
				"mood": "indicative",
				"tense": "imperfect",
				"1s": infinitiveNoEnding + "ía",
				"2s": infinitiveNoEnding + "ías",
				"3s": infinitiveNoEnding + "ía",
				"1p": infinitiveNoEnding + "íamos",
				"2p": infinitiveNoEnding + "íais",
				"3p": infinitiveNoEnding + "ían"
			},
			"indicative past perfect": {
				"mood": "indicative",
				"tense": "past perfect",
				"1s": haber["fulltenses"]["indicative imperfect"]["1s"] + " " + pastparticiple,
				"2s": haber["fulltenses"]["indicative imperfect"]["2s"] + " " + pastparticiple,
				"3s": haber["fulltenses"]["indicative imperfect"]["3s"] + " " + pastparticiple,
				"1p": haber["fulltenses"]["indicative imperfect"]["1p"] + " " + pastparticiple,
				"2p": haber["fulltenses"]["indicative imperfect"]["2p"] + " " + pastparticiple,
				"3p": haber["fulltenses"]["indicative imperfect"]["3p"] + " " + pastparticiple
			},
			"indicative present": {
				"mood": "indicative",
				"tense": "present",
				"1s": infinitiveNoEnding + "o",
				"2s": infinitiveNoEnding + "es",
				"3s": infinitiveNoEnding + "e",
				"1p": infinitiveNoEnding + "emos",
				"2p": infinitiveNoEnding + "éis",
				"3p": infinitiveNoEnding + "en"
			},
			"indicative present perfect": {
				"mood": "indicative",
				"tense": "present perfect",
				"1s": haber["fulltenses"]["indicative present"]["1s"] + " " + pastparticiple,
				"2s": haber["fulltenses"]["indicative present"]["2s"] + " " + pastparticiple,
				"3s": haber["fulltenses"]["indicative present"]["3s"] + " " + pastparticiple,
				"1p": haber["fulltenses"]["indicative present"]["1p"] + " " + pastparticiple,
				"2p": haber["fulltenses"]["indicative present"]["2p"] + " " + pastparticiple,
				"3p": haber["fulltenses"]["indicative present"]["3p"] + " " + pastparticiple
			},
			"indicative preterite": {
				"mood": "indicative",
				"tense": "preterite",
				"1s": infinitiveNoEnding + "í",
				"2s": infinitiveNoEnding + "iste",
				"3s": infinitiveNoEnding + "ió",
				"1p": infinitiveNoEnding + "imos",
				"2p": infinitiveNoEnding + "isteis",
				"3p": infinitiveNoEnding + "ieron"
			},
			"indicative preterite archaic": {
				"mood": "indicative",
				"tense": "preterite archaic",
				"1s": haber["fulltenses"]["indicative preterite"]["1s"] + " " + pastparticiple,
				"2s": haber["fulltenses"]["indicative preterite"]["2s"] + " " + pastparticiple,
				"3s": haber["fulltenses"]["indicative preterite"]["3s"] + " " + pastparticiple,
				"1p": haber["fulltenses"]["indicative preterite"]["1p"] + " " + pastparticiple,
				"2p": haber["fulltenses"]["indicative preterite"]["2p"] + " " + pastparticiple,
				"3p": haber["fulltenses"]["indicative preterite"]["3p"] + " " + pastparticiple
			},
			"subjunctive future": {
				"mood": "subjunctive",
				"tense": "future",
				"1s": infinitiveNoEnding + "iere",
				"2s": infinitiveNoEnding + "ieres",
				"3s": infinitiveNoEnding + "iere",
				"1p": infinitiveNoEnding + "iéremos",
				"2p": infinitiveNoEnding + "iereis",
				"3p": infinitiveNoEnding + "ieren"
			},
			"subjunctive future perfect": {
				"mood": "subjunctive",
				"tense": "future perfect",
				"1s": haber["fulltenses"]["subjunctive future"]["1s"] + " " + pastparticiple,
				"2s": haber["fulltenses"]["subjunctive future"]["2s"] + " " + pastparticiple,
				"3s": haber["fulltenses"]["subjunctive future"]["3s"] + " " + pastparticiple,
				"1p": haber["fulltenses"]["subjunctive future"]["1p"] + " " + pastparticiple,
				"2p": haber["fulltenses"]["subjunctive future"]["2p"] + " " + pastparticiple,
				"3p": haber["fulltenses"]["subjunctive future"]["3p"] + " " + pastparticiple
			},
			"subjunctive imperfect": {
				"mood": "subjunctive",
				"tense": "imperfect",
				"1s": infinitiveNoEnding + "iera",
				"2s": infinitiveNoEnding + "ieras",
				"3s": infinitiveNoEnding + "iera",
				"1p": infinitiveNoEnding + "iéramos",
				"2p": infinitiveNoEnding + "ierais",
				"3p": infinitiveNoEnding + "ieran"
			},
			"subjunctive past perfect": {
				"mood": "subjunctive",
				"tense": "past perfect",
				"1s": haber["fulltenses"]["subjunctive imperfect"]["1s"] + " " + pastparticiple,
				"2s": haber["fulltenses"]["subjunctive imperfect"]["2s"] + " " + pastparticiple,
				"3s": haber["fulltenses"]["subjunctive imperfect"]["3s"] + " " + pastparticiple,
				"1p": haber["fulltenses"]["subjunctive imperfect"]["1p"] + " " + pastparticiple,
				"2p": haber["fulltenses"]["subjunctive imperfect"]["2p"] + " " + pastparticiple,
				"3p": haber["fulltenses"]["subjunctive imperfect"]["3p"] + " " + pastparticiple
			},
			"subjunctive present": {
				"mood": "subjunctive",
				"tense": "present",
				"1s": infinitiveNoEnding + "a",
				"2s": infinitiveNoEnding + "as",
				"3s": infinitiveNoEnding + "a",
				"1p": infinitiveNoEnding + "amos",
				"2p": infinitiveNoEnding + "áis",
				"3p": infinitiveNoEnding + "an"
			},
			"subjunctive present perfect": {
				"mood": "subjunctive",
				"tense": "present perfect",
				"1s": haber["fulltenses"]["subjunctive present"]["1s"] + " " + pastparticiple,
				"2s": haber["fulltenses"]["subjunctive present"]["2s"] + " " + pastparticiple,
				"3s": haber["fulltenses"]["subjunctive present"]["3s"] + " " + pastparticiple,
				"1p": haber["fulltenses"]["subjunctive present"]["1p"] + " " + pastparticiple,
				"2p": haber["fulltenses"]["subjunctive present"]["2p"] + " " + pastparticiple,
				"3p": haber["fulltenses"]["subjunctive present"]["3p"] + " " + pastparticiple
			}
			}
		} 
	elif verbType == "AR":
		pastparticiple = infinitiveNoEnding + "ado"
		conjugation = {
			"gerund": infinitiveNoEnding + "ando",
			"pastparticiple": pastparticiple,
			"fulltenses": {
			"imperative affirmative present": {
				"mood": "imperative",
				"tense": "affirmative present",
				"1s": "-",
				"2s": infinitiveNoEnding + "a",
				"3s": infinitiveNoEnding + "e",
				"1p": "-",
				"2p": infinitiveNoEnding + "ad",
				"3p": infinitiveNoEnding + "en"
			},
			"imperative negative present": {
				"mood": "imperative",
				"tense": "negative present",
				"1s": "-",
				"2s": infinitiveNoEnding + "es",
				"3s": infinitiveNoEnding + "e",
				"1p": "-",
				"2p": infinitiveNoEnding + "éis",
				"3p": infinitiveNoEnding + "en"
			},
			"indicative conditional": {
				"mood": "indicative",
				"tense": "conditional",
				"1s": infinitiveNoEnding + "aría",
				"2s": infinitiveNoEnding + "arías",
				"3s": infinitiveNoEnding + "aría",
				"1p": infinitiveNoEnding + "aríamos",
				"2p": infinitiveNoEnding + "aríais",
				"3p": infinitiveNoEnding + "arían"
			},
			"indicative conditional perfect": {
				"mood": "indicative",
				"tense": "conditional perfect",
				"1s": haber["fulltenses"]["indicative conditional"]["1s"] + " " + pastparticiple,
				"2s": haber["fulltenses"]["indicative conditional"]["2s"] + " " + pastparticiple,
				"3s": haber["fulltenses"]["indicative conditional"]["3s"] + " " + pastparticiple,
				"1p": haber["fulltenses"]["indicative conditional"]["1p"] + " " + pastparticiple,
				"2p": haber["fulltenses"]["indicative conditional"]["2p"] + " " + pastparticiple,
				"3p": haber["fulltenses"]["indicative conditional"]["3p"] + " " + pastparticiple
			},
			"indicative future": {
				"mood": "indicative",
				"tense": "future",
				"1s": infinitiveNoEnding + "aré",
				"2s": infinitiveNoEnding + "arás",
				"3s": infinitiveNoEnding + "ará",
				"1p": infinitiveNoEnding + "aremos",
				"2p": infinitiveNoEnding + "aréis",
				"3p": infinitiveNoEnding + "arán"
			},
			"indicative future perfect": {
				"mood": "indicative",
				"tense": "future perfect",
				"1s": haber["fulltenses"]["indicative future"]["1s"] + " " + pastparticiple,
				"2s": haber["fulltenses"]["indicative future"]["2s"] + " " + pastparticiple,
				"3s": haber["fulltenses"]["indicative future"]["3s"] + " " + pastparticiple,
				"1p": haber["fulltenses"]["indicative future"]["1p"] + " " + pastparticiple,
				"2p": haber["fulltenses"]["indicative future"]["2p"] + " " + pastparticiple,
				"3p": haber["fulltenses"]["indicative future"]["3p"] + " " + pastparticiple
			},
			"indicative imperfect": {
				"mood": "indicative",
				"tense": "imperfect",
				"1s": infinitiveNoEnding + "aba",
				"2s": infinitiveNoEnding + "abas",
				"3s": infinitiveNoEnding + "aba",
				"1p": infinitiveNoEnding + "ábamos",
				"2p": infinitiveNoEnding + "abais",
				"3p": infinitiveNoEnding + "aban"
			},
			"indicative past perfect": {
				"mood": "indicative",
				"tense": "past perfect",
				"1s": haber["fulltenses"]["indicative imperfect"]["1s"] + " " + pastparticiple,
				"2s": haber["fulltenses"]["indicative imperfect"]["2s"] + " " + pastparticiple,
				"3s": haber["fulltenses"]["indicative imperfect"]["3s"] + " " + pastparticiple,
				"1p": haber["fulltenses"]["indicative imperfect"]["1p"] + " " + pastparticiple,
				"2p": haber["fulltenses"]["indicative imperfect"]["2p"] + " " + pastparticiple,
				"3p": haber["fulltenses"]["indicative imperfect"]["3p"] + " " + pastparticiple
			},
			"indicative present": {
				"mood": "indicative",
				"tense": "present",
				"1s": infinitiveNoEnding + "o",
				"2s": infinitiveNoEnding + "as",
				"3s": infinitiveNoEnding + "a",
				"1p": infinitiveNoEnding + "amos",
				"2p": infinitiveNoEnding + "áis",
				"3p": infinitiveNoEnding + "an"
			},
			"indicative present perfect": {
				"mood": "indicative",
				"tense": "present perfect",
				"1s": haber["fulltenses"]["indicative present"]["1s"] + " " + pastparticiple,
				"2s": haber["fulltenses"]["indicative present"]["2s"] + " " + pastparticiple,
				"3s": haber["fulltenses"]["indicative present"]["3s"] + " " + pastparticiple,
				"1p": haber["fulltenses"]["indicative present"]["1p"] + " " + pastparticiple,
				"2p": haber["fulltenses"]["indicative present"]["2p"] + " " + pastparticiple,
				"3p": haber["fulltenses"]["indicative present"]["3p"] + " " + pastparticiple
			},
			"indicative preterite": {
				"mood": "indicative",
				"tense": "preterite",
				"1s": infinitiveNoEnding + "é",
				"2s": infinitiveNoEnding + "aste",
				"3s": infinitiveNoEnding + "ó",
				"1p": infinitiveNoEnding + "amos",
				"2p": infinitiveNoEnding + "asteis",
				"3p": infinitiveNoEnding + "aron"
			},
			"indicative preterite archaic": {
				"mood": "indicative",
				"tense": "preterite archaic",
				"1s": haber["fulltenses"]["indicative preterite"]["1s"] + " " + pastparticiple,
				"2s": haber["fulltenses"]["indicative preterite"]["2s"] + " " + pastparticiple,
				"3s": haber["fulltenses"]["indicative preterite"]["3s"] + " " + pastparticiple,
				"1p": haber["fulltenses"]["indicative preterite"]["1p"] + " " + pastparticiple,
				"2p": haber["fulltenses"]["indicative preterite"]["2p"] + " " + pastparticiple,
				"3p": haber["fulltenses"]["indicative preterite"]["3p"] + " " + pastparticiple
			},
			"subjunctive future": {
				"mood": "subjunctive",
				"tense": "future",
				"1s": infinitiveNoEnding + "are",
				"2s": infinitiveNoEnding + "ares",
				"3s": infinitiveNoEnding + "are",
				"1p": infinitiveNoEnding + "áremos",
				"2p": infinitiveNoEnding + "areis",
				"3p": infinitiveNoEnding + "aren"
			},
			"subjunctive future perfect": {
				"mood": "subjunctive",
				"tense": "future perfect",
				"1s": haber["fulltenses"]["subjunctive future"]["1s"] + " " + pastparticiple,
				"2s": haber["fulltenses"]["subjunctive future"]["2s"] + " " + pastparticiple,
				"3s": haber["fulltenses"]["subjunctive future"]["3s"] + " " + pastparticiple,
				"1p": haber["fulltenses"]["subjunctive future"]["1p"] + " " + pastparticiple,
				"2p": haber["fulltenses"]["subjunctive future"]["2p"] + " " + pastparticiple,
				"3p": haber["fulltenses"]["subjunctive future"]["3p"] + " " + pastparticiple
			},
			"subjunctive imperfect": {
				"mood": "subjunctive",
				"tense": "imperfect",
				"1s": infinitiveNoEnding + "ara",
				"2s": infinitiveNoEnding + "aras",
				"3s": infinitiveNoEnding + "ara",
				"1p": infinitiveNoEnding + "áramos",
				"2p": infinitiveNoEnding + "ais",
				"3p": infinitiveNoEnding + "aran"
			},
			"subjunctive past perfect": {
				"mood": "subjunctive",
				"tense": "past perfect",
				"1s": haber["fulltenses"]["subjunctive imperfect"]["1s"] + " " + pastparticiple,
				"2s": haber["fulltenses"]["subjunctive imperfect"]["2s"] + " " + pastparticiple,
				"3s": haber["fulltenses"]["subjunctive imperfect"]["3s"] + " " + pastparticiple,
				"1p": haber["fulltenses"]["subjunctive imperfect"]["1p"] + " " + pastparticiple,
				"2p": haber["fulltenses"]["subjunctive imperfect"]["2p"] + " " + pastparticiple,
				"3p": haber["fulltenses"]["subjunctive imperfect"]["3p"] + " " + pastparticiple
			},
			"subjunctive present": {
				"mood": "subjunctive",
				"tense": "present",
				"1s": infinitiveNoEnding + "e",
				"2s": infinitiveNoEnding + "es",
				"3s": infinitiveNoEnding + "e",
				"1p": infinitiveNoEnding + "emos",
				"2p": infinitiveNoEnding + "éis",
				"3p": infinitiveNoEnding + "en"
			},
			"subjunctive present perfect": {
				"mood": "subjunctive",
				"tense": "present perfect",
				"1s": haber["fulltenses"]["subjunctive present"]["1s"] + " " + pastparticiple,
				"2s": haber["fulltenses"]["subjunctive present"]["2s"] + " " + pastparticiple,
				"3s": haber["fulltenses"]["subjunctive present"]["3s"] + " " + pastparticiple,
				"1p": haber["fulltenses"]["subjunctive present"]["1p"] + " " + pastparticiple,
				"2p": haber["fulltenses"]["subjunctive present"]["2p"] + " " + pastparticiple,
				"3p": haber["fulltenses"]["subjunctive present"]["3p"] + " " + pastparticiple
			}
			}
		}

	conjugation["infinitive"] = infinitive
	conjugation["verbType"] = verbType
	conjugatedVerbs.append(conjugation)
	print(str(count) + ": conjugated " + infinitive + " (as " + verbType + " form)")

# SAVE AS JSON
jsonFile = open('conjugatedVerbs.json', 'w')
json.dump(conjugatedVerbs, jsonFile)
