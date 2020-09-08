# DeGroot Learning
Implementation of a supplemented version of DeGroot learning. 

DeGroot learning is a social learning process which allows one to find the trust between members of a group, and by analyzing their shared interests, how likely they are to prefer some choices over others.

For example, some member of the group, say personA, has similar interests (based on previous voting patterns) to the others in the group. Then, the votes made by personA will have a higher weighting in the final calculation as their votes are more representative of the group's collective interest. Conversely, some other member of the group, say personB, may have dissimilar interests (as determined by previous voting patterns) to the others in the group. In this case, as their interests are less representative of the group's shared interest, their votes will have a lower weighting in the final calculation.

Formally, DeGroot learning seeks to find the consensus beliefs of a group for which the trust between each individual has already been determined. For my implementation, I was interested most in finding a group's interest in a future choice based on their past habits. So, this implementation takes a matrix of votes as input, and from that matrix, calculates the trust matrix for the group. 

## Files Contained: 
* DeGroot.py,
* DeGrootLearning.pdf

## Libraries Used: 
* [Numpy](https://numpy.org/) - for matrices, calculating vector norm, other matrix operations. 
* [Sympy](https://www.sympy.org/en/index.html) - for computing matrix limit.

## Runnning DeGroot
To run DeGroot independently (that is, from the command line), navigate to the directory containing the files contained herein and enter `python3 DeGroot.py`.

To run DeGroot as a module, download the files contained herein and include `import DeGroot` in your code.

## More Information
The maths behind this implementation of DeGroot learning can be accessed at [DeGroot Learning Maths](https://github.com/benvolioo/DeGroot/blob/master/DeGrootLearning.pdf).

Further reading regarding DeGroot learning can be found at [DeGroot Learning Wikipedia](https://en.wikipedia.org/wiki/DeGroot_learning).

## Future Potential Versions
* Adding check to ensure that beliefs will converge to a limit [Conditions for convergence](https://en.wikipedia.org/wiki/DeGroot_learning#Convergence_of_beliefs_and_consensus).
* Add ability to check for consensus beliefs among subgroups within a main group. 
* Improve command line input for matrices.
* Look into improving time complexity.

## Authors
Marty Rudolf

