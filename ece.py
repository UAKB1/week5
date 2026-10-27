for david in range(0, 29): 
    for Emma in range(0, 29):
        for frank in range(0, 29):
            if Emma + frank + david == 28 and Emma == david + 3 and frank == 3 * david:
                print("David has", david, "Emma has", Emma, "Frank has", frank)