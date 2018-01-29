# Now, we are going to be importing the datafile from HUI3 and running some analysis.

import HUI3 as eq

# First, we will test to make sure that our formula is running correctly. If we input the perfect score for all 8
# attributes, we should get a utility of 1.
print("Score for 'perfect' health", 1,1,1,1,1,1,1,1)
print(eq.scoreHUI3(vision=1, hearing=1, speech=1, ambulation=1, dexterity=1, emotion=1, cognition=1, pain=1))
# 1.0 - It works!

# Now, we will assign random scores for a theoretical patient without a perfect health score.
print("Score for potential patient: [4,4,4,2,1,3,4,1]")
print(eq.scoreHUI3(vision=4, hearing=4, speech=4, ambulation=2, dexterity=1, emotion=3, cognition=4, pain=1))
# 0.1186

# Finally, we will try to set a score of 6 for one of the attributes that we know does not have a 6 point scale
# such as speech, emotion, or pain. This code should give us an error message.
print("Score for potential patient: [4,4,6,2,1,3,4,1]")
print(eq.scoreHUI3(vision=4, hearing=4, speech=6, ambulation=2, dexterity=1, emotion=3, cognition=4, pain=1))
# We get an error message of "value for speech level must be contained within 1-5."

