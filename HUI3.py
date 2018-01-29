# Homework 2
# These are the important coefficients in the dead-perfect health scale. 1.371 is the u*. U* is the utility of the
# health state on a utility scale where dead has a utility of 0.00 and healthy has a utility of 1.00. The 0.371 constant
# is subtracted from the formula. Both numbers were found within the document. Response is a variable that we will
# be using later. Thus, I am creating a dummy variable up here.
constant = 0.371
coefficient = 1.371
response = 1

# Here, we will be setting up a dictionary for each of the attributes. The attributes start with 1 (perfect health)
# and descend. Notice that speech, emotion, and pain do not have a 6th level.

dictHUI3 = {'Vision':         [1.00, 0.98, 0.89, 0.84, 0.75, 0.61],
            'Hearing':        [1.00, 0.95, 0.89, 0.80, 0.74, 0.61],
            'Speech':         [1.00, 0.94, 0.89, 0.81, 0.68],
            'Ambulation':     [1.00, 0.93, 0.86, 0.73, 0.65, 0.58],
            'Dexterity':      [1.00, 0.95, 0.88, 0.76, 0.65, 0.56],
            'Emotion':        [1.00, 0.95, 0.85, 0.64, 0.46],
            'Cognition':      [1.00, 0.92, 0.95, 0.83, 0.60, 0.42],
            'Pain':           [1.00, 0.96, 0.90, 0.77, 0.55]}

# Here, we are able to define each of the scores.

def scoreHUI3(vision, hearing, speech, ambulation, dexterity, emotion, cognition, pain):
    """
    :param vision:
    :param hearing:
    :param speech:
    :param ambulation:
    :param dexterity:
    :param emotion:
    :param cognition:
    :param pain:
    :return:
    """

# These if not statements help Python stop the code if the values are not maintained within certain
# parameters.

    if not(vision in [1 ,2 ,3 ,4 ,5 ,6]):
        raise ValueError('Value for vision must be contained within 1-6.')
    if not(hearing in [1 ,2 ,3 ,4 ,5 ,6]):
        raise ValueError('Value for hearing level must be contained within 1-6.')
    if not(speech in [1 ,2 ,3 ,4 ,5]):
        raise ValueError('Value for speech level must be contained within 1-5.')
    if not(ambulation in [1 ,2 ,3 ,4 ,5 ,6]):
        raise ValueError('Value for ambulation level must be contained within 1-6.')
    if not(dexterity in [1 ,2 ,3 ,4 ,5 ,6]):
        raise ValueError('Value for dexterity level must be contained within 1-6.')
    if not(emotion in [1 ,2 ,3 ,4 ,5]):
        raise ValueError('Value for emotion level must be contained within 1-5.')
    if not(cognition in [1 ,2 ,3 ,4 ,5 ,6]):
        raise ValueError('Value for cognition level must be contained within 1-6.')
    if not(pain in [1 ,2 ,3 ,4 ,5]):
        raise ValueError('Value for pain level must be contained within 1-5.')

# The next section will show two ways of setting up the dead-perfect health scale formula. One section will
# be in notes. You can specify which section you want to use by putting one section in notes and running the other.

    response = coefficient * (dictHUI3['Vision'][vision - 1]
                              * dictHUI3['Hearing'][hearing - 1]
                              * dictHUI3['Speech'][speech - 1]
                              * dictHUI3['Ambulation'][ambulation - 1]
                              * dictHUI3['Dexterity'][dexterity - 1]
                              * dictHUI3['Emotion'][emotion - 1]
                              * dictHUI3['Cognition'][cognition - 1]
                              * dictHUI3['Pain'][pain - 1]) - constant
    return response

# Or you can write the same code like this and get the same answer:

    #response = coefficient

    #response *= dictHUI3['Vision'][vision -1]
    #response *= dictHUI3['Hearing'][hearing -1]
    #response *= dictHUI3['Speech'][speech -1]
    #response *= dictHUI3['Ambulation'][ambulation -1]
    #response *= dictHUI3['Dexterity'][dexterity -1]
    #response *= dictHUI3['Emotion'][emotion -1]
    #response *= dictHUI3['Cognition'][cognition -1]
    #response *= dictHUI3['Pain'][pain -1]

    #response -= constant

    #return response
