# DeGroot
Implementation of a supplemented version of DeGroot learning. 

DeGroot learning is a social learning process which allows one to find the trust between members of a group, and from their shared interests, how likely they are to prefer some choices over others. 

For example, some member of the group, say personA, has similar interests (based on previous voting patterns) to the others in the group. Then, the votes made by personA will have a higher weighting in the final calculation as their votes are more representative of the group's collective interest. Conversely, some other member of the group, say personB, may have dissimilar interests (as determined by previous voting patterns) to the other in the group. In this case, as their interests are less representative of the group's share interest, their votes will have a lower weighting in the final calculation.

Formally, DeGroot learning seeks to find the consensus beliefs of a group for which the trust between each individual has already been determined. For my implementation, I was interested most in finding a group's interest in a future choice based on their past habits. So, this implemenation takes a matrix of votes as input, and from that matrix, calculates the trust matrix for the group. 

