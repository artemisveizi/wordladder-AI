# wordladder-AI
Word Ladder is a word game in which a player essentially computes the [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance "Wikipedia: Levenshtein distance") distance between two words, with the constraint that all intermediary words must also be words (ant --> aat --> cat is not permitted, as "aat" is not a word). 
This computes the word ladder distance between pairs of 6-letter words in a given dictionary. From the classic game, invented by Lewis Carroll:</br>
  rip --> rap</br>
  rap --> tap</br>
  tap --> tar</br>
So, the word ladder distance between rip and tar is 3.

### Example six-letter word paths:
*NOTE: these are on a given, non-comprehensive 6-letter word dictionary. Distances might not be the actual word ladder distances on the full OED.*

| Start -- End    | Distance | Path                                                            | Time (s) |
| ----------------|----------| ----------------------------------------------------------------|-----|
| bellow -- hollow|  4       | hollow follow fellow bellow                                     |0.002|
| slider -- gasket| 11       | gasket basket basked balked balled bulled gulled guiled guided</br> guider glider slider                                                                                                                |0.295|
| vaguer -- drifts| 22       | drifts drafts grafts grants grunts gaunts taunts taints saints stints</br> stilts stiles smiles smiled sailed bailed balled called calved</br> valved valued valuer vaguer                            |0.459|
| abates -- anemia| -        | no possible path                                                |0.473|

### Informed A* search optimization:
+ Blind search: classic BFS, explores every "child" (word with only one letter transposed from parent) until it reaches the goal word.
+ Informed search: Uses h(A), an estimate of current node cost to goal, to prioritize child nodes to explore first.
  + Orders fringe by h(A)
  + Nodes with a smaller h(A) will be "popped off" and explored first, decreasing the time spent exploring  
+ Informed A*: Optimize by making the distance = distance + depth
  + Sorts fringe by f(A) = c(A) + h(A), where c(A) is real cost of A and h(A) is estimated cost to goal (depth + heuristic estimate)
  + A* is optimal. Finds a smallest-cost goal state:
    + If * keeps the entire fringe (can become very large).
    + If h(A) ≤ c(A). h(A) always underestimates cost to the goal (true cost to the goal is admissible).
    + If h(A) is set to 0, always true—results in BFS.

### Pseudo-proof:</br>
Claim: A is optimal goal state; G is suboptimal goal state. f(B) < f(A).</br>
  F(A) = c(A) + h(A)</br> 
  F(A) = c(A) + 0</br>
  F(A) > C(G)</br>
  F(B) = c(B) + h(B) ≤ c(G) < f(A) </br>
